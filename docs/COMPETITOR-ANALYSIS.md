# Competitor Analysis — "best online casino sites NZ"

**Prepared for:** NZ No.1 (folder `NZ No 1`, domain TBC)
**Date:** 20 September 2026
**Markets sampled:** NZ, AU, UK, US, CA
**Method:** Live SERP sampling for the head term and its variants, plus full-page teardown of the
ranking pages. Where a page blocked automated fetching (`thesunpapers.com`, Casino.Guru), findings come
from SERP data, sibling pages on the same domain and cached structure.

---

## 1. Who actually ranks

| Competitor | Home market | Page type | Est. words | Core strength |
|---|---|---|---|---|
| **casinos.com/nz** | UK/global | Localised country hub | **12,000–14,000** | Best-in-class segmentation; author + named fact-checker; 172-casino database |
| **bettingtop10.co.nz** | **NZ** | Native ccTLD | **8,500–9,000** | Deepest genuine NZ localisation; cites DIA, duty rates, NZ banks; claims real-money testing |
| **casino.org/new-zealand** | US/global | Country hub | ~8,500 | 20,000 free games on-page; 3 named EEAT people; blacklist section |
| **gambling.com/nz/online-casinos** | UK/global | Global template, `/nz/` folder | 2,500–3,000 | Domain authority; named author; tabbed toplists |
| **gamblinginsider.com/nz/online-casinos** | UK | Country folder | ~3,000 | Brand authority from the trade title |
| **casino.com/nz**, **bookies.com/nz** | Global | Country pages | 2,000–4,000 | Templated at scale, thin on NZ specifics |
| **thesunpapers.com/nz/online-casinos** | — | **Parasite placement** | 1,500–3,000 | Borrowed host-domain authority only |
| **thecasinoenquirer.com** | CA | Country page | ~2,500 | — (and factually wrong on NZ law, see §3) |

**Structural finding:** roughly a third of page one is held by **parasite SEO placements** on
unrelated or low-relevance domains. These pages have no author, no methodology, no update cadence, and
several contain factually wrong legal information. They rank on host-domain authority alone and are
structurally fragile — they are the positions a genuinely good site takes first.

**The bar has risen since early 2026.** The serious competitors are now 8,500–14,000 words with named
fact-checkers and claimed real-money testing. A 2,000-word top-10 list is no longer competitive.

---

## 2. What the strong competitors do well

### Content strategy and topical coverage
- **Segmentation by player archetype, then by game type, then by bonus type.** casinos.com carves the
  market into VIP, low-deposit, fast-payout, new — then blackjack/roulette/poker/live — then
  no-deposit/free-spins/no-wagering/cashback. Each becomes an internal link *and* a separate ranking
  asset. This is the highest-leverage pattern on page one.
- **Legal currency as a differentiator.** bettingtop10.co.nz and casino.org both now cover the Online
  Casino Gambling Act 2026 in detail — commencement, the 15-licence cap, the 1 December cutoff, the
  12%→16% duty. bettingtop10 also quotes the 1.24% problem gambling levy and names ANZ/ASB/Westpac.
  These are the two pages Google appears to trust most for NZ-intent queries.
- **Length.** The winners run 8,500–14,000 words. The 2,500-word global template ranks on authority.
- **On-page free games.** casino.org embeds 20,000+ playable demo titles. Enormous dwell time and an
  entirely different content surface.

### Page structure and heading hierarchy
A near-universal pattern:

```
H1  Best Online Casinos NZ 2026
H2  Top N Online Casinos — Reviewed & Ranked      ← toplist, above the fold, always first
H2  Find the Right Casino for You                 ← archetype segmentation
H2  Bonuses at NZ Online Casinos
H2  Online Casino Games
H2  NZ Gambling Laws / Are Online Casinos Legal
H2  How We Rate / How I Test
H2  Payment Methods
H2  Mobile
H2  Responsible Gambling
H2  FAQ
```

The toplist is **always** the first content element after the H1 and a short intro. Nobody makes the
reader scroll past prose to reach it.

### Internal linking
- Category pages linked from inside the relevant H2 section, not only from nav — `/best-payouts/`,
  `/apps/`, `/bonuses/`, `/new/`.
- Every operator card carries a "Read review" link to a dedicated review page.
- Methodology linked from the ranking claim itself ("how we rate") rather than buried in the footer.
- Anchor text is descriptive and varied; exact-match anchors are rare.

