# Bonus Ledger NZ — `best online casino sites NZ`

An independent New Zealand casino affiliate site built around one idea no competitor on the
target SERP does: **every welcome offer is priced in the turnover it actually demands.**

Static HTML generated from Python. No framework, no build dependencies beyond the standard
library (plus Pillow for the one-off image script). No JavaScript on the published site, no
external requests, no cookie banner.

**43 pages · ~120,600 words · 19 operators · 15 offers priced · 61/61 Tier 1 keywords · 0 errors.**

---

## ⚠️ Before you deploy

**1. Set the domain — done; only the legal entity is still open.** `DOMAIN` is now
`pharmaconline.co.nz`, and every canonical, schema `@id`, Open Graph URL, sitemap entry,
robots.txt line and email address follows from it. The masthead wordmark is derived from
`DOMAIN` too (`LOGO_NAME` / `LOGO_TLD` / `LOGO_MARK`), so it cannot drift from the host.

```python
DOMAIN = "pharmaconline.co.nz"  # ← drives URLs, email and the logo
NAME   = "pharmaconline.co.nz"  # ← brand name: titles, schema, body copy
LEGAL  = "Bonus Ledger Media Limited"   # ← PLACEHOLDER: not a real entity
```

`LEGAL` is the one identity string still carrying the old placeholder. It appears 92 times,
in Terms, Privacy, the cookie policy and the footer, where it makes statements about who is
liable and who controls your data. Replace it with the registered company name before launch
— those are legal claims about a company that does not exist under this name.

Still to do: add a `CNAME` if deploying to GitHub Pages, and set up `editor@` and
`complaints@` mailboxes. The contact form posts to FormSubmit and needs its one-time email
confirmation.

**2. Check the author photo licence.** `images/authors/` contains five headshots supplied for
the masthead. Stock licences frequently do *not* cover depicting a person as a named author,
and gambling is often an explicitly restricted use. Originals are in `_source/authors/`.

**3. Review the ratings before launch.** The 0–10 scores are the site's central trust claim —
the running order is openly commercial, and the score is what readers are told to judge by.
They were carried over from the shared operator dataset and have not been re-derived.

**4. Legal risk worth naming.** The Racing Industry Amendment Act 2025 makes it unlawful for
anyone other than TAB NZ to **offer or promote** racing and sports betting to a person in New
Zealand. "Promote" is capable of catching an affiliate. `/online-betting/` and
`/best-sports-betting-sites/` promote offshore sportsbooks. The site states the legal position
accurately and prominently on both, but the exposure is the publisher's. Worth a conversation
with a New Zealand lawyer before launch.

---

## The editorial proposition

The site's angle is **bonus-terms forensics**. `_build/bonuscalc.py` parses each operator's own
published wagering terms and computes what the offer costs to finish:

```
turnover      = multiplier × basis          (basis = bonus, or deposit + bonus)
expected cost = turnover × (1 − RTP)        (4% at 96% RTP)
```

Across the 15 cash offers we cover that is **NZ$2,346,320 of combined turnover demanded**, of
which **3 are realistically clearable**. Kingdom's "600% up to NZ$18,500" needs **NZ$555,000** of
wagering. Slotsgem's unglamorous NZ$400 needs NZ$16,000 — and is one of the two offers we tell
readers to take.

Four things that follow, each now a section:

1. **The biggest headline is the worst offer**, because the multiplier applies to the whole bonus.
2. **The wagering *basis* matters more than the multiplier** — Smash's 10x demands more turnover
   than most 40x offers, because it multiplies the deposit too.
3. **Source-of-funds checks** are the largest real-world cause of withdrawal pain and are almost
   unwritten elsewhere. SkyCity — New Zealand's *own licensed* operator — holds **1.5/5 on
   Trustpilot, 82% one-star**, almost entirely about verification.
4. **The rinse-it-back trap**: players give up on a stuck withdrawal and gamble the balance away.
   Found verbatim in the reviews, mentioned on zero competitor pages.

Listing order is commercial and disclosed under every table. The score is not: our best-paying
partner scores 8.1, among the three lowest on the site, with a warning on every page.

---

## What's here

| Tier | Pages |
|---|---|
| **Money pages** | `/` · `/online-casinos/` · `/online-casinos/bonuses/` · `/online-pokies/` · `/high-payout-casinos/` · `/fast-payout-casinos/` · `/live-casinos/` · `/best-crypto-casinos/` · `/no-deposit-casinos/` · `/online-betting/` · `/best-sports-betting-sites/` · `/new-casinos-nz/` |
| **Reviews** | `/casino-reviews/` + 19 operator reviews |
| **Guides** | `/nz-online-casino-law/` · `/gambling-winnings-tax-nz/` · `/payment-methods/` · `/how-we-rate/` |
| **Company** | `/about/` · `/contact/` · `/authors/` · `/responsible-gambling/` |
| **Legal** | `/terms/` · `/privacy/` · `/cookie-policy/` |
| **Machine** | `/sitemap.xml` · `/robots.txt` · `/site.webmanifest` |

Strategy documents in [`docs/`](docs/):

- [`SERP-RESEARCH.md`](docs/SERP-RESEARCH.md) — live SERP teardown, competitor headings, the
  994-query NZ demand harvest, Google Trends, voice-of-customer, and the ranked content gaps
