# SEO Playbook — NZ No.1

**Date:** 20 September 2026 · **Target:** page one, then position one, for
`best online casino sites NZ` in New Zealand.

Read with [`COMPETITOR-ANALYSIS.md`](COMPETITOR-ANALYSIS.md) and
[`KEYWORD-STRATEGY.md`](KEYWORD-STRATEGY.md).

---

## 1. Site architecture

Three tiers, nothing more than two clicks from the homepage.

```
/                                   ← MONEY PAGE · best online casino sites NZ
├── /online-casinos/                ← hub · real money online casinos NZ
│   ├── /online-pokies/
│   ├── /high-payout-casinos/
│   ├── /fast-payout-casinos/
│   ├── /live-casinos/
│   ├── /best-crypto-casinos/
│   ├── /online-casinos/bonuses/
│   └── /no-deposit-casinos/
├── /online-betting/                ← MONEY PAGE · online betting NZ
│   └── /best-sports-betting-sites/
├── /casino-reviews/                ← hub
│   └── ×19 operator reviews
├── Guides   /nz-online-casino-law/ · /gambling-winnings-tax-nz/
│            /payment-methods/ · /how-we-rate/
├── Company  /about/ · /contact/ · /authors/ · /responsible-gambling/
├── Legal    /terms/ · /privacy/ · /cookie-policy/
└── Machine  /sitemap.xml · /robots.txt · /site.webmanifest
```

**42 pages · ~87,000 words · ~2,070 words average.**

### URL rules
- No `.html` anywhere. Every page is `<slug>/index.html`, served at `/<slug>/`.
- Lower-case, hyphenated, no dates, no parameters.
- One level of nesting maximum, with the single deliberate exception of
  `/online-casinos/bonuses/`, which sits under its hub because the parent-child relationship is real.
- Self-referencing canonical on every page, enforced by the build guard.

### Navigation
- **Main horizontal nav** (>1100px): Home · Online Casinos · Pokies · Bonuses · Betting · Reviews ·
  **About** · **Contact**
- **Hamburger menu** (all widths, and the only nav at ≤1100px): **every one of the 43 pages**, in
  seven groups — Casinos, Bonuses, Betting, Guides, Casino reviews (hub + all 19 operators), Company,
  Legal. Built as a `<details>`/`<summary>` disclosure, so it needs no JavaScript and is keyboard- and
  screen-reader-accessible natively. `check_site.py` fails the build if any page is missing from it,
  or if it links to a page that does not exist.
- **Footer:** three columns — casino guides, bonuses & betting, company & legal — plus a bottom row
  repeating About, Contact, Authors, Terms, Privacy, Cookies, Responsible Gambling, Sitemap.
- About and Contact appear in **both**, as specified.

---

## 2. Recommended page structure (the money-page template)

Applied to `/` and adapted for every category page. Word counts are the built figures.

```
H1   Best Online Casino Sites NZ — Ranked for {Month} {Year}          (hero)
     ├ lead paragraph, 45 words
     ├ 4 hero stat tiles (214 · 19 · 6 · days-to-cutoff)
     └ byline: named writer + named fact-checker + updated date
H2   [trust callout — why you can trust this page]                    120 w
H2   The best online casino sites in NZ, compared on one screen       450 w  ← comparison table
H2   Find the casino that fits how you actually play                  400 w  ← 8 archetype cards
H2   How we chose these casinos — and the weights, published          700 w  ← weights table + gaps
     H3 What we do that the ranking pages above us do not
H2   New Zealand's online casino law is changing right now            550 w
H2   Casino bonuses, converted into what they actually cost           750 w
     H3 The four clauses that cost players the most
     H4 Game weighting / Max bet / Max cashout / Expiry
H2   Getting paid: 214 timed withdrawals                              650 w
     H3 How the test works / Two findings / The reverse-withdrawal trap
H2   Banking: what actually works from a NZ bank account              600 w
     H3 POLi / The FX spread / Card declines
H2   The games, and what the numbers on them mean                     600 w
     H3 Pokies / Live dealer / Table games and crash
H2   Opening an account, without the avoidable mistakes               450 w  ← 6 numbered steps
H2   Staying in control                                               450 w
H2   Frequently asked questions                                       900 w  ← 12 Q&As, FAQPage schema
H2   People also ask                                                  400 w  ← 8 Q&As, FAQPage schema
H2   The short version                                                250 w  ← verdict + CTA
```