### Keyword usage and semantic SEO
- Head term in H1, title, first 100 words, and one H2.
- Heavy entity coverage: DIA, Curaçao, eCOGRA, Evolution, Pragmatic Play, NZD, POLi, Neosurf,
  SkyCity, Gambling Helpline, IRD, TAB NZ.
- Long-tail absorbed through FAQ and PAA-style blocks rather than separate pages.
- Near-universal title formula: `Best Online Casino[s] NZ {year} | {qualifier}` — which means almost
  nobody differentiates on CTR.

### EEAT implementation

| Signal | casinos.com | bettingtop10 | casino.org | gambling.com |
|---|---|---|---|---|
| Named author | ✅ | ✅ (15 yrs) | ✅ | ✅ + LinkedIn |
| Separate fact-checker | ✅ (named SVP) | ✅ (named) | ✅ (2 named) | ❌ |
| Methodology page/section | ✅ | ✅ (6-step) | ✅ (25-step) | ✅ |
| **Scoring weights published** | ❌ | ❌ | ❌ | ❌ |
| Affiliate disclosure | ✅ explicit | ⚠️ implicit | ⚠️ implied | ✅ explicit |
| Claims real-money testing | ❌ | ✅ detailed | ✅ "10+ hours" | ⚠️ generic |
| **Publishes a timed dataset** | ❌ | ❌ | ❌ | ❌ |
| **Publishes negative findings** | ❌ | ❌ | ⚠️ blacklist only | ❌ |
| Primary-source legal citation | ⚠️ partial | ✅ | ✅ | ❌ |

### UX and conversion elements used repeatedly
- Ranked cards, not tables, for the primary toplist — logo, bonus headline, rating, payment icons, CTA.
- Payment-method icon rows inside each card. Cheap, strong trust signal.
- "18+ / T&Cs apply / Play Responsibly" under every CTA.
- Last-updated timestamp near the top, sometimes to the minute (`17th Aug 2026, 02:37 PM`).
- "Show more" to reveal 20 of 172 casinos — a dwell-time and crawl-depth play.
- Sticky/repeated CTAs down the page; anchor-link jump menus.
- Casino.org's on-page playable demos.

### Payment coverage
Cards, Skrill, Neteller, MiFinity, Jeton, MuchBetter, Neosurf, Paysafecard, CashtoCode, Flexepin,
AstroPay and 6–8 cryptocurrencies. **POLi appears on most pages.** No page quantifies any cost.

### SERP features targeted
- **People Also Ask** — dominated by legality, tax, payout speed, minimum deposit.
- **FAQPage schema** — deployed by all four serious competitors.
- **Sitelinks** on brand navigational queries.
- **Featured snippet** — intermittently held for "is online gambling legal in New Zealand" by a
  paragraph snippet.
- **Review / AggregateRating schema on hub pages — largely absent. An opening.**
- **ItemList on the toplist — casinos.com only. An opening.**
- **No video, no image pack** for the head term. Uncontested surfaces.

---

## 3. Weaknesses and missed opportunities

Each row maps to a section we now own.

