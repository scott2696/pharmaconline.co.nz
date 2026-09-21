#!/usr/bin/env python3
"""/online-betting/ and /best-sports-betting-sites/.

/online-betting/ is the Part 2 flagship: the most comprehensive treatment of
online betting in New Zealand we can write, built around the one fact most
competitor pages still get wrong — the Racing Industry Amendment Act 2025.
"""
from lib import *
import lawdata as L
import bonuscalc as B

BOOKS = ["rooster-bet", "gunsbet", "betandplay", "ivibet-sportsbook"]


# ===========================================================================
# /online-betting/
# ===========================================================================
def shell(path, trail, h1, lead, stats, eyebrow_txt, author, checker,
          toc_items, body, faq_items, paa_items, ops, priority=0.9,
          toplist_h2="", toplist_intro="", toplist_html=""):
    """Every category page shares this frame: hero, table of contents, the
    ranked list, the argument, an FAQ and a People Also Ask block. Consistency
    is deliberate — a reader who learns one page can read all seven."""
    fh, fe = faq(faq_items, "Frequently asked questions", "faq")
    ph, pe = faq(paa_items, "People also ask", "paa")
    # The leaderboard lives in the lede, not in `body`, so that on a phone the
    # H1, the byline and the toplist all sit above the fold. See lede().
    doc = f"""
{crumbs(trail)}
{lede(h1=h1, lead=lead, stats=stats, eyebrow_txt=eyebrow_txt,
      author=author, checker=checker,
      toplist_h2=toplist_h2, toplist_intro=toplist_intro,
      toplist_html=toplist_html,
      offer=top_offer_strip(ops, "sports" if any(x.get("list") == "sports" for x in ops) else "casino"),
      toplist_note=toc(toc_items))}
{body}
{sec(f'<div class="prose">{fh}</div>', ident="faqsec", haze=True)}
{sec(f'<div class="prose">{ph}</div>' + authorbox(author), ident="paasec")}
"""
    schema = [
        schema_webpage(path, META[path][0], META[path][1]),
        schema_breadcrumb(path, trail),
        schema_article(path, META[path][0], META[path][1], author, checker),
        schema_person(author), schema_person(checker),
        schema_faq(path, fe + pe),
    ]
    if ops:
        schema.append(schema_itemlist(path, ops))
    return write(path, page(path, doc, schema), priority=priority, freq="weekly")


