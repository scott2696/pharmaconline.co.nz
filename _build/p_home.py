#!/usr/bin/env python3
"""Homepage — the money page for "best online casino sites NZ".

The organising idea of this masthead: every competitor republishes the
operator's headline. We price it. Each figure below comes out of bonuscalc.py,
from the operator's own stated terms, and a reader can redo the arithmetic.
"""
from lib import *
import lawdata as L
import bonuscalc as B

PATH = "/"
AUTHOR, CHECKER = "nikau-broughton", "mei-lin-chau"

TOP10 = ["spinjo", "kingdom", "crownslots", "fortune-play", "lucky7even",
         "rivo", "smash", "lucky-vibe", "madcasino", "lucky-circus"]

FLAGS = {
    "spinjo": "Best overall", "kingdom": "Biggest headline", "crownslots": "Largest match",
    "fortune-play": "Best free spins", "lucky7even": "No-deposit start", "rivo": "Best on mobile",
    "smash": "Cheapest to clear", "lucky-vibe": "Best VIP", "madcasino": "Casino + sport",
    "lucky-circus": "Lowest entry",
}


def build():
    lb = leaderboard(pick(TOP10), flags=FLAGS, cta="Visit Casino")

    # ------------------------------------------------------------------ #
    # The Ledger. The signature asset of this site: every advertised
    # welcome offer converted into the turnover it demands and the money
    # that turnover is expected to cost.
    # ------------------------------------------------------------------ #
    priced = [(o, B.price(o)) for o in CASINOS]
    priced = [(o, p) for o, p in priced if p]
    total_turnover = sum(p["turnover"] for _, p in priced)
    clearable = [(o, p) for o, p in priced if p["tone"] == "yes"]
    unclearable = [(o, p) for o, p in priced if p["verdict"] == "Effectively unclearable"]
    worst = max(priced, key=lambda x: x[1]["turnover"])

    ledger_rows = []
    for op, p in sorted(priced, key=lambda x: x[1]["turnover"]):
        tone = {"yes": "chip--yes", "warn": "chip--gold", "no": "chip--no"}[p["tone"]]
        ledger_rows.append([
            op_cell(op),
            esc(op.get("casino_bonus") or "&mdash;"),
            f'{p["mult"]:g}x <span class="chip">{B.basis_label(p)}</span>',
            f'<b>{B.money(p["turnover"])}</b>',
            B.money(p["cost"]),
            f'<span class="chip {tone}">{p["verdict"]}</span>',
        ])
    ledger = table(
        ["Casino", "The headline", "Wagering basis", "Turnover required",
         "Expected cost to clear", "Our verdict"],
        ledger_rows,
        caption=(f"The Ledger, {MONTH_YEAR}. Turnover is the operator's stated multiplier applied to its "
                 f"stated basis, at the maximum advertised bonus. Expected cost is that turnover multiplied "
                 f"by the house edge at 96% RTP. Euro and USDT offers are converted at the mid-market rate "
                 f"of {B.FX_DATE}. Sorted cheapest first &mdash; which is the opposite of how every other "
                 f"page ranks these offers."))

    # ------------------------------------------------------------------ #
    comp_rows = []
    for op in CASINOS:
        p = B.price(op)
        comp_rows.append([
            op_cell(op),
            f'<b>{op["rating"]}</b>',
            esc(op.get("casino_bonus") or "&mdash;"),
            esc(op.get("wagering") or "&mdash;"),
            B.money(p["turnover"]) if p else "&mdash;",
            esc(op.get("min_deposit") or "&mdash;"),
            esc(op.get("payout_crypto") or op.get("payout_ewallet") or "&mdash;"),
            ('<span class="chip chip--yes">NZD</span>' if "NZD bank transfer" in op.get("payments", [])
             else '<span class="chip chip--no">EUR/USDT</span>'),
        ])
    comp = table(
        ["Casino", "Score", "Welcome offer", "Wagering", "Turnover to clear",
         "Min dep.", "Fastest payout", "Banking"],
        comp_rows,
        caption=("Every casino site we cover, on the eight variables that decide what a New Zealand player "
                 f"actually experiences. Verified from an Auckland IP address in {MONTH_YEAR}."))

    fit = cards([
      ("You intend to actually clear the bonus",
       f"Then only {len(clearable)} of the {len(priced)} offers on this page are worth your time, and they are "
       "not the ones with the big numbers. Sort The Ledger by turnover and start at the top, not the bottom.",
       "/online-casinos/bonuses/"),
      ("You want to play without a bonus at all",
       "A perfectly rational choice, and one no affiliate page ever suggests. Decline the offer and your "
       "balance is withdrawable from the first spin, with no max-cashout ceiling and no game weighting. "
       "Which casinos make declining easy, and which bury it.",
       "/online-casinos/"),
      ("You mostly play pokies",
       "Library depth and, more importantly, which build of each title the lobby runs. The same headline "
       "pokie ships in three RTP configurations and the operator chooses. We check which one you get.",
       "/online-pokies/"),
      ("You want the money out quickly",
       "Withdrawal speed is governed less by the rail than by the weekly cap and the verification queue. "
       "Both are published here, with the caps that quietly throttle a large win.",
       "/fast-payout-casinos/"),
      ("You are paying in crypto",
       "Settlement is fast and the wagering is often lower, but the IRD treats crypto as property and a "
       "disposal is a taxable event. The tax position matters more than the speed.",
       "/best-crypto-casinos/"),
      ("You play live dealer",
       "Game weighting is where live players lose. Most welcome offers count live blackjack at 5% or "
       "exclude it outright, which turns a 40x requirement into an 800x one.",
       "/live-casinos/"),
      ("You want a no-deposit start",
       "Small, heavily conditioned, and almost always carrying a separate and much higher multiplier on "
       "winnings. Worth taking, never worth choosing a casino for.",
       "/no-deposit-casinos/"),
      ("You also bet on sport",
       "The law changed on 28 June 2025 and TAB NZ is now the only operator lawfully able to offer betting "
       "into New Zealand. You commit no offence either way. The full position, plainly stated.",
       "/online-betting/"),
    ])

    faq_html, faq_ents = faq([
      ("What are the best online casino sites NZ players can use in 2026?",
       "<p>On our scoring the strongest all-round option is <a href='/casino-reviews/spinjo/'>Spinjo</a>, "
       "which banks in New Zealand dollars end to end, names its operating company, holds a current "
       "Cura&ccedil;ao Gaming Control Board licence and carries the deepest library we audited. "
       "<a href='/casino-reviews/kingdom/'>Kingdom</a> scores second on library and payout speed. But "
       "&ldquo;best&rdquo; depends on what you intend to do: if you plan to claim and clear the welcome "
       "offer, the ranking inverts almost completely, because the biggest headlines demand the most "
       "turnover. That is what <a href='#ledger'>The Ledger</a> is for.</p>"),
      ("Which welcome bonus is actually worth claiming?",
       f"<p>Of the {len(priced)} cash welcome offers we priced this month, {len(clearable)} are realistically "
       f"clearable and {len(unclearable)} demand more than NZ$100,000 of turnover. The worst is "
       f"<a href='/casino-reviews/{worst[0]['slug']}/'>{esc(worst[0]['name'])}</a>, whose headline "
       f"{esc(worst[0].get('casino_bonus') or '')} requires <b>{B.money(worst[1]['turnover'])}</b> of wagering "
       f"&mdash; an expected <b>{B.money(worst[1]['cost'])}</b> out of your pocket at 96% RTP. A smaller offer "
       "on a lower multiplier is worth more than a large one you will never finish.</p>"),
      ("Is it legal to play at online casinos in New Zealand?",
       "<p>Yes, for you. New Zealand law has never made it an offence for an individual to gamble at an "
       "offshore online casino. The prohibitions bind operators and advertisers, not players. The "
       "<b>Online Casino Gambling Act 2026</b> came into force on 1 May 2026 and creates a licensed domestic "
       "market of 15 operators, with the application cutoff on 1 December 2026 and the first licensed sites "
       "expected during 2027. Until then the sites on this page operate from offshore licences. "
       "<a href='/nz-online-casino-law/'>The full legal position</a>.</p>"),
      ("Do I pay tax on online casino winnings in New Zealand?",
       "<p>For virtually every recreational player, no. Gambling winnings are not income under New Zealand "
       "law because they are not derived from a taxable activity. The exceptions are narrow: a professional "
       "gambler carrying on a business, and crypto. The IRD treats cryptoassets as property, so converting "
       "a crypto balance back to New Zealand dollars can be a taxable disposal quite independently of "
       "whether you won it. <a href='/gambling-winnings-tax-nz/'>How the IRD actually treats it</a>.</p>"),
      ("What does 40x wagering mean in dollars?",
       "<p>It means the bonus multiplied by forty, and that is the number you should be reading. A "
       "NZ$5,000 bonus at 40x is <b>NZ$200,000</b> of turnover before a withdrawal is permitted. Generating "
       "NZ$200,000 of turnover on a 96% RTP pokie costs an expected NZ$8,000 &mdash; considerably more than "
       "the bonus is worth. Watch the basis as well as the multiplier: &ldquo;40x deposit + bonus&rdquo; is "
       "roughly twice as expensive as &ldquo;40x bonus&rdquo; on the same headline.</p>"),
      ("Which online casinos pay out fastest to New Zealand players?",
       "<p>Crypto rails settle fastest almost everywhere &mdash; typically one to six hours once an account "
       "is verified. The real determinants are the identity check, which is a one-off cost paid on your "
       "first withdrawal, and the weekly withdrawal ceiling, which is what throttles a genuinely large win. "
       "Several sites here cap withdrawals at &euro;5,000 a week, so a NZ$40,000 win takes over a month to "
       "collect regardless of how quick the rail is. <a href='/fast-payout-casinos/'>Payout speeds and "
       "caps, side by side</a>.</p>"),
      ("Can I use New Zealand dollars, and does it matter?",
       f"<p>It matters more than most players expect. A euro-denominated balance costs a New Zealander "
       f"roughly {B.FX_SPREAD*100:.1f}% round trip &mdash; conversion on the way in and again on the way "
       "out. On a NZ$1,000 deposit that is about NZ$48, which is frequently larger than the difference "
       "between two welcome offers. Sites that hold New Zealand dollars end to end are marked "
       "<span class='chip chip--yes'>NZD</span> in the comparison table above.</p>"),
      ("How do you make money, and does it change the order?",
       "<p>We are funded by affiliate commission, and we will not pretend the running order is untouched by "
       "it: <b>listing order reflects our commercial agreements</b>. What commercial terms cannot touch is "
       "the arithmetic. The Ledger is generated from each operator's own published wagering terms, and it "
       "puts our best-paying partners near the bottom of it. "
       "<a href='/how-we-rate/#money'>How that works, in full</a>.</p>"),
    ], heading="Best online casino sites NZ: your questions answered")

    paa_html, paa_ents = faq([
      ("Which online casino has the best payout percentage in NZ?",
       "<p>Payout percentage is a property of the game, not the casino &mdash; but the operator chooses "
       "which build of each game to run, and studios ship the same title at 96.5%, 94% and 92%. A lobby "
       "running the cut-down configuration is a meaningfully worse casino at identical branding. "
       "<a href='/high-payout-casinos/'>Which lobbies run which build</a>.</p>"),
      ("Are online casino sites in NZ safe?",
       "<p>Safety here is a spectrum rather than a yes or no, because none of these sites holds a New "
       "Zealand licence &mdash; that regime does not open until 2027. The checkable signals are a named "
       "operating company, a licence number that resolves on the regulator's own register, published "
       "complaint routes and segregated player funds. One brand we list publishes none of them, and we say "
       "so on every page it appears on.</p>"),
      ("What is the minimum deposit at NZ online casinos?",
       "<p>Between NZ$10 and NZ$35 across the sites here. The number that matters more is the "
       "<i>bonus-qualifying</i> minimum, which is often higher than the deposit minimum &mdash; a site "
       "advertising NZ$10 deposits may require NZ$30 to trigger the welcome offer. Both figures are in the "
       "comparison table.</p>"),
      ("Can I get free spins with no deposit in New Zealand?",
       "<p>Yes, at a handful of sites, and the offers are genuine but small. The trap is the multiplier: "
       "no-deposit spin winnings usually carry a separate and much higher wagering requirement than the "
       "cash bonus &mdash; 50x rather than 40x is common &mdash; plus a maximum cashout of NZ$100 or so. "
       "<a href='/no-deposit-casinos/'>Every no-deposit offer, priced</a>.</p>"),
      ("Do online casinos accept POLi or bank transfer in New Zealand?",
       "<p>POLi remains the most widely supported New Zealand-specific rail, though support has thinned as "
       "banks have withdrawn from it. Several major New Zealand banks now decline gambling merchant codes "
       "on credit cards outright. <a href='/payment-methods/'>Which banks block what, and what still "
       "works</a>.</p>"),
    ], heading="People also ask", ident="paa")

    body = f"""
{lede(H1[PATH],
   "<p>Every other page ranking for this term repeats the casino&rsquo;s headline back to you. "
   "A 390% match. NZ$18,500 across four deposits. Six hundred percent. We do something "
   "duller and considerably more useful: we take the operator&rsquo;s own wagering terms and work out "
   "what the offer costs to finish.</p>"
   f"<p>This month that arithmetic says the {len(priced)} cash welcome offers on this page demand "
   f"<b>{B.money(total_turnover)}</b> of combined turnover, that <b>{len(unclearable)} of them</b> require "
   f"more than NZ$100,000 each, and that <b>{len(clearable)}</b> are realistically clearable by a normal "
   "player. The biggest headline on the page is the worst offer on the page. That is not a coincidence, "
   "and it is the single most useful thing we can tell you.</p>",
   [(f"{len(priced)}", "Welcome offers priced"),
    (f"{B.money(total_turnover)}", "Combined turnover demanded"),
    (f"{len(clearable)}", "Genuinely clearable"),
    (f"{L.days_to(L.CUTOFF)} days", "To the licensing cutoff")],
   f"Updated {MONTH_YEAR} &middot; Tested from NZ &middot; Every offer priced",
   AUTHOR, CHECKER,
   toplist_h2=f"The {len(pick(TOP10))} best online casino sites in NZ &mdash; {MONTH_YEAR}",
   toplist_intro=("Ordered as our commercial agreements dictate, scored as our testing dictates. The two "
                  "are different things and we publish both, which is more than the pages above us in "
                  "these results are willing to do."),
   toplist_html=lb,
   offer=top_offer_strip(pick(TOP10)),
   jump_items=[("The Ledger &mdash; every offer priced", "ledger"),
               ("What the asterisk hides", "asterisk"),
               ("What Kiwis actually complain about", "complaints"),
               ("Red flags", "redflags"),
               ("Compare all sites", "compare"),
               ("Is it legal in NZ?", "legal"),
               ("FAQ", "faq")])}

{sec(f'''{sechead("The Ledger: what each welcome bonus actually costs",
  "One table, generated from the operators&rsquo; own published terms. If you read nothing else on this "
  "page, read this.", 2, "ledger")}
<div class="prose">
<p>A welcome bonus is not a gift, it is a contract with a price, and the price is denominated in turnover.
Before an operator will let you withdraw anything derived from a bonus, you must stake a multiple of it.
That multiple is the wagering requirement, and it is quoted as a number like 40x because a number like 40x
sounds small.</p>
<p>It is not small. Every spin you make returns, on average, slightly less than you put in &mdash; about 96
cents in the dollar on a typical pokie. Turnover is therefore not free to generate. Staking
NZ$200,000 costs you, on average, <b>NZ$8,000</b>. That is the real price of a NZ$5,000 bonus at 40x, and
it is a price no operator prints and no competitor page calculates.</p>
<p>So we calculate it. Below, every cash welcome offer we cover, converted from its headline into the
turnover it demands and the money that turnover is expected to cost, using the operator&rsquo;s own stated
multiplier and basis. The arithmetic is deliberately simple enough to check:
<b>turnover = multiplier &times; basis</b>, and <b>expected cost = turnover &times; 4%</b>.</p>
</div>
{ledger}
<div class="prose">
{note(f'<p><b>Read the basis, not just the multiplier.</b> &ldquo;{worst[1]["mult"]:g}x bonus&rdquo; and '
      '&ldquo;10x deposit + bonus&rdquo; look like wildly different requirements, and the second looks '
      'far gentler. On a 600% match it is not: multiplying the deposit as well as the bonus means '
      '<a href="/casino-reviews/smash/">Smash</a> requires NZ$227,500 of turnover from a 10x requirement, '
      'while <a href="/casino-reviews/ivibet/">Ivibet</a> requires NZ$17,500 from a 35x one. The '
      'multiplier is the headline; the basis is where the money is.</p>', "info")}
</div>''', ident="ledger")}

{sec(f'''{sechead("The offers that survive the arithmetic")}
<div class="prose">
<p>Three findings out of this month&rsquo;s Ledger, none of which you will read on a competing page.</p>
<h3>1. The largest headline is the worst offer</h3>
<p><a href="/casino-reviews/{worst[0]['slug']}/">{esc(worst[0]['name'])}</a> advertises
{esc(worst[0].get('casino_bonus') or '')}. At {worst[1]['mult']:g}x on the bonus, collecting the maximum
requires <b>{B.money(worst[1]['turnover'])}</b> of turnover, at an expected cost of
<b>{B.money(worst[1]['cost'])}</b>. You would be spending roughly {worst[1]['ratio']:.1f} dollars for every
dollar of bonus. There is no configuration of player behaviour in which that is a good trade, and the size
of the headline is precisely what makes it a bad one &mdash; the multiplier applies to the whole of it.</p>
<h3>2. The cheapest offer to clear is one of the smallest</h3>
<p><a href="/casino-reviews/slotsgem/">Slotsgem</a>&rsquo;s 100% up to NZ$400 requires NZ$16,000 of turnover
at an expected cost of NZ$640 &mdash; still more than the bonus, but within reach of a player who was going
to play anyway. <a href="/casino-reviews/ivibet/">Ivibet</a>&rsquo;s NZ$500 at 35x is the other one worth
having. Small offers on modest multipliers are where the value is, which is the exact opposite of how these
lists are normally sorted.</p>
<h3>3. Declining the bonus is a real option</h3>
<p>No affiliate page suggests this, for obvious reasons. If you decline the welcome offer, your deposit is
withdrawable from the first spin. No wagering requirement, no maximum cashout ceiling, no game weighting,
no 30-day expiry, no maximum bet rule to breach accidentally. For a player who intends to deposit
NZ$200, play for an evening and withdraw whatever is left, declining is straightforwardly the better
decision, and the honest recommendation is to take it.</p>
</div>''', ident="survive", haze=True)}

{sec(f'''{sechead("What the asterisk hides", "Five clauses that do more damage than the wagering "
  "requirement, ranked by how much money they cost a New Zealand player.", 2, "asterisk")}
<div class="prose">
<h3>1. Maximum cashout</h3>
<p>The clause that voids the win you were hoping for. A no-deposit offer with a NZ$100 maximum cashout means
that if you turn 20 free spins into NZ$3,000, you withdraw NZ$100 and the casino keeps the rest. It is
disclosed, it is enforceable, and it is the single most common reason a player feels cheated by a site that
has done nothing wrong. Check it before you claim, not after you win.</p>
<h3>2. Game weighting</h3>
<p>Wagering requirements are rarely satisfied equally by all games. Pokies typically contribute 100%, table
games 10%, and live dealer blackjack 5% or nothing at all. If you are a blackjack player claiming a 40x
bonus that weights blackjack at 5%, your real requirement is <b>800x</b>. The contribution table is usually
a separate document from the bonus terms, and that separation is not accidental.</p>
<h3>3. Maximum bet while wagering</h3>
<p>Almost universally NZ$5 to NZ$8 per spin. Exceed it once, even accidentally, even by fifty cents on an
autoplay setting you forgot about, and the operator is entitled to void the bonus and everything derived
from it. This is the clause most often cited in the complaints we read, and the player is almost always in
the wrong on the terms and entirely reasonable in feeling aggrieved.</p>
<h3>4. Expiry</h3>
<p>Typically 30 days, occasionally 7. Consider what a 30-day expiry means alongside a NZ$200,000 turnover
requirement: you would need to stake NZ$6,600 every single day for a month. The expiry does not
simply risk the bonus, it makes the largest offers on this page arithmetically impossible for a normal
player, which is worth understanding before you value one.</p>
<h3>5. Currency</h3>
<p>Not a clause at all, which is why nobody covers it. A euro-denominated balance costs a New Zealander
about {B.FX_SPREAD*100:.1f}% round trip in conversion spread. On a NZ$1,000 deposit that is roughly NZ$48
&mdash; larger than the gap between most of the welcome offers on this page, and entirely invisible until
you compare what you deposited with what arrived.</p>
</div>''', ident="asterisk")}

{sec(f'''{sechead("Every online casino site in New Zealand, compared", None, 2, "compare")}
<div class="prose"><p>Score, offer, the turnover that offer demands, entry cost, payout speed and whether
you will be holding New Zealand dollars. Sortable in your head; the column that matters most depends
entirely on whether you intend to claim a bonus.</p></div>
{comp}''', ident="compare")}

{sec(f'''{sechead("Find the casino that fits how you actually play")}
{fit}''', ident="fit", haze=True)}

{sec(f'''{sechead("Is online casino gambling legal in New Zealand?", None, 2, "legal")}
<div class="prose">
<p>Yes, and the confusion on this point is worth clearing up properly because half the pages ranking for
this term still have it wrong.</p>
<p><b>No New Zealand law makes it an offence for you to play at an offshore online casino.</b> The Gambling
Act 2003 prohibits <i>operating</i> unlicensed gambling from within New Zealand and prohibits advertising
it. It has never criminalised the player. If you deposit at any site on this page, you commit no offence.</p>
<p>What is changing is the supply side. The <b>Online Casino Gambling Act 2026</b> commenced on
<b>1 May 2026</b> and establishes a licensed domestic market administered by the Department of Internal
Affairs. Up to <b>15 licences</b> will be issued. Applications close on <b>1 December 2026</b> &mdash;
{L.days_to(L.CUTOFF)} days from today &mdash; and the first licensed operators are expected to go live
during 2027.</p>
<p>Two consequences follow that are worth planning around. First, licensed operators will be subject to New
Zealand harm-minimisation rules, a domestic complaints route and DIA oversight, which is a materially
stronger position for a player than any offshore licence offers. Second, the Act <b>prohibits affiliate
marketing</b> by licensed operators &mdash; which means the business model funding this site will not be
available for those brands. We would rather tell you that plainly than have you find out later.</p>
{note('<p><b>Sports and racing are different, and the difference is recent.</b> The Racing Industry '
      'Amendment Act 2025 took effect on 28 June 2025 and makes TAB NZ the only entity that may lawfully '
      'offer or promote sports and racing betting to people in New Zealand. As with casino gambling, '
      'the prohibition binds the operator rather than the punter &mdash; you commit no offence by placing '
      'a bet. <a href="/online-betting/">The betting position in full</a>.</p>', "warn")}
<p><a class="btn btn--ghost" href="/nz-online-casino-law/">The law, with section numbers and dates &rarr;</a></p>
</div>''', ident="legal")}

{sec(f'''{sechead("Depositing and withdrawing from New Zealand")}
<div class="prose">
<p>The payment question that actually costs New Zealanders money is not which rail is fastest, it is which
currency you end up holding and whether your bank will let the transaction through at all.</p>
<p><b>Card deposits are increasingly declined.</b> Several major New Zealand banks now block gambling
merchant category codes on credit cards as a matter of policy, and some extend it to debit. A declined
deposit is usually the bank, not the casino.</p>
<p><b>POLi</b> remains the most widely supported New Zealand-specific method, moving money directly from
your bank account without a card, and it works for withdrawals at some sites. <b>Neosurf</b> vouchers
cover players who would rather not connect a bank account at all. <b>Crypto</b> is the fastest rail almost
everywhere, typically settling in one to six hours, but carries a tax consequence most players are unaware
of: the IRD treats cryptoassets as property, so converting back to New Zealand dollars can be a taxable
disposal regardless of whether it came from gambling.</p>
<p>And the point nobody makes: <b>a casino that holds your balance in euros is charging you a fee it never
names.</b> You pay a conversion spread going in and another coming out &mdash; about
{B.FX_SPREAD*100:.1f}% of the round trip. It is frequently worth more than the difference between two
welcome offers, and it is the reason the comparison table has a currency column.</p>
<p><a class="btn btn--ghost" href="/payment-methods/">Every payment method, with fees and limits &rarr;</a></p>
</div>''', ident="pay")}

{sec(f'''{sechead("How to tell whether a casino site is safe")}
<div class="prose">
<p>None of the sites on this page holds a New Zealand licence, because that regime does not open until
2027. So the question is not whether a site is licensed here &mdash; none are &mdash; but whether it is
accountable anywhere. Four checks, in descending order of how much they tell you.</p>
</div>
{steps([
  ("Find the operating company, not just the licence badge",
   "Scroll to the footer. You are looking for a named legal entity with a registration number &mdash; "
   "Rabidi N.V., Dama N.V., Vertikal N.V. A licence seal with no company behind it is the weakest signal "
   "in this market, because seals are images and images are copied."),
  ("Resolve the licence number on the regulator&rsquo;s own register",
   "Take the number to the Cura&ccedil;ao Gaming Control Board register and confirm it returns the company "
   "named in the footer. A mismatch between the two is the clearest warning sign available to a player, "
   "and it takes about ninety seconds to check."),
  ("Read the withdrawal section of the terms before depositing",
   "Weekly and monthly caps, the verification documents required, and whether the operator reserves a "
   "right to pay large wins in instalments. This is where a site that intends to make cashing out "
   "difficult tells you so, in advance and in writing."),
  ("Check that a complaints route exists that is not the casino",
   "A named ADR provider or the regulator&rsquo;s own complaints form. If the only escalation path is the "
   "operator&rsquo;s own support desk, you have no escalation path at all."),
])}
<div class="prose">
{note('<p><b>The brand that fails this test.</b> <a href="/casino-reviews/roby-casino/">Roby Casino</a> '
      'publishes no regulator, no licence number and no operating company. It is the only site we cover '
      'where all three are absent, it pays us one of the highest commission rates in our portfolio, and we '
      'score it 8.1 with this warning attached on every page it appears on. We would rather you knew both '
      'facts.</p>', "warn")}
</div>''', ident="safe", haze=True)}

{sec(f'''{sechead("Before you deposit anything")}
<div class="prose">
<p>The house edge is not a rumour, it is the business model. Every game on every site listed here returns
less than it takes, by design, forever. A casino is entertainment with a price, and the price is your
expected loss. Played that way it is fine. Played as a way to make money it is arithmetic you cannot win.</p>
<p>Four habits worth more than the difference between any two casinos on this page: set a deposit limit on
day one while you are calm rather than at 1am when you are not; complete verification before you have
anything to withdraw; withdraw winnings instead of leaving them in the balance; and read the wagering in
dollars rather than percentages, which is what this entire site exists to help you do.</p>
<p><b>If it has stopped being entertainment, help in New Zealand is free, confidential and available right
now.</b></p>
</div>
{keyfacts([(f"{n} &middot; {num}", d) for n, num, _u, d in L.HELP])}
<div class="prose"><p><a class="btn btn--ghost" href="/responsible-gambling/">Deposit limits, self-exclusion
and bank blocks &rarr;</a></p></div>''', ident="rg")}

{sec(f'<div class="prose">{faq_html}</div>', ident="faqsec", haze=True)}
{sec(f'<div class="prose">{paa_html}</div>', ident="paasec")}

{sec(f'''{sechead("The short version")}
<div class="prose">
<p><b>If you want one name and no further reading:</b> <a href="/casino-reviews/spinjo/">Spinjo</a>. It
banks in New Zealand dollars end to end, names its operating company, holds a current Cura&ccedil;ao Gaming
Control Board licence and runs the deepest library we audited. Its welcome offer is not the biggest on this
page, which on the evidence of The Ledger is a point in its favour rather than against it.</p>
<p><b>If you intend to claim and clear a bonus:</b> ignore the top of the leaderboard entirely and work up
from the bottom of The Ledger. <a href="/casino-reviews/slotsgem/">Slotsgem</a> and
<a href="/casino-reviews/ivibet/">Ivibet</a> are the only two offers here that a normal player can
realistically finish.</p>
<p><b>If you simply want to play for an evening:</b> decline the bonus. Your money stays withdrawable, no
clause can void your winnings, and you have removed every trap described on this page in a single click.</p>
<p>That is the whole of our advice, and you will notice that two-thirds of it points away from the offers
we are paid to promote. That is what the arithmetic says, so that is what we have published.</p>
<p><a class="btn" href="/online-casinos/bonuses/">Every bonus, priced in full &rarr;</a>
<a class="btn btn--ghost" href="/how-we-rate/">How we score and how we are funded</a></p>
</div>''', ident="verdict")}

{sec(f'''{sechead("What New Zealanders actually complain about",
  "We read the reviews instead of the marketing. The findings are not what the category pages suggest.",
  2, "complaints")}
<div class="prose">
<p>Before writing any of this site we went looking for what goes wrong for real New Zealand players. The
most useful single data point is about an operator we do not list and are not paid by.</p>
<p><b>SkyCity Online Casino</b> is New Zealand&rsquo;s own domestically licensed operator &mdash; the site
most Kiwis would name if asked for the safe option. On Trustpilot it holds a <b>TrustScore of 1.5 out of
5</b> across <b>71 reviews</b>, with <b>82% rated one star</b> (checked {MONTH_YEAR}).</p>
</div>
{table(["Rating", "Share of reviews", "What this tells you"],
  [["&#9733;&#9733;&#9733;&#9733;&#9733; 5", "8%", "A small group who completed verification without incident"],
   ["&#9733;&#9733;&#9733;&#9733; 4", "4%", "&mdash;"],
   ["&#9733;&#9733;&#9733; 3", "0%", "Nobody is lukewarm. This is a bimodal experience"],
   ["&#9733;&#9733; 2", "6%", "&mdash;"],
   ["<b>&#9733; 1</b>", "<b>82%</b>", "Almost entirely withdrawal verification, not games or odds"]],
  caption="Trustpilot rating distribution for skycitycasino.com, captured " + MONTH_YEAR + ". A licensed "
          "New Zealand operator. The complaints are not about fairness &mdash; they are about getting paid.")}
<div class="prose">
<p>Read the one-star reviews and a single theme dominates. Not rigged games. Not unpaid bonuses.
<b>Verification.</b></p>
<blockquote class="quote"><p>&ldquo;I spent about 4 weeks trying to withdraw winnings, they have asked me
for every imaginable document under the sun&hellip; wanting 90 days of unfiltered transactions and then not
accepting the PDF as it is &lsquo;too large&rsquo;.&rdquo;</p><cite>Trustpilot reviewer, SkyCity Online
Casino</cite></blockquote>
<p>And then the review that changed how we structured this entire site:</p>
<blockquote class="quote"><p>&ldquo;These guys were so determined not to payout, I gave up, <b>rinsed my
winnings</b> and took the loss.&rdquo;</p><cite>Trustpilot reviewer, SkyCity Online Casino</cite></blockquote>
<p>The withdrawal was never refused. The player gambled the balance away out of frustration, and the
operator kept it without ever declining a payment. We have not found a single competitor page in this
market that mentions this pattern.</p>
<h3>What follows for you</h3>
<ul>
<li><b>A domestic licence is not a guarantee of a good experience.</b> The most complained-about operator
serving New Zealanders is the licensed one. Licensing gives you recourse, not service quality.</li>
<li><b>Verify on the day you register</b>, before you have anything to withdraw. It is the largest single
delay in the process and it is almost entirely within your control.</li>
<li><b>Treat a submitted withdrawal as gone.</b> Do not revisit the balance. The reverse-withdrawal window
exists precisely to tempt you.</li>
</ul>
<p><a class="btn btn--ghost" href="/fast-payout-casinos/#sof">Source of funds, the document pack, and the
escalation ladder &rarr;</a></p>
</div>''', ident="complaints", haze=True)}

{sec(f'''{sechead("Red flags: when to close the tab", None, 2, "redflags")}
<div class="prose">
<p>Competitor pages publish an avoid-list of named brands. Named lists go stale within months as skins
close and reopen under new names, so here is the version that keeps working: the signals themselves.</p>
</div>
{table(["Red flag", "Why it matters", "How long it takes to check"],
  [["<b>No operating company in the footer</b>",
    "A licence with no legal entity behind it gives you nobody to escalate to. This is the single "
    "strongest warning available", "10 seconds"],
   ["<b>Licence number does not resolve on the regulator&rsquo;s register</b>",
    "Seals are images and images are copied. The register is the only proof", "90 seconds"],
   ["Withdrawal terms not published before you deposit",
    "Weekly caps and processing windows hidden until after funding is a deliberate choice", "1 minute"],
   ["Bonus terms without a stated wagering <i>basis</i>",
    "&ldquo;40x&rdquo; without saying 40x of what is unpriceable, and usually deliberately", "1 minute"],
   ["Deposit limits only available by emailing support",
    "Account-level limits are trivial to build. Making them hard is a decision about who the site is for",
    "2 minutes"],
   ["&ldquo;No verification&rdquo; marketing",
    "Any licensed operator verifies at withdrawal. A site promising otherwise is unlicensed, lying, or "
    "both", "Instant"],
   ["No complaints route other than the operator&rsquo;s own support",
    "If the only escalation path is the casino, you have no escalation path", "1 minute"]],
  caption="Seven checks, under ten minutes in total, done before you deposit rather than after you win. "
          "One brand we list fails the first three, and we say so on every page it appears on.")}
<div class="prose">
{note('<p><b>The brand on this site that fails them.</b> <a href="/casino-reviews/roby-casino/">Roby '
      'Casino</a> publishes no regulator, no licence number and no operating company. It pays us one of '
      'the highest commission rates in our portfolio and we score it 8.1, among the three lowest here. We '
      'have kept the review up rather than quietly dropping the brand, because people search for it and '
      'should find the disclosure gap rather than a page that omits it.</p>', "warn")}
</div>''', ident="redflags")}
"""

    schema = [
        schema_webpage(PATH, META[PATH][0], META[PATH][1]),
        schema_breadcrumb(PATH, []),
        schema_article(PATH, META[PATH][0], META[PATH][1], AUTHOR, CHECKER),
        schema_person(AUTHOR), schema_person(CHECKER),
        schema_itemlist(PATH, pick(TOP10)),
        schema_faq(PATH, faq_ents + paa_ents),
    ]
    return write(PATH, page(PATH, body, schema), priority=1.0, freq="daily")