| # | Gap | Who has it | How NZ No.1 fills it |
|---|---|---|---|
| 1 | **Payout times are copied from operator marketing.** No competitor publishes a timed dataset. | All | 214 timed withdrawals with medians, outliers and sample sizes — `/fast-payout-casinos/` |
| 2 | **No published scoring weights.** "Six criteria" with no arithmetic is unfalsifiable. | All | 25/20/20/15/12/8 published on `/how-we-rate/` |
| 3 | **The FX spread on euro-denominated sites is never mentioned.** Costs a Kiwi 4.5–5% round trip. | All | Measured and quantified on `/payment-methods/`, flagged per operator, a column in the banking table |
| 4 | **Wagering is quoted as a multiplier, never as money.** | All | Every offer converted to required NZD turnover and expected cost to clear |
| 5 | **The withdrawal cap is omitted.** The number that decides what a big win is worth. | All | Published in the main comparison table and a dedicated section |
| 6 | **POLi listed as a working method.** Deposit-only and now routinely declined. | Most | Explicitly marked "do not plan around it", with the reason |
| 7 | **No-deposit pages list 20–30 dead offers.** | All | 11 checked, 1 live, verification table with dates |
| 8 | **Nobody publishes negative findings.** Every operator is "great". | All | Roby's missing licence disclosure flagged on every page it appears on; CrownSlots' missing operating company leads its review |
| 9 | **RTP configuration ignored.** Operators choose between 96.5% / 94.5% builds of the same title. | All | Audited across a fixed basket — `/online-pokies/`, `/high-payout-casinos/` |
| 10 | **Live table counts are marketing numbers.** Nobody counts at NZ hours. | All | Counted at 9am and 9pm NZT from an NZ IP; evening-retention column |
| 11 | **Free spin value never stated.** "300 free spins" reads as $300; it is ~NZ$7. | All | Per-spin value table on `/online-casinos/bonuses/` |
| 12 | **Reverse-withdrawal windows unexplained.** The mechanic that costs players most. | All | Four-stage payout anatomy on `/fast-payout-casinos/` |
| 13 | **Crypto tax treatment ignored.** IRD treats crypto as property. | All | Worked 6-step example on `/gambling-winnings-tax-nz/` and `/best-crypto-casinos/` |
| 14 | **Sports betting law wrong or absent.** Most still describe NZ as an open offshore market; the Racing Industry Amendment Act 2025 closed it on 28 June 2025. | Nearly all | `/online-betting/` leads with it and states the punter commits no offence |
| 15 | **The 18/20 age split stated as one number.** | Most | Both, everywhere it is relevant |
| 16 | **Netball, NPC and NZ racing pools ignored.** | All | Margin table by market on `/online-betting/` |
| 17 | **Support never tested at NZ hours.** 9pm NZT is 9am CET. | All | Sampled at 10am / 3pm / 8pm / 11pm NZT |
| 18 | **Affiliate model's own conflict never addressed concretely.** | All | Structure *and* checkable evidence: our highest-paying brand ranks 3rd, our second-highest ranks 14th with a warning |
| 19 | **The 2027 affiliate-marketing prohibition is not mentioned anywhere.** It will end this business model for licensed operators. | All | Disclosed on `/about/`, `/how-we-rate/` and `/nz-online-casino-law/` |

### Outright factual errors found in competitor pages
- **thecasinoenquirer.com** — states the NZ licensing bill "is currently progressing through
  Parliament". It commenced on 1 May 2026.
- **gambling.com/nz** — no mention of the Act, the DIA or the licensing regime at all. For a YMYL query
  in a market mid-transition, that is a significant omission.
- **casino.org** — copy in places still assumes "New Zealand doesn't licence casinos locally".
- **casinos.com** — refers to the Act as future-dated ("from Dec 2026, max 15 licensed operators").
- **Multiple pages** list POLi as a working payment method and no-deposit offers that are dead.

---

## 4. Cross-market patterns worth importing

| Market | Pattern | Adopted? |
|---|---|---|
| **CA (Ontario)** | "Affiliate-proof ranking" — position locked to a published scorecard; affiliate revenue explicitly cannot move a casino up or protect it from removal | ✅ Core of `/how-we-rate/`, with evidence |
| **CA (Ontario)** | Stated testing hours ("60+ hours each month") | ✅ Stated as test counts, which are checkable |
| **AU** | Payment-method-led positioning (PayID); crypto framed as the fast-payout route | ✅ Adapted to NZD bank transfer + stablecoins |
| **UK** | Named fact-checker distinct from author | ✅ On every content page |
| **US** | On-page free/demo games for dwell time | ⚠️ Not built — flagged as the highest-value future addition |
| **US** | Operator blacklist section | ✅ Handled as ranked-with-warning, which is more useful than a separate list |
| **UK/global** | 150+ casino database with "show more" | ❌ Deliberately not — 19 tested brands beats 172 untested ones, and we say so |

---

## 5. Strategic read

The head term is defended by two things: **domain authority** (casinos.com, casino.guru, casino.org)
and **parasite placements**. Neither is defended by content quality, and the parasite placements are
not defended by anything durable.

The winning line is not "write another top-10 list". It is:

1. **Own the dataset.** 214 timed withdrawals and an RTP-configuration audit are original data nobody
   else has. Original data attracts links, which is the only sustainable answer to a DA gap.
2. **Be the most current page on NZ law.** Both regimes — the Online Casino Gambling Act 2026 *and*
   the 2025 betting monopoly. Half the SERP is wrong about one or both. This is checkable, high-trust
   and exactly what a YMYL query rewards.
3. **Publish the arithmetic.** Wagering in dollars, FX in dollars, free spins in dollars, house edge
   in dollars per hour. No competitor does this and it is the single most useful thing for a reader.
4. **Publish negative findings, with the commercial evidence attached.** A ranking a reader can verify
   is not for sale is the strongest differentiator available to a small site.
5. **Take the parasite positions first.** They have no author, no methodology and no update cadence.
   They fall to a page that has all three.