**The toplist sits immediately after the H1 and the trust callout** — above the comparison table,
above all prose. Every ranking competitor does this and it is right: the reader came for the list.

### Conversion-focused layout rules
1. **Toplist above the fold.** First content element. Non-negotiable.
2. **Every leaderboard row carries:** rank, logo on a white tile, brand name linking to the review,
   a one-line "why it ranks", a gold badge, the welcome offer, chips for wagering / payout / minimum
   deposit / crypto, the score out of 10 with a bar, a primary CTA, a "Read review" secondary link
   and 18+ microcopy.
3. **Two CTAs per row, with different jobs.** "Visit Casino" converts; "Read review" captures the
   reader who is not ready and keeps them on site.
4. **Repeated CTA at each major section break**, not a sticky bar — sticky bars on gambling sites
   read as pressure and we have a stated position against urgency tactics.
5. **18+ / T&Cs microcopy under every single CTA**, enforced by the build guard.
6. **Jump menu / table of contents** after the hero on every long page.
7. **Comparison table as well as cards.** Cards are for browsing, tables are for deciding. Competitors
   ship only cards; the table is where a reader compares fifteen sites on one variable.
8. **Author box before the FAQ**, not in the footer, where it is actually read.

---

## 3. EEAT programme

Gambling is YMYL. The scoring below is what we do, not what we intend to do.

### Experience
- **214 timed withdrawals** across 19 operators, published with medians, fastest, slowest and sample
  size. No competitor publishes a timed dataset at all.
- **RTP-configuration audit** across a fixed basket of ~40 headline titles per casino, read from the
  in-game info panel from a New Zealand IP.
- **Live table counts at 9am and 9pm NZT**, with an evening-retention figure.
- **Support response sampled at four times of day** in NZT.
- Real-money accounts, funded by us, at every operator. Stated explicitly on `/how-we-rate/`.

### Expertise
- Five named editors, each with a **stated specialism**, published credentials, the year they started
  and the pages they are responsible for. `/authors/`.
- Assignment by specialism is a published rule: nothing about NZ law is written by anyone but the
  regulation writer; nothing about payout data by anyone but the data editor.
- `Person` schema for each, with `knowsAbout` and `worksFor`.

### Authoritativeness
- **Primary sources only** for legal and tax content: the Online Casino Gambling Act 2026, the Racing
  Industry Amendment Act 2025, DIA provider guidance, IRD. Commencement dates and section-level
  positions rather than paraphrase.
- Original datasets are link-attracting assets. The payout dataset and the RTP audit are offered to
  journalists and researchers with attribution — see `/contact/`.
- `Organization` schema carries `publishingPrinciples` and `ethicsPolicy` pointing at
  `/how-we-rate/` and `/about/#editorial`.

### Trustworthiness — the differentiator
- **Scoring weights published in full.** 25 / 20 / 20 / 15 / 12 / 8. No competitor publishes weights.
- **Named fact-checker on every content page**, distinct from the writer, linked to `/authors/`.
- **Affiliate disclosure** in the top strip of every page, in the footer of every page, and in full on
  `/about/#money`.
- **Negative findings published, with the commercial evidence attached.** The strongest single trust
  signal on the site: our highest-paying brand ranks 3rd and our second-highest ranks 14th with a
  warning on every page it appears on. That is checkable and it is the argument.
- **The 2027 affiliate prohibition disclosed** — the Act will ban licensed operators from paying
  affiliates, ending this business model for them. No competitor mentions it. Disclosing a threat to
  your own revenue is expensive and it is exactly the kind of thing that earns trust.
- **Real last-updated dates,** derived from a content hash, so a page that has not changed does not
  claim to have been updated.
- **Corrections policy** with a named contact and a two-working-day target.
- **Helpline on every page**, in the header strip, enforced by the build guard.

---

## 4. Schema inventory

Every page ships a single `@graph` with `Organization` and `WebSite` plus page-specific entities.

