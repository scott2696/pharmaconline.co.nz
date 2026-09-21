#!/usr/bin/env python3
"""pharmaconline.co.nz's own editorial copy for each operator.

operators.json holds the FACTS — bonus, wagering, licence, payout windows,
payment rails. Those are shared, checkable and identical wherever they are
published. This module holds the JUDGEMENT — tagline, one-line summary, pros,
cons, verdict and the long-form review narrative.

The house rule for everything in here: lead with what the offer costs, not what
it advertises. The priced ledger table at the top of every review is generated
from bonuscalc, so the narrative below it never has to repeat a number it might
later contradict.
"""

V = {

"crownslots": dict(
  tagline="The largest match on the page, and the most expensive to finish",
  sub="390% to NZ$7,250 &mdash; euro-denominated, crypto-quick, NZ$290k of turnover",
  pros=[
    "The 390% match is the largest percentage offer in this market, and the 175 spins land on Pragmatic Play titles rather than filler nobody has heard of",
    "Crypto withdrawals are genuinely quick at one to six hours, which is top-three among the sites we cover",
    "Five thousand games and a 250-table live floor that stays properly staffed through the late New Zealand evening",
  ],
  cons=[
    "The balance is held in euros, so a New Zealander pays a conversion spread of roughly 4.8% across the round trip &mdash; on the full package that is several hundred dollars before a single spin",
    "No operating company is named anywhere on the site. A Cura&ccedil;ao licence with nobody standing behind it is the weakest disclosure of any brand here except Roby",
    "40x applied to a 390% match produces the second-largest wagering demand in our ledger. The maximum bonus is, in practice, unreachable",
  ],
  verdict=("CrownSlots is the clearest illustration of this site's central argument. It has the biggest "
           "number on the page and, precisely because of that, one of the worst offers on the page &mdash; "
           "the multiplier applies to the whole of a very large bonus. The casino underneath is genuinely "
           "decent: fast crypto rails, a deep library, a live floor that works at New Zealand hours. Deposit "
           "modestly, take the spins, ignore the 390%, and understand that you are banking in euros with an "
           "operator that will not tell you its own name."),
  best_for="Crypto players who will take a small deposit and ignore the headline",
  narr=[
    ("What the 390% is really for",
     "<p>A 390% match is not designed to be claimed in full. It is designed to be the largest number in a "
     "comparison table, and it succeeds at that. Deposit NZ$200 and the first-deposit portion behaves like "
     "an ordinary match; the remainder is staged across subsequent deposits that most players never make.</p>"
     "<p>The interesting question is not whether the offer is generous but whether the casino is worth "
     "using without it, and here CrownSlots does better than its marketing deserves. The library is broad, "
     "the crypto withdrawals are among the fastest we have timed, and the live floor holds up at 9pm NZT "
     "when several rivals have thinned out.</p>"),
    ("The euro problem, quantified",
     "<p>CrownSlots holds your money in euros. Nothing on the site presents this as a cost, because to the "
     "operator it is not one.</p>"
     "<p>For a New Zealander it is. You convert NZD to EUR on the way in and EUR to NZD on the way out, and "
     "the spread on that round trip runs around 4.8%. On a NZ$1,000 deposit that is roughly NZ$48 &mdash; "
     "comfortably more than the difference between most of the welcome offers people agonise over. It does "
     "not appear on a statement as a fee. It appears as a smaller number arriving than the one you "
     "expected.</p>"),
    ("Who is actually operating this",
     "<p>The footer carries a Cura&ccedil;ao licence reference and no corporate entity. There is no company "
     "name, no registration number and no address.</p>"
     "<p>That matters in one specific circumstance: when something goes wrong. Every withdrawal we "
     "requested was paid, promptly, and we have no complaint about conduct. But if a payment were refused, "
     "the practical question is who you escalate to and under what name, and CrownSlots does not answer it. "
     "Compare with Spinjo or Fortune Play, where Rabidi N.V. and Dama N.V. are named in the footer with "
     "registration numbers that resolve on the regulator's own register.</p>"),
    ("The honest recommendation",
     "<p>Use it as a crypto casino with a good library and quick payouts, on a deposit you choose rather "
     "than the one the banner suggests. Do not use it as a bonus play &mdash; our ledger puts the cost of "
     "clearing the full package above ten thousand dollars, which is not a marginal call.</p>"
     "<p>And if you want the same kind of casino while holding New Zealand dollars and knowing who runs it, "
     "<a href='/casino-reviews/spinjo/'>Spinjo</a> does that and scores higher for exactly those reasons.</p>"),
  ]),

"spinjo": dict(
  tagline="The one we would open an account with",
  sub="NZD end to end, Rabidi N.V. named, ~8,000 games, 40x on a sane bonus",
  pros=[
    "Banks in New Zealand dollars from deposit to withdrawal, so there is no conversion spread in either direction &mdash; worth more than most bonus differences",
    "Names Rabidi N.V. in the footer and holds a Cura&ccedil;ao Gaming Control Board licence that resolves on the regulator's own register",
    "Around 8,000 games from 90+ studios and a 400-table live floor &mdash; the deepest lobby we audited, running the top RTP build on the headline titles we checked",
  ],
  cons=[
    "40x on up to NZ$5,000 still demands NZ$200,000 of turnover at the maximum. The offer is ordinary; it is simply not predatory",
    "The NZ$8,000 weekly withdrawal cap means a large win arrives in instalments &mdash; better than most here, but not unlimited",
    "NZ$30 minimum deposit is higher than Lucky Circus or the Anjouan group, which matters on a small bankroll",
  ],
  verdict=("Spinjo is the highest-scoring site we cover and it gets there without a single headline number "
           "worth writing about. It banks in New Zealand dollars, names its operating company, holds a "
           "licence that checks out, runs the deepest library in the market and paid every withdrawal we "
           "requested. The welcome offer is unremarkable, which on the evidence of our ledger is a point in "
           "its favour. If you want one account and no further thought, this is the one."),
  best_for="Players who want a serious casino and are indifferent to the bonus",
  narr=[
    ("Why the boring option wins",
     "<p>Spinjo has no billboard number. There is no 600%, no five-figure headline, nothing that would win "
     "a comparison table sorted by bonus size. It is the best casino here anyway, and the two facts are "
     "related.</p>"
     "<p>What it has instead: New Zealand dollars end to end, a named operator, a licence that resolves, "
     "eight thousand games, four hundred live tables and the fastest published card window of any site here, at one "
     "to three business days. Those are the things you actually interact with every week. The welcome "
     "offer is a single event in the first month of an account you may hold for years.</p>"),
    ("The currency point, which is the whole argument",
     "<p>Spinjo holds NZD. That sounds administrative and it is worth real money.</p>"
     "<p>At a euro-denominated site you pay a conversion spread of roughly 4.8% across a round trip. On "
     "NZ$1,000 that is about NZ$48, every time, regardless of how you play. Spinjo charges nothing "
     "equivalent because no conversion occurs. Over a year of moderate play, that difference dwarfs the gap "
     "between a 40x offer and a 35x one, and unlike a bonus it applies to every dollar you move rather "
     "than once at signup.</p>"),
    ("The library, audited rather than counted",
     "<p>Eight thousand games is a number, and numbers like it are usually inflated by aggregator "
     "duplication. What we checked instead was which build of six headline titles the lobby runs. Spinjo "
     "was on the top configuration for all six &mdash; Gates of Olympus, Sweet Bonanza, Big Bass Bonanza, "
     "Book of Dead, Starburst and Wolf Gold.</p>"
     "<p>That is worth about NZ$20 per NZ$1,000 staked against a lobby running the cut-down versions, and "
     "it is checkable in ten seconds per game from the information panel. "
     "<a href='/online-pokies/#builds'>How to do it yourself</a>.</p>"),
    ("Where it is beatable",
     "<p>Two places. The NZ$30 minimum deposit is high for a small bankroll &mdash; "
     "<a href='/casino-reviews/lucky-circus/'>Lucky Circus</a> opens at NZ$10 and is the better choice if "
     "you are depositing in twenties. And the welcome offer, priced in our table above, is thoroughly "
     "average; if you specifically want an offer worth claiming, "
     "<a href='/casino-reviews/spino/'>Spino</a>'s 0x crypto package is the only one in this market that is "
     "worth its face value.</p>"),
    ("What we would do",
     "<p>Open the account, decline the welcome bonus, deposit what you intended to spend, and play. You "
     "keep a withdrawable balance with no wagering requirement, no maximum cashout and no maximum bet rule "
     "to breach by accident, at the best-run casino on this site. We are paid more when you claim the "
     "bonus. We still think declining it is the right call.</p>"),
  ]),

"madcasino": dict(
  tagline="A competent all-rounder with a sportsbook attached",
  sub="Casino and sport in one account, NZD banking, Vertikal N.V. named",
  pros=[
    "One account covering casino and sportsbook, with a shared balance &mdash; convenient if you do both and rare among the sites here",
    "Banks in New Zealand dollars and names Vertikal N.V. as the operating company",
    "NZ$20 minimum deposit and a NZ$8,000 weekly cap put it among the more accessible sites on both ends",
  ],
  cons=[
    "Anjouan licensing is a weaker consumer-protection regime than the Cura&ccedil;ao Gaming Control Board, with a less developed complaints route",
    "Crypto withdrawals at three to ten hours are the slowest of the Vertikal group &mdash; Kingdom does the same job in two to four",
    "40x on up to NZ$4,000 is NZ$160,000 of turnover. Unremarkable for this market, and still not an offer worth chasing",
  ],
  verdict=("MadCasino does most things adequately and one thing genuinely well: it runs a real sportsbook "
           "alongside the casino on a single New Zealand dollar balance. If you want both from one account "
           "that is a practical advantage. The licensing is a step down from the Cura&ccedil;ao GCB brands "
           "and the payout speeds trail its stablemates, so if you only play casino games there are better "
           "choices at the same or lower cost."),
  best_for="Players who want casino and sportsbook on one NZD balance",
  narr=[
    ("The case for a combined account",
     "<p>Most sites here do one thing. MadCasino runs both a 4,500-game casino and a sportsbook off a "
     "single balance, which removes the tedious business of maintaining two accounts, two verification "
     "processes and two withdrawal queues.</p>"
     "<p>There is a legal wrinkle worth knowing before you use the sports side, and it is not about you. "
     "The Racing Industry Amendment Act 2025 makes TAB NZ the only entity that may lawfully offer sports "
     "and racing betting into New Zealand. The prohibition binds the operator, not the punter &mdash; you "
     "commit no offence. <a href='/online-betting/'>The full position</a>.</p>"),
    ("Anjouan licensing, and what it does not give you",
     "<p>MadCasino is licensed in Anjouan rather than by the Cura&ccedil;ao Gaming Control Board. The "
     "distinction is not academic. The Cura&ccedil;ao GCB regime, reformed in 2023, carries a public "
     "register, defined complaint handling and a regulator that answers correspondence. Anjouan's framework "
     "is newer, thinner and less tested.</p>"
     "<p>Vertikal N.V. is named, which is a genuine positive and puts MadCasino well ahead of the brands "
     "that publish nothing. But if escalation ever matters, a Cura&ccedil;ao GCB brand such as "
     "<a href='/casino-reviews/spinjo/'>Spinjo</a> or <a href='/casino-reviews/fortune-play/'>Fortune "
     "Play</a> gives you a better route.</p>"),
    ("Payouts are the weak spot",
     "<p>Three to ten hours on crypto and eight to twenty-four on e-wallets is acceptable rather than good, "
     "and it is noticeably behind <a href='/casino-reviews/kingdom/'>Kingdom</a>, which shares the same "
     "operator and licence and settles crypto in two to four hours.</p>"
     "<p>The NZ$8,000 weekly cap is mid-table: a NZ$40,000 win takes five weeks to collect. Reasonable, "
     "but read it alongside the payout window rather than instead of it.</p>"),
    ("Who should use it",
     "<p>People who bet on sport and play casino games and want one account for both. That is a real and "
     "underserved use case, and MadCasino serves it competently on a New Zealand dollar balance.</p>"
     "<p>If you only play casino games, the same group's Kingdom is faster and Spinjo is better regulated, "
     "at no extra cost to you.</p>"),
  ]),

"gunsbet": dict(
  tagline="A sportsbook first, with the worst bonus arithmetic we measured",
  sub="285% to NZ$14,700 &mdash; NZ$588k of turnover, no crypto, euro balance",
  pros=[
    "A genuinely deep sportsbook with strong coverage of NPC, Super Rugby and international football, and competitive in-play markets",
    "Established in 2016, which makes it one of the longer-running brands here &mdash; longevity is weak evidence but it is not no evidence",
    "Eight payment rails including Paysafecard, AstroPay and Zimpler, which suits players who would rather not use a card",
  ],
  cons=[
    "The welcome package demands NZ$552,000 of turnover &mdash; the largest figure in our entire ledger, at an expected cost above NZ$22,000",
    "No crypto support at all, so the fastest withdrawal rail is simply unavailable and e-wallets at 12&ndash;24 hours are the best you can do",
    "Euro balance, no named operating company, and a &euro;4,000 weekly cap that is the tightest of any site we cover",
  ],
  verdict=("Gunsbet is a capable sportsbook wearing a casino bonus that our ledger rates as the single worst "
           "offer available to New Zealanders. NZ$552,000 of required turnover is not a bonus, it is a "
           "decoration. The sportsbook underneath is genuinely good and the brand has a decade of history, "
           "but the euro balance, the absent operating company, the tight weekly cap and the lack of crypto "
           "make this a hard site to recommend for casino play at all."),
  best_for="Sports bettors who will decline the casino offer entirely",
  narr=[
    ("The worst offer in our ledger, and why",
     "<p>285% up to NZ$14,700 converts to roughly NZ$14,700 of bonus. At 40x on the bonus, collecting the "
     "maximum requires <b>NZ$552,000</b> of turnover, at an expected cost of more than NZ$22,000 on a 96% "
     "RTP game.</p>"
     "<p>To put that in human terms: at NZ$1 a spin and 600 spins an hour, clearing it would take about 920 "
     "hours of continuous play. The bonus expires long before that is possible. The offer is not difficult, "
     "it is arithmetically impossible, and the only honest thing to do with it is decline it.</p>"),
    ("The sportsbook is the actual product",
     "<p>Judged as a sportsbook rather than a casino, Gunsbet is solid. Market depth on New Zealand sport is "
     "better than most offshore books bother with &mdash; NPC and Super Rugby carry proper markets rather "
     "than a token head-to-head &mdash; and the in-play offering is responsive.</p>"
     "<p>The 5x-at-1.80 turnover requirement on the sports side is a normal, clearable structure, unlike "
     "the casino offer. Sports bonuses in this market are generally far more honest than casino ones, "
     "because turnover requirements on odds of 1.80 are a genuine constraint rather than a theoretical "
     "one.</p>"),
    ("No crypto, and a tight cap",
     "<p>Gunsbet supports no cryptocurrency at all, which removes the fastest withdrawal rail available in "
     "this market. Your best case is an e-wallet at twelve to twenty-four hours.</p>"
     "<p>Worse, the weekly withdrawal ceiling is &euro;4,000 &mdash; about NZ$7,840, the tightest of any "
     "brand we cover. A NZ$40,000 win takes six weeks to reach you. Combined with the euro conversion "
     "spread on every one of those six payments, a large win at Gunsbet is a slow and lossy experience.</p>"),
    ("The legal position on the sports side",
     "<p>Worth stating plainly because it is the reason to think carefully about this brand specifically. "
     "Since 28 June 2025, the Racing Industry Amendment Act 2025 has made TAB NZ the only operator "
     "permitted to offer or promote sports and racing betting to people in New Zealand.</p>"
     "<p>You commit no offence by placing a bet &mdash; the prohibition binds operators. But it means "
     "offshore sportsbooks operate outside the New Zealand framework entirely, with no domestic recourse. "
     "<a href='/online-betting/'>The detail, with dates and sections</a>.</p>"),
  ]),

"lucky7even": dict(
  tagline="The no-deposit start, on a modest and clearable offer",
  sub="20 spins before you deposit, then 100% to NZ$1,700 at 40x",
  pros=[
    "20 no-deposit spins on registration &mdash; one of the few genuinely free offers in this market, and a way to test the cashier before funding anything",
    "The deposit match tops out at NZ$1,700, which produces NZ$68,000 of required turnover: large, but the smallest of the Rabidi group and far short of the six-figure offers elsewhere",
    "Cura&ccedil;ao Gaming Control Board licence with Rabidi N.V. named, NZD banking, and 5,500 games from 70+ studios",
  ],
  cons=[
    "The no-deposit spins carry 50x wagering on winnings, a higher multiplier than the cash bonus, plus a maximum cashout &mdash; realistic value is well under a dollar",
    "Crypto withdrawals at two to eight hours are mid-table, and the NZ$6,000 weekly cap is on the tight side",
    "40x on the deposit match is still a bonus our ledger rates as punishing rather than clearable",
  ],
  verdict=("Lucky7even is the sensible entry point for someone who wants to try a casino without funding one "
           "first. The 20 no-deposit spins are genuinely free and genuinely small &mdash; worth about forty "
           "cents once the 50x wagering and the cashout cap are applied &mdash; but they let you watch a "
           "registration and a lobby work at no cost. Underneath is a properly licensed Rabidi site banking "
           "in New Zealand dollars, with a welcome offer that is merely ordinary rather than absurd."),
  best_for="Trying a casino before depositing anything",
  narr=[
    ("The no-deposit offer, priced honestly",
     "<p>Twenty free spins at NZ$0.20 is NZ$4 of face value. Those spins return about 96% on average, so "
     "call it NZ$3.84. The winnings then carry <b>50x</b> wagering &mdash; a higher multiplier than the "
     "cash bonus &mdash; so withdrawing NZ$3.84 requires NZ$192 of turnover from a NZ$3.84 balance. Most "
     "attempts end at zero before that is done. Cap the survivors at the maximum cashout and the offer is "
     "worth roughly <b>forty cents</b>.</p>"
     "<p>Take it anyway. Forty cents for five minutes and an email address is fine value, and occasionally "
     "somebody clears it. What it should not do is decide which casino you use. "
     "<a href='/no-deposit-casinos/'>Every no-deposit offer priced</a>.</p>"),
    ("The real reason to use a no-deposit offer",
     "<p>Not the money. The information.</p>"
     "<p>Registering and claiming lets you watch how an operator behaves before you have anything at stake: "
     "whether verification is demanded immediately, how the cashier presents its terms, whether support "
     "answers, whether the bonus credits when it says it will. That is a better test of a casino than any "
     "review, including this one, and it costs you nothing.</p>"),
    ("Underneath the offer",
     "<p>Lucky7even is a Rabidi N.V. site on a Cura&ccedil;ao Gaming Control Board licence &mdash; the same "
     "stable as <a href='/casino-reviews/spinjo/'>Spinjo</a> and <a href='/casino-reviews/lucky-vibe/'>Lucky "
     "Vibe</a> &mdash; and it inherits the group's strengths: NZD banking end to end, a named operator, a "
     "licence that resolves on the regulator's register.</p>"
     "<p>The library at 5,500 games is smaller than Spinjo's and the NZ$6,000 weekly cap is tighter. If you "
     "intend to stay, Spinjo is the better long-term account. If you want to start without depositing, this "
     "is the door.</p>"),
  ]),

"lucky-vibe": dict(
  tagline="Rabidi's mid-sized option, with a VIP programme that is actually worth reading",
  sub="NZD banking, 5,200 games, 40x to NZ$3,500, tiered loyalty",
  pros=[
    "Full New Zealand dollar banking with Rabidi N.V. named and a Cura&ccedil;ao Gaming Control Board licence",
    "The loyalty programme pays in withdrawable cashback rather than bonus credit at the upper tiers, which is rare and materially better than the usual structure",
    "Both casino and sportsbook on one balance, with a NZ$25 entry point",
  ],
  cons=[
    "Crypto withdrawals at four to twelve hours are the slowest in the Rabidi group",
    "NZ$3,500 at 40x is NZ$140,000 of turnover &mdash; smaller than its stablemates' offers and still not clearable",
    "The lower VIP tiers pay in bonus credit with wagering attached, which is worth far less than the headline percentage implies",
  ],
  verdict=("Lucky Vibe sits in the middle of the Rabidi range and distinguishes itself with a loyalty "
           "programme that, unusually, becomes genuinely valuable at the top tiers where cashback is paid as "
           "withdrawable cash. For a regular player that structure is worth more over a year than any "
           "welcome bonus in this market. For an occasional player it is irrelevant, and Spinjo is the "
           "better account."),
  best_for="Regular players who will reach the upper loyalty tiers",
  narr=[
    ("The only bonus structure we like",
     "<p>Welcome offers are one-off and, on our pricing, usually negative. Ongoing cashback is the opposite: "
     "it is recurring, it scales with how much you actually play, and in its honest form it carries no "
     "wagering at all.</p>"
     "<p>Lucky Vibe's upper tiers pay cashback as <b>withdrawable cash on net losses</b>. That is the good "
     "version. The two questions that separate real cashback from marketing are whether it is paid on net "
     "losses or on turnover, and whether it arrives as cash or as a bonus with its own multiplier. At the "
     "top tiers here the answers are the right ones.</p>"
     "<p>At the lower tiers they are not &mdash; early cashback arrives as bonus credit with wagering "
     "attached, which is worth a fraction of its stated percentage. Read which tier you are actually in.</p>"),
    ("Where it sits in the Rabidi range",
     "<p>Rabidi N.V. operates <a href='/casino-reviews/spinjo/'>Spinjo</a>, "
     "<a href='/casino-reviews/lucky7even/'>Lucky7even</a>, "
     "<a href='/casino-reviews/lucky-circus/'>Lucky Circus</a>, "
     "<a href='/casino-reviews/betandplay/'>Bet&amp;Play</a> and this. They share infrastructure, "
     "licensing, NZD banking and a broadly common cashier.</p>"
     "<p>Lucky Vibe's distinguishing features are the loyalty programme and the combined sportsbook. Its "
     "weaknesses are payout speed, where it is slowest in the group, and a library that is a third smaller "
     "than Spinjo's. Choose it for the cashback or the sport; otherwise choose Spinjo.</p>"),
    ("The bonus, briefly",
     "<p>NZ$3,500 at 40x is NZ$140,000 of turnover at an expected cost of NZ$5,600. Our ledger rates that "
     "effectively unclearable, as it does most offers in this market. It is smaller than the headline "
     "packages elsewhere, which makes it less bad rather than good.</p>"
     "<p>If you are going to play here regularly, decline it and play for the cashback instead &mdash; the "
     "recurring structure is where the value is, and claiming the welcome offer locks your balance behind a "
     "requirement you will not finish.</p>"),
  ]),

"rooster-bet": dict(
  tagline="The best sportsbook here, on a Dama N.V. licence",
  sub="Casino and sport on one NZD balance, 6,000 games, 320 live tables",
  pros=[
    "The strongest combined casino and sportsbook of any brand we cover, with genuine market depth on NPC, Super Rugby and the ANZ Premiership",
    "Dama N.V. named on a Cura&ccedil;ao Gaming Control Board licence, with NZD banking end to end",
    "The 6x free-bet requirement on the sports offer is a normal, clearable structure &mdash; unlike the 40x casino bonus sitting next to it",
  ],
  cons=[
    "The casino side of the welcome offer is a standard 40x on up to NZ$5,000, demanding NZ$200,000 of turnover",
    "Offshore sportsbooks cannot lawfully be offered into New Zealand since June 2025, so there is no domestic recourse if a dispute arises",
    "The NZ$8,000 weekly cap applies across both casino and sports winnings on the shared balance",
  ],
  verdict=("Rooster Bet is the best all-round account on this site for someone who bets on sport as well as "
           "playing casino games. Dama N.V. is named, the licence resolves, the balance is in New Zealand "
           "dollars and the sportsbook is the deepest here on New Zealand competitions. The casino welcome "
           "bonus is the usual 40x fiction; the sports offer at 6x on a free bet is one of the few "
           "promotional structures in this market a normal person can actually finish."),
  best_for="Sport and casino from one properly licensed NZD account",
  narr=[
    ("Sports offers are honest in a way casino offers are not",
     "<p>Worth drawing out, because it is the most useful comparison on this page. Rooster Bet's casino "
     "bonus requires 40x on the bonus. Its sports offer requires 6x on a free bet at minimum odds.</p>"
     "<p>Those are not the same kind of requirement. A 6x turnover at odds of 1.80 or better is a real "
     "constraint but a finishable one &mdash; a normal bettor placing normal bets will get there in weeks. "
     "A 40x casino requirement on a five-figure bonus cannot be finished by anyone. Sports promotions in "
     "this market are consistently more honest than casino promotions, and Rooster Bet carries both side by "
     "side so you can see it.</p>"),
    ("What the sportsbook actually covers",
     "<p>New Zealand sport is where offshore books usually disappoint, offering a head-to-head line on the "
     "NPC and nothing else. Rooster Bet carries proper depth: NPC and Super Rugby with handicaps, totals "
     "and player markets, the ANZ Premiership for netball, plus the international football and basketball "
     "coverage you would expect.</p>"
     "<p>In-play is responsive and the cash-out function works as advertised. Against TAB NZ, the pricing "
     "is generally sharper on international markets and comparable on domestic ones.</p>"),
    ("The legal position, stated plainly",
     "<p>Since 28 June 2025 the Racing Industry Amendment Act 2025 has made TAB NZ the only entity that may "
     "lawfully offer or promote sports and racing betting to a person in New Zealand.</p>"
     "<p><b>You commit no offence by placing a bet.</b> The prohibition binds the operator, and no New "
     "Zealand law criminalises the punter. What it does mean is that an offshore book sits entirely outside "
     "the New Zealand framework, so if a bet is voided or an account closed, your recourse is the "
     "Cura&ccedil;ao regulator rather than anything domestic. "
     "<a href='/online-betting/'>The full position</a>.</p>"),
    ("Casino or sport?",
     "<p>Both, which is the point. The shared NZD balance means no transfers, one verification and one "
     "withdrawal queue. If you only play casino games, "
     "<a href='/casino-reviews/spinjo/'>Spinjo</a> has a deeper library on the same licensing standard. If "
     "you only bet on sport, this is still the best of the books here.</p>"),
  ]),

"fortune-play": dict(
  tagline="Dama's casino-first brand, and the best live floor at New Zealand hours",
  sub="6,500 games, 300+ live tables, NZD banking, Dama N.V. named",
  pros=[
    "A 300-table live floor that held up better than any rival when we counted at 9pm NZT &mdash; the hour that actually matters to a New Zealand player",
    "Dama N.V. named on a Cura&ccedil;ao Gaming Control Board licence, with New Zealand dollar banking throughout",
    "6,500 games from 80 studios, with the top RTP configuration on every headline title we checked",
  ],
  cons=[
    "40x on up to NZ$5,000 is NZ$200,000 of turnover &mdash; identical arithmetic to Spinjo and Rooster Bet, and equally unclearable",
    "The NZ$7,000 weekly cap is mid-table, so a large win still arrives over several weeks",
    "No sportsbook, so if you want sport as well you need the sister brand Rooster Bet or a second account",
  ],
  verdict=("Fortune Play is the live dealer specialist of this list, and it earns that on the only test that "
           "matters for a New Zealander: how much of the floor is genuinely open in our evening rather than "
           "Europe's. It is otherwise a well-run Dama N.V. site with NZD banking, a deep library and honest "
           "RTP configuration. The welcome bonus is the standard 40x arrangement and we would decline it, "
           "particularly here, because live games barely count toward it."),
  best_for="Live dealer players in the New Zealand evening",
  narr=[
    ("The 9pm test",
     "<p>Live table counts are published as though they were constants. They are not &mdash; they are a "
     "snapshot of a European studio floor, and New Zealand is ten to eleven hours ahead. When you sit down "
     "at 8pm in Auckland it is 9am in Riga, which is the thinnest shift of the studio day.</p>"
     "<p>So we counted what was genuinely open and joinable from a New Zealand IP at 9pm NZT. Fortune Play "
     "held more of its advertised floor through that window than any other site here, with blackjack "
     "available at multiple limits rather than the single table that is often all that survives. "
     "<a href='/live-casinos/#timezone'>Why this happens</a>.</p>"),
    ("And then decline the bonus",
     "<p>An uncomfortable pairing: the best live casino here also has a welcome offer that live players "
     "should refuse outright.</p>"
     "<p>Live blackjack typically contributes 5% toward wagering requirements, and is frequently excluded "
     "entirely. A 40x bonus cleared on live blackjack at 5% weighting is really an <b>800x</b> requirement. "
     "Claim the offer and you have locked yourself out of the games you came here for, or committed to "
     "clearing it on pokies instead.</p>"
     "<p>Decline it. Your deposit stays withdrawable, no weighting table applies, and you can play the "
     "0.5% house edge game that is the whole reason to use this site.</p>"),
    ("The rest of the casino",
     "<p>Strong. 6,500 games from 80 studios, the top RTP build on all six headline titles we audited, NZD "
     "banking end to end and Dama N.V. named in the footer with a licence that resolves on the "
     "Cura&ccedil;ao GCB register.</p>"
     "<p>Payouts are good rather than exceptional &mdash; two to eight hours on crypto, one to three "
     "business days on cards, which is among the quicker card windows here. The NZ$7,000 weekly cap means a "
     "NZ$40,000 win arrives over six weeks.</p>"),
  ]),

"lucky-circus": dict(
  tagline="The lowest entry point, and the only one where the two minimums match",
  sub="NZ$10 deposit, NZ$10 bonus qualifier, 35x, NZD banking",
  pros=[
    "NZ$10 minimum deposit &mdash; the lowest here &mdash; and, unusually, the bonus-qualifying minimum is the same NZ$10 rather than being quietly set higher",
    "35x wagering is below the 40x market standard, and on a NZ$2,500 cap it produces the smallest turnover demand of the mainstream Rabidi brands",
    "Cura&ccedil;ao Gaming Control Board licence, Rabidi N.V. named, full New Zealand dollar banking",
  ],
  cons=[
    "The NZ$5,000 weekly withdrawal cap is among the tightest here &mdash; a NZ$40,000 win takes eight weeks",
    "Crypto withdrawals at four to twelve hours are slow relative to the group",
    "4,800 games is the smallest mainstream library of the Rabidi sites",
  ],
  verdict=("Lucky Circus is the right account for a small bankroll, and it earns that on a detail almost "
           "nobody checks: the deposit minimum and the bonus-qualifying minimum are the same number. At most "
           "sites they are not, and depositing NZ$10 at a site with a NZ$30 qualifying floor gets you no "
           "bonus and no explanation. Add 35x rather than 40x and full NZD banking and this is the most "
           "honest small-stakes option on the site."),
  best_for="Small deposits, where the qualifying minimum actually matters",
  narr=[
    ("The two minimums, and why the gap between them matters",
     "<p>Every casino publishes a minimum deposit. Most also have a separate, higher, <b>bonus-qualifying "
     "minimum</b>, and it is disclosed in the bonus terms rather than at the cashier.</p>"
     "<p>The consequence is a specific and common disappointment: you deposit the advertised NZ$10 or "
     "NZ$20, no bonus appears, and nothing tells you why. The money is fine &mdash; you simply did not "
     "qualify for an offer you thought you were taking.</p>"
     "<p>Lucky Circus sets both at NZ$10. That is a small piece of honesty and it is rarer than it should "
     "be. Both figures for every site are in our "
     "<a href='/online-casinos/'>comparison table</a>.</p>"),
    ("35x is not generous, it is merely less bad",
     "<p>Worth being precise. NZ$2,500 at 35x is NZ$87,500 of required turnover, at an expected cost of "
     "NZ$3,500. Our ledger rates that <i>punishing</i> rather than unclearable, which is a genuine "
     "improvement on the 40x six-figure offers elsewhere and still not an offer we would tell you to "
     "claim.</p>"
     "<p>The better use of this account is small deposits without the bonus, where the NZ$10 floor and the "
     "low minimum spin sizes let a modest bankroll last an evening.</p>"),
    ("The cap is the real limitation",
     "<p>NZ$5,000 a week is tight. If you win NZ$40,000 here it will reach you over roughly eight weeks, in "
     "eight separate payments, regardless of how quickly each one is processed.</p>"
     "<p>For a small-stakes player that is mostly theoretical, which is why it does not disqualify the site "
     "for its intended use. If you play for larger sums, <a href='/casino-reviews/kingdom/'>Kingdom</a> at "
     "NZ$10,000 a week or <a href='/casino-reviews/spino/'>Spino</a> with no stated cap are the better "
     "choices. <a href='/fast-payout-casinos/#caps'>Why caps matter more than speed</a>.</p>"),
  ]),

"kingdom": dict(
  tagline="The deepest library here, attached to the largest turnover demand in the market",
  sub="7,000 games, NZ$10k weekly cap, and a 600% offer requiring NZ$555k of wagering",
  pros=[
    "Seven thousand games from 80+ studios and a 350-table live floor &mdash; the second-deepest lobby we audited, on the top RTP build throughout",
    "The NZ$10,000 weekly withdrawal ceiling is the most generous cap of any capped site here, and crypto settles in two to four hours",
    "Banks in New Zealand dollars, names Vertikal N.V., and accepts eleven payment rails including Dogecoin and Jeton",
  ],
  cons=[
    "The 600% headline demands NZ$555,000 of turnover at the maximum &mdash; the largest figure in our ledger, at an expected cost of NZ$22,200",
    "Anjouan licensing rather than the Cura&ccedil;ao Gaming Control Board, with a thinner complaints route",
    "The bonus is staged across four deposits, so the advertised NZ$18,500 requires a sequence of deposits most players will never make",
  ],
  verdict=("Kingdom is a genuinely excellent casino carrying a genuinely absurd bonus, and the two should be "
           "assessed separately. The library is deep and honestly configured, the weekly cap is the best "
           "among capped sites, payouts are quick and the balance is in New Zealand dollars. The 600% offer "
           "is the worst-priced casino bonus we track. Open the account, decline the offer, and it is one of "
           "the two or three best choices on this site."),
  best_for="Serious players who will decline the bonus and use the NZ$10k cap",
  narr=[
    ("Two products in one review",
     "<p>Kingdom illustrates why this site separates the casino from the offer.</p>"
     "<p><b>The casino</b> is excellent: 7,000 games, a 350-table live floor, the top RTP configuration on "
     "every headline title we checked, two-to-four-hour crypto payouts, NZD banking and the most generous "
     "weekly withdrawal ceiling of any capped site here at NZ$10,000.</p>"
     "<p><b>The offer</b> is the worst in our ledger. 600% up to NZ$18,500 at 30x requires "
     "<b>NZ$555,000</b> of turnover, at an expected cost of NZ$22,200. The 30x multiplier is below the "
     "market standard of 40x, which is exactly the trap &mdash; a lower multiplier on a vastly larger bonus "
     "produces a far larger requirement. The multiplier is the headline; the size of the bonus is where the "
     "damage is.</p>"),
    ("The cap is the underrated feature",
     "<p>Payout speed gets all the attention and the withdrawal ceiling decides what actually happens after "
     "a good night.</p>"
     "<p>At NZ$10,000 a week, a NZ$40,000 win reaches you in four weeks. At the &euro;4,000 cap two brands "
     "here run, the same win takes six weeks and pays a currency conversion spread on every instalment. "
     "Kingdom has the best cap of any capped site we cover, and combined with two-to-four-hour crypto "
     "settlement that makes it the strongest practical choice for anyone playing for meaningful sums. "
     "<a href='/fast-payout-casinos/#caps'>The full cap comparison</a>.</p>"),
    ("Anjouan, and what you give up",
     "<p>Kingdom is licensed in Anjouan rather than by the Cura&ccedil;ao Gaming Control Board. Vertikal "
     "N.V. is named, which puts it well ahead of the brands publishing nothing at all, but the regulatory "
     "framework behind it is newer and less tested than the reformed Cura&ccedil;ao regime.</p>"
     "<p>In practice this matters only if a dispute escalates beyond the operator's own support desk. If "
     "that possibility concerns you more than library depth does, "
     "<a href='/casino-reviews/spinjo/'>Spinjo</a> gives you a Cura&ccedil;ao GCB licence and a named "
     "operator at the cost of a smaller weekly cap.</p>"),
    ("What we would actually do here",
     "<p>Open the account. Decline the 600%. Deposit what you planned to spend, keep it withdrawable, and "
     "use one of the best lobbies in this market with the best cap in this market.</p>"
     "<p>We are paid more if you claim the bonus. The arithmetic is not close enough for that to change "
     "what we tell you.</p>"),
  ]),

"smash": dict(
  tagline="A 10x multiplier that is not what it looks like",
  sub="600% to NZ$19,500 at 10x &mdash; on deposit <i>plus</i> bonus",
  pros=[
    "10x is the lowest multiplier on any large offer here, and on a small deposit it produces a genuinely modest turnover requirement",
    "The NZ$10,000 weekly cap ties Kingdom for the most generous ceiling among capped sites",
    "NZD banking, Vertikal N.V. named, and ten payment rails including Dogecoin",
  ],
  cons=[
    "The 10x applies to <b>deposit plus bonus</b>, not bonus alone, which roughly doubles the requirement relative to an identical-looking headline",
    "At the maximum the offer still demands NZ$227,500 of turnover, at an expected cost of NZ$9,100",
    "4,500 games from 40+ studios is the thinnest library of the Vertikal group",
  ],
  verdict=("Smash is the best worked example on this site of why the wagering <i>basis</i> matters more than "
           "the multiplier. A 10x requirement looks four times gentler than the market-standard 40x, and on "
           "a 600% match applied to deposit plus bonus it is not. On a small deposit this is one of the more "
           "reasonable offers available; at the advertised maximum it is among the worst. Same offer, same "
           "terms, completely different answer depending on how much you put in."),
  best_for="Small-deposit bonus players who understand the basis",
  narr=[
    ("The most important number on this page is not 10x",
     "<p>Wagering requirements have two parts and comparison tables only ever print one. The multiplier is "
     "the famous half. The <b>basis</b> is the half that decides the answer.</p>"
     "<p>Most offers here are quoted as &lsquo;40x bonus&rsquo; &mdash; forty times the bonus alone. Smash "
     "is quoted as &lsquo;10x deposit + bonus&rsquo;, which multiplies your own money as well as the "
     "casino's.</p>"
     "<p>On a 600% match that changes everything. To receive the maximum NZ$19,500 bonus you deposit about "
     "NZ$3,250, so the basis is NZ$22,750 rather than NZ$19,500, and 10x of that is <b>NZ$227,500</b>. A "
     "multiplier four times lower than the market standard produces a turnover demand larger than most 40x "
     "offers here.</p>"),
    ("And yet on a small deposit it is one of the better offers",
     "<p>The same structure works in your favour at the bottom end. Deposit NZ$100 and take a 100% match: "
     "the basis is NZ$200 and the requirement is NZ$2,000 of turnover, at an expected cost of about NZ$80 "
     "for a NZ$100 bonus. That is a positive expected value, which is true of almost nothing else in this "
     "market.</p>"
     "<p>So the honest advice is unusually specific: <b>take this offer small.</b> The advertised maximum is "
     "a trap and the same terms at NZ$100 are among the best available to a New Zealander. "
     "<a href='/online-casinos/bonuses/#realistic'>The NZ$200 comparison across every site</a>.</p>"),
    ("The casino itself",
     "<p>Middling by the standards of its group. 4,500 games from 40+ studios is noticeably thinner than "
     "Kingdom's 7,000, and the live floor at 200 tables is the smaller of the two. Crypto settles in three "
     "to eight hours, slower than Kingdom's two to four.</p>"
     "<p>What it shares is the good part: NZD banking, Vertikal N.V. named, and the NZ$10,000 weekly "
     "withdrawal ceiling that is the most generous cap among capped sites here.</p>"),
  ]),

"rivo": dict(
  tagline="The best mobile experience of the Vertikal brands",
  sub="35x, NZD banking, 5,000 games, a lobby that actually works on a phone",
  pros=[
    "The only lobby here where provider filtering and search work properly on a phone &mdash; a small thing that decides whether 5,000 games is a library or a haystack",
    "35x rather than the 40x market standard, on a NZ$4,500 cap",
    "NZD banking with Vertikal N.V. named, and a NZ$8,000 weekly cap",
  ],
  cons=[
    "Anjouan licensing rather than Cura&ccedil;ao GCB, with the thinner complaints route that implies",
    "NZ$157,500 of required turnover at the maximum is still firmly in unclearable territory",
    "Crypto at three to eight hours is mid-table, and card withdrawals at two to four days trail the Rabidi sites",
  ],
  verdict=("Rivo wins on something no comparison table measures: it is the only site here whose lobby is "
           "genuinely usable on a phone. Filters work, provider search works, and the games you want are "
           "findable in seconds rather than after three screens of scrolling. Given that most play in this "
           "market happens on mobile, that is worth more than another thousand games nobody can locate. "
           "Everything else is a competent Vertikal site with a slightly better-than-average multiplier."),
  best_for="Playing on a phone, which is how most people actually play",
  narr=[
    ("The metric nobody publishes",
     "<p>Comparison pages count games. Nobody asks whether you can find them.</p>"
     "<p>Most casino lobbies are built desktop-first and degrade badly on a phone: provider filters "
     "disappear, search returns unsorted results, and the practical effect is that a 5,000-game library "
     "becomes whatever is on the first screen. If the majority of your play happens on mobile &mdash; as it "
     "does for most people &mdash; that is the difference between a deep lobby and a shallow one, "
     "regardless of what the number says.</p>"
     "<p>Rivo is the one site here where we could filter by studio, sort sensibly and find a specific title "
     "on a phone without frustration. It is unglamorous and it is the reason to use it.</p>"),
    ("35x, and what that actually buys",
     "<p>NZ$4,500 at 35x is NZ$157,500 of required turnover at an expected cost of NZ$6,300. Better than "
     "the 40x six-figure offers elsewhere and still an offer our ledger rates as effectively unclearable.</p>"
     "<p>The gap between 35x and 40x sounds meaningful and is worth about NZ$900 of expected cost on this "
     "bonus size &mdash; real, but small next to the question of whether to claim an offer of this shape at "
     "all. On a NZ$200 deposit the picture is much more reasonable.</p>"),
    ("Where it sits",
     "<p>Vertikal N.V. runs <a href='/casino-reviews/kingdom/'>Kingdom</a>, "
     "<a href='/casino-reviews/smash/'>Smash</a>, <a href='/casino-reviews/madcasino/'>MadCasino</a> and "
     "this. Kingdom is the deepest and fastest, Smash has the lowest multiplier, MadCasino carries the "
     "sportsbook, and Rivo is the one you can actually use on a phone.</p>"
     "<p>All four share Anjouan licensing and NZD banking. If regulatory strength matters more to you than "
     "any of those differences, the Rabidi and Dama brands on Cura&ccedil;ao GCB licences are the better "
     "class of site.</p>"),
  ]),

"betandplay": dict(
  tagline="A small, clearable sports offer from a properly licensed operator",
  sub="100% to NZ$500 at 5x on odds of 1.80+ &mdash; a requirement you can finish",
  pros=[
    "The 5x-at-1.80 turnover requirement is a genuinely finishable structure, which almost nothing on the casino side of this market can claim",
    "Rabidi N.V. named on a Cura&ccedil;ao Gaming Control Board licence, with NZD banking",
    "NZ$500 is a sensible ceiling &mdash; small enough to be real, which is the opposite of how casino bonuses are built",
  ],
  cons=[
    "Offshore sportsbooks cannot lawfully be offered into New Zealand since June 2025, so there is no domestic recourse",
    "The casino side is thin at 3,500 games, well behind the group's dedicated casino brands",
    "Market depth on New Zealand competitions is narrower than Rooster Bet's",
  ],
  verdict=("Bet&amp;Play offers the single most honest promotional structure on this site, and it is worth "
           "understanding why: a 5x turnover requirement at minimum odds of 1.80 on a NZ$500 offer is "
           "something a normal bettor genuinely completes. Compare that with a 40x casino bonus demanding "
           "six figures. Same industry, same operator group, entirely different intent. The sportsbook is "
           "mid-sized and the casino attached to it is thin, but the offer is real."),
  best_for="Bettors who want a bonus they can actually clear",
  narr=[
    ("What a finishable offer looks like",
     "<p>Set this against the casino bonuses in our ledger. A NZ$500 sports bonus at 5x requires NZ$2,500 "
     "of turnover at minimum odds of 1.80. A bettor placing NZ$50 bets gets there in fifty bets &mdash; a "
     "few weeks of ordinary activity.</p>"
     "<p>Now the casino comparison: a NZ$500 casino bonus at 40x requires NZ$20,000 of turnover, and the "
     "large headline offers here require several hundred thousand. The sports offer is designed to be "
     "completed. The casino offers are designed to be advertised.</p>"
     "<p>The minimum-odds condition is the real constraint and it is a fair one &mdash; it stops you "
     "clearing the requirement by backing heavy favourites at 1.05, which would carry almost no risk. It is "
     "a condition with a purpose rather than a condition designed to catch you out.</p>"),
    ("The sportsbook itself",
     "<p>Competent rather than outstanding. International football, basketball and tennis are well covered; "
     "New Zealand competitions get proper markets but less depth than "
     "<a href='/casino-reviews/rooster-bet/'>Rooster Bet</a> offers on the same domestic fixtures.</p>"
     "<p>The casino attached to it is the thinnest of the Rabidi group at 3,500 games. If you want both "
     "properly, Rooster Bet does the combination better; if the sports bonus is what brought you, this is "
     "the better offer.</p>"),
    ("The legal position",
     "<p>Since 28 June 2025, TAB NZ has been the only entity lawfully able to offer or promote sports and "
     "racing betting to people in New Zealand, under the Racing Industry Amendment Act 2025.</p>"
     "<p>The prohibition binds operators, not punters &mdash; you commit no offence by placing a bet. But "
     "an offshore book operates wholly outside the New Zealand framework, so if a market is voided or an "
     "account restricted, your escalation route is the Cura&ccedil;ao regulator. "
     "<a href='/online-betting/'>The full position, with dates</a>.</p>"),
  ]),

"roby-casino": dict(
  tagline="Pays us the most, tells you the least",
  sub="No regulator, no licence number, no company &mdash; and 45x wagering",
  pros=[
    "Every withdrawal we requested was paid, without dispute or unusual delay",
    "The 250% match and 250 spins is a large headline offer by the standards of the mid-tier brands",
    "4,000 games from 50+ studios is an adequate library for a casual player",
  ],
  cons=[
    "Publishes no regulator, no licence number and no operating company anywhere on the site &mdash; the only brand we cover where all three are absent",
    "45x is the highest multiplier in this market, demanding NZ$225,000 of turnover at an expected cost of NZ$9,000",
    "The slowest payouts here &mdash; six to twenty-four hours on crypto, one to two days on e-wallets &mdash; behind a tight NZ$5,000 weekly cap",
  ],
  verdict=("Roby Casino pays us one of the highest commission rates in our portfolio and scores 8.1, among "
           "the three lowest on this site. Both facts belong in the same sentence. It publishes no "
           "regulator, no licence number and no operating company, which means that if a withdrawal were "
           "ever refused there is no named entity to escalate to and no register on which to check "
           "anything. It paid us every time. We still cannot recommend it, and we have left it here rather "
           "than removing it because people search for it and deserve to find this rather than a page that "
           "does not mention the disclosure gap."),
  best_for="Nobody, on our assessment &mdash; and we are paid well to say otherwise",
  narr=[
    ("The disclosure gap, precisely",
     "<p>Most casinos in this market publish three things in the footer: a regulator, a licence number and "
     "an operating company with a registration number. The combination lets you verify, in about ninety "
     "seconds, that the entity taking your money exists and is accountable to somebody.</p>"
     "<p>Roby publishes none of the three. Not an unverifiable licence, not a mismatched company &mdash; "
     "nothing at all. It is the only brand we cover where that is true, and it fails the single most "
     "important check on <a href='/how-we-rate/'>our scorecard</a>, which is worth 20 of 100 points.</p>"),
    ("What that means in practice",
     "<p>Nothing, right up until it means everything.</p>"
     "<p>Our withdrawals were paid. If yours are too, the disclosure gap will never affect you. The gap "
     "matters in exactly one situation: a payment is refused, support stops being helpful, and you need to "
     "escalate. At <a href='/casino-reviews/spinjo/'>Spinjo</a> you would take Rabidi N.V.'s registration "
     "number to the Cura&ccedil;ao Gaming Control Board. At Roby there is no name to take anywhere.</p>"
     "<p>You are relying entirely on the operator's continued goodwill, with no mechanism if it stops.</p>"),
    ("The bonus is the worst-priced mid-tier offer here",
     "<p>45x is the highest multiplier of any brand we cover. On a NZ$5,000 cap that is <b>NZ$225,000</b> of "
     "turnover at an expected cost of NZ$9,000 &mdash; you would spend NZ$1.80 for every dollar of bonus.</p>"
     "<p>Combined with the slowest payout windows here and a NZ$5,000 weekly cap that stretches a NZ$40,000 "
     "win across eight weeks, there is no dimension on which this offer competes.</p>"),
    ("Why this review exists at all",
     "<p>We could quietly drop the brand. We have not, for two reasons.</p>"
     "<p>People search for it, and if we remove the review they will find pages that do not mention any of "
     "this. And it is the clearest demonstration we can offer that our scores are not for sale: Roby is "
     "among our best-paying partners and carries one of our lowest scores with a warning on every page it "
     "appears on. Our listing order is commercial and we say so everywhere. The number is not. "
     "<a href='/how-we-rate/#money'>How that works</a>.</p>"),
  ]),

"spino": dict(
  tagline="The only offer in this market worth its face value",
  sub="0x wagering, crypto only, no stated weekly cap, 10-minute payouts",
  pros=[
    "<b>0x wagering</b> on the welcome package &mdash; winnings are withdrawable immediately, which is true of no other offer we track",
    "The fastest payouts here by a wide margin: ten minutes to two hours, with no stated weekly withdrawal ceiling",
    "Eight coins supported including USDT, USDC and Solana, so you can use a stablecoin and avoid price exposure entirely",
  ],
  cons=[
    "Crypto only &mdash; no cards, no bank transfer, no e-wallets, so it is unusable if you do not already hold or want to buy cryptocurrency",
    "Tobique licensing is the least established regime of any brand here, and no operating company is named",
    "3,500 games is the smallest library we cover, with a 150-table live floor to match",
  ],
  verdict=("Spino is the only site on this list whose welcome offer survives our arithmetic intact, because "
           "there is no arithmetic to survive: 0x wagering means the bonus is worth exactly what it says. "
           "Add ten-minute payouts and no stated weekly cap and it is, on offer quality and withdrawal "
           "terms, the best-structured product here. The counterweights are real &mdash; crypto only, the "
           "weakest licensing, no named company and the smallest library &mdash; so it is a specialist "
           "choice rather than a general recommendation."),
  best_for="Crypto holders who want a bonus that is actually worth its face value",
  narr=[
    ("What 0x actually means",
     "<p>Every other cash offer we track requires you to stake a multiple of the bonus before withdrawing. "
     "That requirement is the entire subject of this website, because it is what turns an advertised "
     "NZ$5,000 into a NZ$200,000 obligation costing NZ$8,000 to discharge.</p>"
     "<p>Spino's crypto package has no such requirement. Win, and withdraw. There is no turnover to "
     "generate, no expected cost of clearing, no maximum bet rule to breach and no thirty-day clock.</p>"
     "<p>It is the only offer in our ledger with a verdict of <b>No wagering</b>, and it is the only offer "
     "here that is worth its face value rather than a fraction of it.</p>"),
    ("Payouts are the other headline",
     "<p>Ten minutes to two hours, and <b>no stated weekly withdrawal cap</b>.</p>"
     "<p>The second is the rarer feature. Every other site here caps weekly withdrawals somewhere between "
     "&euro;4,000 and NZ$10,000, which means a large win arrives in instalments over weeks. Spino states no "
     "ceiling, so a big result can come out in one movement. Read alongside "
     "<a href='/fast-payout-casinos/#caps'>our cap comparison</a>, that is a more valuable property than "
     "any payout window.</p>"),
    ("The reasons for caution, stated fairly",
     "<p>Tobique is the least established licensing regime of any brand we cover, and no operating company "
     "is named. That is a materially weaker accountability position than the Cura&ccedil;ao GCB sites, and "
     "it is the main reason Spino scores 8.3 rather than higher despite having the best offer and the best "
     "withdrawal terms on the site.</p>"
     "<p>It is also crypto-only, which rules it out entirely for anyone who does not want to buy "
     "cryptocurrency. And the library at 3,500 games is the smallest here.</p>"),
    ("The tax point, which applies specifically here",
     "<p>Because Spino is crypto-only, the IRD's treatment of cryptoassets as <b>property</b> applies to "
     "everything you do with it. Your gambling winnings are not taxable. Converting the crypto back to New "
     "Zealand dollars can be a taxable disposal on any gain since acquisition, quite separately.</p>"
     "<p>Using a stablecoin such as USDT or USDC keeps that gain close to zero, which is a genuine and "
     "rarely-mentioned argument for stablecoins over Bitcoin for casino play. "
     "<a href='/best-crypto-casinos/#tax'>The full position</a>.</p>"),
  ]),

"ivibet": dict(
  tagline="A small offer that our ledger actually approves of",
  sub="NZ$500 at 35x &mdash; NZ$17,500 of turnover, genuinely clearable",
  pros=[
    "One of only two cash offers here our ledger rates as genuinely clearable: NZ$17,500 of turnover at an expected cost of NZ$700",
    "A 300-table live floor, which is disproportionately large for a 4,000-game site and holds up reasonably at New Zealand hours",
    "TechOptions Group is named as operator, and the brand has been running since 2022",
  ],
  cons=[
    "Euro-denominated, so a New Zealander pays roughly 4.8% across the conversion round trip",
    "A standard Cura&ccedil;ao licence rather than the reformed Gaming Control Board regime",
    "The NZ$5,000 weekly cap is tight, and crypto payouts at two to twelve hours are inconsistent",
  ],
  verdict=("Ivibet is the quiet vindication of this site's whole argument. Its welcome offer is one of the "
           "smallest in the market and one of only two we rate as worth claiming, because NZ$500 at 35x "
           "produces NZ$17,500 of turnover rather than the six-figure demands attached to the big headlines. "
           "The casino around it is unremarkable and euro-denominated, but if you came here looking for a "
           "bonus you can actually finish, this is one of two places to find it."),
  best_for="Bonus players who want an offer they can realistically clear",
  narr=[
    ("Small is the whole point",
     "<p>Ivibet advertises 100% up to NZ$500 &mdash; a figure that would be invisible in a comparison table "
     "sorted by bonus size, sitting alongside 600% offers and five-figure headlines.</p>"
     "<p>Priced properly it is one of the two best cash offers available to New Zealanders. NZ$500 at 35x "
     "is NZ$17,500 of turnover, at an expected cost of about NZ$700. You are still paying more than the "
     "bonus is worth &mdash; that is true of nearly every match offer &mdash; but you are within reach of "
     "finishing it, which is true of almost nothing else.</p>"
     "<p>This is the inversion our <a href='/online-casinos/bonuses/'>ledger</a> exists to show. The "
     "multiplier applies to the whole bonus, so a bigger headline on the same multiplier is a worse offer, "
     "every time.</p>"),
    ("The live floor is the surprise",
     "<p>Three hundred live tables on a 4,000-game site is a disproportionate allocation, and it shows: the "
     "floor is the third-strongest here despite the modest overall library, and it held up better than the "
     "site's size would suggest when we counted at 9pm NZT.</p>"
     "<p>The standard warning applies with force. Live blackjack typically contributes 5% or nothing toward "
     "wagering, so if the live floor is why you are here, decline the bonus &mdash; even this one. "
     "<a href='/live-casinos/#bonus'>Why</a>.</p>"),
    ("The euro cost",
     "<p>Ivibet holds euros. On a NZ$1,000 deposit the round-trip conversion spread is about NZ$48.</p>"
     "<p>Set that against the offer: you would be giving back a meaningful share of a NZ$500 bonus's value "
     "in conversion costs on any substantial play. It does not cancel the advantage of a clearable offer, "
     "but it narrows it, and it is the reason this site scores 8.2 rather than higher.</p>"),
  ]),

"ivibet-sportsbook": dict(
  tagline="The sports side of Ivibet, on a clearable 5x offer",
  sub="100% to NZ$200 at 5x on odds of 2.00+, shared balance with the casino",
  pros=[
    "5x at odds of 2.00 or better is a finishable requirement, unlike anything on the casino side of this market",
    "Shares one balance and one verification with the Ivibet casino, so you are not maintaining two accounts",
    "TechOptions Group named, running since 2022, with nine payment rails",
  ],
  cons=[
    "NZ$200 is the smallest welcome offer on this site &mdash; finishable, but modest",
    "Minimum odds of 2.00 is a stiffer condition than the 1.80 required by Bet&amp;Play",
    "Offshore sports betting cannot lawfully be offered into New Zealand, so there is no domestic recourse",
  ],
  verdict=("Ivibet's sportsbook is a straightforward, small, clearable offer attached to a competent "
           "mid-sized book, sharing a balance with the casino side. The 5x turnover requirement is real and "
           "finishable; the minimum odds of 2.00 is a stiffer condition than most, which makes it slower to "
           "clear than Bet&amp;Play's 1.80 version. Useful mainly if you already hold or want the Ivibet "
           "casino account."),
  best_for="Existing Ivibet players who also bet on sport",
  narr=[
    ("The odds condition is the real term",
     "<p>The 5x multiplier is easy. The condition attached to it is what determines how long it takes.</p>"
     "<p>At minimum odds of 2.00, every qualifying bet is roughly an even-money proposition, which means "
     "you cannot clear the requirement cheaply by backing short-priced favourites. Compare "
     "<a href='/casino-reviews/betandplay/'>Bet&amp;Play</a> at 1.80, which is meaningfully easier to "
     "satisfy on ordinary betting.</p>"
     "<p>Neither is unfair &mdash; a minimum-odds condition exists to stop risk-free clearing, which is a "
     "legitimate purpose. But 2.00 will take you longer, and on a NZ$200 offer the reward for that effort "
     "is small.</p>"),
    ("One balance, two products",
     "<p>The practical case for this account is that it shares everything with "
     "<a href='/casino-reviews/ivibet/'>Ivibet Casino</a> &mdash; one balance, one verification, one "
     "withdrawal queue and one weekly cap. If you already hold the casino account, adding sports costs you "
     "nothing administratively.</p>"
     "<p>As a standalone sportsbook it is mid-sized. <a href='/casino-reviews/rooster-bet/'>Rooster Bet</a> "
     "carries more depth on New Zealand competitions and banks in New Zealand dollars rather than "
     "euros.</p>"),
    ("The legal position",
     "<p>TAB NZ has been the only entity lawfully permitted to offer or promote sports and racing betting "
     "into New Zealand since the Racing Industry Amendment Act 2025 commenced on 28 June 2025.</p>"
     "<p>You commit no offence by placing a bet &mdash; the prohibition binds operators. It does mean there "
     "is no New Zealand recourse if something goes wrong. "
     "<a href='/online-betting/'>The full position</a>.</p>"),
  ]),

"hellspin": dict(
  tagline="The longest-running TechOptions brand, on a borderline offer",
  sub="NZ$500 at 40x &mdash; NZ$20,000 of turnover, right on the line",
  pros=[
    "Running since 2021, which makes it the longest-established brand on this site",
    "At NZ$20,000 of required turnover the offer sits just above our clearable threshold &mdash; demanding, but not in the fantasy territory of the big headlines",
    "TechOptions Group named, 4,500 games and 60+ studios",
  ],
  cons=[
    "Euro-denominated, with the usual 4.8% round-trip conversion cost for New Zealanders",
    "A standard Cura&ccedil;ao licence rather than the Gaming Control Board regime",
    "NZ$5,000 weekly cap and inconsistent crypto payouts of two to twelve hours",
  ],
  verdict=("Hellspin is a small, old, unremarkable casino with an offer that sits almost exactly on the "
           "boundary between punishing and clearable &mdash; NZ$20,000 of turnover for a NZ$500 bonus. Five "
           "years of continuous operation is the most interesting thing about it, and in a market where "
           "brands appear and vanish within eighteen months, that is not nothing. If you want the same "
           "shape of offer slightly better priced, its stablemate Ivibet is at 35x rather than 40x."),
  best_for="Players who value a brand with some history behind it",
  narr=[
    ("Longevity as a weak signal",
     "<p>Hellspin has been operating since 2021. Eleven of the nineteen brands we cover launched in 2023 or "
     "2024.</p>"
     "<p>That is worth something, carefully qualified. Continuous operation means an operator has processed "
     "years of withdrawals without the reputational collapse that usually follows systematic "
     "non-payment. It is weak evidence rather than strong &mdash; plenty of long-running operators are "
     "mediocre, and a 2024 launch on a Cura&ccedil;ao GCB licence with a named company is a better "
     "structural position than a 2021 launch without one.</p>"
     "<p>As one input among several, though, five years of history beats eighteen months.</p>"),
    ("The offer, on the boundary",
     "<p>NZ$500 at 40x is NZ$20,000 of turnover at an expected cost of NZ$800. Our ledger calls that "
     "<i>punishing</i> &mdash; it sits immediately above the NZ$20,000 line we draw for clearable.</p>"
     "<p>The comparison that matters is with <a href='/casino-reviews/ivibet/'>Ivibet</a>, the same "
     "operator group offering the same NZ$500 at 35x. That is NZ$17,500 of turnover and NZ$700 of expected "
     "cost. Identical headline, same company, and one is on the right side of the line.</p>"),
    ("The rest of it",
     "<p>4,500 games from 60+ studios and a 200-table live floor is an ordinary mid-sized lobby. Euro "
     "balances cost a New Zealander about 4.8% across the round trip, the NZ$5,000 weekly cap stretches a "
     "large win over two months, and crypto payouts range from two to twelve hours, which is a wide enough "
     "spread to be unpredictable.</p>"),
  ]),

"slotsgem": dict(
  tagline="The smallest offer here, and the cheapest to finish",
  sub="NZ$400 at 40x &mdash; NZ$16,000 of turnover, the lowest demand we track",
  pros=[
    "The lowest turnover demand of any cash offer we price: NZ$16,000, at an expected cost of NZ$640",
    "One of only two offers our ledger rates as genuinely clearable, alongside Ivibet",
    "TechOptions Group named, with a NZ$20 entry point",
  ],
  cons=[
    "The slowest withdrawals on this site &mdash; four to twenty-four hours on crypto and up to two days on e-wallets",
    "The tightest weekly cap here at NZ$4,000, stretching a NZ$40,000 win across ten weeks",
    "3,800 games and a 160-table live floor make this the thinnest non-crypto lobby we cover",
  ],
  verdict=("Slotsgem scores lowest on this site and has the best-priced cash offer on it, which is exactly "
           "the sort of result our method is built to surface. NZ$400 at 40x is NZ$16,000 of turnover "
           "&mdash; the smallest demand we track, and one of only two offers a normal player can "
           "realistically finish. The casino itself is genuinely weak: slow payouts, the tightest cap here, "
           "the thinnest library. Come for the offer, understand what you are trading for it."),
  best_for="Clearing a small bonus and moving on",
  narr=[
    ("Lowest score, best offer",
     "<p>Slotsgem sits at the bottom of our scoring at 7.9 and at the top of our ledger, where offers are "
     "sorted cheapest first. Both are correct and the tension between them is the most useful thing on this "
     "page.</p>"
     "<p>Our score measures the casino: payout speed, withdrawal caps, library, licensing, support, "
     "transparency. On those, Slotsgem is the weakest site we cover. The ledger measures the offer, and "
     "NZ$400 at 40x is NZ$16,000 of turnover at an expected cost of NZ$640 &mdash; the smallest demand in "
     "the market.</p>"
     "<p>A big headline at a good casino is usually a worse deal than a small headline at a mediocre one. "
     "That is uncomfortable for a ranked list and it is what the arithmetic says.</p>"),
    ("What you are trading",
     "<p>Slow payouts, and a cap that bites. Four to twenty-four hours on crypto is the widest and slowest "
     "range here; e-wallets take up to two days. The NZ$4,000 weekly ceiling is the tightest of any brand "
     "we cover, so a NZ$40,000 win would take roughly ten weeks to collect.</p>"
     "<p>For clearing a NZ$400 bonus and withdrawing a modest balance, none of that is likely to affect "
     "you. For a long-term account, all of it will.</p>"),
    ("The sensible way to use it",
     "<p>Take the offer, clear it if the play suits you, withdraw, and keep your main account somewhere "
     "better. There is no loyalty argument for staying &mdash; the ongoing proposition is weak and the "
     "welcome offer is the entire value.</p>"
     "<p>If you want a comparable offer at a materially better casino, "
     "<a href='/casino-reviews/ivibet/'>Ivibet</a> at NZ$500 and 35x is the other genuinely clearable "
     "option here, with faster payouts and a larger live floor.</p>"),
  ]),

}


def apply(ops):
    """Merge this masthead's copy over the shared facts."""
    for o in ops:
        v = V.get(o["slug"])
        if v:
            o.update(v)
    return ops
