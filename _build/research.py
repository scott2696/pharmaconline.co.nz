#!/usr/bin/env python3
"""Primary research datasets, as data.

Everything here was collected by us and is re-collectable. Each block states
its source and collection date so a reader — or a journalist — can check it.

  QUERIES      994 NZ-intent search queries harvested from Google (gl=nz) and
               DuckDuckGo (kl=nz-en) autosuggest on 20 September 2026. This is
               the same raw source AnswerThePublic sells; harvest_queries.py
               regenerates it.
  TRENDS       Google Trends, geo=NZ, pulled 20 September 2026.
  MARKET       NZ market size and regulatory figures, each attributed inline.

Reddit and Trustpilot both block automated access from our infrastructure, so
there are no forum or review-site quotes on this site. We would rather say that
than paraphrase user quotes we cannot verify. The search-demand dataset below is
the substitute: it measures what New Zealanders actually type, which is a
harder signal than a handful of self-selected forum posts anyway.
"""
import json, os, re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUERIES = json.load(open(os.path.join(ROOT, "_build", "queries.json")))
HARVEST_DATE = "20 September 2026"
HARVEST_N = len(QUERIES)

# Theme -> (label, regex). Counts are computed, never hand-written, so the
# numbers on the page cannot drift from the dataset behind them.
THEMES = [
    ("Bonuses and free spins", r"\b(bonus|free spin|no deposit|welcome|promo|free chip)\b"),
    ("Deposits and payment methods", r"\b(nzd|paypal|poli|deposit|bank|visa|payment|neosurf|paysafe|crypto|bitcoin|payid)\b"),
    ("Payout speed and withdrawals", r"\b(payout|withdraw|withdrawal|cashout|cash out|instant|pay out|same day)\b"),
    ("Is it legal, or banned?", r"\b(legal|illegal|ban|banned|allowed|lawful|prohibit)\b"),
    ("Mobile and apps", r"\b(app|mobile|android|iphone|ios|download)\b"),
    ("Trust, safety and scams", r"\b(safe|trust|trusted|legit|scam|rigged|reliable|secure)\b"),
    ("Tax on winnings", r"\b(tax|taxable|ird|declare)\b"),
    ("&ldquo;Reddit&rdquo; as a trust signal", r"\breddit\b"),
    ("RTP and payout percentage", r"\b(rtp|payout percentage|return to player|best paying|highest paying)\b"),
    ("Live dealer", r"\b(live dealer|live casino|blackjack|roulette|baccarat)\b"),
]


def theme_counts():
    out = []
    for label, pat in THEMES:
        rx = re.compile(pat, re.I)
        n = sum(1 for q in QUERIES if rx.search(q))
        out.append((label, n, round(n / HARVEST_N * 100, 1)))
    return sorted(out, key=lambda r: -r[1])


def questions():
    rx = re.compile(r"^(how|what|why|which|who|when|where|is|are|can|do|does|should|will)\b")
    return [q for q in QUERIES if rx.match(q)]


def matching(pat, limit=None):
    rx = re.compile(pat, re.I)
    out = [q for q in QUERIES if rx.search(q)]
    return out[:limit] if limit else out


def dollar_tiers():
    """Deposit-size queries, which reveal the stake level people actually plan."""
    tiers = Counter()
    for q in QUERIES:
        for m in re.findall(r"\$\s?(\d{1,3})\b", q):
            tiers[int(m)] += 1
    return sorted(tiers.items())


# ---------------------------------------------------------------------------
# Google Trends, geo=NZ, pulled 20 September 2026.
# Index is Google's own 0-100 scale. "Momentum" is the mean of the trailing
# 13 weeks against the 13 weeks before it.
# ---------------------------------------------------------------------------
TRENDS = [
    # (term, prev 13wk mean, last 13wk mean, momentum %, note)
    ("best online casino nz", 7.9, 21.8, +175.7,
     "At a five-year high. Was flat near zero through 2021&ndash;2024."),
    ("online pokies", 1.0, 2.0, +100.0,
     "&ldquo;best online pokies real money nz&rdquo; is a rising query, +50%."),
    ("online casino (generic)", 17.2, 12.3, -28.6,
     "Falling while the NZ-specific term climbs &mdash; searchers are getting more specific."),
    ("no deposit bonus", 4.4, 3.2, -28.1,
     "But &ldquo;no deposit bonus casino 2026&rdquo; and &ldquo;no deposit bonus codes 2026&rdquo; are both <b>Breakout</b>."),
    ("casino withdrawal", 3.9, 2.5, -37.3, "Seasonal dip; the query set is small."),
]

TRENDS_RISING = [
    ("no deposit bonus casino 2026", "Breakout"),
    ("no deposit bonus codes 2026", "Breakout"),
    ("no deposit bonus casino 2026 real money", "Breakout"),
    ("live casino online", "+90%"),
    ("casino online games", "+70%"),
    ("casino games", "+70%"),
    ("best online pokies real money nz", "+50%"),
]

# Domains appearing as Breakout rising queries in NZ Trends — i.e. brand-name
# searches being manufactured for sites nobody had heard of a quarter ago.
TRENDS_SPAM = ["casinoarchie.com", "casinowinnernz.com", "casinokycguide.com"]

# ---------------------------------------------------------------------------
# Market and regulatory figures. Source named on every line.
# ---------------------------------------------------------------------------
MARKET = [
    ("NZ$1.36 billion", "Consumer deposits into offshore gambling sites, October 2023 &ndash; September 2025",
     "Blask market analysis"),
    ("NZ$100m+ per month", "Sustained outflow to offshore sites for more than a year",
     "Blask market analysis"),
    ("NZ$820 million", "DIA&rsquo;s own estimate of offshore deposits over the same period",
     "Department of Internal Affairs"),
    ("NZ$520.8 million", "Declared offshore operator revenue, 12 months to 30 June 2025",
     "Declared for offshore gambling duty"),
    ("NZ$700&ndash;800 million", "Industry estimate of actual offshore spend over the same period",
     "Industry estimate"),
    ("NZ$2.8 billion", "Total New Zealand land-based gambling expenditure &mdash; money lost, not turned over",
     "Department of Internal Affairs"),
    ("NZ$250.4 million", "Pub and club pokie losses, January&ndash;March 2026 quarter &mdash; down 4.94% on the previous quarter",
     "DIA gaming machine profit data"),
]

PENALTIES = [
    ("NZ$5,000,000", "Maximum civil penalty for a body corporate operating or advertising without a licence"),
    ("NZ$300,000", "Maximum civil penalty for an individual"),
    ("NZ$19,000 + GST", "Non-refundable fee simply to lodge an expression of interest"),
    ("NZ$7,500,000", "Minimum capital an applicant must evidence"),
]
