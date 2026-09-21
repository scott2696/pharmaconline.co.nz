#!/usr/bin/env python3
"""The Ledger: what a welcome offer actually costs to clear.

Every figure on this site that carries a dollar sign is produced here, from the
operator's own published headline and wagering basis. Nothing is estimated from
a rate card and nothing is copied from an operator's marketing.

The arithmetic is deliberately simple so a reader can check it:

    turnover = multiplier x base
    expected cost = turnover x (1 - RTP)

`base` is whatever the operator says it is. "40x bonus" multiplies the bonus.
"10x deposit + bonus" multiplies both, which is the more expensive basis and the
one operators tend not to draw attention to. Where an offer states a total match
percentage we can recover the qualifying deposit from the cap, which is the only
way to price a "deposit + bonus" requirement honestly.

FX is applied at a published, dated rate. A euro-denominated bonus is not worth
its face value to a New Zealander and pretending otherwise is the single most
common error on competing pages.
"""
import re

# Mid-market, captured 2026-09-20. Republished monthly with the month stamp.
FX_DATE = "20 September 2026"
FX = {"EUR": 1.84, "USD": 1.68, "USDT": 1.68, "NZD": 1.0}

# The round-trip conversion cost a New Zealand player carries on a euro or USD
# balance: card/e-wallet conversion in, and again on withdrawal. This is the
# typical retail FX margin on those rails, not a figure specific to one operator.
FX_SPREAD = 0.048

DEFAULT_RTP = 0.96

# Turnover thresholds, in NZD, for the verdict language used across the site.
CLEARABLE, PUNISHING = 20_000, 100_000


def _num(s):
    return float(s.replace(",", ""))


def parse_bonus(op):
    """(currency, face_value, nzd_value) for the headline cash bonus, or None.

    Reads the operator's own casino_bonus string. Free spins are counted
    separately and never folded into a cash figure, because they are not cash.
    """
    b = op.get("casino_bonus") or ""
    m = re.search(r"(NZ\$|€|\$)\s*([\d,]+(?:\.\d+)?)", b)
    if m:
        cur = {"NZ$": "NZD", "€": "EUR", "$": "NZD"}[m.group(1)]
        face = _num(m.group(2))
        return cur, face, round(face * FX[cur])
    m = re.search(r"([\d,]+)\s*USDT", b)
    if m:
        face = _num(m.group(1))
        return "USDT", face, round(face * FX["USDT"])
    return None


def parse_spins(op):
    b = op.get("casino_bonus") or ""
    m = re.search(r"(\d+)\s*(?:no-deposit\s*)?(?:free\s*)?spins", b, re.I)
    return int(m.group(1)) if m else 0


def parse_match(op):
    """Total match percentage from the headline, e.g. 390% or 600%."""
    m = re.search(r"([\d,]+)\s*%", op.get("casino_bonus") or "")
    return _num(m.group(1)) if m else None


def parse_wagering(op):
    """(multiplier, base) where base is 'bonus', 'deposit+bonus', 'freebet' or None."""
    w = (op.get("wagering") or "").lower()
    if not w:
        return None, None
    # A brand running both a casino and a sportsbook offer states both bases in
    # one string ("40x bonus / 6x free bet"). The casino basis is the one that
    # prices the casino bonus, so it wins; the free-bet basis is only used when
    # there is nothing else.
    m = re.search(r"([\d.]+)\s*x\s*(?:on\s+)?(?:the\s+)?(?:deposit|bonus|crypto|wagering)", w)
    if m:
        mult = float(m.group(1))
        seg = w[:m.end() + 24]
        base = "deposit+bonus" if ("deposit" in seg and "bonus" in seg) else "bonus"
        return mult, base
    if "free bet" in w or "odds of" in w:
        m = re.search(r"([\d.]+)\s*x", w)
        return (float(m.group(1)) if m else None), "freebet"
    m = re.search(r"([\d.]+)\s*x", w)
    if not m:
        return None, None
    return float(m.group(1)), "bonus"


def price(op, rtp=DEFAULT_RTP):
    """The full ledger entry for an operator's welcome offer.

    Returns None where there is no cash casino bonus to price (sportsbook-only
    brands, and brands whose offer we have not been able to verify).
    """
    pb = parse_bonus(op)
    mult, base = parse_wagering(op)
    if not pb or mult is None or base == "freebet":
        return None
    cur, face, bonus_nzd = pb

    match = parse_match(op)
    deposit_nzd = None
    if base == "deposit+bonus":
        # Recover the qualifying deposit from the cap and the stated match.
        # 600% total up to NZ$19,500 means NZ$3,250 of the player's own money.
        deposit_nzd = round(bonus_nzd / (match / 100)) if match else bonus_nzd
        staked = bonus_nzd + deposit_nzd
    else:
        staked = bonus_nzd

    turnover = round(mult * staked)
    cost = round(turnover * (1 - rtp))
    fx_cost = round((bonus_nzd + (deposit_nzd or 0)) * FX_SPREAD) if cur != "NZD" else 0

    if turnover >= PUNISHING:
        verdict, tone = "Effectively unclearable", "no"
    elif turnover >= CLEARABLE:
        verdict, tone = "Punishing", "warn"
    elif turnover > 0:
        verdict, tone = "Genuinely clearable", "yes"
    else:
        verdict, tone = "No wagering", "yes"
    if mult == 0:
        verdict, tone = "No wagering", "yes"
        turnover, cost = 0, 0

    return {
        "currency": cur, "face": face, "bonus_nzd": bonus_nzd,
        "deposit_nzd": deposit_nzd, "match": match,
        "mult": mult, "base": base, "staked": staked,
        "turnover": turnover, "cost": cost, "rtp": rtp,
        "fx_cost": fx_cost, "spins": parse_spins(op),
        "verdict": verdict, "tone": tone,
        "ratio": round(cost / bonus_nzd, 2) if bonus_nzd else None,
    }


def basis_label(p):
    return "deposit + bonus" if p["base"] == "deposit+bonus" else "bonus only"


def money(n):
    return f"NZ${n:,.0f}"