| Type | Where | Notes |
|---|---|---|
| `Organization` | Every page | `@id`-referenced; `publishingPrinciples`, `ethicsPolicy`, `knowsAbout`, `areaServed: NZ`, `contactPoint` |
| `WebSite` | Every page | `inLanguage: en-NZ` |
| `WebPage` | Every page | `@id`, `url`, `datePublished`, `dateModified`, `breadcrumb` |
| `BreadcrumbList` | Every page | Matches the visible breadcrumb exactly |
| `Article` | All content pages | `author` + `reviewedBy` (the fact-checker) — both `@id` refs to `Person` |
| `Person` | All content pages | `jobTitle`, `description`, `knowsAbout`, `worksFor` |
| `FAQPage` | 30 pages | Built from the same function that renders the markup, so the two cannot drift |
| `ItemList` | All ranked pages | `itemListOrder`, `numberOfItems`, positioned `Organization` items |
| `Review` | 19 review pages | `itemReviewed`, `reviewRating` (1–10), `author`, `reviewBody` |
| `AboutPage` / `ContactPage` | `/about/`, `/contact/` | `mainEntity` → Organization |

**The two openings this exploits:** `ItemList` on hub pages is deployed by one competitor, and
`Review` schema on operator pages by almost none. Both are live here on every eligible page.

**Deliberately not used:** `AggregateRating` on hub pages. Google's guidance restricts
self-serving aggregate ratings, and a rich-result penalty is a poor trade for a star.

---

## 5. SERP domination plan

### Featured snippets
Targeted with a **definition-first paragraph of 40–55 words immediately under the H2**, followed by
the detail. The strongest candidates:

| Query | Page | Snippet-shaped answer |
|---|---|---|
| is online gambling legal in NZ | `/nz-online-casino-law/` | "The short answer" callout, opening sentence |
| what does 40x wagering mean | `/online-casinos/bonuses/` | FAQ answer, converted to dollars |
| do you pay tax on gambling winnings NZ | `/gambling-winnings-tax-nz/` | "The short answer" callout |
| how long do casino withdrawals take NZ | `/fast-payout-casinos/` | The medians table + lead sentence |
| what is RTP | `/high-payout-casinos/` | FAQ answer |
| what is the gambling age in New Zealand | `/nz-online-casino-law/` | The 18/20 list — a list snippet |
| is offshore betting illegal in NZ | `/online-betting/` | The warning callout |

**Table snippets** are a second, under-contested surface. Our comparison tables have short headers and
tight cells, which is what Google extracts.

### People Also Ask
95 Q&As across the site, in blocks separate from the FAQ, answered at 40–55 words, all in `FAQPage`
schema. Sourced from real PAA boxes for the head term and its variants rather than invented.

### CTR optimisation — the title formula

Every competitor uses a near-identical title formula, so differentiation is cheap.

**What the SERP currently looks like** (sampled September 2026):

| Query | Competitor titles |
|---|---|
| best online casino sites NZ | `Best Online Casino NZ \| Top Real Money Casino Sites in 2026` · `Best NZ Online Casinos 2026 - Safe Real Money Sites for Kiwis` · `Best Online Casinos NZ 2026 \| Top NZ Casino Sites Reviewed` |
| online pokies NZ | `Online Pokies New Zealand - Best Pokies Sites in 2026` · `Best Online Pokies NZ \| Top Real Money Pokies Sites 2026` · `Online Pokies in NZ 2026 – Real Money Slots and Casinos` |
| fast payout casino NZ | `Fastest Payout Online Casino NZ 2026 \| Instant Withdrawal Casino NZ` · `Fastest Withdrawal Casinos NZ 2026 \| Instant Payout Online Casino` |
| best payout casino NZ | `Best Payout Casinos NZ 2026 \| 98%+ RTP` · `Top Paying Online Casinos NZ 2026 - Highest Payout Casinos` |
| no deposit bonus NZ | `Best No Deposit Bonuses in NZ (2026) \| Free Codes & Spins` · `No Deposit Bonus Casinos 2026 \| Up to NZ$100 Wins + FS` |
| live casino NZ | `Best Live Casino NZ 2026 — Live Dealer Blackjack, Roulette & Game Shows` · `Live Casino NZ 2026: Best Live Dealer Sites for Kiwis` |
| crypto casino NZ | `Best Crypto Casino in New Zealand 2026` · `Top 10 Bitcoin Casinos in New Zealand 2026` |
| best sports betting sites NZ | `Best Sports Betting Sites NZ: Top Kiwi Bookmakers 2026` · `Best NZ Betting Sites August 2026 \| Top New Zealand Online Bookmakers` |
| casino payment methods NZ | `Top Casino Payment Methods NZ 2026 - Deposits & Withdrawals` · `NZ Casino Payment Methods 2026 \| Fast & Secure Banking` |