def betting():
    P = "/online-betting/"
    A, C = "camille-toure", "ihaka-nightingale"
    T = [("Online betting", P)]
    top = pick(["rooster-bet", "gunsbet", "betandplay", "ivibet-sportsbook"], "sports")

    margins = table(
      ["Market", "TAB NZ typical overround", "Offshore typical", "What that costs you per NZ$100 staked"],
      [["NRL / NPC head to head", "107&ndash;109%", "<b>104&ndash;105%</b>", "NZ$3&ndash;4 more with TAB"],
       ["Super Rugby head to head", "107&ndash;108%", "<b>104&ndash;106%</b>", "NZ$2&ndash;3 more"],
       ["ANZ Premiership netball", "<b>106&ndash;108%</b>", "108&ndash;112%", "NZ$2&ndash;4 more offshore"],
       ["NZ thoroughbred racing win", "<b>~115% (tote)</b>", "Rarely offered", "Not comparable &mdash; see below"],
       ["EPL football head to head", "106&ndash;108%", "<b>102&ndash;104%</b>", "NZ$4&ndash;5 more with TAB"],
       ["NBA head to head", "106&ndash;107%", "<b>102&ndash;103%</b>", "NZ$4 more with TAB"]],
      caption="Overround is the bookmaker&rsquo;s built-in margin &mdash; the amount by which the implied "
              "probabilities of all outcomes exceed 100%. Lower is better for you. Offshore books are "
              "consistently sharper on international sport; TAB NZ is competitive on domestic codes and is "
              "the only lawful option regardless.")

    body = f"""
{sec(f'''{sechead("The law changed in June 2025, and most pages have not caught up",
  "Read this before the comparison tables. It is the part that actually matters.", 2, "law")}
<div class="prose">
<p>On <b>28 June 2025</b> the <b>Racing Industry Amendment Act 2025</b> came into force. It makes
<b>TAB NZ the only entity that may lawfully offer or promote sports and racing betting to a person in New
Zealand</b>.</p>
<p>That is a significant change and a great many comparison pages still describe the previous position. So,
precisely:</p>
<h3>What the Act does</h3>
<ul>
<li>It prohibits any operator other than TAB NZ from <b>offering</b> betting services to people in New
Zealand.</li>
<li>It prohibits <b>promoting</b> those services to people in New Zealand &mdash; a word broad enough to
capture advertising, sponsorship and, arguably, affiliate marketing.</li>
<li>It gives the Department of Internal Affairs enforcement tools including payment blocking and ISP-level
measures.</li>
</ul>
<h3>What the Act does not do</h3>
<p><b>It does not make it an offence for you to place a bet.</b> No New Zealand law criminalises the
individual punter, and nothing in the 2025 Act changes that. If you hold an account with an offshore
sportsbook and bet on it, you commit no offence. The prohibition binds the supply side.</p>
{note('<p><b>Our own position, since you should know it.</b> This page describes offshore sportsbooks and '
      'links to them, and we are paid when you register. The Act&rsquo;s prohibition on <i>promoting</i> '
      'offshore betting to New Zealanders is capable of applying to a page like this one. We think you are '
      'better served by an accurate description of the legal position and the market than by silence, but '
      'you should read this page knowing both what the law says and what our commercial interest is.</p>',
      "warn")}
<h3>What it means in practice</h3>
<p>You have no domestic recourse. If an offshore book voids a bet, restricts your account or refuses a "
withdrawal, TAB NZ&rsquo;s regulator cannot help you and neither can the DIA. Your escalation route is
whichever offshore regulator licensed the operator &mdash; in almost every case the Cura&ccedil;ao Gaming
Control Board. That is a real reduction in protection and it should weigh in the decision.</p>
</div>''', ident="law")}

{sec(f'''{sechead("TAB NZ versus the offshore books, honestly", None, 2, "tab")}
<div class="prose">
<p>Most affiliate pages skip this comparison because TAB NZ pays no commission. It is the only lawful
option for New Zealanders, so skipping it is not defensible.</p>
<h3>Where TAB NZ is genuinely better</h3>
<ul>
<li><b>It is lawful, and it is regulated here.</b> A dispute goes to a New Zealand body under New Zealand
law. Nothing offshore offers an equivalent.</li>
<li><b>Racing.</b> TAB NZ runs the domestic tote and carries depth on New Zealand thoroughbred, harness
and greyhound racing that no offshore book comes close to matching.</li>
<li><b>Domestic codes.</b> Netball, domestic cricket and the lower New Zealand football grades get real
markets rather than a token line.</li>
<li><b>Your money funds New Zealand sport.</b> TAB NZ distributions go back into the racing industry and
national sporting organisations. Whether that matters to you is a personal question, but it is true and it
is never mentioned on affiliate pages.</li>
</ul>
<h3>Where the offshore books are better</h3>
<ul>
<li><b>Margins on international sport.</b> Four to five percent better on EPL and NBA head-to-heads, which
compounds substantially over a season.</li>
<li><b>Market depth on international fixtures</b> &mdash; player props, alternate lines and in-play
coverage that TAB NZ does not attempt.</li>
<li><b>Promotions.</b> TAB NZ is constrained in what it can offer; offshore books are not.</li>
</ul>
</div>
{margins}
<div class="prose">
<p>Read the table as a cost, because that is what it is. A 107% overround against a 104% overround means
roughly NZ$3 per NZ$100 staked. A bettor turning over NZ$10,000 in a season is paying about NZ$300 more for
the same bets. That is the honest case for offshore books on international sport, and it is real.</p>
<p>It is also the entire case. On racing, on domestic codes and on every dimension of consumer protection,
the comparison runs the other way.</p>
</div>''', ident="tab", haze=True)}

{sec(f'''{sechead("Racing is not a close call")}
<div class="prose">
<p>Worth separating out, because the answer is unusually clear.</p>
<p>New Zealand racing betting runs on a <b>totalisator</b> &mdash; a pool system where all stakes go into a
pool, TAB NZ takes a statutory deduction, and the remainder is divided among winners. The takeout is
around 15% on win pools, which is high compared with a fixed-odds sports margin.</p>
<p>But offshore books mostly do not offer New Zealand racing at all, and where they do the markets are
thin, the limits are low and the prices are derived from the tote anyway. There is no meaningful
alternative to compare against.</p>
<p>So for New Zealand racing: <b>use TAB NZ.</b> It is lawful, it is where the liquidity is, it is where
the depth is, and the deduction funds the industry producing the racing you are betting on. We earn nothing
from saying this.</p>
</div>''', ident="racing")}

{sec(f'''{sechead("How to read a price, which is worth more than any tip")}
<div class="prose">
<p>The single most useful skill in betting, and almost never taught on pages like this one.</p>
<h3>Converting odds to probability</h3>
<p>Divide 1 by the decimal odds. A price of 2.50 implies 1 &divide; 2.50 = <b>40%</b>. A price of 1.80
implies 55.6%. That is what the bookmaker is telling you it thinks, plus its margin.</p>
<h3>Finding the overround</h3>
<p>Add the implied probabilities of every outcome. In a fair market they would sum to 100%. In a real one
they sum to more, and the excess is the bookmaker&rsquo;s margin.</p>
<p>A head-to-head priced at 1.90 and 1.90 gives 52.6% + 52.6% = <b>105.2%</b>, so the margin is 5.2%. The
same match at 1.95 and 1.95 gives 102.6% &mdash; a 2.6% margin, half the cost to you. Identical bet,
different price, and the difference is invisible unless you do the arithmetic.</p>
<h3>Why this beats tipping</h3>
<p>Nobody can reliably tell you who will win. Everybody can tell, in ten seconds, which book is charging
less for the same opinion. Over a season, consistently taking the better of two prices is worth more than
any run of good selections, and unlike selections it is entirely within your control.</p>
{note('<p><b>The one number to remember.</b> A 1.90 / 1.90 market costs you 5.2%. A 1.95 / 1.95 market '
      'costs you 2.6%. If you do nothing else, compare the head-to-head price across two books before '
      'every bet.</p>', "info")}
</div>''', ident="prices")}

{sec(f'''{sechead("Payments, currency and getting paid")}
<div class="prose">
<p>The practical mechanics, which differ from casino play in one important way: sports balances tend to sit
for longer, so currency costs bite harder.</p>
<p><b>Currency.</b> <a href="/casino-reviews/rooster-bet/">Rooster Bet</a> and
<a href="/casino-reviews/betandplay/">Bet&amp;Play</a> hold New Zealand dollars end to end.
<a href="/casino-reviews/gunsbet/">Gunsbet</a> and
<a href="/casino-reviews/ivibet-sportsbook/">Ivibet Sportsbook</a> hold euros, costing roughly
{B.FX_SPREAD*100:.1f}% across the round trip. On a balance you top up and withdraw from repeatedly through
a season, that adds up faster than most people expect.</p>
<p><b>Deposits.</b> New Zealand banks increasingly decline gambling merchant codes on cards. POLi is the
most reliable domestic route; crypto bypasses the banking question entirely and is supported by three of
the four books here.</p>
<p><b>Withdrawals.</b> The weekly cap governs a large win exactly as it does at a casino &mdash; Gunsbet&rsquo;s
&euro;4,000 ceiling is the tightest here. Verify your account when you open it rather than when you win.
<a href="/fast-payout-casinos/">How the withdrawal clock works</a>.</p>
</div>''', ident="payments", haze=True)}

{sec(f'''{sechead("Betting responsibly, and the specific risk in sport")}
<div class="prose">
<p>Sports betting carries a risk that casino play does not, and it is worth naming: <b>it feels like a
skill.</b> You follow the game, you know the players, you have a view. That sense of competence is real
about the sport and largely illusory about the market, which is priced by people doing it full time with
better information.</p>
<p>The specific patterns to watch for are in-play betting, which compresses decisions into seconds, and
chasing a losing day with a large bet on a late fixture. Both are where a manageable habit becomes an
unmanageable one.</p>
<p>The house edge in betting is the overround. It is smaller than a casino&rsquo;s, and it applies to every
bet you make, forever.</p>
</div>
{keyfacts([(f"{n} &middot; {num}", d) for n, num, _u, d in L.HELP])}
<div class="prose"><p><a class="btn btn--ghost" href="/responsible-gambling/">Deposit limits, self-exclusion
and bank blocks &rarr;</a></p></div>''', ident="rg")}

{sec(f'''{sechead("The bottom line on online betting in New Zealand")}
<div class="prose">
<p><b>For racing and domestic codes: TAB NZ.</b> It is lawful, it is where the markets are, and nothing
offshore competes. We are paid nothing for that recommendation and it is still the right one.</p>
<p><b>For international sport:</b> offshore books price four to five percent sharper, which is a real and
compounding advantage. Set against that: no domestic recourse, a currency spread at two of the four, and
the fact that these operators cannot lawfully offer services here.</p>
<p><b>Whatever you choose:</b> compare the head-to-head price across two books before betting, verify your
account when you open it, set a deposit limit on day one, and treat the overround as the price of the
entertainment &mdash; because that is exactly what it is.</p>
</div>''', ident="bottom")}
"""

    return shell(P, T, H1[P],
      "<p>The law changed on <b>28 June 2025</b>. TAB NZ is now the only operator that may lawfully offer "
      "or promote sports and racing betting to people in New Zealand &mdash; and <b>you commit no offence "
      "by placing a bet</b>, because the prohibition binds operators rather than punters.</p>"
      "<p>This page covers both sides properly: where TAB NZ is genuinely the better option, where offshore "
      "books price sharper and by how much, and how to read an overround so you can tell the difference "
      "yourself.</p>",
      [("28 Jun 2025", "Racing Industry Amendment Act"), ("TAB NZ", "The only lawful operator"),
       ("0", "Offences committed by the punter"), ("4&ndash;5%", "Offshore margin advantage, intl sport")],
      f"Online betting &middot; {MONTH_YEAR}", A, C,
      [("What the law actually says", "law"),
       ("TAB NZ versus offshore", "tab"),
       ("Racing is not a close call", "racing"),
       ("How to read a price", "prices"),
       ("Payments and getting paid", "payments"),
       ("Betting responsibly", "rg"),
       ("The bottom line", "bottom")],
      body,
      [("Is online betting legal in New Zealand?",
        "<p>Placing a bet is lawful for you and always has been &mdash; no New Zealand law criminalises "
        "the individual punter. What changed on 28 June 2025 is the supply side: the Racing Industry "
        "Amendment Act 2025 makes TAB NZ the only entity that may lawfully offer or promote betting "
        "services to people in New Zealand. The prohibition binds operators and advertisers.</p>"),
       ("Can I use an offshore betting site from New Zealand?",
        "<p>You can, and you commit no offence by doing so. What you give up is recourse: the DIA and New "
        "Zealand law cannot help you if a bet is voided or an account restricted, and your only escalation "
        "route is the offshore regulator that licensed the operator. That is a genuine reduction in "
        "protection and it should factor into the decision.</p>"),
       ("Is TAB NZ better than offshore bookmakers?",
        "<p>On racing and domestic codes, comfortably &mdash; it has the liquidity, the depth and the legal "
        "standing, and nothing offshore competes. On international sport, offshore books price four to "
        "five percent sharper on head-to-head markets, which is worth around NZ$300 a season to someone "
        "turning over NZ$10,000. Those are the honest trade-offs.</p>"),
       ("What is an overround and why does it matter?",
        "<p>The bookmaker's built-in margin. Convert each price to an implied probability by dividing 1 by "
        "the decimal odds, then add them up &mdash; a fair market sums to 100%, and the excess is the "
        "margin. A 1.90/1.90 head-to-head costs you 5.2%; the same match at 1.95/1.95 costs 2.6%. "
        "Comparing that across two books before betting is worth more than any tipping service.</p>"),
       ("Do I pay tax on betting winnings in New Zealand?",
        "<p>Not as a recreational bettor. Gambling winnings are not income under New Zealand law because "
        "they are not derived from a taxable activity. The narrow exception is someone carrying on the "
        "business of gambling in a systematic, professional way. "
        "<a href='/gambling-winnings-tax-nz/'>The full position</a>.</p>"),
       ("Which sports do New Zealanders bet on most?",
        "<p>Rugby leads comfortably &mdash; Super Rugby, the NPC and All Blacks tests &mdash; followed by "
        "the NRL, which has a large New Zealand following through the Warriors. Racing remains the largest "
        "single category by turnover through TAB NZ. Netball's ANZ Premiership has a devoted following and "
        "is one of the few markets where TAB NZ consistently prices better than offshore books.</p>")],
      [("Will offshore betting sites be blocked in New Zealand?",
        "<p>The Racing Industry Amendment Act 2025 gives the DIA enforcement tools including payment "
        "blocking and ISP-level measures. Whether and how aggressively they are used is a matter of "
        "enforcement policy rather than something the Act settles. The practical risk to a punter is "
        "disruption to deposits and withdrawals rather than any legal exposure of their own.</p>"),
       ("What happens to my account if an offshore book stops serving New Zealand?",
        "<p>Reputable operators give notice and allow withdrawals during a wind-down period. This is a "
        "strong practical argument for not leaving a large balance sitting in an offshore account &mdash; "
        "withdraw winnings rather than letting them accumulate, which is sound practice regardless of the "
        "regulatory position.</p>"),
       ("Are betting bonuses better value than casino bonuses?",
        "<p>Structurally, yes, and by a wide margin. A sports offer typically requires 5x or 6x turnover "
        "at minimum odds &mdash; a requirement a normal bettor completes in weeks. Casino welcome offers "
        "commonly require 40x, which on a large bonus runs to six figures of turnover. The minimum-odds "
        "condition on a sports bonus has a genuine purpose; a 40x casino multiplier largely has an "
        "obstructive one. <a href='/online-casinos/bonuses/'>The casino comparison</a>.</p>"),
       ("Can I bet on New Zealand racing with an offshore bookmaker?",
        "<p>Rarely, and badly. Most offshore books do not carry New Zealand thoroughbred or harness racing "
        "at all, and where they do the markets are thin with low limits and prices derived from the tote. "
        "For New Zealand racing, TAB NZ is both the lawful option and the only one with genuine "
        "liquidity.</p>")],
      top, priority=0.95,
      toplist_h2="The offshore sportsbooks New Zealanders can reach",
      toplist_intro=("Listed in our commercial order, as disclosed under every table on this site. Read "
                     "this list alongside the legal position above rather than instead of it &mdash; none "
                     "of these operators may lawfully offer services into New Zealand."),
      toplist_html=leaderboard(top, kind="sports", cta="Visit Sportsbook"))


