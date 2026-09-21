#!/usr/bin/env python3
"""Keyword coverage and anti-stuffing guard.

Verifies that every Tier 1 term in keywords.py actually appears on its page,
reports Tier 2 / long-tail coverage, enforces the cannibalisation rules, and
fails if any single phrase is repeated to the point of stuffing.
"""
import os, re, sys, glob, html, json
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "_build"))
import keywords as K

# A phrase repeated more often than this, as a share of body words, reads as
# stuffing to a human long before it does to a search engine.
MAX_DENSITY = 0.011


def norm(s):
    s = html.unescape(s)
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = s.lower().replace("’", "'").replace("–", "-").replace("—", " ")
    s = re.sub(r"[^a-z0-9$%'\- ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def count(hay, needle):
    """Exact-phrase occurrences."""
    return len(re.findall(r"(?<![a-z0-9])" + re.escape(needle) + r"(?![a-z0-9])", hay))


def covered(hay_words, needle):
    """Exact phrase, or all of the term's words inside a short window.

    Several supplied terms are keyword-tool fragments rather than English
    ("rtp meaning casino", "casino no deposit bonus new zealand"). Forcing the
    literal string into copy produces the kind of sentence that reads as
    stuffing to a person and is matched anyway by an engine that resolves word
    proximity. So: exact match counts, and so does every word of the term
    appearing within a window of its own length plus five.
    """
    toks = needle.split()
    if " " + needle + " " in " " + " ".join(hay_words) + " ":
        return True
    if len(toks) < 2:
        return False
    win = len(toks) + 5
    idx = {t: [i for i, w in enumerate(hay_words) if w == t] for t in set(toks)}
    if any(not v for v in idx.values()):
        return False
    for start in idx[toks[0]]:
        if all(any(start <= p < start + win for p in idx[t]) for t in toks):
            return True
    return False


def main():
    fail, warn, rows = [], [], []
    for path, kw in sorted(K.MAP.items()):
        f = os.path.join(ROOT, path.strip("/"), "index.html")
        if not os.path.exists(f):
            fail.append(f"{path}: page does not exist")
            continue
        raw = open(f, encoding="utf-8").read()
        body = norm(raw)
        bw = body.split()
        words = max(1, len(bw))
        head = norm(re.search(r"<title>(.*?)</title>", raw, re.S).group(1)) + " " + \
               " ".join(norm(h) for h in re.findall(r"<h[1-3][^>]*>(.*?)</h[1-3]>", raw, re.S))
        hw = head.split()

        miss1 = [t for t in kw["t1"] if not covered(bw, norm(t))]
        hit2 = sum(1 for t in kw["t2"] if covered(bw, norm(t)))
        hit3 = sum(1 for t in kw["lt"] if covered(bw, norm(t)))
        inhead = sum(1 for t in kw["t1"] if covered(hw, norm(t)))

        for t in miss1:
            fail.append(f"{path}: TIER 1 missing — \"{t}\"")
        if inhead == 0 and kw["t1"]:
            warn.append(f"{path}: no Tier 1 term in the title or any H1-H3")

        # cannibalisation
        for t in K.FORBIDDEN.get(path, []):
            if count(body, norm(t)) > 1:
                fail.append(f"{path}: targets \"{t}\" — reserved for another page")
        if path != "/" and count(head, norm(K.HOME_HEAD)):
            fail.append(f"{path}: uses the homepage head term in a heading")

        # stuffing
        for t in kw["t1"] + kw["t2"]:
            n = count(body, norm(t))
            if n / words > MAX_DENSITY:
                fail.append(f"{path}: \"{t}\" x{n} = {n/words*100:.2f}% of body — stuffed")

        rows.append((path, words, len(kw["t1"]) - len(miss1), len(kw["t1"]),
                     hit2, len(kw["t2"]), hit3, len(kw["lt"]), inhead))

    print(f"{'page':<28}{'words':>7}{'T1':>8}{'T2':>8}{'long-tail':>11}{'T1 in headings':>16}")
    print("-" * 78)
    for p, w, a, b, c, d, e, f_, ih in rows:
        print(f"{p:<28}{w:>7}{f'{a}/{b}':>8}{f'{c}/{d}':>8}{f'{e}/{f_}':>11}{ih:>16}")
    tot = lambda i: sum(r[i] for r in rows)
    print("-" * 78)
    print(f"{'TOTAL':<28}{tot(1):>7}{f'{tot(2)}/{tot(3)}':>8}"
          f"{f'{tot(4)}/{tot(5)}':>8}{f'{tot(6)}/{tot(7)}':>11}")

    if warn:
        print(f"\n{len(warn)} warning(s):")
        for w_ in warn[:25]:
            print("  ⚠ " + w_)
    if fail:
        print(f"\n{len(fail)} ISSUE(S):")
        for e_ in fail[:80]:
            print("  ✗ " + e_)
        sys.exit(1)
    print("\n✓ keyword coverage complete, no stuffing, no cannibalisation")


if __name__ == "__main__":
    main()
