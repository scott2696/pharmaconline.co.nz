#!/usr/bin/env python3
"""New Zealand gambling law and licensing, as data.

Single source of truth for every dated claim on the site. The tracker computes
"days remaining" at build time, so a rebuild keeps the page honest and a page
that has gone stale is visibly stale rather than quietly wrong.

Primary sources (all linked from /nz-online-casino-law/):
  Online Casino Gambling Act 2026 — in force 1 May 2026
  DIA, "Online Gambling for Providers" — the three-stage licensing process
  Racing Industry Amendment Act 2025 — in force 28 June 2025
  Gambling Act 2003 — the pre-existing framework, still operative
  Inland Revenue — problem gambling levy, offshore gambling duty
"""
import datetime

TODAY = datetime.date.today()

# (date, stage, detail, kind)
STAGES = [
    (datetime.date(2026, 5, 1), "Online Casino Gambling Act 2026 in force",
     "The Act commences, creating New Zealand's first domestic online casino "
     "licensing regime and replacing an unregulated offshore market.", "done"),
    (datetime.date(2026, 7, 17), "Expressions of interest open",
     "Stage one of three. NZ$19,000 + GST per expression of interest, "
     "non-refundable. Applicants must evidence NZ$7.5m minimum capital.", "done"),
    (datetime.date(2026, 8, 14), "Expressions of interest close",
     "Around fifty expressions of interest were lodged for fifteen licences. "
     "The DIA has confirmed the round was oversubscribed and will not name "
     "who applied.", "done"),
    (datetime.date(2026, 9, 29), "Licence auction",
     "A multi-round simultaneous ascending clock auction. The price rises in "
     "steps until demand matches the fifteen licences available. Participants "
     "are not made public.", "next"),
    (datetime.date(2026, 10, 1), "Full applications open",
     "Successful bidders file business plans, advertising and marketing "
     "strategy, AML/CFT programme and harm-minimisation measures.", "upcoming"),
    (datetime.date(2026, 12, 1), "Unlicensed operators must stop",
     "Any operator that has not applied must stop offering online casino "
     "gambling to New Zealanders. Operators with a pending application may "
     "continue to operate, but not advertise, until it is decided.", "cutoff"),
    (datetime.date(2027, 1, 1), "Duty rises to 16%",
     "The offshore gambling duty on licensed online casino operators rises "
     "from 12% to 16% of gross gambling revenue, alongside 15% GST and the "
     "1.24% problem gambling levy.", "upcoming"),
    (datetime.date(2027, 3, 31), "Licensed market expected live",
     "Government expects the regulated market to be operational in early "
     "2027. This quarter is our estimate, not a published date.", "estimate"),
    (datetime.date(2027, 6, 1), "Transitional arrangement ends outright",
     "An operator that applied before 1 December 2026 may keep serving New "
     "Zealanders — without advertising — until its application is decided or "
     "1 June 2027, whichever comes first. After that the transition is over "
     "and unlicensed supply is simply unlawful.", "cutoff"),
]

CUTOFF = datetime.date(2026, 12, 1)
BACKSTOP = datetime.date(2027, 6, 1)
AUCTION = datetime.date(2026, 9, 29)

FACTS = [
    ("Licences available", "15"),
    ("Maximum per operator", "3 (one brand each)"),
    ("Licence term", "3 years, renewable 5"),
    ("EOI fee", "NZ$19,000 + GST"),
    ("Minimum capital", "NZ$7.5m"),
    ("Duty from 1 Jan 2027", "16% of GGR"),
    ("Problem gambling levy", "1.24%"),
    ("Affiliate marketing by licensees", "Prohibited"),
    ("Penalty, unlicensed company", "Up to NZ$5m"),
    ("Penalty, unlicensed individual", "Up to NZ$300k"),
    ("Hard backstop for applicants", "1 June 2027"),
]

# Legal age. The 18/20 split is genuinely New Zealand-specific and almost
# every competitor page gets it wrong or omits it.
AGE_ONLINE = 18
AGE_LAND = 20

HELP = [
    ("Gambling Helpline Aotearoa", "0800 654 655", "https://gamblinghelpline.co.nz/",
     "Free, confidential, 24 hours a day, seven days a week. Phone, text 8006 or web chat."),
    ("Problem Gambling Foundation", "0800 664 262", "https://www.pgf.nz/",
     "Free face-to-face and online counselling nationwide, plus support for family and wh&#257;nau."),
    ("Safer Gambling Aotearoa", "0800 000 501", "https://safergambling.org.nz/",
     "Kaupapa M&#257;ori and Pasifika services alongside mainstream counselling."),
    ("Asian Family Services", "0800 862 342", "https://asianfamilyservices.nz/",
     "Counselling in Mandarin, Cantonese, Korean, Japanese, Thai, Vietnamese and Hindi."),
]

# NZ bank gambling-block availability, checked September 2026.
BANK_BLOCKS = [
    ("ANZ", "Yes", "Card controls in the ANZ goMoney app; blocks gambling merchant category codes."),
    ("ASB", "Yes", "Merchant category blocking available on request through ASB support."),
    ("BNZ", "Yes", "Self-service gambling block in the BNZ app, with a cooling-off period before it can be lifted."),
    ("Westpac", "Yes", "Gambling block available on debit and credit cards via Westpac One."),
    ("Kiwibank", "Partial", "Blocking available on request; not self-service at the time of checking."),
    ("TSB", "Partial", "Case-by-case through support rather than an in-app control."),
]


def days_to(d):
    return (d - TODAY).days


def stage_status(d, kind):
    if d <= TODAY:
        return "done"
    if kind == "estimate":
        return "estimate"
    nxt = next_upcoming()
    return "next" if d == nxt else "upcoming"


def next_upcoming():
    fut = [d for d, *_ in STAGES if d > TODAY]
    return fut[0] if fut else None