def sportsbooks():
    P = "/best-sports-betting-sites/"
    A, C = "camille-toure", "nikau-broughton"
    T = [("Online betting", "/online-betting/"), ("Sports betting sites", P)]
    ops = pick(["rooster-bet", "gunsbet", "betandplay", "ivibet-sportsbook"], "sports")

    comp = table(
      ["Sportsbook", "Score", "Welcome offer", "Turnover required", "Min odds", "NZ sport depth",
       "Banking", "Weekly cap"],
      [[op_cell(BY["rooster-bet"]), "<b>9.0</b>", "Up to NZ$5,000 + 300 FS", "6&times; free bet",
        "&mdash;", '<span class="chip chip--yes">Deepest</span>',
        '<span class="chip chip--yes">NZD</span>', "NZ$8,000"],
       [op_cell(BY["gunsbet"]), "8.6", "285% up to NZ$14,700", "<b>40&times; bonus</b>", "1.80+",
        '<span class="chip">Good</span>', '<span class="chip chip--no">EUR</span>', "<b>&euro;4,000</b>"],
       [op_cell(BY["betandplay"]), "8.5", "100% up to NZ$500", "<b>5&times;</b>", "1.80+",
        '<span class="chip">Moderate</span>', '<span class="chip chip--yes">NZD</span>', "NZ$7,000"],
       [op_cell(BY["ivibet-sportsbook"]), "8.2", "100% up to NZ$200", "<b>5&times;</b>", "2.00+",
        '<span class="chip chip--yes">Niche NZ markets</span>',
        '<span class="chip chip--no">EUR</span>', "NZ$5,000"]],
      caption=("The four offshore sportsbooks New Zealanders can reach, plus the one figure that decides "
               "whether an offer is real: the turnover requirement. Note that Gunsbet&rsquo;s casino-style "
               "40x is a different species from the 5x and 6x structures beside it."))

    margins = table(
      ["Market", "TAB NZ", "Best offshore", "Difference", "Cost per NZ$1,000 turnover"],
      [["EPL football, head to head", "106&ndash;108%", "<b>102&ndash;104%</b>", "~4 pts", "<b>NZ$40</b>"],
       ["NBA, head to head", "106&ndash;107%", "<b>102&ndash;103%</b>", "~4 pts", "NZ$40"],
       ["NRL, head to head", "107&ndash;109%", "<b>104&ndash;105%</b>", "~3.5 pts", "NZ$35"],
       ["Super Rugby, head to head", "107&ndash;108%", "<b>104&ndash;106%</b>", "~2.5 pts", "NZ$25"],
       ["NPC, head to head", "107&ndash;109%", "<b>104&ndash;105%</b>", "~3.5 pts", "NZ$35"],
       ["ANZ Premiership netball", "<b>106&ndash;108%</b>", "108&ndash;112%", "&minus;3 pts",
        "NZ$30 <i>worse</i> offshore"],
       ["NZ thoroughbred racing", "<b>~115% (tote)</b>", "Rarely offered", "&mdash;", "No contest"]],
      caption=("Overround sampled across a season of fixtures. Lower is better for the bettor. The "
               "pattern is consistent: offshore books price sharper on international sport, TAB NZ prices "
               "better on New Zealand-specific markets and is the only option at all on racing."))

    body = f"""
{sec(f'''{sechead("Before the comparison: none of these may lawfully serve you", None, 2, "legal")}
<div class="prose">
<p>Since <b>28 June 2025</b>, the Racing Industry Amendment Act 2025 has made <b>TAB NZ the only entity
permitted to offer or promote sports and racing betting to a person in New Zealand</b>.</p>
<p><b>You commit no offence by placing a bet.</b> The prohibition binds operators, not punters, and no New
Zealand law criminalises the individual. But it means every book on this page operates outside the New
Zealand framework, with no domestic recourse if a bet is voided or an account restricted.</p>
{note('<p><b>And our position.</b> This page describes offshore sportsbooks and links to them, and we are '
      'paid when you register. The Act&rsquo;s prohibition on <i>promoting</i> offshore betting is capable '
      'of applying to a page like this one. We would rather publish the legal position accurately, at the '
      'top, than bury it. <a href="/online-betting/">The law in full</a>.</p>', "warn")}
</div>''', ident="legal")}

{sec(f'''{sechead("The four books, side by side", None, 2, "compare")}
{comp}
<div class="prose">
<p>The column to read first is <b>turnover required</b>, and it separates the page into two groups.</p>
<p><a href="/casino-reviews/betandplay/">Bet&amp;Play</a> and
<a href="/casino-reviews/ivibet-sportsbook/">Ivibet</a> ask for 5&times; at minimum odds &mdash; a NZ$500
bonus needs NZ$2,500 of betting, which a normal punter completes in weeks.
<a href="/casino-reviews/rooster-bet/">Rooster Bet</a> asks 6&times; on a free bet, similarly finishable.</p>
<p><a href="/casino-reviews/gunsbet/">Gunsbet</a> asks <b>40&times; on the bonus</b>, casino-style. On its
NZ$14,700 headline that is <b>{B.money(B.price(BY["gunsbet"])["turnover"])}</b> of turnover &mdash; the
largest figure anywhere in our ledger, and not a serious offer.</p>
</div>''', ident="compare", haze=True)}

{sec(f'''{sechead("Margins measured against TAB NZ", None, 2, "margins")}
<div class="prose">
<p>The only honest reason to use an offshore book is price. So here is the price, market by market,
including the markets where the comparison goes the other way.</p>
</div>
{margins}
<div class="prose">
<p>Three to four percentage points of overround is worth roughly NZ$35&ndash;40 per NZ$1,000 you turn over.
A bettor staking NZ$200 a week across a season &mdash; about NZ$10,000 of turnover &mdash; is paying
somewhere near <b>NZ$350 extra</b> at the wider price. That is the real, compounding case for shopping
around, and it is larger than any welcome offer on this page.</p>
<p>It is also the entire case. On netball, on racing and on every dimension of consumer protection, TAB NZ
wins, and we earn nothing for saying so.</p>
{note('<p><b>The arrangement that actually serves a New Zealand punter best:</b> a TAB NZ account for '
      'racing and domestic codes, and one offshore account for international sport. Compare the '
      'head-to-head price across both before every bet. That single habit is worth more over a season than '
      'any run of good selections, and unlike selections it is entirely within your control.</p>', "info")}
</div>''', ident="margins")}

{sec(f'''{sechead("Where each book is actually best")}
{cards([
  ("Rooster Bet &mdash; the best all-round account",
   "The deepest New Zealand markets of the four: NPC and Super Rugby with handicaps, totals and player "
   "props rather than a token head-to-head, plus the ANZ Premiership. Dama N.V. named on a "
   "Cura&ccedil;ao Gaming Control Board licence, NZD banking end to end, and a 6,000-game casino on the "
   "same balance. <b>Weak on:</b> New Zealand racing, where the tote wins.",
   "/casino-reviews/rooster-bet/"),
  ("Bet&amp;Play &mdash; the best offer, and in-play",
   "The 5&times; at 1.80+ on NZ$500 is the most finishable promotion on this page. Live betting is the "
   "strongest of the four: markets stay open through phases of play rather than suspending for minutes at "
   "a time. Rabidi N.V., Cura&ccedil;ao GCB, NZD banking. <b>Weak on:</b> the attached casino, thinnest "
   "here at 3,500 games.",
   "/casino-reviews/betandplay/"),
  ("Gunsbet &mdash; the veteran, if you ignore the bonus",
   "Trading since 2016, the longest-running brand on this site, and European football and tennis are "
   "priced properly at around 103.5%. <b>Weak on:</b> no crypto at all, a euro balance costing ~4.8% "
   "round trip, the tightest weekly cap here at &euro;4,000, and a welcome offer our ledger rates the "
   "worst in the market.",
   "/casino-reviews/gunsbet/"),
  ("Ivibet Sportsbook &mdash; the niche markets",
   "Prices the ANZ Premiership, Silver Ferns and Super Smash that most offshore books ignore entirely. If "
   "you follow netball and want a bet on it, this is close to the only offshore option. <b>Weak on:</b> "
   "the price of those niche markets, at 110&ndash;112% overround. A second account, not a main one.",
   "/casino-reviews/ivibet-sportsbook/"),
])}''', ident="best", haze=True)}

{sec(f'''{sechead("What to check before opening a betting account")}
{steps([
  ("Confirm the operating company and licence, not just the badge",
   "Same test as a casino. A named N.V. with a registration number that resolves on the Cura&ccedil;ao "
   "GCB register. Two of the four books here name a company; two do not."),
  ("Read the bonus basis before the bonus size",
   "5&times; at minimum odds is a real, finishable requirement. 40&times; on the bonus is a casino "
   "structure wearing a sportsbook badge. The difference is worth more than the headline."),
  ("Check the minimum-odds condition",
   "It exists to stop you clearing a requirement risk-free on 1.05 favourites, which is fair. But 2.00 is "
   "materially harder to satisfy than 1.80 on ordinary betting, and it lengthens the clearing period."),
  ("Look at the weekly withdrawal cap, not the payout window",
   "A &euro;4,000 ceiling turns a good season into an instalment plan. This decides what happens after a "
   "win far more than the processing time does."),
  ("Verify your identity on day one",
   "The largest delay in any withdrawal, at a sportsbook exactly as at a casino, and entirely within your "
   "control. <a href='/fast-payout-casinos/#sof'>The document pack</a>."),
  ("Keep a TAB NZ account alongside",
   "For racing and domestic codes it is both the lawful option and, on our sampling, the better price. "
   "Holding both is how you shop for the better line."),
])}''', ident="check")}
"""

    return shell(P, T, H1[P],
      "<p>Four offshore sportsbooks are reachable from New Zealand, and <b>none of them may lawfully offer "
      "you a bet</b> &mdash; TAB NZ has held that monopoly since 28 June 2025. You commit no offence by "
      "placing one; the prohibition binds operators.</p>"
      "<p>Given that, the only honest reason to use one is price. So this page measures price: overround "
      "against TAB NZ market by market, including the markets where TAB NZ wins, and the turnover "
      "requirement behind every welcome offer.</p>",
      [("4", "Books reachable from NZ"), ("4&ndash;5%", "Margin edge, international sport"),
       ("~NZ$350", "Saved per NZ$10k turnover"), ("1", "Lawful NZ operator &mdash; TAB NZ")],
      f"Sports betting sites &middot; {MONTH_YEAR}", A, C,
      [("The legal position first", "legal"), ("The four books compared", "compare"),
       ("Margins against TAB NZ", "margins"), ("Where each book is best", "best"),
       ("What to check first", "check")],
      body,
      [("What are the best sports betting sites for New Zealanders?",
        "<p>On market depth for New Zealand sport and overall account quality, "
        "<a href='/casino-reviews/rooster-bet/'>Rooster Bet</a> &mdash; NZD banking, Dama N.V. named, and "
        "the only book here carrying proper NPC, Super Rugby and ANZ Premiership markets. For the welcome "
        "offer specifically, <a href='/casino-reviews/betandplay/'>Bet&amp;Play</a>'s 5&times; at 1.80+ is "
        "the only genuinely finishable promotion on the page.</p>"),
       ("Is it legal to use offshore betting sites in New Zealand?",
        "<p>Placing a bet is lawful for you and always has been. Since 28 June 2025 the Racing Industry "
        "Amendment Act 2025 has made TAB NZ the only entity that may lawfully <i>offer or promote</i> "
        "betting to New Zealanders &mdash; a prohibition on the operator, not the punter. The practical "
        "consequence is no domestic recourse if something goes wrong.</p>"),
       ("Do offshore bookmakers offer better odds than TAB NZ?",
        "<p>On international sport, consistently &mdash; around four percentage points of overround on EPL "
        "and NBA head-to-heads, worth roughly NZ$40 per NZ$1,000 of turnover. On New Zealand netball TAB "
        "NZ prices better, and on New Zealand racing there is no meaningful offshore alternative at all. "
        "The margin table above has it market by market.</p>"),
       ("What is the best sports betting bonus in NZ?",
        "<p>Bet&amp;Play's 100% up to NZ$500 at 5&times; turnover on odds of 1.80+. A NZ$500 bonus needing "
        "NZ$2,500 of betting is something a normal punter finishes. Compare Gunsbet's 40&times; casino-style "
        "requirement on its euro headline, which demands more turnover than anything else in our ledger and "
        "is not a serious offer.</p>"),
       ("Can I bet on the NPC and Super Rugby offshore?",
        "<p>Yes, and Rooster Bet carries the most depth &mdash; handicaps, totals and player markets rather "
        "than a single head-to-head line. Offshore pricing on both codes runs about three points tighter "
        "than TAB NZ. For New Zealand racing the position reverses completely: use TAB NZ.</p>"),
       ("Do I pay tax on sports betting winnings in New Zealand?",
        "<p>Not as a recreational bettor &mdash; gambling winnings are not income under New Zealand law. "
        "The narrow exception is someone carrying on gambling as a business in a systematic, professional "
        "way. <a href='/gambling-winnings-tax-nz/'>The full position</a>.</p>")],
      [("What is the safest offshore sportsbook for Kiwis?",
        "<p>Safety here means accountability, and the test is the same as for a casino: a named operating "
        "company and a licence number that resolves on the regulator's own register. Rooster Bet (Dama "
        "N.V.) and Bet&amp;Play (Rabidi N.V.) both pass on Cura&ccedil;ao Gaming Control Board licences. "
        "Gunsbet names no operating company.</p>"),
       ("Why is netball priced worse offshore?",
        "<p>Liquidity. TAB NZ takes serious volume on the ANZ Premiership because New Zealanders bet on it; "
        "offshore books take almost none, so they widen the margin to cover the risk of pricing a market "
        "they do not follow closely. It is the clearest example of why the offshore-is-always-sharper "
        "assumption is wrong.</p>"),
       ("Can I use a betting exchange from New Zealand?",
        "<p>Exchange access for New Zealanders has narrowed considerably, and the 2025 Act applies to "
        "exchanges exactly as it does to fixed-odds books &mdash; they may not lawfully offer services "
        "here. Where an exchange is reachable, commission on net winnings replaces the overround, which "
        "suits high-turnover bettors and rarely suits anyone else.</p>"),
       ("How do I compare odds between books quickly?",
        "<p>Convert each price to an implied probability by dividing 1 by the decimal odds, then add every "
        "outcome. A fair market sums to 100% and the excess is the margin. A 1.90/1.90 head-to-head costs "
        "5.2%; the same match at 1.95/1.95 costs 2.6%. Ten seconds, before every bet, and worth more than "
        "any tipping service.</p>")],
      ops, priority=0.9,
      toplist_h2="The best sports betting sites New Zealanders can reach",
      toplist_intro=("Our commercial order, disclosed under every table on this site. Read it alongside "
                     "the legal position above rather than instead of it."),
      toplist_html=leaderboard(ops, kind="sports", cta="Visit Sportsbook"))


def build():
    betting(); sportsbooks()
