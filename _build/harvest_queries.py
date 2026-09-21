#!/usr/bin/env python3
"""Harvest real New Zealand autosuggest queries — the data source behind
AnswerThePublic — from Google (gl=nz) and DuckDuckGo (kl=nz-en).

Seeds x modifiers x A-Z gives a broad sweep of what Kiwis actually type.
"""
import json, urllib.parse, urllib.request, time, sys, re
from collections import Counter

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/121.0 Safari/537.36"

SEEDS = [
    "online casino nz", "best online casino nz", "online casino new zealand",
    "online pokies nz", "casino bonus nz", "no deposit bonus nz",
    "casino withdrawal nz", "online gambling nz", "crypto casino nz",
    "live casino nz", "online betting nz", "tab nz", "gambling tax nz",
    "casino payment nz", "fast payout casino nz",
]
QUESTIONS = ["how", "what", "why", "which", "who", "when", "where", "is", "are",
             "can", "do", "does", "should", "will"]
PREPS = ["for", "with", "without", "vs", "near", "like", "that", "to"]
ALPHA = list("abcdefghijklmnopqrstuvwxyz")


def google(q):
    u = ("https://suggestqueries.google.com/complete/search?client=firefox"
         f"&gl=nz&hl=en-NZ&q={urllib.parse.quote(q)}")
    try:
        r = urllib.request.Request(u, headers={"User-Agent": UA})
        d = json.loads(urllib.request.urlopen(r, timeout=12).read().decode("utf-8", "replace"))
        return d[1] if len(d) > 1 else []
    except Exception:
        return []


def ddg(q):
    u = f"https://duckduckgo.com/ac/?q={urllib.parse.quote(q)}&kl=nz-en"
    try:
        r = urllib.request.Request(u, headers={"User-Agent": UA})
        d = json.loads(urllib.request.urlopen(r, timeout=12).read().decode("utf-8", "replace"))
        return [x.get("phrase", "") for x in d]
    except Exception:
        return []


out = set()
probes = []
for s in SEEDS:
    probes.append(s)
    for m in QUESTIONS:
        probes.append(f"{m} {s}")
    for m in PREPS + ALPHA:
        probes.append(f"{s} {m}")

print(f"probing {len(probes)} stems...", file=sys.stderr)
for i, p in enumerate(probes):
    out.update(google(p))
    if i % 3 == 0:
        out.update(ddg(p))
    if i % 60 == 0:
        print(f"  {i}/{len(probes)}  unique={len(out)}", file=sys.stderr)
    time.sleep(0.12)

# NZ intent filter — drop obvious spam/other-market noise
NZ = re.compile(r"\b(nz|new zealand|kiwi|aotearoa|nzd|tab|pokies)\b", re.I)
SPAM = re.compile(r"\.(com|info|net|org|co|xyz|site)\b|casinorank|jackpotguide|brainal", re.I)
clean = sorted({q.strip().lower() for q in out
                if q and NZ.search(q) and not SPAM.search(q) and 3 <= len(q.split()) <= 12})

json.dump(clean, open("/private/tmp/claude-501/-Users-scotthamilton-Documents-MY-SITES/c0ec9a58-b58e-435b-8ad5-e7af4ea32f4d/scratchpad/queries.json", "w"), indent=1)
print(f"\n{len(clean)} NZ-intent queries harvested (from {len(out)} raw)", file=sys.stderr)

QW = re.compile(r"^(how|what|why|which|who|when|where|is|are|can|do|does|should|will)\b")
qs = [q for q in clean if QW.match(q)]
print(f"{len(qs)} are questions\n", file=sys.stderr)
for q in qs: print(q)