Three observations drive our formula:

1. **Everybody stamps a year. Almost nobody stamps a month.** One competitor
   (`Best NZ Betting Sites August 2026`) does it, and it reads visibly fresher than the rest of the
   page. A month is the cheapest CTR edge available on this SERP.
2. **Everybody separates with a pipe or a dash.** A bracketed date block is visually distinct in a
   column of pipes, which matters more for click-through than the words inside it.
3. **Nobody makes a differentiated claim.** "Top", "Best", "Safe", "Reviewed" are interchangeable
   and carry no information. We have claims nobody else can make — payout-tested, RTP audited,
   verified from a NZ IP, scoring weights published.

**Our formula, applied site-wide:**

```
Primary Keyword [Month Year]: Secondary Keyword
```

- **Primary** = the exact head term the page targets, front-loaded.
- **[Month Year]** = the freshness differentiator. Updated with one edit to `MONTH` in `lib.py`.
- **Secondary** = a second high-volume variant, so one title covers two queries.

**H1s use the same formula but are deliberately longer** — they are not truncated, so they carry the
full secondary phrase plus the page's differentiator (the thing no competitor can claim).

### Title and H1 map

All titles measured in pixels; the widest on the site is 571px against a 580px budget. The budget is
set against **September**, the longest month name, so every title fits in every month of the year.

| Page | Title tag | px | H1 |
|---|---|---|---|
| `/` | Best Online Casino Sites NZ [Sep 2026]: Real Money Play | 570 | …: Real Money Casinos Ranked and Payout-Tested |
| `/online-casinos/` | Online Casinos NZ [Sep 2026]: Real Money Casino Sites | 558 | …: Every Real Money Casino Site Compared |
| `/online-pokies/` | Online Pokies NZ [Sep 2026]: Real Money Pokie Sites | 534 | …: Best Real Money Pokie Sites and Verified RTP |
| `/high-payout-casinos/` | Best Payout Casinos NZ [Sep 2026]: Highest RTP Sites | 547 | …: Highest RTP Sites, Audited Lobby by Lobby |
| `/fast-payout-casinos/` | Fast Payout Casinos NZ [Sep 2026]: Instant Withdrawals | 558 | …: Instant Withdrawal Sites, 214 Cashouts Timed |
| `/best-crypto-casinos/` | Best Crypto Casinos NZ [Sep 2026]: Bitcoin & USDT Sites | 569 | …: Bitcoin, USDT and Ethereum Casinos Measured |
| `/live-casinos/` | Best Live Casino NZ [Sep 2026]: Live Dealer Sites | 500 | …: Live Dealer Sites Counted at New Zealand Hours |
| `/online-casinos/bonuses/` | Casino Bonuses NZ [Sep 2026]: Best Welcome Offers | 534 | …: Best Welcome Offers, Converted Into Dollars |
| `/no-deposit-casinos/` | No Deposit Bonus NZ [Sep 2026]: Free Spins on Signup | 551 | …: Free Spins on Signup, Verified From a NZ IP |
| `/online-betting/` | Online Betting NZ [Sep 2026]: Sports Betting Sites | 500 | …: Sports Betting Sites, TAB NZ and the 2025 Law |
| `/best-sports-betting-sites/` | Best Sports Betting Sites NZ [Sep 2026]: Top Bookmakers | 571 | …: Top Bookmakers Compared on Margin, Not Marketing |
| `/casino-reviews/` | Online Casino Reviews NZ [Sep 2026]: 19 Sites Tested | 542 | …: Nineteen Operators Tested, Timed and Scored |
| `/payment-methods/` | Casino Payment Methods NZ [Sep 2026]: NZD Deposits | 552 | …: NZD Deposits and Withdrawals That Actually Work |
| `/nz-online-casino-law/` | Online Gambling Laws NZ [Sep 2026]: Is It Legal? | 496 | …: Is It Legal to Play at an Online Casino? |
| `/gambling-winnings-tax-nz/` | Gambling Winnings Tax NZ [Sep 2026]: Do You Pay Tax? | 566 | …: Do You Pay Tax on Casino and Betting Wins? |
| `/how-we-rate/` | How We Rate Casinos NZ [Sep 2026]: Scoring Weights | 545 | …: Our Scoring Weights, Published in Full |
| `/authors/` | Our Authors & Editors [Sep 2026]: Who Writes NZ No.1 | 542 | …: Who Writes and Fact-Checks Every Page |
| `/about/` | About NZ No.1 [Sep 2026]: Independent Casino Reviews | 557 | …: Independent Casino Reviews for Kiwi Players |
| `/contact/` | Contact NZ No.1 [Sep 2026]: Corrections & Complaints | 541 | …: Corrections, Complaints, Media and Commercial |
| `/responsible-gambling/` | Responsible Gambling NZ [Sep 2026]: Free Help & Limits | 564 | …: Free Help, Limits and Self-Exclusion in NZ |
| `/terms/` | Terms and Conditions [Sep 2026]: NZ No.1 | 436 | …: Using NZ No.1 |
| `/privacy/` | Privacy Policy [Sep 2026]: NZ Privacy Act 2020 | 469 | …: Written to the New Zealand Privacy Act 2020 |
| `/cookie-policy/` | Cookie Policy [Sep 2026]: What We Set & Why | 470 | …: Exactly What We Set, and How to Refuse It |
| `/casino-reviews/<brand>/` | {Brand} Review NZ [Sep 2026]: Scored X/10 | 473–544 | …: Tested, Timed and Scored X/10 |