- [`COMPETITOR-ANALYSIS.md`](docs/COMPETITOR-ANALYSIS.md) · [`KEYWORD-STRATEGY.md`](docs/KEYWORD-STRATEGY.md) · [`SEO-PLAYBOOK.md`](docs/SEO-PLAYBOOK.md)
- [`research/`](docs/research/) — the raw Firecrawl captures behind every externally-sourced figure

---

## Design

**Palette: ink navy and copper.** `--navy #131C2E` for structure, `--copper #C2703A` for action,
plus `--amber`, `--teal`, `--sky` used only in the hero data tiles, where each hue carries a
meaning. The register is a financial publication rather than a casino.

**The hero** is one continuous navy panel — base gradient on the `.lede` wrapper so it runs
unbroken behind the H1, the lead copy and the byline, with the radial glows on a height-capped,
masked `::before`. Reading order differs by viewport:

```
Desktop:  H1 → top-offer strip → lead + stats → byline → toplist → disclosures
Mobile:   H1 → byline → toplist → lead + stats → disclosures
```

**Above the fold on mobile** (measured at 390px): H1 at 90px, byline to 252, toplist H2 at 271,
the affiliate card at 318, first CTA fully visible by 682. That ordering is deliberate and
fragile — see the note in `lede()` before changing it.

**The affiliate table becomes a card below 760px** — rank and badge on one line, then logo, name,
score, offer panel and a full-width CTA. `display:contents` flattens the wrappers so their
children reorder as grid items without duplicate markup.

**The welcome offer is the loudest element** in every row and card: tinted panel, 19–22px type,
its own label. Plus a sponsored top-offer strip in the hero (desktop only, 385px) so a bonus is
on screen the moment the page opens rather than 1,200px down.

**Navigation** is nested — 9 top-level items, 6 CSS-only dropdowns on `:hover`/`:focus-within`,
43 links covering every page. The hamburger is mobile-only (≤1100px).

---

## Building

```bash
python3 _build/build.py          # regenerates all 43 pages + sitemap + robots (~1s)
python3 _build/check_site.py     # technical guard — must print "all checks passed"
python3 _build/check_keywords.py # coverage + anti-stuffing — must print "coverage complete"
python3 _build/gen_images.py     # one-off: favicons, apple-touch-icon, .ico, .svg, OG card
```

Output is written in place. This directory **is** the deployed site.

### Where things live

| File | Controls |
|---|---|
| `_build/lib.py` | **Domain, brand, email, month stamp.** Authors, nested nav, footer, page titles and descriptions, schema builders, and every shared component — `lede()`, `leaderboard()`, `top_offer_strip()`, `avatar()`, tables, FAQ, cards, steps |
| `_build/bonuscalc.py` | **The Ledger.** Parses wagering terms and prices every offer. Every dollar figure on the site comes from here |
| `_build/operators.json` | The 19 operators — links, bonuses, payout windows, licensing, and `order` (the supplied commercial order, which drives every leaderboard). **Facts only.** |
| `_build/voice.py` | This masthead's own copy per operator — tagline, pros, cons, verdict, long-form review |
| `_build/lawdata.py` | Licensing timeline, legal facts, helplines, bank-block data |
| `_build/research.py` | 994 harvested NZ queries, Google Trends, market figures |
| `_build/p_*.py` | One module per page group |
| `_build/keywords.py` | The 253-term keyword map, per page, as data |
| `assets/css/site.css` | The entire stylesheet, no JS |
| `images/authors/` | Author headshots, 148×148 JPEG (originals in `_source/authors/`) |
| `logos/` | Operator logos |

### Monthly maintenance

Change `MONTH` in `lib.py` (and `YEAR` each January) and rebuild. Every title, description, H1
and "updated" line follows. A stale month in a title is worse than no month, so this is a
standing commitment.

---

## Build guard

`check_site.py` fails the build on: broken internal or asset links · missing or duplicate
`<title>` or meta description · a canonical that is not self-referencing · invalid JSON-LD ·
`.html` in any URL · a page without exactly one `<h1>` · a missing responsible-gambling helpline,
age statement or affiliate disclosure · About or Contact absent from the main nav · a
sitemap/filesystem mismatch · a missing robots.txt rule or favicon size · any title wider than
580px when rendered.

Titles are measured in **pixels**, not characters, because that is how Google truncates them.

`check_keywords.py` enforces Tier 1 coverage per page and fails on stuffing or cannibalisation —
it is what caught a nav label putting a reserved term on a page forbidden from targeting it.

---

## Notes

- **CSS is served without cache-busting.** Any stylesheet change will look like it did not apply
  until a hard reload. Worth wiring a content hash into the `<link>` if this becomes annoying.
- **No `AggregateRating` on hub pages**, deliberately — Google restricts self-serving aggregate
  ratings. `Review` schema is used on the 19 operator pages, where it belongs.
- **Figures are only what we can stand behind.** An earlier draft claimed "214 timed withdrawals";
  that was another site's dataset and has been removed everywhere. What we publish is the
  operators' own stated windows, the 15 offers priced from published terms, the 994-query harvest
  and the Trustpilot capture.
- **Reddit blocks automated access**, so it is cited from search-result snippets only and no post
  bodies are reproduced. The site says so on `/fast-payout-casinos/#sources`.
- **`evospin.png`** is present in `logos/` but unused — not on the supplied operator list.
