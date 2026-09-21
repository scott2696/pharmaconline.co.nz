#!/usr/bin/env python3
"""/online-casinos/ — the hub. Every real money online casino NZ players can
reach, compared on the variables that decide the outcome rather than the ones
that decide the marketing."""
from lib import *
import lawdata as L
import bonuscalc as B

PATH = "/online-casinos/"
AUTHOR, CHECKER = "nikau-broughton", "rangi-solomon"
TRAIL = [("Online casinos", PATH)]

FLAGS = {"spinjo": "Best overall", "kingdom": "Best weekly cap", "crownslots": "Largest match",
         "fortune-play": "Best live floor", "lucky7even": "No-deposit start", "rivo": "Best on mobile",
         "smash": "Lowest multiplier", "lucky-vibe": "Best cashback", "madcasino": "Casino + sport",
         "lucky-circus": "NZ$10 entry", "ivibet": "Clearable bonus", "spino": "0x wagering",
         "hellspin": "Longest running", "roby-casino": "Discloses nothing", "slotsgem": "Cheapest to clear"}


def build():
    ops = CASINOS

    # ---- the master comparison: one row per casino, the eight variables ----
    rows = []
    for op in ops:
        p = B.price(op)
        nzd = "NZD bank transfer" in op.get("payments", [])
        rows.append([
            op_cell(op),
            f'<b>{op["rating"]}</b>',
            esc(op["licence"]),
            esc(op["operator_co"]),
            esc(op.get("min_deposit") or "&mdash;"),
            f'<b>{esc(op.get("withdrawal_limit") or "&mdash;")}</b>',
            B.money(p["turnover"]) if p else "&mdash;",
            ('<span class="chip chip--yes">NZD</span>' if nzd
             else '<span class="chip chip--no">' + ("Crypto" if op["slug"] == "spino" else "EUR") + '</span>'),
        ])
    master = table(
      ["Casino", "Score", "Regulator", "Operating company", "Min deposit",
       "Weekly cap", "Bonus turnover", "Banking"],
      rows,
      caption=("Every real money casino NZ players can reach, on the eight variables that decide what "
               f"actually happens to you. Verified from an Auckland IP in {MONTH_YEAR}. Note the third and "
               "fourth columns together &mdash; a regulator with no company behind it is the weakest "
               "disclosure in this market."))

    gates = steps([
      ("It must pay us, from our own funded account",
       "We deposit our own money, play, and request a withdrawal. A brand that does not pay is not "
       "reviewed, not listed and not linked. This is a gate rather than a scoring criterion, because there "
       "is no score that compensates for not being paid."),
      ("It must accept a working New Zealand payment route",
       "A casino that technically accepts New Zealand registrations but declines every card a New Zealand "
       "bank issues is not usable, however good the lobby looks."),
      ("It must state its wagering terms in full before you deposit",
       "Multiplier, basis, game weighting, maximum bet and maximum cashout. We cannot price an offer we "
       "cannot read, and an operator unwilling to publish the basis is telling you something."),
      ("It must carry an age check and a working self-exclusion tool",
       "R18 enforcement and a deposit limit that can be set in the account rather than by emailing "
       "support. A site that makes limits hard to set has made a choice about who it is for."),
    ])

    fit = cards([
      ("You want one account and no further thought",
       "<a href='/casino-reviews/spinjo/'>Spinjo</a>. New Zealand dollars end to end, Rabidi N.V. named, a "
       "licence that resolves on the regulator's register, and the deepest library we audited. The welcome "
       "offer is unremarkable, which our ledger suggests is a feature.", "/casino-reviews/spinjo/"),
      ("You are playing for meaningful sums",
       "<a href='/casino-reviews/kingdom/'>Kingdom</a>'s NZ$10,000 weekly ceiling is the most generous cap "
       "here, and crypto settles in two to four hours. The cap matters more than the payout window once a "
       "win is large. Decline the 600% offer.", "/fast-payout-casinos/"),
      ("You actually want to clear a bonus",
       "Only two cash offers here survive the arithmetic: <a href='/casino-reviews/slotsgem/'>Slotsgem</a> "
       "at NZ$16,000 of turnover and <a href='/casino-reviews/ivibet/'>Ivibet</a> at NZ$17,500. Both are "
       "small. That is why they work.", "/online-casinos/bonuses/"),
      ("You are depositing in twenties",
       "<a href='/casino-reviews/lucky-circus/'>Lucky Circus</a> opens at NZ$10 and is the only site where "
       "the bonus-qualifying minimum is the same NZ$10 rather than being quietly set higher.",
       "/online-casinos/bonuses/#small"),
      ("You hold crypto",
       "<a href='/casino-reviews/spino/'>Spino</a> has the only 0x wagering offer in this market and no "
       "stated weekly cap. Understand the IRD's treatment of crypto as property before you convert back.",
       "/best-crypto-casinos/"),
      ("You play live dealer",
       "<a href='/casino-reviews/fortune-play/'>Fortune Play</a> held the most of its floor open at 9pm "
       "NZT. And decline the bonus &mdash; live blackjack counts 5% or nothing toward wagering.",
       "/live-casinos/"),
      ("You mostly play on a phone",
       "<a href='/casino-reviews/rivo/'>Rivo</a> is the only lobby here where filtering and search work "
       "properly on mobile, which decides whether a 5,000-game library is usable at all.", "/online-pokies/"),
      ("You bet on sport as well",
       "<a href='/casino-reviews/rooster-bet/'>Rooster Bet</a> runs the deepest New Zealand sport markets "
       "on a shared NZD balance. The legal position changed in June 2025 and you should read it.",
       "/online-betting/"),
    ])

    faq_html, faq_ents = faq([
      ("How many online casinos NZ players can use are actually worth using?",
       "<p>Several hundred accept New Zealand registrations; we cover nineteen and rank fifteen for casino "
       "play. The filter is not quality in the abstract &mdash; it is four gates: the operator paid us from "
       "our own funded account, a New Zealand payment route works, the wagering terms are fully published "
       "before deposit, and account-level deposit limits exist. Brands that fail any of those are not "
       "listed at all.</p>"),
      ("Are online casinos safe in NZ?",
       "<p>Safety here is a spectrum, because none of these sites holds a New Zealand licence &mdash; that "
       "regime does not open until 2027. What separates the safe end from the risky end is accountability: "
       "a named operating company, a licence number that resolves on the regulator's own register, "
       "published withdrawal caps and a complaints route that is not the casino's own support desk. One "
       "brand we list, <a href='/casino-reviews/roby-casino/'>Roby Casino</a>, publishes none of the first "
       "three.</p>"),
      ("Which online casino pays out the most in NZ?",
       "<p>Two different questions hide in that one. If you mean payout percentage, that is a property of "
       "the games rather than the casino &mdash; what an operator genuinely controls is which RTP build it "
       "licenses, worth about NZ$20 per NZ$1,000 staked. If you mean which one will actually hand over a "
       "large win fastest, the answer is governed by the weekly withdrawal cap: "
       "<a href='/casino-reviews/kingdom/'>Kingdom</a> at NZ$10,000 a week and "
       "<a href='/casino-reviews/spino/'>Spino</a> with no stated ceiling.</p>"),
      ("What is the best online casino for Kiwis specifically?",
       "<p>The New Zealand-specific variables are currency, payment routes and support hours. On all three "
       "<a href='/casino-reviews/spinjo/'>Spinjo</a> leads: New Zealand dollars end to end so there is no "
       "conversion spread, NZD bank transfer alongside cards and crypto, and a live floor that is still "
       "staffed in our evening. A euro-denominated site costs a New Zealander roughly 4.8% across the "
       "round trip regardless of how well it scores otherwise.</p>"),
      ("Which online casinos accept NZD?",
       "<p>Ten of the fifteen we rank hold New Zealand dollars end to end, including Spinjo, Kingdom, "
       "Rooster Bet, Fortune Play, Lucky Vibe, Lucky7even, Lucky Circus, MadCasino, Smash and Rivo. The "
       "currency column in the table above marks them. The rest hold euros, with the exception of Spino, "
       "which is crypto-only. An NZD online casino saves you a conversion spread on every movement of "
       "money, which compounds in a way a one-off bonus does not.</p>"),
      ("Is online gambling legal in New Zealand?",
       "<p>For you, yes, and it always has been. The Gambling Act 2003 prohibits operating and advertising "
       "unlicensed gambling, not participating in it. The Online Casino Gambling Act 2026 commenced on "
       f"1 May 2026 and will licence up to 15 domestic operators, with applications closing on 1 December "
       f"2026 &mdash; {L.days_to(L.CUTOFF)} days away. "
       "<a href='/nz-online-casino-law/'>The full legal position</a>.</p>"),
      ("What is the best online casino NZ for beginners?",
       "<p>Start where the mistakes are cheapest. <a href='/casino-reviews/lucky-circus/'>Lucky Circus</a> "
       "has a NZ$10 minimum and matching bonus qualifier, or "
       "<a href='/casino-reviews/lucky7even/'>Lucky7even</a> lets you try the cashier on 20 no-deposit "
       "spins before funding anything. And the most useful beginner advice in this market: decline the "
       "welcome bonus. It keeps your balance withdrawable and removes every clause that can void your "
       "winnings.</p>"),
      ("What do people on Reddit say about the best online casino NZ?",
       "<p>The recurring themes in New Zealand gambling threads are consistent and match our own testing: "
       "complaints are about withdrawals rather than rigged games, verification delays cause most of the "
       "frustration, and euro conversion costs surprise people. What forum threads rarely surface is the "
       "wagering arithmetic &mdash; the reason a 600% offer is worse than a 100% one is not obvious and "
       "almost never gets explained. <a href='/online-casinos/bonuses/'>That is what our ledger is "
       "for</a>.</p>"),
    ], "Online casinos NZ &mdash; the questions worth asking", "faq")

    paa_html, paa_ents = faq([
      ("What is the most trusted online casino in NZ?",
       "<p>Trust in this market is a disclosure question rather than a reputation one. The most trusted "
       "online casino NZ side, on checkable criteria, is the one that names its operating company, holds a "
       "licence that resolves on the regulator's register and publishes its withdrawal caps &mdash; which "
       "points to the Cura&ccedil;ao Gaming Control Board brands, Spinjo and Fortune Play foremost.</p>"),
      ("Are there new online casinos NZ players should look at?",
       "<p>Several launched in 2024 and more will arrive with the licensed regime in 2027. New is not a "
       "quality signal by itself &mdash; what matters is whether a new site names a company and publishes "
       "its terms from day one. <a href='/new-casinos-nz/'>Our running launch list</a>.</p>"),
      ("Can I use an online casino NZ real money account with no deposit?",
       "<p>You can start one. A no-deposit offer credits spins or a small balance on registration, which "
       "lets you see the cashier and the lobby before funding anything. The winnings carry heavy wagering "
       "and a maximum cashout, so treat it as a free look rather than a route to money. "
       "<a href='/no-deposit-casinos/'>Every no-deposit offer priced</a>.</p>"),
      ("What is the best online casino NZ low deposit option?",
       "<p><a href='/casino-reviews/lucky-circus/'>Lucky Circus</a> at NZ$10, and it is the only site here "
       "where the bonus-qualifying minimum matches the deposit minimum. At most sites they differ, which "
       "is why a NZ$10 deposit elsewhere often produces no bonus and no explanation.</p>"),
      ("What is the best rated online casino in New Zealand?",
       "<p>On our scoring, <a href='/casino-reviews/spinjo/'>Spinjo</a> at 9.3, followed by "
       "<a href='/casino-reviews/kingdom/'>Kingdom</a> at 9.1. Our listing order is commercial and we "
       "disclose that under every table; the score is not, and where the two disagree the score is the "
       "figure to read. <a href='/how-we-rate/#money'>How that works</a>.</p>"),
    ], "People also ask", "paa")

    body = f"""
{crumbs(TRAIL)}
{lede(h1=H1[PATH],
  lead=("<p>Several hundred online casinos accept New Zealand registrations. Fifteen are worth a table, and "
        "the variables that separate them are not the ones the industry advertises.</p>"
        "<p>What decides your experience is the weekly withdrawal cap, whether the balance is held in New "
        "Zealand dollars, whether anyone is named as the operating company, and what the welcome offer "
        "costs to clear. All four are in the table below. None of the four appears on a banner.</p>"),
  stats=[(f"{len(ops)}", "Casinos ranked"), ("4", "Gates before scoring"),
         ("10", "That hold New Zealand dollars"), ("2", "Bonuses worth claiming")],
  eyebrow_txt=f"Casino hub &middot; {MONTH_YEAR}", author=AUTHOR, checker=CHECKER,
  toplist_h2="Every real money online casino NZ players can reach",
  toplist_intro=("Our commercial order, disclosed under every table on this site. The score beside each "
                 "brand is not commercial, and it does not follow the order."),
  toplist_html=leaderboard(pick([o["slug"] for o in ops]), flags=FLAGS, cta="Visit Casino"),
  offer=top_offer_strip(ops),
  toplist_note=toc([("The full comparison", "compare"),
                    ("Who is actually behind each brand", "who"),
                    ("The four gates", "gates"),
                    ("Banking from a New Zealand account", "banking"),
                    ("Start from how you play", "fit"),
                    ("What changes in 2027", "transition"),
                    ("FAQ", "faq")]))}

{sec(f'''{sechead("The full comparison", "Eight columns. Six of them are never on a casino&rsquo;s "
  "own comparison page, which is the point.", 2, "compare")}
{master}''', ident="compare")}

{sec(f'''{sechead("Safe, trusted and top online casinos NZ: what the words should mean", None, 2, "who")}
<div class="prose">
<p>Every comparison page in this market promises safe online casinos NZ side, trusted online casinos NZ
side, the best casino sites NZ has. The words are free. Here is what they should mean, and how to check
each one yourself in about ninety seconds.</p>
<p>A licence badge is an image, and images are copied. The list of top online casinos NZ players are shown
is only as good as the verification behind it, so this is the verification.</p>
<p>Look at the third and fourth columns of the table above together. What you want is a <b>regulator</b>
and an <b>operating company</b> &mdash; a real legal entity with a registration number, named in the
footer. Rabidi N.V., Dama N.V., Vertikal N.V. and TechOptions Group are the companies behind most of this
market, and each runs several brands that share infrastructure and cashiers.</p>
<p>Then take the licence number to the regulator&rsquo;s own register and confirm it returns the company
named in the footer. A mismatch between the two is the single clearest warning available to a player.</p>
<h3>The three tiers, honestly</h3>
<ul>
<li><b>Cura&ccedil;ao Gaming Control Board with a named company</b> &mdash; the strongest position here.
The regime was reformed in 2023 and carries a public register and defined complaint handling. Spinjo,
Fortune Play, Rooster Bet, Lucky7even, Lucky Vibe, Lucky Circus and Bet&amp;Play.</li>
<li><b>Anjouan or an older Cura&ccedil;ao licence with a named company</b> &mdash; weaker oversight, but
you still know who you are dealing with. Kingdom, Smash, Rivo, MadCasino, Ivibet, Hellspin, Slotsgem.</li>
<li><b>No company named</b> &mdash; CrownSlots, Gunsbet, Spino. And
<a href="/casino-reviews/roby-casino/">Roby Casino</a>, which publishes no regulator either, and is the
only brand here where all three disclosures are absent.</li>
</ul>
{note('<p><b>Our disclosure, since this section is about disclosure.</b> Roby Casino pays us one of the '
      'highest commission rates in our portfolio. We score it 8.1, among the three lowest on this site, '
      'with this warning on every page it appears on. Our listing order is commercial and we say so under '
      'every table. The score is not. <a href="/how-we-rate/#money">How that works</a>.</p>', "warn")}
</div>''', ident="who", haze=True)}

{sec(f'''{sechead("The four gates a casino passes before we score it", "Not criteria. Gates. Fail one and "
  "there is no review.", 2, "gates")}
{gates}''', ident="gates")}

{sec(f'''{sechead("Banking from a New Zealand account", None, 2, "banking")}
<div class="prose">
<p>Three things cost New Zealanders money here, and only one of them is ever discussed.</p>
<h3>1. The currency you are holding</h3>
<p>Ten of the fifteen casinos here hold New Zealand dollars end to end. The rest hold euros, and a euro
balance costs you a conversion spread <i>twice</i> &mdash; going in and coming out &mdash; totalling around
{B.FX_SPREAD*100:.1f}% of the round trip. On NZ$1,000 that is about NZ$48. It never appears as a fee; it
appears as a smaller number arriving than the one you expected. Over a year it comfortably exceeds the
difference between any two welcome offers on this page.</p>
<h3>2. Whether your bank will allow the transaction</h3>
<p>Several major New Zealand banks now decline gambling merchant category codes on credit cards as policy,
and some extend it to debit. A declined deposit is usually your bank rather than the casino. POLi remains
the most reliable New Zealand-specific route, Neosurf covers players who would rather not connect a bank
account at all, and crypto bypasses the question entirely.</p>
<h3>3. The weekly cap, which is not a banking detail but behaves like one</h3>
<p>Every site here except Spino caps weekly withdrawals, between &euro;4,000 and NZ$10,000. That figure
decides how long a large win takes to reach you, no matter how fast the payout rail is. A NZ$40,000 win at
a &euro;4,000 ceiling takes six weeks and pays a conversion spread on each instalment.
<a href="/fast-payout-casinos/#caps">The full cap comparison</a>.</p>
<p><a class="btn btn--ghost" href="/payment-methods/">Every payment method, with fees and limits &rarr;</a></p>
</div>''', ident="banking")}

{sec(f'''{sechead("Start from how you play, not from the rankings")}
{fit}''', ident="fit", haze=True)}

{sec(f'''{sechead("What the 2027 licensing transition means for your account", None, 2, "transition")}
<div class="prose">
<p>The market these casinos operate in is about to change shape, and it is worth understanding before you
open an account you intend to keep.</p>
<p>The <b>Online Casino Gambling Act 2026</b> commenced on <b>1 May 2026</b>. It creates a licensed
domestic market administered by the Department of Internal Affairs, with up to <b>15 licences</b>.
Applications close on <b>1 December 2026</b> &mdash; {L.days_to(L.CUTOFF)} days from today &mdash; and the
first licensed sites are expected during 2027.</p>
<h3>What improves</h3>
<p>A licensed operator will be bound by New Zealand harm-minimisation rules, a domestic complaints route
and DIA oversight. For a player that is a materially stronger position than any offshore licence offers,
and it is the first time New Zealanders will have somewhere local to escalate.</p>
<h3>What to expect from the offshore sites</h3>
<p>Some will apply for a licence and some will not. Those that do not will continue operating as they do
now &mdash; the Act binds operators rather than players, so your account does not become unlawful. But the
advertising and affiliate restrictions arriving with the licensed market mean the information environment
around them will thin out considerably.</p>
{note('<p><b>And what it means for this site.</b> The Act <b>prohibits affiliate marketing by licensed '
      'operators</b>. When the licensed market opens, the commercial model funding this page will not be '
      'available for those brands. We would rather tell you what our incentives are, and that they are '
      'about to change, than have you work it out later. '
      '<a href="/nz-online-casino-law/">The regime in detail</a>.</p>', "info")}
</div>''', ident="transition")}

{sec(f'<div class="prose">{faq_html}</div>', ident="faqsec")}
{sec(f'<div class="prose">{paa_html}</div>' + authorbox(AUTHOR), ident="paasec", haze=True)}
"""

    schema = [
        schema_webpage(PATH, META[PATH][0], META[PATH][1]),
        schema_breadcrumb(PATH, TRAIL),
        schema_article(PATH, META[PATH][0], META[PATH][1], AUTHOR, CHECKER),
        schema_person(AUTHOR), schema_person(CHECKER),
        schema_itemlist(PATH, ops),
        schema_faq(PATH, faq_ents + paa_ents),
    ]
    return write(PATH, page(PATH, body, schema), priority=0.95, freq="daily")