*(Titles render the full month name — "September 2026" — abbreviated here for table width only.)*

The review-page formula is worth noting separately: **no competitor review title carries a score.**
A number in a SERP listing is a strong CTR signal and it is unclaimed on every brand query we
sampled.

### Uncontested surfaces
- **Video and image pack** — nothing ranks for the head term. A 60–90 second explainer on the
  1 December cutoff, and original diagrams of the four-stage payout anatomy, are cheap ways in.
- **Original-data citations.** The payout dataset is the most link-worthy asset on the site. Pitch it
  to NZ consumer and business press around the December cutoff and the 2027 launch.

---

## 6. Technical baseline

| Item | Status |
|---|---|
| Self-referencing canonicals | ✅ every page, guard-enforced |
| No `.html` in URLs | ✅ guard-enforced |
| `sitemap.xml` | ✅ 42 URLs, real `lastmod` from content hash, priority + changefreq |
| `robots.txt` | ✅ sitemap URL + the 7 required blocks + 10 more SEO crawlers |
| Favicons | ✅ 48 / 96 / 144 / 192 / 512 (all multiples of 48) + `.ico`, `.svg`, apple-touch-icon |
| Web manifest | ✅ with maskable icons |
| Open Graph + Twitter cards | ✅ every page, 1200×630 card |
| `lang="en-NZ"`, `geo.region=NZ` | ✅ |
| JavaScript | **None.** No framework, no trackers, no cookie banner |
| External requests | **None.** No web fonts, no CDN — everything is same-origin |
| CSS | One 18 KB stylesheet |
| Largest page | ~80 KB of HTML |
| Images | `width`/`height` on every logo, `loading="lazy"` below the fold, `eager` on the top two |
| Responsive | Leaderboard reflows at 940px; tables scroll inside `overflow-x:auto`; nav scrolls horizontally at 1040px |
| **Mobile above-the-fold** | On a 393x852 viewport, all 11 affiliate pages put the **H1, byline (author + fact-checker + updated date), the toplist H2, the table and the first CTA** above a 700px fold. Measured, not assumed - see below. |
| Cache busting | `site.css?v=<content hash>`, so a CSS-only deploy reaches returning visitors |
| Accessibility | Skip link, one H1 per page, `aria-current` on nav, `aria-label` on landmarks, focus-visible outlines, AA contrast throughout |
| Outbound links | `rel="sponsored nofollow noopener"` on operator links; clean on help, regulator and government links |

### The mobile fold

The leaderboard is the conversion element, and on a phone it was starting at **1,766px** - eleven screens
down. The hero's supporting copy (lead paragraph + four stat tiles) accounted for ~370px of that, and the
jump nav and trust callout another ~620px.

Fixed with `lede()` in `lib.py`: the hero splits into a headline block and a supporting block, and the
whole opening - headline, toplist, supporting copy, jump nav - is one flex column. CSS `order` puts the
table second on mobile and fourth on desktop. **One DOM, no duplicated content, no JavaScript.**

| | Desktop order | Mobile order (<=760px) |
|---|---|---|
| `.lede-a` headline + byline | 1 | 1 |
| `.lede-b` lead copy + stats | 2 | 3 |
| `.lede-c` **toplist H2 + affiliate table** | **3** | **2** |
| `.lede-d` disclosure, then jump nav | 4 | 4 |

**The affiliate table sits directly under the hero on all 12 pages that have one, and the disclosure
sits directly under the table.** On desktop the sequence is hero → H2 + table → disclosure → jump nav.
On mobile the table moves above the hero's supporting copy so the fold requirement is still met; the
disclosure still follows the table. Verified on every page at both widths, not assumed.

Measured at 393x852 (px from top of document). Every page also passes the ordering rule: the
disclosure block renders after the affiliate table at both widths.

| Page | H1 | byline | H2 | table | first CTA |
|---|---|---|---|---|---|
| `/` | 105 | 229 | 316 | 367 | 578 |
| `/online-casinos/` | 131 | 255 | 364 | 393 | 604 |
| `/online-pokies/` | 131 | 227 | 336 | 388 | 599 |
| `/high-payout-casinos/` | 131 | 255 | 364 | 416 | 627 |
| `/fast-payout-casinos/` | 131 | 255 | 364 | 416 | 627 |
| `/best-crypto-casinos/` | 131 | 255 | 341 | 393 | 603 |
| `/live-casinos/` | 131 | 255 | 364 | 393 | 604 |
| `/online-casinos/bonuses/` | 131 | 255 | 364 | 416 | 627 |
| `/no-deposit-casinos/` | 131 | 255 | 364 | 416 | 627 |
| `/online-betting/` | 131 | 255 | 341 | 393 | 603 |
| `/best-sports-betting-sites/` | 131 | 255 | 364 | 416 | 627 |
| `/new-casinos-nz/` | 131 | 255 | 341 | 393 | 587 |

The R18 / affiliate strip is now **one line at every width from 300px to 1440px**. On phones the
verbose wording swaps for compact wording via CSS (`.ts-lg` / `.ts-sm`) rather than being duplicated or
truncated — same four disclosures, fewer characters:

| Width | Rendered |
|---|---|
| ≤1100px | `R18 · Gambling can harm · 0800 654 655 · We earn commission` |
| >1100px | `R18 · Gambling can be harmful. Free help 0800 654 655 · We earn commission from links — how that works` |

A clipped disclosure is not a disclosure, so the strip gives up side padding and a little type size at
≤360px rather than ellipsing. Verified at 300 / 320 / 360 / 375 / 393 / 414 / 430 / 768 / 1200 / 1440px:
one line, no overflow, at all of them.

Replacing the scrolling nav strip with the hamburger collapsed the mobile header from **89px to
45px**, which moved everything above it up by the same amount — the first CTA now clears the fold by
73–122px on every page.

The rest of the saving came from things that cost space without carrying information: the eyebrow (it
duplicates the byline), the brand tagline in the header, the badge chip sitting on its own line instead of
beside the brand name, and the toplist caption - which is **moved below the table on mobile, not hidden**.
No operator data is removed at any breakpoint.

**Build guard** (`_build/check_site.py`) fails the build on: broken internal links, broken asset
links, missing or duplicate titles and descriptions, non-self-referencing canonicals, invalid
JSON-LD, `.html` in a URL, a page without exactly one H1, a missing helpline, a missing age
statement, a missing affiliate disclosure, About or Contact absent from the main nav, a
sitemap/filesystem mismatch, a missing robots rule, a missing favicon size, and any title over
580px.

---

## 7. Scalability

### Supporting cluster pages — next 10, in priority order

| Page | Target keyword | Est. vol | Why |
|---|---|---|---|
| `/new-casinos-nz/` | new online casinos NZ | 880 | Running list, high refresh frequency, strong internal-link source |
| `/licensed-online-casinos/` | licensed online casinos NZ | 720 | Owns the licensing-transition query as it peaks toward December |
| `/casino-apps-nz/` | casino apps NZ | 590 | Mobile intent, currently thin across the SERP |
| `/minimum-deposit-casinos/` | $10 deposit casino NZ | 480 | Clear archetype, already half-written inside the no-deposit page |
| `/online-blackjack-nz/` | online blackjack NZ | 480 | Game-type split from `/live-casinos/` |
| `/online-roulette-nz/` | online roulette NZ | 390 | Same |
| `/free-pokies-nz/` | free pokies NZ | 2,400 | Highest-volume gap on the list; demo-play hub, huge dwell time |
| `/casino-withdrawal-times/` | casino withdrawal times NZ | 210 | Dataset page, link-attracting on its own |
| `/skycity-vs-online/` | SkyCity online casino | 320 | Captures a strong NZ brand query with a genuine comparison |
| `/vip-casinos-nz/` | VIP casino NZ, high roller casino NZ | 170 | Archetype completion; high value per visitor |

### Supporting blog posts — topical authority, low competition

1. What the 1 December 2026 cutoff means for your casino balance
2. Every no-deposit bonus advertised to Kiwis this month, re-checked (monthly series)
3. We timed 50 more withdrawals — the September update (quarterly data series)
4. Which NZ banks block gambling transactions, and how to turn it on
5. The same pokie at 96.5% and 94.5%: why your casino chooses
6. What happens to your money if an offshore casino exits New Zealand
7. NPC vs the All Blacks: where offshore books are and are not worth using
8. The reverse withdrawal, explained with our own data
9. Crypto and IRD: what a Kiwi casino player actually needs to record
10. What the licensed NZ market will look like in 2027 — and what you lose

### Cross-linking strategy
- **Hub-and-spoke.** `/online-casinos/` links to all seven category pages; each links back to the hub
  and laterally to the two most related siblings. No orphan pages.
- **Data pages are the authority sink.** Every page citing a payout figure links to
  `/fast-payout-casinos/`; every page citing RTP links to `/high-payout-casinos/`. This concentrates
  link equity on the pages holding original data, which are the ones that will attract external links.
- **Reviews link up, not sideways.** Each review links to the hub, the main ranking and the two
  category pages where the brand ranks well. Reviews do not link to each other, which would dilute.
- **Legal pages are linked from every commercial page**, which is both an EEAT signal and a way to
  push authority to the pages most likely to win featured snippets.

### Additional high-value keywords to target later
`casino sign up bonus NZ` · `best paying pokies NZ` · `Mega Moolah NZ` · `Evolution live casino NZ` ·
`casino self exclusion NZ` · `how to verify a casino account` · `Neosurf casinos NZ` ·
`MiFinity casinos NZ` · `esports betting NZ` · `horse racing betting NZ` · `Melbourne Cup betting NZ` ·
`NZ casino complaints` · `SkyCity online` · `Lotto NZ vs online casino`

---

## 8. Operating cadence

| Frequency | Task |
|---|---|
| **Monthly** | Change `MONTH` in `lib.py` and rebuild — every title, description and H1 follows. Re-verify no-deposit offers from an NZ IP and update the table date. Re-check bonus terms across all 19 operators. |
| **Monthly** | Publish one data or law post from the list above. |
| **Quarterly** | Full operator re-test: 5+ timed withdrawals each, RTP basket, live table count, support sampling. Recalculate scores. |
| **On change** | Any DIA announcement, any commencement date, any operator terms change. Legal pages are the site's trust anchor and a stale one is worse than none. |
| **Ongoing** | Log every reader complaint against the operator; a pattern is grounds for removal. |

### The three dates that matter next
- **1 December 2026** — unlicensed operators must stop serving New Zealanders. Traffic and query
  volume around "is X still available in NZ" will spike. Have the tracker current and a post ready.
- **1 January 2027** — duty rises 12% → 16%. Expect bonus terms to tighten across the market;
  re-audit everything in the first week of January.
- **Q1 2027** — licensed market expected live, and the affiliate-marketing prohibition bites. Plan the
  revenue model change now, and be the site that explained it first.
