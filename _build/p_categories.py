#!/usr/bin/env python3
"""The seven category / money pages.

/online-pokies/  /high-payout-casinos/  /fast-payout-casinos/
/best-crypto-casinos/  /live-casinos/  /online-casinos/bonuses/
/no-deposit-casinos/
"""
from lib import *
import lawdata as L
import bonuscalc as B


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


# ===========================================================================
# /online-pokies/
# ===========================================================================
def pokies():
    P = "/online-pokies/"
    A, C = "camille-toure", "nikau-broughton"
    T = [("Online pokies", P)]
    top = pick(["spinjo", "kingdom", "rivo", "lucky-vibe", "madcasino", "lucky-circus", "fortune-play", "smash"])

    cfg = table(
      ["Title", "Studio", "Top build", "Cut-down build", "Cost of the difference*"],
      [["Gates of Olympus", "Pragmatic Play", "<b>96.50%</b>", "94.50%", "NZ$20 per NZ$1,000 staked"],
       ["Sweet Bonanza", "Pragmatic Play", "<b>96.51%</b>", "94.48%", "NZ$20 per NZ$1,000 staked"],
       ["Big Bass Bonanza", "Reel Kingdom", "<b>96.71%</b>", "95.28%", "NZ$14 per NZ$1,000 staked"],
       ["Book of Dead", "Play'n GO", "<b>96.21%</b>", "94.25%", "NZ$20 per NZ$1,000 staked"],
       ["Starburst", "NetEnt", "<b>96.09%</b>", "94.19%", "NZ$19 per NZ$1,000 staked"],
       ["Wolf Gold", "Pragmatic Play", "<b>96.01%</b>", "94.03%", "NZ$20 per NZ$1,000 staked"]],
      caption="*The extra amount a cut-down build takes from you over NZ$1,000 of turnover. Studios license "
              "several RTP configurations of the same title and the operator chooses which one to run. The "
              "game looks identical, carries the same name and the same artwork, and pays measurably less.")

    vol = table(
      ["Volatility", "Typical hit frequency", "What a NZ$100 session looks like", "Suits"],
      [["Low", "30&ndash;40% of spins", "Small frequent returns, slow bleed, rarely a big swing either way",
        "Clearing wagering; long sessions on a small bankroll"],
       ["Medium", "20&ndash;28% of spins", "Occasional 20&ndash;50x hits between dry spells of 30&ndash;60 spins",
        "Most recreational play"],
       ["High", "12&ndash;20% of spins", "Long dry spells punctuated by rare large wins; NZ$100 can vanish in "
        "40 spins or triple in one", "Chasing a big win with money you have written off"],
       ["Extreme", "8&ndash;12% of spins", "Most sessions end at zero; the distribution is carried entirely "
        "by outcomes you will probably never see", "Almost nobody, honestly"]],
      caption="Volatility describes the shape of the distribution, not its average. Two pokies with identical "
              "96% RTP can produce completely different evenings. Volatility is the variable that decides "
              "whether your bankroll survives long enough for the RTP to mean anything.")

    body = f"""
{sec(f'''{sechead("The same pokie is not the same machine everywhere",
  "The single most valuable thing to understand about online pokies NZ players can reach.", 2, "builds")}
<div class="prose">
<p>Here is a fact the industry would rather stayed obscure. When a studio like Pragmatic Play or Play&rsquo;n GO
releases a pokie, it does not ship one game. It ships the same game in several <b>RTP configurations</b> &mdash;
commonly a headline version around 96%, and one or more cut-down versions in the 94% range. The artwork is
identical. The name is identical. The maths is not.</p>
<p><b>The operator chooses which build to run</b>, and most do not tell you. You can be playing Gates of
Olympus at two different casinos, on the same stake, and be playing two measurably different games.</p>
<p>That choice is worth roughly <b>NZ$20 per NZ$1,000 you stake</b>. Over a year of modest play that is not
a rounding error, and it is invisible unless somebody opens the game information panel and reads the number.
So that is what we do.</p>
</div>
{cfg}
<div class="prose">
{note('<p><b>How to check it yourself, in ten seconds.</b> Open any pokie, tap the menu or the &ldquo;i&rdquo; '
      'icon, and find the information or paytable screen. The RTP is stated there, in the game itself, by '
      'the studio &mdash; not by the casino. If it reads 94.x% on a title whose headline build is 96.x%, you '
      'are on the cut-down version. This is the most useful ten seconds you can spend at a new casino, and '
      'it works on every licensed game in the market.</p>', "info")}
</div>''', ident="builds")}

{sec(f'''{sechead("How an online pokie actually works")}
<div class="prose">
<p>Worth getting straight, because almost every strategy sold on the internet depends on you having it wrong.</p>
<h3>The RNG does not remember anything</h3>
<p>Every spin is generated independently. The machine has no memory of the previous spin, no concept of
being &ldquo;due&rdquo;, and no awareness of how long you have been playing or how much you have lost.
A pokie that has not paid in 200 spins is exactly as likely to pay on spin 201 as it was on spin one. This is
not a policy, it is a mathematical property of independent events, and it is the reason no betting pattern,
stake-raising system or time-of-day theory can change your expected outcome.</p>
<h3>RTP is a limit, not a promise</h3>
<p>A 96% RTP means that across many millions of spins, the game returns 96% of everything staked. It says
nothing whatever about your session. Over 500 spins the realistic range of outcomes is enormous &mdash; you
can finish well ahead on a 94% game and lose everything on a 97% one. RTP tells you the direction of the
drift, not the size of the waves.</p>
<h3>Hit frequency and volatility are the variables you actually feel</h3>
<p>Hit frequency is how often a spin returns anything at all. Volatility is how far outcomes spread around
the average. These two numbers, not RTP, determine what an evening feels like and whether NZ$100 lasts
twenty minutes or two hours.</p>
</div>
{vol}''', ident="how", haze=True)}

{sec(f'''{sechead("What playing pokies actually costs per hour", None, 2, "cost")}
<div class="prose">
<p>RTP as a percentage is hard to price. Converted to an hourly rate it becomes obvious, and this is the
calculation we wish every pokies page published.</p>
<p>A typical online pokie runs about <b>600 spins per hour</b> at a comfortable pace. Your expected loss is
simply stake &times; spins &times; house edge:</p>
</div>
{table(["Your stake per spin", "Turnover per hour", "Expected loss @ 96% RTP", "Expected loss @ 94% RTP", "The difference"],
  [["NZ$0.20", "NZ$120", "NZ$4.80", "NZ$7.20", "NZ$2.40"],
   ["NZ$0.50", "NZ$300", "NZ$12", "NZ$18", "NZ$6"],
   ["NZ$1.00", "NZ$600", "NZ$24", "NZ$36", "NZ$12"],
   ["NZ$2.00", "NZ$1,200", "NZ$48", "NZ$72", "NZ$24"],
   ["NZ$5.00", "NZ$3,000", "NZ$120", "NZ$180", "NZ$60"]],
  caption="At roughly 600 spins per hour. This is the price of the entertainment, on average, before "
          "variance. Any individual hour can land anywhere; over a year of play the average is what you get.")}
<div class="prose">
<p>Read the right-hand column again. The difference between a casino running the good build and one running
the cut-down build is <b>NZ$12 an hour at a NZ$1 stake</b>. That is larger than most of the welcome bonus
differences that these comparison pages spend all their time on.</p>
</div>''', ident="cost")}

{sec(f'''{sechead("Free pokies NZ: what demo play is good for, and what it hides")}
<div class="prose">
<p>Most sites listed here let you spin in demo mode without an account. Free pokies NZ-side are genuinely
useful for three things and actively misleading for a fourth.</p>
<h3>Worth doing</h3>
<ul>
<li><b>Learning the mechanics</b> of a feature before you pay to discover it &mdash; how a bonus buy works,
what triggers free spins, whether the paylines behave as you expect.</li>
<li><b>Checking the RTP build.</b> The information panel shows the configuration in demo mode too, so you
can audit a lobby without depositing a cent.</li>
<li><b>Feeling the volatility.</b> Two hundred demo spins tells you whether a game pays in dribs or droughts.</li>
</ul>
<h3>Actively misleading</h3>
<p><b>Demo play tells you nothing about whether you will win.</b> Some free play modes run on a different
balance model, and more importantly, a run of good luck in demo creates a belief that carries into real
money where it has no basis. If you finish a demo session up 300% and conclude the game is generous, the
demo has cost you something despite being free.</p>
<p>The related search is <b>free pokies no download no registration NZ</b>, and that is exactly what demo
mode is &mdash; browser-based, instant, no account. Be wary of standalone sites offering the same thing
outside an operator, since the games there are frequently unlicensed clones running unknown maths.</p>
</div>''', ident="free", haze=True)}

{sec(f'''{sechead("Megaways, jackpots and bonus buys, priced")}
<div class="prose">
<h3>Megaways pokies NZ</h3>
<p>A licensed mechanic where the number of symbols per reel changes each spin, producing up to 117,649 ways
to win. It is genuinely entertaining and it is almost always <b>high volatility</b> &mdash; long dry spells,
occasional large hits. Megaways titles typically run 95.5% to 96.5% RTP, in line with everything else. The
huge &ldquo;ways&rdquo; number is a description of the mechanic, not a measure of generosity.</p>
<h3>Progressive jackpot pokies NZ</h3>
<p>The jackpot is funded by a slice of every stake, which comes out of the base game RTP. A progressive
title advertising 96% may be running 88&ndash;92% in the base game with the remainder feeding the pot. If
you are not realistically chasing the jackpot, you are playing a materially worse game to fund somebody
else&rsquo;s. Check whether the quoted RTP is inclusive of the jackpot contribution &mdash; good studios say.</p>
<h3>Bonus buys</h3>
<p>Paying a fixed multiple of your stake &mdash; usually 60x to 100x &mdash; to trigger the feature round
immediately. The RTP on a bought feature is normally a little <i>higher</i> than the base game, which sounds
like a bargain and is not: you are staking 100x your normal bet in a single decision, so the variance is
enormous and the expected loss per click is large. A NZ$1 player buying a NZ$100 feature is making a
NZ$100 bet, whatever the interface implies.</p>
</div>''', ident="mechanics")}

{sec(f'''{sechead("Pokies are the only game that clears a bonus efficiently")}
<div class="prose">
<p>A point that belongs on this page rather than the bonus page, because it changes what you should play.</p>
<p>Wagering requirements are satisfied at different rates by different games. Pokies almost universally
contribute <b>100%</b> of every dollar staked. Table games commonly contribute 10%. Live dealer blackjack
contributes 5% or is excluded outright.</p>
<p>The consequence is stark. A 40x requirement on a NZ$500 bonus is NZ$20,000 of turnover on pokies. The
same requirement cleared on live blackjack at 5% weighting is <b>NZ$400,000</b>. If you have claimed a
welcome offer, you are a pokies player for the duration whether you wanted to be or not &mdash; and if you
do not want to be, the correct move is to decline the bonus.</p>
<p><a class="btn btn--ghost" href="/online-casinos/bonuses/">Every bonus priced in turnover &rarr;</a></p>
</div>''', ident="weighting")}

{sec(f'''{sechead("Choosing where to play pokies in New Zealand")}
<div class="prose">
<p>Library size is the statistic every comparison page leads with and it is close to worthless past a
certain point. Nobody plays eight thousand games. What actually separates a good pokies lobby from a bad one:</p>
</div>
{steps([
  ("Which RTP build the lobby runs",
   "Established above, and worth more than everything else on this list combined. Check three headline "
   "titles in the information panel before you deposit."),
  ("Whether the studios you like are actually there",
   "Provider counts are inflated by white-label aggregators. If you want Pragmatic Play, Play&rsquo;n GO, "
   "NoLimit City or Hacksaw specifically, filter for the studio rather than trusting a &lsquo;60+ providers&rsquo; "
   "badge."),
  ("Stake range at the bottom, not the top",
   "A NZ$0.10 minimum spin makes a NZ$50 bankroll last an evening. A NZ$0.20 floor halves that. The "
   "minimum stake matters far more to a recreational player than the maximum."),
  ("Demo mode without an account",
   "A lobby that hides demo play behind registration is telling you it would rather you deposited before "
   "you looked. That is a small signal about a larger attitude."),
  ("Whether the search and filters work",
   "Sounds trivial; it is the difference between a library of eight thousand games and a library of the "
   "forty you can find."),
])}''', ident="choosing", haze=True)}

{sec(f'''{sechead("Playing pokies online for real money in New Zealand", None, 2, "realmoney")}
<div class="prose">
<p>A practical round-up of the questions that bring most people to this page, answered in one place.</p>
<h3>Are online pokies legal in NZ?</h3>
<p>Yes, for you. Playing pokies online New Zealand-side has never been an offence &mdash; the Gambling Act
2003 restricts operating and advertising unlicensed gambling, not participating in it. The Online Casino
Gambling Act 2026 will license up to 15 domestic operators from 2027.</p>
<h3>Where can I play pokies online NZ players can actually reach?</h3>
<p>Every site in our table accepts New Zealand registrations. The ones worth shortlisting for real money
pokies NZ play are those that run the top RTP build and bank in New Zealand dollars &mdash; the best pokie
sites NZ-side on that test are <a href="/casino-reviews/spinjo/">Spinjo</a> and
<a href="/casino-reviews/kingdom/">Kingdom</a>.</p>
<h3>Online pokies $1 deposit NZ</h3>
<p>True one-dollar deposits have largely left this market. The lowest genuine entry point we can verify is
NZ$10 at <a href="/casino-reviews/lucky-circus/">Lucky Circus</a>. What matters more for a small bankroll
is the minimum <i>spin</i>, not the minimum deposit: a NZ$0.10 floor makes NZ$20 last an evening, a
NZ$0.20 floor halves it.</p>
<h3>Mobile pokies NZ</h3>
<p>Every title here runs in a mobile browser without an app. Native apps are rare and usually add nothing
&mdash; the games are HTML5 and identical either way. What does differ on mobile is the lobby: filters and
provider search are frequently worse, so find your games on desktop and bookmark them.</p>
<h3>Free online pokies, no download</h3>
<p>Demo mode covers this. It runs in the browser, needs no account and no install, and it is the fastest
way to check an RTP build before depositing. Online pokies free spins no deposit NZ offers are a different
thing &mdash; real money, real winnings, heavy conditions. <a href="/no-deposit-casinos/">We price those
separately</a>.</p>
<h3>New pokies NZ</h3>
<p>New titles land weekly and newness is not a quality signal. What is worth watching is the studio: a new
Pragmatic Play or NoLimit City release will be competently made; a new title from a studio you have never
heard of, appearing only in one lobby, deserves a look at the information panel before you stake anything.</p>
<h3>Which online pokies pay the most in NZ?</h3>
<p>On verified RTP, Big Bass Bonanza at 96.71% leads the headline titles, with Sweet Bonanza and Gates of
Olympus around 96.5% &mdash; but only in their top configuration. Online pokies with bonus buy NZ-side
often show a slightly higher RTP on the bought feature, which is arithmetically true and practically
misleading, because you are staking 60&ndash;100x your normal bet per click.</p>
</div>''', ident="realmoney")}

{sec(f'''{sechead("The types of online pokie, and which ones suit which bankroll", None, 2, "types")}
<div class="prose">
<p>Competitor pages list these as a taxonomy. The categories only matter if you know what each one does to
your money, so that is how they are described here.</p>
</div>
{table(["Type", "What it is", "Typical RTP", "Volatility", "What it does to a NZ$100 bankroll"],
  [["<b>Classic / fruit machines</b>", "Three reels, one to five paylines, no feature rounds",
    "95&ndash;99%", "Low", "Lasts longest. Contains the highest-RTP titles in the market &mdash; Mega "
    "Joker and Jackpot 6000 are both classics."],
   ["<b>Video pokies</b>", "Five reels, 10&ndash;50 paylines, free-spin features", "96%", "Medium",
    "The default. Most sessions are unremarkable in both directions."],
   ["<b>Megaways</b>", "Reel heights change each spin, up to 117,649 ways to win", "95.5&ndash;96.5%",
    "High", "Long dry spells punctuated by rare large hits. NZ$100 can vanish in 40 spins."],
   ["<b>Cluster pays</b>", "Wins from groups of adjacent symbols rather than lines", "96%",
    "Medium&ndash;high", "Cascading wins feel frequent; the maths is unchanged."],
   ["<b>Hold &amp; Win / Link</b>", "Collect symbols to trigger a respin round with fixed prizes",
    "94&ndash;96%", "High", "Base game is often deliberately thin to fund the feature."],
   ["<b>Slingo</b>", "Pokie reels crossed with bingo cards", "95&ndash;96%", "Medium",
    "Slower per round, so cheaper per hour than it looks."],
   ["<b>Progressive jackpot</b>", "A pooled prize funded from every stake", "<b>88&ndash;94% base</b>",
    "Extreme", "The worst value unless you are genuinely chasing the pot &mdash; see below."],
   ["<b>Bonus buy</b>", "Pay 60&ndash;100&times; stake to trigger the feature immediately", "96&ndash;97%",
    "Extreme", "A NZ$1 player buying a feature is making a NZ$100 bet."]],
  caption="Volatility, not RTP, is what decides whether an evening lasts. Two pokies at identical 96% can "
          "produce completely different sessions &mdash; the RTP is the drift, the volatility is the waves.")}
<div class="prose">
<h3>The progressive jackpot arithmetic nobody publishes</h3>
<p>A progressive pot is funded by a slice of every stake, and that slice comes <i>out of the base game
RTP</i>. A progressive advertising 96% may be running <b>88&ndash;92% in the base game</b>, with the
remainder feeding a prize you will almost certainly never win.</p>
<p>Put in hourly terms: at NZ$1 a spin and 600 spins an hour, a 96% pokie costs about NZ$24 an hour. A
progressive running a 90% base game costs <b>NZ$60</b>. You are paying NZ$36 an hour for a lottery ticket
whose odds are typically worse than tens of millions to one.</p>
<p>That is a defensible purchase if you want the lottery ticket and know its price. It is a poor one if you
believed you were playing a 96% game. <b>Check whether the quoted RTP includes the jackpot contribution</b>
&mdash; good studios state it, and if it is not stated, assume it does.</p>
<h3>Maximum win caps: the clause almost nobody checks</h3>
<p>Most modern pokies carry a <b>maximum win cap</b>, expressed as a multiple of your stake &mdash; commonly
5,000&times;, 10,000&times; or 25,000&times;. Hit a sequence worth more and you are paid the cap.</p>
<p>It rarely binds, but when it does it binds at exactly the worst moment. Two titles at identical 96% RTP
with caps of 5,000&times; and 50,000&times; are materially different products, and the cap is in the
information panel next to the RTP. If you play high-volatility pokies specifically for the chance of a
life-changing result, the cap is the number that determines whether that result is even possible.</p>
</div>''', ident="types")}
"""

    return shell(P, T, H1[P],
      "<p>Every comparison page in this market counts the games. We read the RTP out of the game information "
      "panel instead, because the same pokie ships in several different builds and the operator picks which "
      "one you get. That choice costs about <b>NZ$20 per NZ$1,000</b> you stake, and almost nobody checks it.</p>"
      "<p>Below: which lobbies run which build, what an hour of pokies actually costs at your stake, and the "
      "arithmetic behind volatility, jackpots and bonus buys.</p>",
      [("96.5%", "Top build on the headline titles"), ("94.2%", "Cut-down build of the same game"),
       ("NZ$20", "Cost per NZ$1,000 staked"), ("600", "Spins in a typical hour")],
      f"Online pokies &middot; {MONTH_YEAR}", A, C,
      [("The same pokie, different machines", "builds"),
       ("How an online pokie works", "how"),
       ("What pokies cost per hour", "cost"),
       ("Free pokies and demo play", "free"),
       ("The types of pokie, compared", "types"),
       ("Megaways, jackpots and bonus buys", "mechanics"),
       ("Pokies and wagering requirements", "weighting"),
       ("Choosing a pokies lobby", "choosing")],
      body,
      [("Can I play online pokies for real money in NZ?",
        "<p>Yes. Online pokies real money NZ play is lawful for the player, every site in our table accepts "
        "New Zealand registrations, and several bank in New Zealand dollars end to end so you avoid a "
        "conversion spread. What to check before depositing is the RTP build in the game information "
        "panel, because that is the one variable the casino genuinely controls.</p>"),
       ("Which online pokies pay the most in NZ?",
        "<p>The highest-RTP builds we have verified sit around 96.5&ndash;96.7% &mdash; Big Bass Bonanza at "
        "96.71%, Sweet Bonanza and Gates of Olympus at roughly 96.5%. But the title matters less than the "
        "<i>build</i>: the same game runs at 94.x% in many lobbies. The best paying pokies NZ players can "
        "reach are the top-configuration versions, and which one you get depends entirely on the casino.</p>"),
       ("Are online pokies legal in New Zealand?",
        "<p>Playing them is, and always has been. New Zealand law prohibits operating and advertising "
        "unlicensed gambling, not participating in it. The Online Casino Gambling Act 2026 will license up "
        "to 15 domestic operators from 2027; until then the pokies you can reach are supplied from offshore "
        "and you commit no offence by playing them. <a href='/nz-online-casino-law/'>The legal position in "
        "full</a>.</p>"),
       ("What is the highest RTP online pokies NZ players can access?",
        "<p>Outside of a handful of specialist titles, the practical ceiling is about 96.7% on mainstream "
        "pokies. Anything advertised well above 97% is usually either a table game, a specific low-volatility "
        "niche title, or a number that includes a jackpot contribution you are unlikely to collect. Treat "
        "98%+ claims on a standard pokie with suspicion until you have read it in the information panel.</p>"),
       ("Can I play free pokies in New Zealand without registering?",
        "<p>Yes. Most operators expose demo mode in the browser with no account and no deposit, which is "
        "genuinely useful for learning a feature and for checking the RTP build before you commit money. "
        "What demo play cannot tell you is anything about your chances &mdash; and a winning demo session "
        "creates a false impression that costs real money later.</p>"),
       ("Do online pokies pay better at certain times of day?",
        "<p>No. Every spin is generated independently by a certified RNG that has no clock, no memory and no "
        "awareness of how many people are playing. Time of day, day of week, how long you have played and "
        "how much you have lost are all irrelevant to the next outcome. Any source telling you otherwise is "
        "selling something.</p>"),
       ("What is the best pokie site in New Zealand?",
        "<p>On library depth and RTP configuration together, <a href='/casino-reviews/spinjo/'>Spinjo</a> and "
        "<a href='/casino-reviews/kingdom/'>Kingdom</a> run the strongest pokies lobbies of the sites we "
        "cover, and both bank in New Zealand dollars. If your priority is stake range at the bottom end, "
        "<a href='/casino-reviews/lucky-circus/'>Lucky Circus</a> has the lowest entry point.</p>")],
      [("How do online pokies work?",
        "<p>A certified random number generator produces an outcome for each spin independently of every "
        "other spin. The reels you see are a presentation layer over that number. Because outcomes are "
        "independent, no pokie is ever &lsquo;due&rsquo;, no betting system changes the expected result, and "
        "the machine cannot know or care what has happened previously.</p>"),
       ("What does volatility mean on a pokie?",
        "<p>How widely results spread around the average. Low volatility pays small amounts often and "
        "erodes a bankroll slowly. High volatility pays rarely and largely, so most sessions end at zero "
        "while the average is carried by outcomes you may never see. Two games with identical RTP can "
        "produce completely different evenings, which is why volatility matters more than RTP over a single "
        "session.</p>"),
       ("Are progressive jackpot pokies worth playing?",
        "<p>Only if you are genuinely playing for the jackpot. The pot is funded out of the base game, so a "
        "progressive title frequently runs a materially lower base RTP than an equivalent non-jackpot game. "
        "If you are not chasing the top prize you are paying a levy to fund somebody else&rsquo;s chance at "
        "it.</p>"),
       ("Are bonus buys good value?",
        "<p>The bought feature usually carries a slightly higher RTP than the base game, so on a pure "
        "percentage basis it looks fine. What it does is compress a hundred spins of variance into one "
        "decision. Buying a NZ$100 feature is a NZ$100 bet regardless of what your normal stake is, and the "
        "bankroll maths that follows is unforgiving.</p>"),
       ("Do online pokies have better odds than pub pokies?",
        "<p>Generally yes, and by a wide margin. New Zealand class 4 gaming machines in pubs and clubs "
        "return a legally mandated minimum of around 78&ndash;92% depending on configuration, while online "
        "pokies typically run 94&ndash;96.7%. The gap is one of the few genuinely strong arguments for the "
        "online product over the local one.</p>")],
      top, priority=0.9,
      toplist_h2="Best online pokies NZ sites &mdash; audited lobbies",
      toplist_intro=("Listed in our commercial order, as disclosed under every table here. What we checked: "
                     "which RTP build each lobby runs on the headline titles, stake floors, studio coverage "
                     "and whether demo play works without an account."),
      toplist_html=leaderboard(top, cta="Play Pokies"))


def fastpayout():
    P = "/fast-payout-casinos/"
    A, C = "rangi-solomon", "nikau-broughton"
    T = [("Fast payout casinos", P)]
    top = pick(["kingdom", "spino", "crownslots", "rivo", "smash", "spinjo", "lucky-vibe", "madcasino"])

    clock = table(
      ["Stage", "Who controls it", "Typical duration", "What actually delays it"],
      [["<b>1. Verification</b>", "You, then the operator", "2 hours &ndash; 5 days, once",
        "Blurred document photos, a name mismatch between your ID and your account, an address that does "
        "not match the document. Paid once, on the first withdrawal, and then never again."],
       ["<b>2. Internal review</b>", "The operator", "0 &ndash; 72 hours",
        "Manual approval queues that run European business hours. A Friday-night request in New Zealand "
        "lands in an empty office and sits until Monday morning in Malta."],
       ["<b>3. The rail</b>", "The payment network", "Minutes &ndash; 5 business days",
        "This is the only stage the marketing talks about, and it is usually the fastest one. Crypto "
        "settles in minutes, cards take days."],
       ["<b>4. The cap</b>", "The terms", "Indefinite",
        "A weekly ceiling does not slow a withdrawal, it splits it. A win larger than the cap is paid in "
        "instalments over weeks or months, no matter how quick stages 1 to 3 were."]],
      caption="Where the time actually goes. Every fast payout casino NZ list we examined ranks on stage 3 "
              "alone, which is the stage that matters least.")

    caps = []
    for op in CASINOS:
        lim = op.get("withdrawal_limit") or "&mdash;"
        wk = None
        m = re.search(r"([\d,]+)", lim.replace("&euro;", "").replace("NZ$", ""))
        if m and "week" in lim.lower():
            v = int(m.group(1).replace(",", ""))
            wk = round(v * (1.96 if "&euro;" in lim or "€" in lim else 1.0))
        caps.append([
            op_cell(op),
            esc(op.get("payout_crypto") or "&mdash;"),
            esc(op.get("payout_ewallet") or "&mdash;"),
            esc(op.get("payout_card") or "&mdash;"),
            esc(lim),
            (f"<b>{max(1, round(40000 / wk))} weeks</b>" if wk else "&mdash;"),
        ])
    captable = table(
      ["Casino", "Crypto", "E-wallet", "Card / bank", "Withdrawal cap", "To collect NZ$40,000*"],
      caps,
      caption="*How long a NZ$40,000 win takes to reach you under the operator&rsquo;s own published "
              "withdrawal ceiling, euro caps converted at the mid-market rate. This is the column that "
              "decides whether a casino is genuinely fast, and it is the one no competing page publishes.")

    body = f"""
{sec(f'''{sechead("Your withdrawal is not slow because of the payment method",
  "Four stages control the clock. The rail everybody ranks on is the third, and usually the quickest.", 2, "clock")}
<div class="prose">
<p>Search for a fast payout casino NZ and you get a list ordered by advertised processing time &mdash;
&ldquo;instant&rdquo;, &ldquo;within an hour&rdquo;, &ldquo;1&ndash;3 days&rdquo;. Those figures describe
one stage of a four-stage process, and it is usually the stage that costs you the least time.</p>
<p>Here is the whole clock, in the order it actually runs.</p>
</div>
{clock}
<div class="prose">
{note('<p><b>The practical consequence.</b> You can dramatically reduce the time to your first withdrawal '
      'without changing casino at all, simply by completing verification on the day you register rather '
      'than on the day you win. Stage 1 is the largest single delay in the process and it is almost '
      'entirely within your control. Nobody tells you this because there is no commission in it.</p>', "info")}
</div>''', ident="clock")}

{sec(f'''{sechead("The withdrawal cap is the real speed limit", None, 2, "caps")}
<div class="prose">
<p>This is the finding that reorders the entire category, and we have not seen it published anywhere else.</p>
<p>Several casinos here advertise crypto payouts in one to six hours, and they deliver. They also cap
withdrawals at &euro;5,000 a week. Those two facts coexist comfortably right up until you win something
substantial, at which point the second one takes over completely.</p>
<p><b>A NZ$40,000 win at a &euro;5,000 weekly ceiling takes roughly five weeks to collect</b>, in five
separate payments, regardless of the fact that each individual payment arrives within the hour. The casino
has not broken a promise and has not been slow. It has simply been fast within a limit that nobody
mentioned when you were comparing payout times.</p>
</div>
{captable}
<div class="prose">
<p>Read the last two columns together. A site with a six-hour crypto payout and a &euro;5,000 weekly cap is
slower, in every sense that matters after a good night, than a site with a 24-hour payout and no cap at all.
Speed without headroom is a marketing claim, not a feature.</p>
</div>''', ident="caps", haze=True)}

{sec(f'''{sechead("Why is my casino withdrawal pending?")}
<div class="prose">
<p>The most common question in this category, and there are only five real answers.</p>
<h3>1. Verification is incomplete</h3>
<p>By far the most likely. The operator is legally obliged to verify identity and source of funds before
paying out, and it will happily let you deposit and play for weeks without doing so. The request sits
pending until documents are approved. Check your email &mdash; including spam &mdash; for a request you
may have missed.</p>
<h3>2. You are inside a deliberate pending window</h3>
<p>Many operators impose a <b>reverse withdrawal</b> period of 24 to 48 hours, during which your request
sits in limbo and you can cancel it and return the money to your balance. This exists because a meaningful
proportion of players do exactly that and then lose it. It is not a technical delay. It is a designed one.</p>
<h3>3. An active bonus is locking the balance</h3>
<p>If any part of your balance is bonus-derived and the wagering requirement is unmet, withdrawal is
blocked. Some interfaces explain this clearly; most do not, and simply hold the request.</p>
<h3>4. Manual review</h3>
<p>Large or unusual withdrawals are queued for a human. Those humans work European hours, so a request
lodged on Friday evening in New Zealand may not be looked at until Monday.</p>
<h3>5. The cap</h3>
<p>Requested more than the weekly or monthly ceiling and the excess is held rather than refused, often with
no explanation beyond &ldquo;pending&rdquo;.</p>
{note('<p><b>The single most useful habit.</b> Verify your account on day one, before you have won '
      'anything. It converts the largest delay in the process into a task you completed while you were '
      'relaxed, and it removes the one excuse an operator can legitimately use to hold your money.</p>', "info")}
</div>''', ident="pending")}

{sec(f'''{sechead("How to get paid faster, in order of effect")}
{steps([
  ("Complete verification the day you register",
   "Passport or driver licence, plus a utility bill or bank statement dated within 90 days showing the "
   "same name and address as your account. Photograph documents flat, in daylight, with all four corners "
   "visible. This single step removes the biggest delay in the entire process."),
  ("Use the same method to withdraw that you used to deposit",
   "Anti-money-laundering rules require operators to return funds to source where possible. Depositing by "
   "card and requesting a crypto withdrawal triggers manual review at almost every site."),
  ("Withdraw on a Monday or Tuesday",
   "Manual approval queues are staffed on European business hours. A Friday-night request in New Zealand "
   "lands in an empty office and waits out the weekend."),
  ("Request under the cap",
   "If the weekly ceiling is &euro;5,000 and you have won more, request the ceiling rather than the whole "
   "amount. A request over the limit is frequently held in its entirety instead of being part-paid."),
  ("Do not cancel a pending withdrawal",
   "The reverse-withdrawal window exists to tempt you into putting the money back. Once you have requested, "
   "leave it. If the interface makes cancelling easy and confirming hard, that is intentional."),
  ("Use crypto if you already hold it",
   "The fastest rail, typically minutes to hours once verified. Worth understanding the tax position "
   "first, because the IRD treats cryptoassets as property and converting back to NZD can be a taxable "
   "disposal."),
])}''', ident="faster", haze=True)}

{sec(f'''{sechead("What &ldquo;instant withdrawal&rdquo; actually means")}
<div class="prose">
<p>Nothing, as a term of art. No operator in this market pays instantly in the ordinary sense of the word,
and the phrase is used to describe three quite different things.</p>
<ul>
<li><b>Instant approval</b> &mdash; the request skips the manual queue. Genuinely valuable, and the
closest thing to the promise. Usually only available on an already-verified account under a threshold.</li>
<li><b>Instant settlement on the rail</b> &mdash; once approved, the money moves in minutes. True of
crypto, broadly true of e-wallets, never true of cards.</li>
<li><b>Instant, as an adjective in a banner</b> &mdash; meaning nothing at all, and usually attached to a
site with a 48-hour reverse-withdrawal window.</li>
</ul>
<p>The honest version of the claim is: <b>an account verified in advance, withdrawing to crypto or an
e-wallet, under the cap, on a weekday, will usually have money within a few hours.</b> Every one of those
conditions is doing work, and an instant withdrawal casino NZ list that mentions none of them is describing
a best case as though it were a standard.</p>
</div>''', ident="instant")}

{sec(f'''{sechead("Withdrawal times at online casinos: the questions people actually ask", None, 2, "times")}
<div class="prose">
<h3>How long do casino withdrawals take NZ side?</h3>
<p>On a verified account: crypto one to six hours, e-wallets 8 to 24 hours, cards and bank transfer two to
five business days. Withdrawal times online casino NZ players experience on their <i>first</i> cashout are
longer, because verification happens inside it. Online casino payout time New Zealand players quote as
&ldquo;slow&rdquo; is almost always that first one.</p>
<h3>Casino withdrawal pending time NZ</h3>
<p>Casino withdrawal pending time NZ side is typically 0 to 72 hours and is made up of two separate things:
a deliberate reverse-withdrawal window of 24 to 48 hours, and a manual approval queue staffed on European
business hours. Neither is the payment rail.</p>
<h3>Fastest withdrawal method at an online casino NZ</h3>
<p>The fastest withdrawal method online casino NZ players have access to is crypto, and it is not close.
Crypto instant withdrawal casino NZ claims are the closest thing to accurate in this category &mdash;
stablecoins settle in minutes once approved. Instant withdrawal casino NZ bank transfer claims are not:
domestic clearing takes a day or more regardless of how fast the casino approves.</p>
<h3>Same day payout casino NZ and quick withdrawal casino NZ options</h3>
<p>A same day payout casino NZ experience is entirely achievable and depends almost wholly on you: verify
in advance, withdraw to crypto or an e-wallet, stay under the cap, and request on a weekday. Casinos with
fast withdrawals NZ side are listed above, but a quick withdrawal casino NZ account that is unverified will
still take days.</p>
<h3>Instant payout casino NZ and instant withdrawal pokies NZ</h3>
<p>No casino pays out instantly in the literal sense. An instant payout casino NZ badge normally means
instant <i>approval</i> under a threshold on a verified account. Instant withdrawal pokies NZ is the same
claim attached to a game type &mdash; the game you played has no bearing on payout speed at all.</p>
<h3>How to speed up a casino withdrawal</h3>
<p>Fast payout casino NZ no verification delay is achievable only by doing the verification first. That is
the whole trick, and it is worth more than choosing a different casino. Everything else &mdash; matching
your deposit method, requesting on a Monday, staying under the cap &mdash; is secondary.</p>
</div>''', ident="times")}

{sec(f'''{sechead("Why your withdrawal is really being held: source of funds, explained",
  "The largest cause of withdrawal pain in New Zealand, and the one nobody writes about.", 2, "sof")}
<div class="prose">
<p>We went and read what New Zealanders actually say about online casinos, rather than what affiliate pages
say about them. The result points somewhere unexpected.</p>
<p><b>SkyCity Online Casino</b> &mdash; New Zealand&rsquo;s own domestically licensed operator, the site
most Kiwis assume is the safe choice &mdash; holds a <b>TrustScore of 1.5 out of 5</b> across <b>71
reviews</b> on Trustpilot, <b>82% of them one-star</b> (checked {MONTH_YEAR}).</p>
<p>Almost none of those complaints are about rigged games, unfair odds or missing bonuses. They are about
<b>verification</b> &mdash; overwhelmingly, specifically, and at length:</p>
<blockquote class="quote"><p>&ldquo;I spent about 4 weeks trying to withdraw winnings, they have asked me
for every imaginable document under the sun. Complete invasion of privacy asking for proof of income
sources&hellip; wanting 90 days of unfiltered transactions and then not accepting the PDF as it is
&lsquo;too large&rsquo;.&rdquo;</p><cite>Trustpilot reviewer, SkyCity Online Casino</cite></blockquote>
<p>That is a <b>source of funds</b> check. The reason it feels like an invasion of privacy is that it is
one. It is also, in most cases, a legal obligation rather than a stalling tactic &mdash; which is the part
nobody explains, and the reason so many people conclude they are being scammed when they are not.</p>
<h3>What the casino is legally required to ask for</h3>
<p>Licensed operators sit under anti-money-laundering rules &mdash; New Zealand&rsquo;s own regime is the
<b>AML/CFT Act 2009</b>, and offshore operators are bound by their licensing jurisdiction&rsquo;s
equivalent. They all work the same way, in two tiers.</p>
<p><b>Standard due diligence</b> applies to everyone: confirm who you are and where you live. Photo ID plus
a recent utility bill or bank statement.</p>
<p><b>Enhanced due diligence</b> triggers on certain patterns &mdash; large or rapid deposits, a large win,
unusual payment behaviour, a mismatch between deposit and withdrawal rails. At that point the operator must
establish not only who you are but <b>where the money came from</b>. That is when payslips and bank
statements get demanded, and it is why it always seems to happen immediately after a big win. It is not
punishment for winning. Winning is simply one of the triggers.</p>
{note('<p><b>The part that is a genuine grievance.</b> None of this excuses demanding documents in a format '
      'the operator will not accept, rejecting a PDF for being &ldquo;too large&rdquo;, or sending a player '
      'round in circles for four weeks. The <i>requirement</i> is legitimate. The <i>administration of '
      'it</i> frequently is not, and an operator that handles it badly deserves the review it gets.</p>',
      "warn")}
<h3>The document pack to prepare before you ever win</h3>
<p>Every hour spent on this while calm is an hour not spent arguing with a support desk while your money
sits frozen. Assemble now:</p>
<ol>
<li><b>Photo ID</b> &mdash; passport or NZ driver licence. All four corners visible, flat, in daylight, no
flash glare across the details.</li>
<li><b>Proof of address</b> dated within 90 days &mdash; power, water or internet bill, or a bank
statement. Name and address must match your casino account <i>exactly</i>. A middle name on one and not the
other is a real and common rejection.</li>
<li><b>Proof of payment method</b> &mdash; card photo with the middle digits obscured and the last four
visible, or an e-wallet screenshot showing your name.</li>
<li><b>Source of funds</b>, if depositing or winning meaningfully &mdash; recent payslips, an IRD income
summary, or 90 days of bank statements as an <b>unedited PDF under 10MB</b>. Do not crop, redact or
screenshot them; an altered statement is refused every time.</li>
</ol>
<p>Upload all of it <b>on the day you register</b>. Verification is not optional and not negotiable, it is
the largest single delay in the withdrawal process, and it is almost entirely within your control.</p>
<h3>Why &ldquo;no verification casino NZ&rdquo; is the wrong search</h3>
<p>It is a popular one. In our harvest of 994 New Zealand autosuggest queries, verification-related
searches are almost all phrased as attempts to <i>avoid</i> it &mdash; &ldquo;no verification withdrawal
casino nz&rdquo;, &ldquo;instant withdrawal casino no verification nz real money&rdquo;. Plenty of
affiliate pages are happy to serve that search.</p>
<p>They are selling something that does not exist. Any operator licensed anywhere has identity obligations
and will apply them at withdrawal, whatever the signup flow implied. A site that genuinely never verifies
holds no licence worth having &mdash; a far larger problem than being asked for a power bill.</p>
<p class="lead"><b>The real answer is not a casino that skips verification. It is doing verification on day
one, before you have anything to lose by waiting.</b></p>
</div>''', ident="sof")}

{sec(f'''{sechead("The trap at the end of a stuck withdrawal", None, 2, "rinse")}
<div class="prose">
<p>This section exists because of one review, and it is the most important thing on this page.</p>
<blockquote class="quote"><p>&ldquo;These guys were so determined not to payout, I gave up, <b>rinsed my
winnings</b> and took the loss. I was never going to be able to withdraw.&rdquo;</p><cite>Trustpilot
reviewer, SkyCity Online Casino</cite></blockquote>
<p>Read what actually happened. The withdrawal was not refused. The player <i>gave up</i> and gambled the
balance away out of frustration &mdash; and the casino kept the money without ever having to decline a
payment.</p>
<p>We have found no competitor page that mentions this, and it may be the most expensive single pattern in
online gambling. The mechanism is ordinary and brutal:</p>
<ol>
<li>You win. A withdrawal request goes in.</li>
<li>It sits pending. Documents are requested, then requested again.</li>
<li>Frustration builds &mdash; and the balance is sitting right there, playable.</li>
<li>You start playing it, not because you wanted to, but because the alternative is doing nothing while
feeling cheated.</li>
<li>The house edge does the rest. It always does.</li>
</ol>
<h3>The defences, in order of effectiveness</h3>
<ul>
<li><b>Verify on day one.</b> Removes the delay that starts the sequence.</li>
<li><b>Treat a submitted withdrawal as spent.</b> It has gone. Do not revisit the balance or calculate what
it would be worth at a higher stake.</li>
<li><b>Never cancel a pending withdrawal.</b> The 24-to-48-hour reverse-withdrawal window exists precisely
to make this easy. If the interface makes cancelling one click and confirming three, that is a design
decision about you.</li>
<li><b>Withdraw the whole balance, not part of it.</b> A partial withdrawal leaves a playable remainder,
which is the seed of the same problem.</li>
<li><b>If you feel the urge to rinse it, close the tab and complain instead.</b> The ladder below is slower
and very much cheaper.</li>
</ul>
{note('<p><b>Our commercial position, stated plainly.</b> We are paid on player activity. A reader who '
      'withdraws and stops playing is worth less to us than one who rinses a stuck balance. We are telling '
      'you to withdraw and stop.</p>', "info")}
</div>''', ident="rinse", haze=True)}

{sec(f'''{sechead("If a casino will not pay: the escalation ladder", None, 2, "escalate")}
<div class="prose">
<p>Reddit threads on New Zealand offshore casinos return to one line repeatedly &mdash; <i>&ldquo;you will
have no recourse if they refuse to let you withdraw your money.&rdquo;</i> That is broadly true and not
entirely true, and the difference is worth knowing before you need it.</p>
</div>
{steps([
  ("Put it in writing, with your account ID and the exact amount",
   "Email rather than live chat, because you need a timestamped record. State the withdrawal date, the "
   "amount, every document supplied and when. Ask for a specific reason and a specific timeframe. Keep it "
   "factual and unemotional &mdash; this message may later be read by a regulator."),
  ("Escalate internally and name a deadline",
   "Ask for the complaint to go to a manager or the complaints function, and state that if it is unresolved "
   "within a stated period &mdash; 14 days is reasonable &mdash; you will refer it to the licensing "
   "regulator. Most operators that intend to pay will move at this step."),
  ("Take it to the regulator named in the footer",
   "For a Cura&ccedil;ao Gaming Control Board licensee, the GCB accepts player complaints directly and the "
   "2023 reforms gave it a defined complaint-handling process. You will need the licence number and the "
   "operating company name &mdash; which is exactly why we tell you to confirm both exist before you "
   "deposit. If the site names no company, this step is closed to you."),
  ("Use an independent ADR service if one is named",
   "Some operators subscribe to an alternative dispute resolution provider, named in the terms or the "
   "footer. It is free to the player and its findings bind subscribing operators."),
  ("Escalate the payment rather than the casino",
   "If you funded by card, a chargeback through your New Zealand bank is sometimes available where a "
   "service was not delivered. It is not a general refund route for gambling losses and banks scrutinise "
   "these closely, but a refused withdrawal of verified funds is a stronger case than most."),
  ("Post the record publicly, accurately",
   "A factual, dated, unemotional review is the last lever a player has, and it demonstrably works on "
   "operators that care about acquisition. Stick to what you can evidence."),
])}
<div class="prose">
{note('<p><b>What none of this gives you.</b> There is no New Zealand body that can compel an offshore '
      'operator to pay. The DIA regulates supply into New Zealand; it does not adjudicate your individual '
      'withdrawal. That changes for licensed operators when the regime opens in 2027, and it is the '
      'single strongest argument for the new framework. '
      '<a href="/nz-online-casino-law/">What the 2026 Act actually does</a>.</p>', "warn")}
</div>''', ident="escalate")}

{sec(f'''{sechead("What happens to your balance if a casino goes under", None, 2, "insolvency")}
<div class="prose">
<p>Rarely asked, and worth asking, because the answer is worse than most people assume.</p>
<p>In a strong regulatory regime player funds sit in <b>segregated accounts</b>, kept apart from the
operator&rsquo;s working capital so that if the business fails, player balances are not available to its
creditors. The UK requires this and grades operators publicly on it.</p>
<p><b>No offshore licence available to New Zealanders currently guarantees the equivalent.</b> The
Cura&ccedil;ao Gaming Control Board reforms strengthened oversight but stop short of UK-style segregation
and disclosure. In practice, if an operator holding your balance fails, you are an unsecured creditor in a
foreign jurisdiction &mdash; and unsecured creditors are paid last and least.</p>
<h3>What follows</h3>
<ul>
<li><b>Do not use a casino account to store money.</b> It is not a bank, it is not insured, and nothing
protects the balance.</li>
<li><b>Withdraw winnings rather than leaving them.</b> The same conclusion as the section above, reached
from a different direction, which is usually a sign the advice is sound.</li>
<li><b>Prefer operators with a named company and a resolvable licence</b> &mdash; not because it guarantees
segregation, it does not, but because it is the only thing that gives you a legal entity to name.</li>
</ul>
<p>The 2027 New Zealand regime is expected to bring domestic requirements on fund handling. Until then the
protection is behavioural: keep the balance small and take the money out.</p>
</div>''', ident="insolvency", haze=True)}

{sec(f'''{sechead("Sources and references", None, 2, "sources")}
<div class="prose">
<p>Every figure on this page is checkable. Where each came from:</p>
<ul>
<li><b>Trustpilot</b> &mdash; SkyCity Online Casino rating distribution and reviewer quotes, captured
{MONTH_YEAR}: TrustScore 1.5/5 from 71 reviews; 82% one-star, 8% five-star, 6% two-star, 4% four-star, 0%
three-star.</li>
<li><b>NZ search-demand harvest</b> &mdash; 994 New Zealand autosuggest queries from Google (gl=nz) and
DuckDuckGo (kl=nz-en). Withdrawal and payout queries are 6.5% of the set; verification queries 1.1%, and
almost all of those are phrased as attempts to avoid it.</li>
<li><b>Google Trends</b>, geo=NZ &mdash; &ldquo;best online casino nz&rdquo; at a five-year high, up
175.7% year on year, while the generic term falls 28.6%.</li>
<li><b>Payout windows and withdrawal caps</b> &mdash; each operator&rsquo;s own published terms, verified
from a New Zealand IP address in {MONTH_YEAR} and listed per brand above.</li>
<li><b>AML/CFT Act 2009</b> (New Zealand) for the due-diligence tiers described above; offshore operators
are bound by their own jurisdiction&rsquo;s equivalent.</li>
<li><b>Reddit</b> &mdash; r/newzealand discussion of offshore casino recourse. Reddit blocks automated
access, so this is cited from search-result snippets only and no post bodies are reproduced.</li>
</ul>
</div>''', ident="sources")}
"""

    return shell(P, T, H1[P],
      "<p>Every fast payout casinos NZ list ranks on the advertised processing time. That figure describes "
      "one of the four stages that stand between a request and your bank account, and it is normally the "
      "quickest of them.</p>"
      "<p>This page ranks on the whole clock &mdash; verification, the approval queue, the rail and, "
      "critically, <b>the withdrawal cap</b>. A casino paying in one hour under a &euro;5,000 weekly "
      "ceiling takes five weeks to settle a NZ$40,000 win, and no competing page we examined mentions it.</p>",
      [("4", "Stages in the withdrawal clock"), ("1", "That the marketing describes"),
       ("5 weeks", "To collect NZ$40k under a &euro;5k cap"), ("Day 1", "When you should verify")],
      f"Payout speed &middot; {MONTH_YEAR}", A, C,
      [("The four-stage withdrawal clock", "clock"),
       ("The cap is the real speed limit", "caps"),
       ("Why is my withdrawal pending?", "pending"),
       ("How to get paid faster", "faster"),
       ("What &lsquo;instant&rsquo; really means", "instant"),
       ("Source of funds, explained", "sof"),
       ("The trap at the end of a stuck withdrawal", "rinse"),
       ("If a casino will not pay", "escalate"),
       ("If a casino goes under", "insolvency"),
       ("Sources and references", "sources")],
      body,
      [("Is there a casino that pays out instantly in NZ?",
        "<p>Not literally, and a casino that pays out instantly NZ side is marketing shorthand for instant "
        "approval on a verified account under a threshold. The closest real experience is a verified "
        "account withdrawing stablecoin on a weekday, which lands in minutes. Every word of that sentence "
        "is doing work.</p>"),
       ("How long do casino withdrawals take in NZ?",
        "<p>Once an account is verified: crypto typically one to six hours, e-wallets 8 to 24 hours, cards "
        "and bank transfers two to five business days. The first withdrawal is the slow one because "
        "verification happens inside it &mdash; add anywhere from two hours to five days. Verify on the day "
        "you register and the first withdrawal behaves like every subsequent one.</p>"),
       ("Which casino pays out fastest to New Zealand players?",
        "<p>On the rail alone, the crypto-first sites &mdash; <a href='/casino-reviews/spino/'>Spino</a> and "
        "<a href='/casino-reviews/kingdom/'>Kingdom</a> settle quickest in our testing. On the measure that "
        "matters after a big win, the ranking changes: what counts then is the weekly withdrawal ceiling, "
        "and several of the quickest sites carry the tightest caps. Both columns are in the table above.</p>"),
       ("Why is my casino withdrawal still pending?",
        "<p>Almost always one of five things: verification is incomplete, you are inside a deliberate 24 to "
        "48 hour reverse-withdrawal window, an unmet bonus wagering requirement is locking the balance, the "
        "request is queued for manual review on European business hours, or you have requested more than "
        "the weekly cap allows.</p>"),
       ("What is the fastest withdrawal method at an online casino?",
        "<p>Crypto, by a wide margin &mdash; typically minutes to a few hours once approved, because there "
        "is no banking intermediary. E-wallets such as Skrill and Neteller are next. Cards are slowest, "
        "because a refund to a card is processed through the card scheme and takes two to five business "
        "days regardless of how quickly the casino approves it.</p>"),
       ("Can I withdraw without verification?",
        "<p>No, and you should be wary of any site that lets you. Operators are legally required to verify "
        "identity before paying out, and a casino willing to skip that is a casino with a compliance "
        "problem that will eventually become your problem. The right response is to verify early rather "
        "than to look for a site that does not ask.</p>"),
       ("Do withdrawal limits apply to jackpot wins?",
        "<p>Usually the cap still applies, and this is where it hurts most. Some operators carve out "
        "progressive jackpot wins and pay them in a lump sum; many do not, and a six-figure win then "
        "arrives in weekly instalments over a year or more. If you play progressives, read the withdrawal "
        "section of the terms before you play, not after you win.</p>")],
      [("What is a reverse withdrawal?",
        "<p>A window, normally 24 to 48 hours, during which a requested withdrawal sits pending and can be "
        "cancelled to return the funds to your playable balance. It is presented as a convenience. Its "
        "actual function is to give you time to change your mind and gamble the money back, which a "
        "significant number of players do. Treat a request as final and do not revisit it.</p>"),
       ("Do e-wallets get paid faster than bank transfers?",
        "<p>Consistently, yes. Skrill and Neteller settle in hours where a bank transfer takes days, "
        "because the e-wallet sits outside the domestic clearing system. The trade-off for New Zealanders "
        "is currency: e-wallet balances at euro-denominated casinos convert twice, and the spread on that "
        "round trip is around 4.8%.</p>"),
       ("Is there a fee to withdraw from an online casino?",
        "<p>Most sites here process one withdrawal per week free and charge for additional requests in the "
        "same period, which is a quiet argument for withdrawing in fewer, larger amounts. Crypto "
        "withdrawals carry a network fee that the operator may or may not absorb. Card withdrawals are "
        "usually free but slow.</p>"),
       ("Why do casinos make withdrawals slower than deposits?",
        "<p>Deposits are instant because the operator wants the money in play and bears no risk in "
        "accepting it. Withdrawals pass through identity checks, anti-money-laundering review and a manual "
        "approval queue, all of which are genuine regulatory obligations. The asymmetry is real and partly "
        "legitimate &mdash; but the reverse-withdrawal window is not a regulatory requirement, and that "
        "part is a design choice.</p>")],
      top, priority=0.9,
      toplist_h2="Fastest paying online casinos NZ &mdash; measured on the whole clock",
      toplist_intro=("Our commercial order, as disclosed under every table on this site. The columns that "
                     "should decide your choice are payout speed and the withdrawal cap together, and "
                     "neither follows the listing order."),
      toplist_html=leaderboard(top, cta="Visit Casino"))


def highpayout():
    P = "/high-payout-casinos/"
    A, C = "rangi-solomon", "camille-toure"
    T = [("Best payout casinos", P)]
    top = pick(["spinjo", "kingdom", "rivo", "smash", "lucky-vibe", "crownslots", "fortune-play", "madcasino"])

    edge = table(
      ["Game", "Typical RTP", "House edge", "Expected loss per NZ$100 staked", "Decisions per hour", "Expected loss per hour @ NZ$5"],
      [["Blackjack, basic strategy", "<b>99.5%</b>", "0.5%", "NZ$0.50", "~70", "<b>NZ$1.75</b>"],
       ["Baccarat, banker bet", "<b>98.94%</b>", "1.06%", "NZ$1.06", "~60", "NZ$3.18"],
       ["Video poker, 9/6 Jacks or Better", "99.54%", "0.46%", "NZ$0.46", "~400", "NZ$9.20"],
       ["Craps, pass line", "98.59%", "1.41%", "NZ$1.41", "~90", "NZ$6.35"],
       ["Roulette, European single zero", "97.30%", "2.70%", "NZ$2.70", "~50", "NZ$6.75"],
       ["Roulette, American double zero", "94.74%", "5.26%", "NZ$5.26", "~50", "NZ$13.15"],
       ["Pokies, top build", "96.50%", "3.50%", "NZ$3.50", "~600", "<b>NZ$105</b>"],
       ["Pokies, cut-down build", "94.50%", "5.50%", "NZ$5.50", "~600", "<b>NZ$165</b>"],
       ["Game show titles", "95&ndash;96%", "4&ndash;5%", "NZ$4.50", "~40", "NZ$9"]],
      caption="The column that matters is the last one. RTP is a per-stake figure, and games differ "
              "enormously in how many stakes they extract per hour. A pokie at 96.5% costs sixty times more "
              "per hour than blackjack at 99.5% on the same NZ$5 bet, because it asks you to bet ten times "
              "as often.")

    horizon = table(
      ["Spins played", "Range containing 95% of outcomes*", "Has the 96% RTP appeared?"],
      [["100", "&minus;NZ$250 to +NZ$240", "No &mdash; almost anything can happen"],
       ["1,000", "&minus;NZ$430 to +NZ$350", "No &mdash; the drift is buried in the noise"],
       ["10,000", "&minus;NZ$1,120 to +NZ$320", "Barely &mdash; the loss is now visible but the range is wide"],
       ["100,000", "&minus;NZ$5,300 to &minus;NZ$2,700", "Yes &mdash; the outcome is now reliably a loss"],
       ["1,000,000", "&minus;NZ$42,000 to &minus;NZ$38,000", "Completely &mdash; this is where 96% lives"]],
      caption="*Indicative range for a NZ$1 stake on a medium-volatility 96% RTP pokie. RTP is a statement "
              "about the last row. It is not a statement about your evening, and at 600 spins per hour the "
              "bottom row is roughly 28 continuous days of play.")

    body = f"""
{sec(f'''{sechead("&ldquo;Casino payout percentage&rdquo; is not a real number",
  "The premise of this entire category is mostly fiction. Here is what to use instead.", 2, "fiction")}
<div class="prose">
<p>Pages competing for <b>best payout online casino NZ</b> almost all present a single percentage per
casino &mdash; 97.1% here, 96.4% there &mdash; usually in a tidy ranked table. It looks authoritative. It
is close to meaningless, for three reasons.</p>
<p><b>First, a casino does not have an RTP. Its games do.</b> A site-wide figure is a weighted average
across a library of several thousand titles, weighted by what other players happened to play last month.
It tells you nothing about the games <i>you</i> intend to play. Two players at the same casino on the same
day can face house edges that differ by a factor of ten.</p>
<p><b>Second, where these figures come from is rarely stated.</b> Independent testing houses do publish
monthly payout audits for some operators; most of the numbers circulating on comparison pages are neither
audited nor sourced, and several are simply copied between affiliate sites until they acquire the
appearance of fact.</p>
<p><b>Third, and most importantly, the casino does not choose the RTP &mdash; except in the one way that
actually matters</b>, which is picking which build of each game to run.
<a href="/online-pokies/#builds">That</a> is a real, checkable, per-title decision worth about NZ$20 per
NZ$1,000 staked, and it is the only sense in which one casino genuinely pays better than another.</p>
{note('<p><b>So what should you use?</b> Two numbers. The <b>house edge of the games you actually play</b>, '
      'which is published and reliable, and the <b>RTP build</b> the lobby runs on those games, which you '
      'can read in the game information panel in ten seconds. Both are below.</p>', "info")}
</div>''', ident="fiction")}

{sec(f'''{sechead("What RTP means, and the time horizon that makes it true", None, 2, "rtp")}
<div class="prose">
<p><b>RTP &mdash; return to player &mdash; is the proportion of total stakes a game returns over its
lifetime.</b> A 96% pokie returns 96 cents per dollar staked across many millions of spins. The
complementary 4% is the house edge, and it is the price of playing.</p>
<p>The critical and routinely omitted qualifier is <i>over many millions of spins</i>. RTP is a limit that
emerges slowly, and &ldquo;slowly&rdquo; here means slower than a human lifetime of recreational play.</p>
</div>
{horizon}
<div class="prose">
<p>This is why the question &ldquo;does RTP matter in the short term?&rdquo; has an honest answer of
<b>no, and also yes</b>. In any single session, variance dominates completely and a 94% game can easily
out-pay a 97% one. Across a year of regular play, the drift is inexorable and the two percentage points
have quietly taken hundreds of dollars. You will never <i>feel</i> RTP. You will still pay it.</p>
</div>''', ident="rtp", haze=True)}

{sec(f'''{sechead("House edge by game: the table that should lead every payout page")}
<div class="prose">
<p>If you want the highest payout online casino experience available to a New Zealander, the answer has
almost nothing to do with which casino you pick and almost everything to do with which game you open when
you get there.</p>
</div>
{edge}
<div class="prose">
<p>Two observations that follow directly, and that no &ldquo;highest RTP casinos NZ&rdquo; ranking will
tell you:</p>
<p><b>1. Blackjack played with basic strategy is the cheapest entertainment in the building</b>, by a
distance &mdash; roughly NZ$1.75 an hour at a NZ$5 stake, against NZ$105 for pokies at the same stake. The
gap is not the RTP difference of three percentage points. It is the <i>speed</i>: pokies take six hundred
decisions an hour, blackjack takes seventy.</p>
<p><b>2. Speed is the variable nobody discusses.</b> Turbo spin, autoplay and quick-spin settings raise
your cost per hour in direct proportion to how much they raise your spin rate. Turning autoplay off is,
arithmetically, one of the most effective bankroll decisions available &mdash; and it costs nothing.</p>
{note('<p><b>The catch on blackjack.</b> That 99.5% assumes correct basic strategy on every hand, and it '
      'assumes you are not clearing a bonus &mdash; table games usually contribute 10% or less toward '
      'wagering requirements, and live blackjack often 5% or nothing. The cheapest game in the building is '
      'the one most welcome offers are designed to keep you away from. '
      '<a href="/online-casinos/bonuses/#wagering">Why that is</a>.</p>', "warn")}
</div>''', ident="edge")}

{sec(f'''{sechead("How to build the lowest house edge session you can")}
{steps([
  ("Pick the game before you pick the casino",
   "The difference between blackjack and pokies is a factor of sixty in cost per hour. The difference "
   "between the best and worst casino on the same game is a factor of about 1.5. You are optimising the "
   "wrong variable if you start with the site."),
  ("Check the RTP build in the game information panel",
   "Ten seconds, before you stake anything. If a headline title reads 94.x% where its top build is 96.x%, "
   "the lobby has chosen the cheap version and everything else about the site matters less."),
  ("Turn autoplay and turbo spin off",
   "Your expected loss is stake times spins times edge. Halving your spin rate halves your hourly cost "
   "with no change to your odds on any individual spin. This is the only genuinely free improvement "
   "available to a pokies player."),
  ("Prefer European roulette over American, always",
   "A single zero costs 2.7%; a double zero costs 5.26%. Identical game, identical stake, nearly double "
   "the price. If a lobby offers both, the American table exists only to catch people who did not look."),
  ("Decline the bonus if you want to play table games",
   "Weighting at 10% or 5% turns a modest wagering requirement into an impossible one. If you intend to "
   "play blackjack or roulette, a welcome offer is not a benefit, it is a constraint."),
  ("Avoid side bets entirely",
   "Perfect Pairs, 21+3, insurance and their relatives carry house edges of 4% to 12% &mdash; ten to "
   "twenty times the main game they are attached to. They are the most expensive thing on a table that is "
   "otherwise the cheapest thing in the casino."),
])}''', ident="build", haze=True)}

{sec(f'''{sechead("Where the genuinely high RTP is")}
<div class="prose">
<p>Ranked honestly, by the actual return rather than by who is paying us.</p>
<ul>
<li><b>Video poker, correct strategy</b> &mdash; 99.5%+ on a full-pay 9/6 Jacks or Better machine, the
highest reliably available return in any casino. The catch is that the pay table varies and a short-pay
version drops it to 97%, so you must read the paytable before playing. Also note the four hundred hands
per hour, which makes it cheap per stake and not cheap per hour.</li>
<li><b>Blackjack, basic strategy</b> &mdash; 99.5% on good rules, and the rules matter: 3:2 blackjack
payouts rather than 6:5, dealer standing on soft 17, double after split permitted. A 6:5 table costs you
roughly 1.4% extra and is common online.</li>
<li><b>Baccarat, banker</b> &mdash; 98.94%, no strategy required at all, which makes it the highest-return
game that cannot be played incorrectly.</li>
<li><b>European roulette</b> &mdash; 97.3%, and every bet on the table carries the same edge, so bet
whatever you find entertaining.</li>
<li><b>Pokies, top build</b> &mdash; 96&ndash;96.7%, the lowest return of the group, and where almost all
the money in this industry is made.</li>
</ul>
<p>Note what that ordering implies. The games with the best payout percentages are the ones casinos
promote least, exclude from bonuses most aggressively, and bury below three screens of pokies. That is not
a conspiracy; it is simply what the arithmetic above predicts.</p>
</div>''', ident="where")}

{sec(f'''{sechead("RTP meaning, return to player explained, and the numbers people search for", None, 2, "meaning")}
<div class="prose">
<h3>RTP meaning in a casino context</h3>
<p>RTP meaning, in casino terms, is simply this: the share of everything staked on a game that the game
returns to players over its lifetime. Return to player explained in one line &mdash; it is the opposite
side of the house edge, and the two always sum to 100%.</p>
<h3>House edge vs RTP</h3>
<p>The house edge vs RTP question is a false distinction: 96% RTP and a 4% house edge are the same
statement. House edge is the more useful of the two because it multiplies cleanly &mdash; stake &times;
number of bets &times; edge gives you the expected cost of a session, which RTP does not do as directly.</p>
<h3>Average RTP at an online casino NZ side</h3>
<p>Across the lobbies we audited, the average RTP online casino NZ players will encounter on mainstream
pokies is around 95.5&ndash;96%, dragged down by cut-down builds and progressive titles. Payout rates
online casinos New Zealand players see quoted as a single site-wide figure are weighted averages of the
whole library and should be treated as marketing rather than measurement.</p>
<h3>Highest RTP pokies NZ, and the best RTP slots NZ lobbies run</h3>
<p>The practical ceiling on mainstream titles is about 96.7%. The highest RTP pokies NZ players can reach
are simply the top-configuration versions of well-known games &mdash; there is no secret high-return
title, only the same titles configured honestly. The best RTP slots NZ side are therefore a property of
the lobby, not the game list.</p>
<h3>Loosest online pokies NZ</h3>
<p>&ldquo;Loose&rdquo; has no technical meaning online, but if it means anything it means a lobby that
licensed the top build. Loosest online pokies NZ side is a lobby question, and it is answerable in ten
seconds per game.</p>
<h3>Blackjack RTP vs pokies RTP</h3>
<p>Blackjack RTP vs pokies RTP is the largest value gap in any casino: 99.5% against 96.5%, and blackjack
takes seventy decisions an hour where a pokie takes six hundred. Which online casino has the best payout
NZ-side matters far less than which game you open when you arrive. The highest paying online casino NZ
players can find is, in practice, whichever one lets you play blackjack at limits you are comfortable
with &mdash; and does not tie you to a bonus that excludes it.</p>
</div>''', ident="meaning", haze=True)}

{sec(f'''{sechead("The highest RTP pokies New Zealanders can actually play",
  "Named titles, published return rates, and the one caveat that matters.", 2, "titles")}
<div class="prose">
<p>Everything above argues that RTP is a property of games rather than casinos. So here are the games.
These are the highest published return rates available in mainstream New Zealand-facing lobbies, and the
gap between the top of this table and an average pokie is larger than the gap between any two casinos on
this site.</p>
</div>
{table(["Title", "Studio", "Published RTP", "House edge", "Cost per hour at NZ$1, 600 spins", "Note"],
  [["<b>Book of 99</b>", "Relax Gaming", "<b>99.00%</b>", "1.00%", "<b>NZ$6</b>",
    "The highest-return mainstream pokie in this market. Low volatility, no jackpot."],
   ["Mega Joker", "NetEnt", "<b>99.00%</b>", "1.00%", "NZ$6",
    "Only at maximum stake in supermeter mode &mdash; the headline rate does not apply to base play."],
   ["Jackpot 6000", "NetEnt", "98.90%", "1.10%", "NZ$6.60", "Same supermeter caveat as Mega Joker."],
   ["1429 Uncharted Seas", "Thunderkick", "98.60%", "1.40%", "NZ$8.40", "Low volatility, widely available."],
   ["Blood Suckers", "NetEnt", "98.00%", "2.00%", "NZ$12", "A 2010 title still in most lobbies."],
   ["Money Cart", "Relax Gaming", "98.00%", "2.00%", "NZ$12", "Bonus-round-only format, high volatility."],
   ["Golden Tour", "Playtech", "97.71%", "2.29%", "NZ$13.74", "Golf-themed, unusually high for Playtech."],
   ["White Rabbit Megaways", "Big Time Gaming", "97.00%+", "3.00%", "NZ$18", "High volatility Megaways."],
   ["<i>Typical NZ lobby average</i>", "&mdash;", "<i>~96.0%</i>", "4.00%", "<i>NZ$24</i>",
    "What you get by opening whatever is on the front page."]],
  caption="Return rates as published by the studio. Compare the fifth column with the last row: choosing "
          "Book of 99 over an average front-page pokie is worth about NZ$18 an hour at a NZ$1 stake. No "
          "casino choice on this site comes close to that.")}
<div class="prose">
{note('<p><b>The caveat that matters, and it is the whole point of this page.</b> These are the rates the '
      'studio publishes for the <i>top build</i>. Operators licence cut-down configurations of many of '
      'these same titles. A lobby can offer &ldquo;Blood Suckers&rdquo; at 96% rather than 98% and it is '
      'still Blood Suckers. <b>Open the game information panel and read the number before you stake '
      'anything</b> &mdash; it takes ten seconds and it is the only way to know which version you have. '
      '<a href="/online-pokies/#builds">How the builds work</a>.</p>', "warn")}
<h3>Why these titles are not on the front page</h3>
<p>You will notice the list skews old &mdash; Blood Suckers is from 2010, Mega Joker older still. That is
not nostalgia, it is economics. A 99% RTP pokie generates a quarter of the revenue per spin that a 96% one
does, so there is no commercial reason to promote it. High-RTP titles survive because a minority of
players seek them out, and they are found through the search box rather than the carousel.</p>
<p>Two practical consequences. First, <b>use the search function</b>, by exact title. Second, a lobby that
offers a <i>filter</i> for high-RTP games is telling you something genuine about its attitude to players
&mdash; very few do, and it costs them money to provide it.</p>
</div>''', ident="titles", haze=True)}
"""

    return shell(P, T, H1[P],
      "<p>Most pages targeting <b>best payout online casino NZ</b> publish a single payout percentage per "
      "casino. A casino does not have an RTP &mdash; its games do, and the spread between them is far "
      "wider than the spread between any two sites.</p>"
      "<p>So this page prices the games instead. House edge per hour by game type, how long RTP actually "
      "takes to appear, and the one thing a casino genuinely controls: which build of each pokie it runs.</p>",
      [("99.5%", "Blackjack, basic strategy"), ("96.5%", "Pokies, top build"),
       ("60&times;", "Cost per hour, pokies vs blackjack"), ("1M", "Spins before RTP is reliable")],
      f"Payout percentages &middot; {MONTH_YEAR}", A, C,
      [("Why casino payout percentage is fiction", "fiction"),
       ("What RTP means, and over what horizon", "rtp"),
       ("House edge by game", "edge"),
       ("Building a low house edge session", "build"),
       ("The highest RTP pokies, named", "titles"),
       ("Where the high RTP really is", "where")],
      body,
      [("What does RTP mean at a casino?",
        "<p>RTP meaning at a casino is return to player: the proportion of all stakes a game pays back over "
        "its lifetime. A 96% RTP leaves a 4% house edge. It is a long-run property of the game's maths, "
        "certified before release, and it says nothing about what will happen in your session.</p>"),
       ("What is RTP in pokies and casino games?",
        "<p>Return to player: the percentage of all money staked that a game returns over its lifetime. A "
        "96% pokie returns 96 cents per dollar wagered across millions of spins, leaving a 4% house edge. "
        "The figure is a long-run limit rather than a prediction &mdash; over a single session, variance "
        "swamps it entirely.</p>"),
       ("Which online casino has the best payout percentage in NZ?",
        "<p>The question contains a false premise. Payout percentage is a property of each game, not of a "
        "casino, and a site-wide figure is a weighted average across thousands of titles that says nothing "
        "about what you will play. The one genuine difference between casinos is which RTP build of each "
        "game they run &mdash; worth about NZ$20 per NZ$1,000 staked, and checkable in the game "
        "information panel in ten seconds.</p>"),
       ("What is a good RTP percentage?",
        "<p>For pokies, 96% and above is good and 94% or below is poor. For table games the bar is far "
        "higher: blackjack should return 99%+ with basic strategy, baccarat 98.9% on the banker bet, "
        "European roulette 97.3%. Anything advertised above 97% on a standard pokie deserves a check in "
        "the paytable before you believe it.</p>"),
       ("Does RTP matter in the short term?",
        "<p>Honestly, barely. Over a few hundred spins variance dominates so completely that a 94% game "
        "will often out-pay a 97% one. RTP describes what happens over hundreds of thousands of spins. "
        "Across a year of regular play it is very real and very expensive; across a Friday night it is "
        "noise.</p>"),
       ("What is the difference between house edge and RTP?",
        "<p>They are the same number stated from opposite ends. RTP is what comes back to players; house "
        "edge is what the operator keeps. A 96% RTP is a 4% house edge. House edge is generally the more "
        "useful framing because it multiplies cleanly: stake &times; number of bets &times; edge gives you "
        "the expected cost of a session.</p>"),
       ("Are loose pokies a real thing online?",
        "<p>In the land-based sense of a machine set deliberately generous to attract play, no. What is "
        "real is the RTP configuration: studios ship the same title at several return levels and operators "
        "choose. So &lsquo;loose&rsquo; online means &lsquo;the lobby licensed the top build&rsquo;, and "
        "that is verifiable rather than folklore.</p>")],
      [("How is casino RTP calculated?",
        "<p>By the studio, mathematically, from the game's own pay table and probability model, then "
        "verified by an independent testing laboratory before certification. It is a derived property of "
        "the game design rather than a measurement of recent results, which is why a game can be certified "
        "at 96% while paying out nothing for hours.</p>"),
       ("Is blackjack really better value than pokies?",
        "<p>Dramatically, on both measures. The house edge is roughly 0.5% against 3.5%, and blackjack "
        "takes about seventy decisions an hour against six hundred for pokies. Combined, that is around "
        "NZ$1.75 an hour versus NZ$105 at the same NZ$5 stake. The catch is bonus weighting: most welcome "
        "offers count blackjack at 10% or less.</p>"),
       ("Does the casino change the RTP of a game?",
        "<p>It cannot alter a certified game's maths, but it very often chooses between several certified "
        "versions the studio supplies at different return levels. That is a real decision made by the "
        "operator, it is not usually disclosed, and it is the single most useful thing to check before "
        "depositing.</p>"),
       ("Why do game shows have lower RTP than pokies?",
        "<p>Because the production cost is enormous &mdash; live studios, presenters, camera crews, "
        "physical equipment &mdash; and it is funded out of the return. Crazy Time and its relatives "
        "typically run 95&ndash;96%, and the bonus rounds that make them entertaining carry the widest "
        "variance in the whole category.</p>")],
      top, priority=0.9,
      toplist_h2="Best payout casinos NZ &mdash; audited on the builds they run",
      toplist_intro=("Our commercial order, disclosed as always. What we checked on each: which RTP "
                     "configuration the lobby runs on six headline titles, and whether the table game "
                     "selection includes single-zero roulette and 3:2 blackjack."),
      toplist_html=leaderboard(top, cta="Visit Casino"))


def crypto():
    P = "/best-crypto-casinos/"
    A, C = "rangi-solomon", "ihaka-nightingale"
    T = [("Crypto casinos", P)]
    top = pick(["spino", "kingdom", "crownslots", "smash", "rivo", "madcasino", "lucky-vibe", "fortune-play"])

    tax = table(
      ["What you did", "Is it a taxable event?", "Why"],
      [["Bought BTC with NZD from an exchange", "<b>No</b>",
        "Acquisition is not a disposal. But this is the moment your cost base is set, so record the date, "
        "the NZD amount and the fee."],
       ["Deposited that BTC to a casino", "<b>Generally no</b>",
        "A transfer between wallets you control is not a disposal. Keep the transaction hash."],
       ["Won 0.5 BTC playing pokies", "<b>No, on the gambling</b>",
        "Gambling winnings are not income for a recreational player. The crypto question is separate and "
        "arrives later."],
       ["Withdrew BTC back to your own wallet", "<b>Generally no</b>",
        "Still a transfer between your own wallets."],
       ["Converted that BTC to NZD", "<b>Yes &mdash; almost certainly</b>",
        "This is a disposal of property. The IRD's long-standing position is that cryptoassets acquired "
        "are generally acquired for the purpose of disposal, so the gain between your cost base and the "
        "NZD you received is taxable."],
       ["Used BTC directly to buy something", "<b>Yes</b>",
        "Spending crypto is a disposal at market value on the day, exactly as if you had sold it for cash "
        "first."]],
      caption="Indicative only and not tax advice &mdash; your circumstances decide the answer and the IRD "
              "is the authority. The point of the table is that the taxable moment is the conversion back "
              "to New Zealand dollars, not the gambling, and it catches people who were told gambling "
              "winnings are tax free and stopped reading there.")

    rails = table(
      ["Coin", "Typical settlement", "Network fee", "Price volatility while you hold it", "Best for"],
      [["<b>USDT</b> (Tether)", "2&ndash;15 min", "Low on TRON, high on Ethereum",
        "<b>Effectively none</b> &mdash; pegged to USD", "Almost everybody. The sane default."],
       ["<b>USDC</b>", "2&ndash;15 min", "Low on Solana or Base",
        "Effectively none", "Same as USDT, better regulated issuer"],
       ["Bitcoin (BTC)", "10&ndash;60 min", "Moderate to high, varies with congestion",
        "<b>High</b>", "Players who already hold BTC"],
       ["Ethereum (ETH)", "1&ndash;5 min", "High on mainnet, low on layer 2",
        "High", "Players already in the ETH ecosystem"],
       ["Litecoin (LTC)", "2&ndash;10 min", "Very low",
        "High", "Cheap, fast transfers without stablecoin exposure"],
       ["Dogecoin (DOGE)", "1&ndash;5 min", "Very low",
        "<b>Extreme</b>", "Honestly, very little"]],
      caption="The column most guides omit is the fourth. A volatile coin sitting in a casino balance is an "
              "unhedged currency position you did not intend to take &mdash; you can win at the tables and "
              "still finish the week down.")

    body = f"""
{sec(f'''{sechead("The crypto casino problem nobody puts on the page: tax",
  "Gambling winnings are tax free in New Zealand. Crypto is property. Those two facts collide.", 2, "tax")}
<div class="prose">
<p>Every crypto casino NZ page will tell you that gambling winnings are not taxable in New Zealand. That is
true, and it is not the part that catches people.</p>
<p>The Inland Revenue Department treats <b>cryptoassets as property</b>, not as currency. Its long-standing
position is that crypto is generally acquired for the purpose of disposal, which makes a gain on disposal
taxable income. And a disposal includes <b>converting your crypto back into New Zealand dollars</b>.</p>
<p>So the sequence that catches people is this. You buy USDT at one price, deposit it, gamble &mdash;
tax-free, correctly &mdash; withdraw your USDT, and convert to NZD. The gambling created no tax liability.
<b>The conversion may well have.</b> And because the gambling was tax-free, most players never think to
track a cost base at all.</p>
</div>
{tax}
<div class="prose">
{note('<p><b>The practical advice, which is boring and worth following.</b> Keep a record of every '
      'acquisition: date, amount, NZD value and fee. Keep the transaction hashes for deposits and '
      'withdrawals. If you use a stablecoin such as USDT or USDC, the gain between acquisition and '
      'conversion is usually small &mdash; which is a genuine and rarely-mentioned argument for '
      'stablecoins over Bitcoin for this specific purpose. If the amounts are material, talk to an '
      'accountant rather than an affiliate site. '
      '<a href="/gambling-winnings-tax-nz/">More on the tax position</a>.</p>', "warn")}
</div>''', ident="tax")}

{sec(f'''{sechead("Which coin to actually use", None, 2, "coins")}
<div class="prose">
<p>Most crypto casino guides list the accepted coins and stop. The choice between them has real
consequences &mdash; on settlement speed, on fees, and above all on whether your balance is still worth
what it was when you deposited it.</p>
</div>
{rails}
<div class="prose">
<h3>The volatility point, because it is the one that costs money</h3>
<p>If you deposit NZ$1,000 of Bitcoin on Monday and withdraw the same quantity of Bitcoin on Friday having
broken exactly even at the tables, you have not broken even. You have taken a five-day unhedged position in
a volatile asset. It might be worth NZ$1,080. It might be worth NZ$920. Neither outcome has anything to do
with how you played.</p>
<p><b>Stablecoins remove this entirely</b>, which is why USDT and USDC are the sensible default for casino
play even for people who hold other crypto. Your balance means what it says, your bonus arithmetic stays
valid, and your tax position is far simpler because the gain on conversion is close to nil.</p>
<h3>Network fees, briefly</h3>
<p>The same coin can cost wildly different amounts to move depending on the network. USDT on TRON costs
cents; USDT on Ethereum mainnet can cost more than a small deposit is worth. When a casino offers a choice
of network, it matters more than the choice of coin. If you are depositing under NZ$100, check the fee
before you send &mdash; it is entirely possible to pay 15% of a small deposit in gas.</p>
</div>''', ident="coins", haze=True)}

{sec(f'''{sechead("Crypto bonuses are structurally better, and here is why")}
<div class="prose">
<p>An unusual case where the marketing and the arithmetic agree. Crypto-specific welcome packages in this
market genuinely tend to carry <b>lower wagering multipliers</b> than the equivalent fiat offer, and the
only 0x wagering offer we have been able to verify for New Zealand players is a crypto one.</p>
<p>The reason is unglamorous: crypto deposits are cheaper for the operator. No card scheme fees, no
chargeback risk, no acquiring bank taking a percentage and no failed-payment attrition. Some of that saving
is passed through as better terms because it is the cheapest way to compete.</p>
<p><a href="/casino-reviews/spino/">Spino</a>&rsquo;s crypto package runs at <b>0x</b> &mdash; winnings
withdrawable immediately, no turnover requirement. Priced against the rest of the market, where a typical
40x offer on a NZ$5,000 bonus demands NZ$200,000 of turnover at an expected cost of NZ$8,000, that is not
a marginal difference. It is the difference between an offer that is worth its face value and one that
costs more than it gives.</p>
<p><a class="btn btn--ghost" href="/online-casinos/bonuses/">Every bonus priced in turnover &rarr;</a></p>
</div>''', ident="bonuses")}

{sec(f'''{sechead("Provably fair, explained without the marketing")}
<div class="prose">
<p>&ldquo;Provably fair&rdquo; is used as a trust badge across this category and it is a genuine
cryptographic technique that is also routinely oversold. Worth understanding precisely what it does and
does not prove.</p>
<h3>What it actually is</h3>
<p>Before a round, the casino generates a random seed and publishes a cryptographic hash of it &mdash; a
fingerprint that cannot be reversed but that commits them to that exact seed. You supply a seed of your
own. The outcome is computed from both. Afterwards the casino reveals its seed, and you can verify that it
hashes to the fingerprint published beforehand.</p>
<p><b>What that proves:</b> the operator did not change the result after seeing your bet. That is a real
guarantee and it is more than a conventional RNG offers.</p>
<h3>What it does not prove</h3>
<ul>
<li><b>It does not make the game fair in the ordinary sense.</b> A provably fair game can have a 20% house
edge. The mechanism proves the outcome was not tampered with, not that the odds are reasonable.</li>
<li><b>It only covers games built for it</b> &mdash; dice, crash, plinko, limbo and similar in-house
titles. Third-party pokies from Pragmatic Play or Play&rsquo;n GO are not provably fair; they are
conventionally certified by a testing laboratory instead. A site can advertise &ldquo;provably fair&rdquo;
while almost everything in its lobby is not.</li>
<li><b>It says nothing about whether you will be paid.</b> The overwhelming majority of real complaints in
this industry concern withdrawals, terms and account closures &mdash; none of which provable fairness
touches.</li>
</ul>
{note('<p><b>The honest summary.</b> Provably fair is a good property and a poor proxy for trustworthiness. '
      'A named operating company, a licence that resolves on the regulator&rsquo;s register and published '
      'withdrawal limits tell you far more about whether you will see your money.</p>', "info")}
</div>''', ident="fair")}

{sec(f'''{sechead("Depositing crypto at a casino, step by step")}
{steps([
  ("Decide on the coin and the network first",
   "USDT on TRON is the pragmatic default for most people: fast, cents to move, and no price exposure "
   "while your balance sits. Whatever you choose, the network must match at both ends."),
  ("Buy from a New Zealand exchange and record the cost base",
   "Easy Crypto, Independent Reserve and Binance all serve New Zealand customers. Record the date, the "
   "NZD spent and the quantity received &mdash; this is the number you will need when you convert back."),
  ("Copy the deposit address from the casino cashier, and check the network label",
   "The single most expensive mistake in crypto is sending on the wrong network. USDT-TRC20 sent to an "
   "ERC20 address is generally unrecoverable. Casinos show the network next to the address; match it "
   "exactly."),
  ("Send a small test amount first",
   "On any new site, and on any new address. A NZ$20 test costs cents in fees and eliminates the only "
   "irreversible risk in the process."),
  ("Confirm it credited before depositing the rest",
   "Most casinos credit after one to three network confirmations. If a test deposit does not arrive "
   "within the expected window, stop and contact support before sending more."),
  ("Verify your account now, not later",
   "Crypto casinos still have KYC obligations and will apply them at withdrawal. Completing verification "
   "before you have winnings removes the longest delay in the payout process."),
])}''', ident="how", haze=True)}

{sec(f'''{sechead("Bitcoin casinos, altcoins and the practical questions", None, 2, "practical")}
<div class="prose">
<h3>Bitcoin casino NZ and bitcoin gambling NZ</h3>
<p>Bitcoin gambling NZ side is lawful for the player and widely supported. A bitcoin casino NZ account
behaves like any other except that settlement is faster and the balance moves in value while you hold it.
The best bitcoin casino NZ 2026 option among the sites we cover is
<a href="/casino-reviews/kingdom/">Kingdom</a>, which pairs crypto rails with NZD banking. Bitcoin pokies
NZ are simply ordinary pokies funded in BTC &mdash; the coin has no effect on the game maths.</p>
<h3>Are crypto casinos legal in NZ?</h3>
<p>Yes for the player, on exactly the same footing as any offshore casino. Crypto casinos New Zealand
players can reach operate under offshore licences until the domestic regime opens in 2027.</p>
<h3>Ethereum, USDT, Litecoin and Dogecoin</h3>
<p>An ethereum casino NZ deposit is fast but can be expensive on mainnet; use a layer 2 where offered. A
usdt casino NZ deposit is the pragmatic default &mdash; pegged value, cents to move on TRON. Litecoin
casino NZ transfers are cheap and quick but price-volatile. A dogecoin casino NZ deposit is all of the
volatility with none of the advantages, and we would not recommend it for this purpose.</p>
<h3>How to deposit bitcoin at an online casino NZ side</h3>
<p>Buy from a New Zealand exchange, record the cost base, copy the deposit address from the cashier,
<b>match the network exactly</b>, and send a small test first. How to withdraw crypto from an online casino
NZ side is the same process reversed, and the crypto casino minimum deposit NZ players face is usually the
NZD equivalent of NZ$10 to NZ$30.</p>
<h3>Speed, conversion and anonymity</h3>
<p>The fastest crypto withdrawal casino NZ experience is a verified account withdrawing stablecoin, which
lands in minutes &mdash; instant withdrawal crypto casino NZ claims are roughly accurate for once. Crypto
vs bank transfer casino withdrawals is not a close contest: minutes against days. A crypto casino with NZD
conversion holds your balance in dollars and removes the price risk, at the cost of a conversion spread.
An anonymous casino NZ side is a partial thing only &mdash; identity checks still arrive at withdrawal.</p>
<h3>Crypto bonuses</h3>
<p>A crypto casino welcome bonus NZ players are offered tends to carry lower wagering than the fiat
equivalent, for the reasons above. A crypto casino no deposit bonus NZ side does exist but is rare and
carries the same maximum-cashout structure as any other no deposit offer.</p>
</div>''', ident="practical")}

{sec(f'''{sechead("KYC at a crypto casino: what anonymity actually gets you", None, 2, "kyc")}
<div class="prose">
<p>Crypto casinos are marketed on privacy, and the marketing outruns the reality in a way worth
understanding before you deposit.</p>
<h3>What is true</h3>
<p>Registration is genuinely lighter. Many crypto casinos open an account on an email address alone, with
no name, no address and no document upload. You can deposit and play within minutes, and for small-stakes
recreational play you may never be asked for anything else.</p>
<h3>What is not</h3>
<p><b>Identity obligations arrive at withdrawal, not at signup.</b> Any operator holding a licence worth
having carries anti-money-laundering duties, and those bite hardest on the way out &mdash; particularly on
a large win, a rapid deposit pattern, or a withdrawal to a different wallet than the one that funded the
account.</p>
<p>The practical outcome is the worst of both worlds if you are unprepared: you register anonymously, play
happily for months, win, and only then discover that a full verification pack is required &mdash; at the
exact moment you want the money. That sequence is the single largest source of complaints in this industry
and it is not unique to crypto. <a href="/fast-payout-casinos/#sof">The full source-of-funds explanation,
with the document pack to prepare</a>.</p>
<h3>The crypto-specific wrinkle</h3>
<p>Source-of-funds checks are <i>harder</i> to satisfy with crypto, not easier. A casino asking where your
money came from wants a paper trail, and "I bought it on an exchange in 2021" needs exchange records to
support it. Keep your acquisition records &mdash; the same ones you need for the IRD &mdash; and the
verification request becomes an inconvenience rather than a crisis.</p>
{note('<p><b>A genuinely anonymous casino is a casino with no licence.</b> If no verification is ever '
      'required at any withdrawal size, no regulator is supervising the operator, and you have no '
      'escalation route whatsoever if a payment is refused. That is a much larger risk than being asked '
      'for a power bill.</p>', "warn")}
</div>''', ident="kyc", haze=True)}
"""

    return shell(P, T, H1[P],
      "<p>Crypto casinos settle faster and carry structurally better bonus terms &mdash; the only 0x "
      "wagering offer we can verify for New Zealanders is a crypto one. Both of those are real advantages "
      "and both are well covered elsewhere.</p>"
      "<p>What is not covered anywhere is the tax. Gambling winnings are tax free in New Zealand; the IRD "
      "treats crypto as <b>property</b>, so converting your winnings back to NZD can be a taxable disposal "
      "quite separately from the gambling. That collision is the most important thing on this page.</p>",
      [("0x", "Wagering on the best crypto offer"), ("2&ndash;15 min", "Stablecoin settlement"),
       ("Property", "How the IRD classifies crypto"), ("USDT", "The sane default coin")],
      f"Crypto casinos &middot; {MONTH_YEAR}", A, C,
      [("The tax problem nobody mentions", "tax"),
       ("Which coin to actually use", "coins"),
       ("Why crypto bonuses are better", "bonuses"),
       ("Provably fair, explained honestly", "fair"),
       ("KYC and anonymity", "kyc"),
       ("How to deposit crypto safely", "how")],
      body,
      [("Is a bitcoin casino NZ players use any different from a normal one?",
        "<p>Only in the rails and the terms. The games, licences and withdrawal policies are the same. "
        "Bitcoin gambling NZ side settles faster and often carries lower wagering, and it adds one thing a "
        "fiat account does not have: a price exposure on your balance, plus a tax question on conversion "
        "back to New Zealand dollars.</p>"),
       ("Are crypto casinos legal in New Zealand?",
        "<p>Playing at one is lawful for you, exactly as with any offshore online casino &mdash; New "
        "Zealand law binds operators and advertisers, not players. Crypto itself is entirely legal to buy, "
        "hold and use. The complication is not legality, it is tax: the IRD treats cryptoassets as "
        "property, so disposing of them, including by converting back to NZD, can create a tax liability.</p>"),
       ("Do you pay tax on crypto casino winnings in NZ?",
        "<p>Not on the gambling itself &mdash; recreational gambling winnings are not income in New "
        "Zealand. But the crypto is a separate asset, and converting it back to New Zealand dollars is a "
        "disposal of property which may well be taxable on any gain since you acquired it. Using a "
        "stablecoin keeps that gain close to zero, which is a genuine reason to prefer USDT or USDC.</p>"),
       ("What is the best crypto casino for NZ players?",
        "<p>On bonus terms, <a href='/casino-reviews/spino/'>Spino</a> &mdash; the only 0x wagering "
        "welcome package we have verified, which makes it the only offer in this market worth its face "
        "value. If you want crypto speed alongside ordinary New Zealand payment methods and NZD banking, "
        "<a href='/casino-reviews/kingdom/'>Kingdom</a> is the better all-round choice.</p>"),
       ("Which crypto is best for online casino deposits?",
        "<p>A stablecoin, for almost everybody &mdash; USDT or USDC, ideally on a cheap network such as "
        "TRON, Solana or Base. Settlement is a few minutes, fees are cents, and crucially your balance "
        "does not move in value while you play. Depositing Bitcoin means taking an unhedged currency "
        "position alongside your gambling, and the two outcomes are unrelated.</p>"),
       ("How fast are crypto casino withdrawals?",
        "<p>Once your account is verified, typically two to fifteen minutes for stablecoins and ten to "
        "sixty for Bitcoin &mdash; the fastest rail in the market by a wide margin. The delays that "
        "actually matter are verification, which is a one-off, and the weekly withdrawal cap, which crypto "
        "does not exempt you from. <a href='/fast-payout-casinos/'>How the withdrawal clock works</a>.</p>"),
       ("What does provably fair mean?",
        "<p>A cryptographic method where the casino commits to a random seed in advance by publishing its "
        "hash, so you can verify afterwards that the result was not altered once your bet was placed. It "
        "proves the outcome was not tampered with. It does not prove the odds are good, it only covers "
        "in-house games such as dice and crash, and it says nothing about whether you will be paid.</p>")],
      [("Can I stay anonymous at a crypto casino?",
        "<p>Partially at best, and less than the marketing implies. Many crypto casinos let you register "
        "and play with only an email address, but licensed operators still carry identity obligations and "
        "will apply them when you withdraw a meaningful sum. Treat anonymity as a convenience during "
        "signup rather than a property of the account.</p>"),
       ("What happens if I send crypto on the wrong network?",
        "<p>Usually it is lost permanently. USDT sent on TRC20 to an ERC20 address, or a coin sent to an "
        "address for a different chain, is generally unrecoverable and no support desk can reverse it. "
        "This is the one genuinely irreversible risk in the process, which is why a small test transaction "
        "on any new address is always worth the few cents it costs.</p>"),
       ("Do crypto casinos convert to NZD?",
        "<p>Some hold your balance in the coin you deposited; others convert to a fiat display currency at "
        "deposit and back at withdrawal, which reintroduces a conversion spread. Neither is wrong, but "
        "they behave differently &mdash; a coin-denominated balance moves with the market while you play, "
        "a converted one does not. Check which model a site uses before depositing a volatile coin.</p>"),
       ("Are crypto casino bonuses better than regular ones?",
        "<p>Structurally, yes, and unusually the marketing is accurate here. Crypto deposits cost the "
        "operator far less to process &mdash; no card fees, no chargebacks &mdash; and some of that saving "
        "reaches the player as lower wagering multipliers. The only 0x offer we have verified in this "
        "market is crypto-only.</p>")],
      top, priority=0.9,
      toplist_h2="Best crypto casinos NZ &mdash; ranked with the tax position attached",
      toplist_intro=("Our commercial order, disclosed as always. What we checked: coins and networks "
                     "supported, settlement times from a verified account, whether balances are held in "
                     "coin or converted, and the wagering terms on the crypto-specific offer."),
      toplist_html=leaderboard(top, cta="Visit Casino"))


def live():
    P = "/live-casinos/"
    A, C = "camille-toure", "nikau-broughton"
    T = [("Live casinos", P)]
    top = pick(["ivibet", "kingdom", "spinjo", "lucky-vibe", "madcasino", "rivo", "smash", "fortune-play"])

    tz = table(
      ["Time in New Zealand", "Time in Malta / Latvia (studio hours)", "What the floor looks like"],
      [["6:00pm NZT", "7:00am CET", "Thinnest of the day. Overnight dealers finishing, European players "
        "asleep. Fewest tables open, longest waits for a seat at popular limits."],
       ["9:00pm NZT", "10:00am CET", "Filling up. European morning shift fully staffed; most advertised "
        "tables are genuinely open by now."],
       ["12:00am NZT", "1:00pm CET", "Strong. Full European daytime floor, widest limit range, all game "
        "shows running."],
       ["3:00am NZT", "4:00pm CET", "Peak. Everything the studio has is open."],
       ["9:00am NZT", "10:00pm CET", "European prime time. Excellent floor, but an unusual hour to be "
        "playing from Auckland."],
       ["1:00pm NZT", "2:00am CET", "Declining into the overnight skeleton floor."]],
      caption="Live studios serve a European clock. New Zealand evening play &mdash; 6pm to 11pm NZT &mdash; "
              "lands squarely in the European small hours, which is the thinnest part of the day. This is "
              "the single most important practical fact about live casino NZ play and we have not seen it "
              "stated anywhere else.")

    ledge = table(
      ["Live game", "House edge", "Rounds per hour", "Cost per hour at NZ$10", "Bonus weighting, typical"],
      [["Live blackjack, basic strategy", "<b>0.5%</b>", "~60", "<b>NZ$3</b>", "<b>5% or excluded</b>"],
       ["Live baccarat, banker", "1.06%", "~70", "NZ$7.40", "10% or excluded"],
       ["Live roulette, single zero", "2.70%", "~45", "NZ$12.15", "10%"],
       ["Lightning Roulette", "2.99%", "~40", "NZ$12", "10%"],
       ["Live three card poker", "3.37%", "~55", "NZ$18.50", "10%"],
       ["Crazy Time", "~4.0%", "~30", "NZ$12", "0&ndash;10%"],
       ["Monopoly Live", "~3.8%", "~28", "NZ$10.60", "0&ndash;10%"],
       ["Dream Catcher", "~4.2%", "~35", "NZ$14.70", "0&ndash;10%"]],
      caption="Live dealer games are the cheapest entertainment in an online casino per round and among "
              "the worst possible choices for clearing a welcome bonus. Both facts follow from the same "
              "cause: the house edge is low, so operators refuse to let the wagering requirement be "
              "satisfied there.")

    body = f"""
{sec(f'''{sechead("Live casino runs on a European clock, and you do not",
  "The most practical thing to know about playing live dealer games from New Zealand.", 2, "timezone")}
<div class="prose">
<p>Live dealer games are not software. They are a television production, streamed from physical studios
staffed by physical people &mdash; overwhelmingly in Malta, Latvia, Georgia and Romania. Those studios
scale their floor to European demand, because that is where the audience is.</p>
<p>New Zealand is 10 to 11 hours ahead of Central European Time. <b>Your evening is their small hours.</b>
When you sit down at 8pm in Auckland it is 9am in Riga and the floor is running its thinnest shift of the
day. Tables that a comparison page counted at European peak are simply not open.</p>
</div>
{tz}
<div class="prose">
{note('<p><b>What this means in practice.</b> Counts of &ldquo;250+ live tables&rdquo; are real numbers '
      'captured at the wrong time of day. If you play live in the New Zealand evening, the number you want '
      'is how many tables are open at 9pm NZT &mdash; which is generally between a half and two-thirds of '
      'the advertised figure, concentrated in the mainstream games. Blackjack at your preferred limit is '
      'the first thing to disappear and the last to come back.</p>', "info")}
<p>Two workarounds worth knowing. First, <b>late evening is better than early evening</b> &mdash; 11pm NZT
is materially better staffed than 6pm, because Europe has woken up. Second, some operators run
<b>dedicated tables</b> that are open on their own schedule rather than the studio&rsquo;s general floor,
and those are more reliably available.</p>
</div>''', ident="timezone")}

{sec(f'''{sechead("Why live players should decline almost every welcome bonus", None, 2, "bonus")}
<div class="prose">
<p>If you take one thing from this page, take this one, because it is worth more money than any casino
choice you could make.</p>
<p>Wagering requirements are satisfied at different rates by different games. Pokies contribute 100% of
every dollar staked. <b>Live blackjack typically contributes 5%, and is frequently excluded outright.</b>
Live roulette and baccarat usually contribute 10%.</p>
<p>Run the arithmetic on a normal offer. A NZ$500 bonus at 40x requires NZ$20,000 of turnover. Cleared on
pokies, that is NZ$20,000 of pokie spins. Cleared on live blackjack at 5% weighting, you must stake
<b>NZ$400,000</b> to satisfy the same requirement.</p>
<p class="lead">A 40x bonus is really an <b>800x</b> bonus if you are a live blackjack player.</p>
<p>And the excluded case is worse than the weighted one, because it is silent: staking on an excluded game
contributes nothing at all toward the requirement, while the bonus expiry clock continues to run. Players
routinely discover this at the end of thirty days having made no progress whatsoever.</p>
{note('<p><b>The correct move, stated plainly.</b> If you primarily play live dealer games, <b>decline the '
      'welcome bonus.</b> Your deposit stays withdrawable, no weighting table applies, no maximum bet rule '
      'can void your winnings, and you are free to play the lowest house edge games in the building &mdash; '
      'which is precisely what the bonus was designed to prevent. We are paid commission on bonus claims '
      'and we are still telling you to decline, because the arithmetic is not close.</p>', "warn")}
</div>''', ident="bonus", haze=True)}

{sec(f'''{sechead("What live games actually cost per hour")}
<div class="prose">
<p>Live dealer play has a reputation for being expensive. Per round it is the opposite &mdash; the cheapest
thing in an online casino, because human dealing is slow and slowness is your friend when every round
carries a house edge.</p>
</div>
{ledge}
<div class="prose">
<p>Compare the fourth column with a pokie. Live blackjack at NZ$10 a hand costs about <b>NZ$3 an hour</b>.
A pokie at NZ$1 a spin costs about <b>NZ$24 an hour</b>, and at NZ$5 a spin about NZ$105. The live table
asks for a much larger minimum bet and takes far less of your money, because it makes sixty decisions an
hour instead of six hundred.</p>
<p>This is the single most counter-intuitive fact in online gambling and almost nobody publishes it: the
games that feel expensive are cheap, and the games that feel cheap are expensive.</p>
</div>''', ident="cost")}

{sec(f'''{sechead("Who actually supplies the floor")}
<div class="prose">
<p>Almost every live casino NZ players can reach is served by one of a small number of studios, and the
casino&rsquo;s branding tells you nothing about which. Worth knowing the difference.</p>
<h3>Evolution</h3>
<p>The dominant supplier, and the one behind most of the games people name &mdash; Lightning Roulette,
Crazy Time, Monopoly Live, Dream Catcher, Immersive Roulette, and the bulk of mainstream blackjack and
baccarat. Production quality is the benchmark, table counts are the deepest, and limits run from a couple
of dollars to five figures. If a site advertises &ldquo;Evolution tables&rdquo;, that is genuine signal.</p>
<h3>Pragmatic Play Live</h3>
<p>The strongest challenger, and often better at the lower limits &mdash; Mega Wheel, Sweet Bonanza
Candyland and a solid roulette and blackjack range. Frequently the better option for a small-stakes New
Zealand player because the minimums start lower.</p>
<h3>Playtech, Ezugi and the rest</h3>
<p>Smaller floors, fewer game shows, but often the more approachable table limits. Ezugi in particular
tends to carry very low minimums, which matters more to most players than a fourth variant of roulette.</p>
{note('<p><b>The white-label problem.</b> A site advertising &ldquo;250+ live tables&rdquo; may be counting '
      'every table across several aggregated suppliers, including regional tables restricted by '
      'geography that a New Zealand account cannot open at all. The number to trust is what you can see in '
      'the lobby, filtered by provider, at the hour you actually play.</p>', "warn")}
</div>''', ident="studios")}

{sec(f'''{sechead("Choosing a live casino from New Zealand")}
{steps([
  ("Open the lobby at 9pm NZT before you deposit",
   "Most sites let you browse the live section without funding an account. Count what is genuinely open "
   "and joinable at the hour you intend to play, not what the marketing claims at European peak."),
  ("Check the minimum bet, not the maximum",
   "Live tables carry higher minimums than pokies &mdash; typically NZ$1 to NZ$5, sometimes NZ$10. A "
   "NZ$100 bankroll behaves completely differently at a NZ$1 table than a NZ$5 one, and the limit range "
   "matters far more than the table count."),
  ("Look for single-zero roulette and 3:2 blackjack",
   "Double-zero roulette costs nearly twice the house edge of single zero. Blackjack paying 6:5 rather "
   "than 3:2 costs about 1.4% extra. Both variants exist online and both exist to catch people who did "
   "not check."),
  ("Confirm the currency at the table",
   "A euro-denominated site means euro-denominated table limits, so a &lsquo;&euro;1 minimum&rsquo; is "
   "NZ$1.96 and your balance converts twice across the round trip. On live play, where sessions are long "
   "and stakes higher, the spread adds up."),
  ("Decline the bonus if live is your main game",
   "Covered above and worth repeating because it is the most expensive mistake available in this category."),
])}''', ident="choosing", haze=True)}

{sec(f'''{sechead("Live dealer games from New Zealand: the practical round-up", None, 2, "games")}
<div class="prose">
<h3>Live blackjack NZ</h3>
<p>The best value on any live floor &mdash; about 0.5% house edge with correct basic strategy. Live dealer
blackjack online NZ real money tables start around NZ$1 to NZ$5. The catch is bonus weighting at 5% or
exclusion, covered above.</p>
<h3>Live roulette NZ and Lightning Roulette</h3>
<p>Always choose single zero: 2.7% against 5.26% on the double-zero table. Lightning roulette NZ side adds
random multipliers at the cost of a slightly higher edge of about 2.99%, which is a fair price for the
mechanic. The best live roulette site NZ players can use is whichever runs single-zero tables at limits
you like.</p>
<h3>Live baccarat NZ</h3>
<p>Live baccarat NZ tables carry a 1.06% edge on the banker bet and require no strategy whatsoever, which
makes it the highest-return game that cannot be played incorrectly. Never take the tie bet &mdash; it runs
above 14%.</p>
<h3>Crazy Time NZ and Monopoly Live NZ</h3>
<p>Crazy Time NZ side runs around a 4% edge with enormous variance; Monopoly Live NZ is similar at about
3.8%. Both are genuinely entertaining and both are entertainment priced by the hour rather than value
plays.</p>
<h3>Evolution Gaming casinos NZ</h3>
<p>Evolution gaming casinos NZ players will recognise supply most of the games named above. A site
advertising Evolution tables is telling you something real about production quality and floor depth.
Pragmatic Play Live is the strongest alternative and often better at low limits.</p>
<h3>Live casino vs RNG games</h3>
<p>Live casino vs RNG games comes down to speed and cost. Live is roughly ten times slower, which makes it
far cheaper per hour at the same stake, and the low-edge games are all there. RNG games are faster, start
at lower minimums, never queue and contribute fully toward bonus wagering.</p>
<h3>Live casino with NZD tables, minimum bets and apps</h3>
<p>A live casino with NZD tables is one that holds your balance in New Zealand dollars &mdash; limits are
denominated in the account currency, so a euro site quotes euro minimums. Live casino minimum bet NZ side
is typically NZ$1 to NZ$5. A live casino app NZ players need does not really exist and is not needed: the
streams run in a mobile browser at the same quality.</p>
</div>''', ident="games", haze=True)}

{sec(f'''{sechead("Live casino versus RNG games: the honest comparison", None, 2, "vs")}
<div class="prose">
<p>Competitor pages run this comparison and reach a conclusion about atmosphere. The answer that matters is
about cost, and it is counter-intuitive enough to be worth stating plainly.</p>
</div>
{proscons(
  ["<b>Far cheaper per hour.</b> Roughly 60 decisions an hour against 600 for pokies, so the same stake "
   "buys ten times less exposure to the house edge",
   "<b>The lowest-edge games are all here</b> &mdash; blackjack at 0.5%, baccarat banker at 1.06%, "
   "single-zero roulette at 2.7%",
   "Physical outcomes, filmed from several angles and watched by hundreds of players simultaneously",
   "No possibility of a cut-down RTP build &mdash; a real deck is a real deck",
   "Basic strategy actually works, and is worth about 1.5% against playing by instinct",
   "Sociable, and the pace makes it much harder to lose track of time or spend"],
  ["<b>Almost useless for clearing a bonus</b> &mdash; 5% weighting or outright exclusion is standard",
   "Higher minimum bets: NZ$1&ndash;5 at a live table against NZ$0.10 on a pokie",
   "Table availability collapses in the New Zealand evening, which is Europe&rsquo;s small hours",
   "You can be queued out of a full table at popular limits",
   "No demo mode &mdash; every hand is real money",
   "Euro-denominated sites quote euro limits, so a &lsquo;&euro;1 table&rsquo; is NZ$1.96"])}
<div class="prose">
<p class="lead"><b>The summary:</b> live blackjack at NZ$10 a hand costs about NZ$3 an hour. A pokie at
NZ$1 a spin costs about NZ$24. The game that demands a bigger minimum bet takes far less of your money,
because it asks for it ten times less often.</p>
<h3>Live dealer game statistics, at a glance</h3>
</div>
{table(["Game", "House edge", "Rounds/hour", "Min bet, typical", "Best bet", "Worst bet on the same table"],
  [["Blackjack", "<b>0.50%</b>", "~60", "NZ$1&ndash;5", "Main hand, basic strategy",
    "Insurance (~7%) and side bets (4&ndash;12%)"],
   ["Baccarat", "1.06%", "~70", "NZ$1&ndash;5", "Banker", "Tie (~14.4%)"],
   ["Roulette (single zero)", "2.70%", "~45", "NZ$0.50&ndash;2", "Any bet &mdash; all carry the same edge",
    "The American double-zero table (5.26%)"],
   ["Lightning Roulette", "2.99%", "~40", "NZ$0.50", "Straight-up, for the multipliers", "&mdash;"],
   ["Three card poker", "3.37%", "~55", "NZ$1", "Ante and play", "Pair Plus"],
   ["Crazy Time", "~4.0%", "~30", "NZ$0.10", "Top slot alignment is luck, not strategy",
    "Chasing a single bonus segment"]],
  caption="The right-hand column is where most live-table losses actually come from. Side bets carry house "
          "edges ten to twenty times the main game they are attached to, on the cheapest table in the "
          "building.")}''', ident="vs")}
"""

    return shell(P, T, H1[P],
      "<p>Live dealer tables are a television production on a European clock, and New Zealand&rsquo;s "
      "evening is Europe&rsquo;s small hours. The table counts on every comparison page were captured at "
      "the wrong time of day for you.</p>"
      "<p>This page covers what is actually open at 9pm NZT, what each live game costs per hour &mdash; "
      "live blackjack is the cheapest entertainment in the building at around NZ$3 &mdash; and why a live "
      "player should almost always <b>decline</b> the welcome bonus.</p>",
      [("NZ$3", "Live blackjack, per hour at NZ$10"), ("800x", "A 40x bonus at 5% weighting"),
       ("10&ndash;11h", "New Zealand ahead of the studios"), ("9pm", "When the floor starts filling")],
      f"Live dealer &middot; {MONTH_YEAR}", A, C,
      [("The timezone problem", "timezone"),
       ("Why live players should decline bonuses", "bonus"),
       ("What live games cost per hour", "cost"),
       ("Live versus RNG, compared", "vs"),
       ("Who supplies the floor", "studios"),
       ("Choosing a live casino", "choosing")],
      body,
      [("What is the best live dealer casino NZ players can use?",
        "<p>For a live dealer casino NZ side the test that matters is how many tables are genuinely open at "
        "9pm NZT, not the advertised count. The best live casino sites New Zealand players can reach on "
        "that measure are the ones carrying both Evolution and Pragmatic Play Live, which keeps the floor "
        "staffed across more of the European day.</p>"),
       ("What is the best live casino in NZ?",
        "<p>On floor depth at New Zealand-evening hours, <a href='/casino-reviews/ivibet/'>Ivibet</a> and "
        "<a href='/casino-reviews/kingdom/'>Kingdom</a> held the most genuinely joinable tables at 9pm NZT "
        "in our checks. If you want the lowest table minimums rather than the largest floor, look for "
        "sites carrying Pragmatic Play Live and Ezugi rather than Evolution alone.</p>"),
       ("How does a live casino work?",
        "<p>A real dealer runs a real table in a studio, filmed by multiple cameras and streamed to you in "
        "real time. Your bets are placed through an interface overlaid on the video, and optical character "
        "recognition reads the physical cards, wheel or dice to settle them. There is no RNG involved in "
        "the outcome &mdash; the cards and the ball are physical.</p>"),
       ("Is live casino better than RNG games?",
        "<p>Different rather than better, though on cost per hour live wins comfortably. Live games are "
        "much slower, which means far less exposure to the house edge for the same stake, and the low-edge "
        "games are all there. RNG games are faster, available at lower minimums, never queue, and "
        "contribute fully toward bonus wagering. If you are clearing a bonus, RNG; if you are playing for "
        "entertainment, live is cheaper per hour.</p>"),
       ("What are the minimum bets at live casino tables in NZ?",
        "<p>Typically NZ$1 to NZ$5 at mainstream tables, dropping to around NZ$0.50 on some Pragmatic Play "
        "and Ezugi roulette, and rising to NZ$10 or more at premium and VIP tables. That is considerably "
        "higher than pokies, which start around NZ$0.10 &mdash; but because live play is roughly ten times "
        "slower, the cost per hour is still far lower.</p>"),
       ("Can I play live blackjack for real money in New Zealand?",
        "<p>Yes, at every casino on this page, and it is the single best-value game they offer &mdash; "
        "about 0.5% house edge with correct basic strategy. The one thing to watch is bonus weighting: "
        "live blackjack usually counts 5% or nothing toward wagering requirements, so claim a welcome "
        "offer and you have effectively locked yourself out of the best game in the building.</p>"),
       ("Do live casinos have NZD tables?",
        "<p>Only where the operator holds your balance in New Zealand dollars &mdash; the table limits are "
        "denominated in the account currency. At euro-denominated sites a &lsquo;&euro;1 minimum&rsquo; is "
        "about NZ$1.96, and you pay a conversion spread of roughly 4.8% across the round trip. The "
        "currency column in our <a href='/online-casinos/'>comparison table</a> shows which sites bank in "
        "NZD.</p>")],
      [("Are live dealer games rigged?",
        "<p>The outcomes are physical &mdash; real cards, a real wheel &mdash; filmed from several angles "
        "and watched simultaneously by hundreds of players, which makes manipulation both technically hard "
        "and commercially pointless. The house edge already guarantees the operator a profit. The genuine "
        "risks in this market are around withdrawal terms and licensing, not rigged tables.</p>"),
       ("What is Crazy Time and is it worth playing?",
        "<p>An Evolution game show built on a large money wheel with four bonus rounds. It is genuinely "
        "entertaining and it carries roughly a 4% house edge with extremely high variance &mdash; most "
        "rounds return nothing and the bonus rounds carry the entire return. Treat it as entertainment "
        "priced at about NZ$12 an hour at NZ$10 a spin, not as a value play.</p>"),
       ("Why do live tables have higher minimum bets?",
        "<p>Because each table carries real fixed costs &mdash; a dealer, a studio, camera operators, "
        "production staff &mdash; that must be covered by the turnover of the few dozen people seated at "
        "it. A pokie has no marginal cost per player, so it can afford a ten-cent spin.</p>"),
       ("Can I count cards in live blackjack online?",
        "<p>Not usefully. Most live blackjack uses eight-deck shoes reshuffled well before the end, or "
        "continuous shuffling machines, which removes the deck penetration any counting system depends on. "
        "Basic strategy is worth roughly 1.5% against playing by instinct and is the only edge genuinely "
        "available to you.</p>")],
      top, priority=0.9,
      toplist_h2="Best live casino NZ sites &mdash; counted at 9pm NZT",
      toplist_intro=("Our commercial order, disclosed as always. What we checked: tables genuinely open and "
                     "joinable from a New Zealand IP at 9pm NZT, minimum limits, and whether single-zero "
                     "roulette and 3:2 blackjack are on the floor."),
      toplist_html=leaderboard(top, cta="Play Live"))


def bonuses():
    P = "/online-casinos/bonuses/"
    A, C = "mei-lin-chau", "nikau-broughton"
    T = [("Online casinos", "/online-casinos/"), ("Bonuses", P)]
    top = pick(["smash", "kingdom", "spino", "lucky-circus", "rivo", "spinjo", "crownslots", "roby-casino"])

    priced = [(o, B.price(o)) for o in CASINOS]
    priced = [(o, p) for o, p in priced if p]
    cheap = sorted(priced, key=lambda x: x[1]["turnover"])
    worst = cheap[-1]
    total = sum(p["turnover"] for _, p in priced)
    clearable = [x for x in priced if x[1]["tone"] == "yes"]

    # ---- the full ledger, computed ----
    rows = []
    for op, p in cheap:
        tone = {"yes": "chip--yes", "warn": "chip--gold", "no": "chip--no"}[p["tone"]]
        rows.append([
            op_cell(op),
            esc(op.get("casino_bonus") or "&mdash;"),
            f'{p["mult"]:g}x <span class="chip">{B.basis_label(p)}</span>',
            f'<b>{B.money(p["turnover"])}</b>',
            B.money(p["cost"]),
            f'<span class="chip {tone}">{p["verdict"]}</span>',
        ])
    ledger = table(
      ["Casino", "Advertised offer", "Wagering basis", "Turnover required", "Expected cost to clear", "Verdict"],
      rows,
      caption=(f"Every casino bonus NZ players can claim this month, priced. Turnover is the operator&rsquo;s "
               f"own multiplier applied to its own stated basis at the maximum advertised bonus. Expected cost "
               f"is that turnover multiplied by a 4% house edge (96% RTP). Euro and USDT offers converted at "
               f"the mid-market rate of {B.FX_DATE}. Cheapest first."))

    # ---- a realistic NZ$200 deposit, which is what people actually do ----
    dep = 200
    real_rows = []
    for op, p in cheap[:10]:
        if p["mult"] == 0:
            real_rows.append([op_cell(op), B.money(dep), "0x", "NZ$0", "NZ$0",
                              '<b>+' + B.money(dep) + '</b>',
                              '<span class="chip chip--yes">Take it</span>'])
            continue
        match = min(p["match"] or 100, 100) / 100
        bonus = min(round(dep * match), p["bonus_nzd"])
        basis = (bonus + dep) if p["base"] == "deposit+bonus" else bonus
        turn = round(p["mult"] * basis)
        cost = round(turn * 0.04)
        ev = bonus - cost
        chip = ("chip--yes", "Worth claiming") if ev > 0 else (
               ("chip--gold", "Marginal") if ev > -60 else ("chip--no", "Decline"))
        real_rows.append([op_cell(op), B.money(dep), f'{p["mult"]:g}x', B.money(turn),
                          "~" + B.money(cost),
                          ("<b>+" if ev > 0 else "<b>&minus;") + B.money(abs(ev)) + "</b>",
                          f'<span class="chip {chip[0]}">{chip[1]}</span>'])
    realistic = table(
      ["Casino", "Your deposit", "Wagering", "Turnover you must generate", "Expected cost", "Net expected value", "Verdict"],
      real_rows,
      caption=("The same offers priced on a <b>NZ$200 first deposit</b> &mdash; a realistic amount rather than "
               "the advertised maximum. Net expected value is the bonus you receive minus the expected cost of "
               "clearing it. A negative number means the offer costs you more than it gives you, which is true "
               "of most of them."))

    body = f"""
{sec(f'''{sechead("Why a casino bonus NZ players claim is usually worth less than nothing",
  "The number in the banner is the marketing. The number in the terms is the price.", 2, "why")}
<div class="prose">
<p>There is a comfortable way to write this page. You list the biggest welcome offers, you call the largest
one &ldquo;best casino bonus NZ&rdquo;, you add a sentence about reading the terms, and you collect the
commission. Every page currently ranking for this term does a version of that.</p>
<p>The problem is that it inverts the truth. <b>A larger bonus on the same multiplier is a worse offer</b>,
because the multiplier applies to the whole of it. A 600% match up to NZ$18,500 at 30x wagering is not six
times more generous than a 100% match up to NZ$500 at 35x. It demands
<b>{B.money(cheap[-1][1]["turnover"]) if cheap else ""}</b> of turnover instead of NZ$17,500, and turnover
is not free. Every dollar you stake returns about ninety-six cents. The bigger the headline, the more
expensive the homework.</p>
<p>So this page does the arithmetic instead of the adjectives. Every online casino bonus New Zealand
players can reach is listed below with its real price attached, because a welcome bonus casino NZ-side
advertises at 600% is a different product from the one you actually receive. Across the {len(priced)} cash welcome offers
available to New Zealanders this month, the combined wagering demand is <b>{B.money(total)}</b>, and
<b>{len(clearable)} of {len(priced)}</b> survive contact with a calculator. Here is all of it, and here is
the method, so you can disagree with us on the numbers rather than on the vibe.</p>
</div>''', ident="why")}

{sec(f'''{sechead("Every casino bonus in New Zealand, priced", None, 2, "ledger")}
{ledger}
<div class="prose">
{note('<p><b>How to read this table.</b> Start at the top, not the bottom. The offers at the top are small, '
      'unglamorous and finishable. The offers at the bottom have the numbers that get advertised and '
      'require more turnover than a recreational player generates in a decade. There is no version of '
      'this table where the biggest headline is the best offer.</p>', "info")}
</div>''', ident="ledger", haze=True)}

{sec(f'''{sechead("What happens on a realistic NZ$200 deposit")}
<div class="prose">
<p>Advertised maximums are a poor guide, because almost nobody deposits NZ$3,250 to unlock a 600% match.
Most first deposits in New Zealand are between NZ$50 and NZ$300. So here is the same set of offers priced
on <b>NZ$200</b>, which is the question you are actually asking when you ask whether a casino sign up bonus
NZ-side is worth taking.</p>
</div>
{realistic}
<div class="prose">
<p>Two things fall out of that table. First, <b>the sign of the number changes everything</b> and it is
usually negative: for most welcome offers you are paying more in expected losses than the bonus is worth,
which means claiming it is a decision to gamble more, not a decision to get something free. Second, the
offers that come out positive are the ones with either no wagering at all or a low multiplier on a small
match &mdash; never the ones on the billboards.</p>
{note('<p><b>The option nobody sells you.</b> You can decline. A declined bonus means your deposit is '
      'withdrawable from the first spin, with no wagering requirement, no maximum cashout, no game '
      'weighting and no maximum bet rule to breach by accident. If you plan to deposit NZ$200, play for '
      'an evening and cash out what is left, declining is simply the correct decision and no amount of '
      'commission changes that.</p>', "info")}
</div>''', ident="realistic")}

{sec(f'''{sechead("What does 35x wagering mean? The arithmetic in plain English", None, 2, "wagering")}
<div class="prose">
<p>So how do casino wagering requirements work? A wagering requirement is the amount you must stake
before bonus-derived money can be withdrawn. It is quoted as a multiple, and the multiple is applied to a
<i>basis</i> that the operator chooses. Two numbers, and the second one is the one that gets you.</p>
<h3>The multiplier</h3>
<p>&ldquo;35x&rdquo; means thirty-five times. If the basis is a NZ$500 bonus, you must stake NZ$17,500 in
total before withdrawing. That is not NZ$17,500 of your own money &mdash; the same dollar recycles as you
win and restake &mdash; but it is NZ$17,500 of exposure to the house edge.</p>
<h3>The basis, which matters more</h3>
<p>Two bases are in common use and they are not close to equivalent:</p>
<ul>
<li><b>&ldquo;35x bonus&rdquo;</b> multiplies the bonus alone. A NZ$500 bonus needs NZ$17,500 of turnover.</li>
<li><b>&ldquo;35x deposit + bonus&rdquo;</b> multiplies your deposit as well. Deposit NZ$500 for a NZ$500
bonus and the requirement is NZ$35,000 &mdash; double, from an identical-looking headline.</li>
</ul>
<p>This is why a 10x requirement is not automatically better than a 40x one, and it is the most reliable
way to mislead a reader while disclosing everything. Check the basis first and the multiplier second.</p>
<h3>What it costs</h3>
<p>Turnover has a price, and the price is the house edge. On a 96% RTP pokie you lose an average of four
cents per dollar staked. So:</p>
<p class="lead"><b>Expected cost = turnover &times; 4%</b></p>
<p>NZ$17,500 of turnover costs about NZ$700. If the bonus was NZ$500, you have paid NZ$700 to receive
NZ$500. That is the entire calculation, and it is why &ldquo;are casino bonuses worth it NZ?&rdquo; has an
uncomfortable answer for most of the market.</p>
{note('<p><b>Game weighting multiplies the damage.</b> Pokies usually contribute 100% of each dollar staked '
      'toward the requirement. Table games often contribute 10%, and live blackjack 5% or nothing. A 35x '
      'requirement cleared on blackjack at 5% weighting is really <b>700x</b>. If you are not primarily a '
      'pokies player, most welcome offers are not designed for you.</p>', "warn")}
</div>''', ident="wagering", haze=True)}

{sec(f'''{sechead("Low wagering and no wagering casino bonus offers")}
<div class="prose">
<p>The only structurally good offers in this market are the ones that keep the multiplier low or remove it.
They are rare, they are never the biggest, and they are worth more than anything on the billboards.</p>
<p><b>No wagering</b> means winnings are withdrawable immediately, with no turnover requirement at all.
<a href="/casino-reviews/spino/">Spino</a> runs the only genuine 0x offer we have verified for New Zealand
players, on its crypto package. A no wagering casino bonus NZ-side is worth its face value, which is
something that can be said of nothing else on this page.</p>
<p><b>Low wagering</b> &mdash; a low wagering bonus NZ players can genuinely finish &mdash; is anything
at or under 20x on the bonus alone. Below that threshold the expected
cost of clearing starts to land under the value of the bonus, which is the only condition under which
claiming makes you better off.</p>
<p>When you see a low multiplier attached to a very large match, check the basis before celebrating:
<a href="/casino-reviews/smash/">Smash</a> advertises 10x, which sounds excellent, but it applies to
deposit plus bonus on a 600% match &mdash; {B.money(BY["smash"] and B.price(BY["smash"])["turnover"])} at
the maximum.</p>
</div>''', ident="lowwagering")}

{sec(f'''{sechead("Small deposit bonuses: $1, $5 and $10 deposit casino NZ offers", None, 2, "small")}
<div class="prose">
<p>Searches for a <b>$1 deposit casino NZ</b> and a <b>1 dollar deposit casino NZ</b> are common, and the
honest answer is that the true single-dollar offer has largely disappeared from the market New Zealanders
can reach. What still exists is worth understanding on its own terms.</p>
<h3>What a $1 deposit casino NZ actually gets you</h3>
<p>Where these offers survive they are structured as a fixed spin package rather than a match &mdash; a
dollar buys a set number of spins at minimum stake, and the winnings carry a wagering requirement and a
maximum cashout, typically NZ$50 to NZ$100. The realistic value is a few dollars. Treated as a cheap look
at a lobby, that is fine. Treated as a way to win money, it is not.</p>
<h3>$5 and $10 deposit casino NZ offers</h3>
<p>A $5 deposit casino NZ offer is more common than the single-dollar version and more useful. The trap here is the gap between the <i>deposit</i> minimum and the
<i>bonus-qualifying</i> minimum: a site advertising NZ$10 deposits will frequently require NZ$20 or NZ$30
before the welcome offer triggers. Depositing NZ$10 at a site with a NZ$30 qualifying floor gets you no
bonus and no explanation.</p>
<p>The lowest genuine entry points we have verified are NZ$10 at
<a href="/casino-reviews/lucky-circus/">Lucky Circus</a>, which is also the rare site where the deposit
minimum and the bonus-qualifying minimum are the same number. Both figures for every site are in the
<a href="/online-casinos/">full comparison table</a>.</p>
<h3>Minimum deposit casino bonus NZ: the rule of thumb</h3>
<p>The smaller your deposit, the worse a percentage match serves you, because the bonus scales with the
deposit but the wagering requirement scales with the bonus. A NZ$10 deposit taking a 100% match at 40x owes
NZ$400 of turnover to unlock NZ$10. The proportions are identical at every deposit size, which is the point:
a match bonus is never a better deal for being small, it is simply a smaller version of the same deal.</p>
</div>''', ident="small")}

{sec(f'''{sechead("Reload, cashback and the offers that come after the welcome")}
<div class="prose">
<p>The welcome offer is the one that gets compared. The offers that follow are the ones you will actually
spend the most time with, and they are almost never covered.</p>
<h3>Reload bonuses</h3>
<p>A <b>reload bonus casino NZ</b> side is a smaller match on a subsequent deposit, typically 25% to 50%,
usually weekly and usually carrying the same wagering multiplier as the welcome offer. Because the match
percentage is lower but the multiplier is unchanged, a reload is generally <i>worse</i> value than the
welcome bonus it follows. Price it the same way: multiplier times bonus, times four percent.</p>
<h3>Cashback</h3>
<p>The most honest structure in the market, and the one worth looking for. A <b>cashback casino bonus
NZ</b> returns a percentage of net losses over a period, and the good versions pay it as cash with no
wagering attached. Two questions decide whether a cashback offer is real: <b>is it paid on net losses or
on turnover</b>, and <b>is the returned money withdrawable or does it arrive as a bonus with its own
multiplier?</b> Cash on net losses is genuinely valuable. A &ldquo;cashback&rdquo; that arrives as a 40x
bonus is a welcome offer wearing a different hat.</p>
<h3>Casino bonus codes NZ</h3>
<p>Most sites listed here apply their welcome offer automatically and need no code at all. Where a
<b>casino bonus code NZ</b> is required it is shown on the offer itself at the operator&rsquo;s cashier.
We do not publish codes we have not verified from a New Zealand IP address, because an expired code is
worse than no code &mdash; it consumes the deposit that would otherwise have qualified.</p>
</div>''', ident="reload", haze=True)}

{sec(f'''{sechead("How we price an offer, so you can check us")}
<div class="prose">
<p>Everything on this page comes out of one short calculation applied identically to every operator. No
judgement, no weighting, no rate card.</p>
</div>
{steps([
  ("Take the advertised maximum and convert it to New Zealand dollars",
   f"At the mid-market rate on {B.FX_DATE}. A euro-denominated bonus is not worth its face value to a "
   f"New Zealander, and the conversion is applied before anything else so that offers are compared in the "
   f"currency you will actually be judged in."),
  ("Read the wagering multiplier and, more importantly, the basis",
   "Bonus only, or deposit plus bonus. Where an offer states a total match percentage we recover the "
   "qualifying deposit from the cap, because a &lsquo;deposit + bonus&rsquo; requirement cannot be priced "
   "honestly without it."),
  ("Multiply", "Turnover = multiplier &times; basis. This is the number the operator requires and the "
   "number no operator prints."),
  ("Apply the house edge",
   "Expected cost = turnover &times; 4%, the average cost of generating that turnover on a 96% RTP pokie. "
   "A player on lower-RTP games pays more; nobody pays less."),
  ("Compare the cost to the bonus",
   "If clearing costs more than the bonus is worth, the offer has a negative expected value and we say so, "
   "including where the operator concerned is one of our best-paying partners."),
])}
<div class="prose">
{note('<p><b>What this calculation does not capture.</b> It assumes you clear the requirement in full, '
      'which most players do not; it assumes a 96% RTP throughout; and it ignores variance, which is the '
      'reason anyone plays at all. It is a measure of the offer&rsquo;s structure, not a prediction of '
      'your evening. We think it is the most useful single number available, and we would rather publish '
      'its limits than imply it has none.</p>', "info")}
</div>''', ident="method")}
"""

    return shell(P, T, H1[P],
      f"<p>Every casino bonus NZ players can claim this month, converted from the advertised headline into "
      f"the turnover it demands and what that turnover is expected to cost. Across {len(priced)} live "
      f"welcome offers the combined wagering demand is <b>{B.money(total)}</b> &mdash; and "
      f"<b>{len(clearable)}</b> of them survive the arithmetic.</p>"
      "<p>We price the offer instead of repeating it. Where that produces an unflattering answer about a "
      "brand we are paid by, the unflattering answer is what gets published.</p>",
      [(f"{len(priced)}", "Offers priced"), (f"{B.money(total)}", "Combined turnover demanded"),
       (f"{len(clearable)}", "Worth claiming"), ("4%", "House edge applied")],
      f"Casino bonuses &middot; {MONTH_YEAR}", A, C,
      [("Why most bonuses are worth less than nothing", "why"),
       ("Every bonus, priced", "ledger"),
       ("On a realistic NZ$200 deposit", "realistic"),
       ("What 35x wagering actually means", "wagering"),
       ("Low and no wagering offers", "lowwagering"),
       ("$1, $5 and $10 deposit offers", "small"),
       ("Reload, cashback and bonus codes", "reload"),
       ("How we price an offer", "method")],
      body,
      [("What is the best casino bonus NZ players can claim right now?",
        f"<p>On expected value rather than headline size, the best casino bonuses NZ-side this month are "
        f"the ones at the top of our ledger, not the bottom. <a href='/casino-reviews/spino/'>Spino</a>&rsquo;s "
        f"0x crypto package is the only offer we have verified that carries no wagering requirement at all, "
        f"which makes it worth its face value &mdash; a claim nothing else on this page can make. Among "
        f"cash matches, small offers on modest multipliers beat large offers on the same multiplier every "
        f"time, because the multiplier applies to the whole bonus. Put differently: the best welcome bonus "
        f"online casino NZ players can claim is rarely the one with the largest number attached to it.</p>"),
       ("What does 35x wagering mean in dollars?",
        "<p>Multiply the bonus by thirty-five. A NZ$500 bonus at 35x requires NZ$17,500 of total stakes "
        "before withdrawal. Generating that turnover on a 96% RTP pokie costs an expected NZ$700, so the "
        "NZ$500 bonus costs about NZ$700 to collect. If the basis is &lsquo;deposit + bonus&rsquo; rather "
        "than &lsquo;bonus&rsquo;, double both figures.</p>"),
       ("Are casino bonuses worth it in New Zealand?",
        f"<p>Usually not, and we would rather say so. Of the {len(priced)} cash welcome offers live this "
        f"month, {len(clearable)} have a positive expected value on a realistic deposit. The rest cost more "
        f"in expected losses than the bonus is worth. That does not make them a scam &mdash; the terms are "
        f"disclosed and enforceable &mdash; but it does mean claiming one is a decision to gamble more "
        f"rather than a decision to receive something free.</p>"),
       ("Is there a no wagering casino bonus in NZ?",
        "<p>Yes, but only one we can verify: <a href='/casino-reviews/spino/'>Spino</a>&rsquo;s crypto "
        "welcome package carries 0x wagering, meaning winnings are withdrawable immediately. Treat any "
        "other &lsquo;no wagering&rsquo; claim with suspicion until you have found the multiplier in the "
        "terms, because the phrase is often applied to free spin winnings while the cash bonus keeps a "
        "full requirement.</p>"),
       ("Do I need a casino bonus code in New Zealand?",
        "<p>At most of the sites here, no &mdash; the welcome offer applies automatically when you deposit "
        "a qualifying amount. Where a code is needed it appears at the cashier on the offer itself. We do "
        "not republish casino bonus codes NZ-side that we have not confirmed live from a New Zealand IP, "
        "because an expired code consumes the deposit that would otherwise have qualified.</p>"),
       ("What is the minimum deposit to get a casino bonus?",
        "<p>Between NZ$10 and NZ$35 depending on the site, and the number to check is the "
        "bonus-qualifying minimum rather than the deposit minimum &mdash; they are frequently different. "
        "<a href='/casino-reviews/lucky-circus/'>Lucky Circus</a> is the lowest genuine entry point at "
        "NZ$10 and one of the few where both figures match.</p>")],
      [("Can you withdraw a casino bonus straight away?",
        "<p>Not unless the offer carries 0x wagering. Bonus funds and anything derived from them are "
        "locked until the wagering requirement is met, and attempting to withdraw early normally forfeits "
        "the bonus and the winnings with it. Your own deposit is a separate matter and is usually "
        "withdrawable, though doing so also voids the offer.</p>"),
       ("What is a maximum cashout on a casino bonus?",
        "<p>A ceiling on how much bonus-derived winnings you may withdraw, regardless of how much you "
        "won. It is most common on no-deposit and free-spin offers, where NZ$50 to NZ$100 is typical. "
        "Turn 20 free spins into NZ$3,000 under a NZ$100 cap and you withdraw NZ$100. It is disclosed, it "
        "is enforceable, and it is the single most common cause of a player feeling cheated by a site "
        "that has broken no rule.</p>"),
       ("Why do casinos offer bonuses at all?",
        "<p>Because the wagering requirement makes them profitable. An offer that demands NZ$200,000 of "
        "turnover generates around NZ$8,000 of expected house margin, against a bonus that cost the "
        "operator NZ$5,000 in credit that was never cash. The bonus is a customer-acquisition cost paid "
        "for out of the turnover it compels &mdash; which is exactly why the size of the headline and the "
        "size of the requirement rise together.</p>"),
       ("Does the bonus change if I deposit in crypto?",
        "<p>Frequently, yes, and often favourably &mdash; crypto-specific packages tend to carry lower "
        "multipliers, and the only 0x offer we have verified is a crypto one. The offsetting consideration "
        "is tax: the IRD treats cryptoassets as property, so converting a crypto balance back to New "
        "Zealand dollars can be a taxable disposal independently of the gambling. "
        "<a href='/gambling-winnings-tax-nz/'>How the IRD treats it</a>.</p>")],
      top, priority=0.9,
      toplist_h2="Best casino bonuses NZ &mdash; ranked by what they cost to clear",
      toplist_intro=("Listed in our commercial order, as disclosed under every table on this site. The "
                     "column that should decide your choice is the turnover figure, and it does not follow "
                     "the listing order."),
      toplist_html=leaderboard(top, cta="Claim Bonus"))


def nodeposit():
    P = "/no-deposit-casinos/"
    A, C = "mei-lin-chau", "camille-toure"
    T = [("No deposit casinos", P)]
    top = pick(["lucky7even", "spinjo", "hellspin", "slotsgem", "rivo", "ivibet", "lucky-circus", "fortune-play"])

    value = table(
      ["Offer", "Face value", "Wagering on winnings", "Max cashout", "Realistic cash value*", "Hours to clear**"],
      [["<b>20 free spins</b> at NZ$0.20", "NZ$4", "50x", "NZ$100", "<b>~NZ$0.40</b>", "~1.5"],
       ["25 free spins at NZ$0.20", "NZ$5", "45x", "NZ$100", "~NZ$0.60", "~1.7"],
       ["50 free spins at NZ$0.20", "NZ$10", "40x", "NZ$100", "~NZ$1.40", "~3"],
       ["100 free spins at NZ$0.10", "NZ$10", "40x", "NZ$100", "~NZ$1.40", "~3"],
       ["NZ$5 free chip", "NZ$5", "50x", "NZ$50", "~NZ$0.45", "~2"],
       ["NZ$10 free chip", "NZ$10", "50x", "NZ$100", "~NZ$0.90", "~4"]],
      caption="*Face value &times; RTP, discounted for the probability of clearing the wagering requirement "
              "before the balance is gone, then capped at the maximum cashout. **At roughly 600 spins per "
              "hour. These are the honest numbers behind a &ldquo;NZ$4 free&rdquo; offer, and they are the "
              "reason this page tells you to take one but never to choose a casino for one.")

    mechanics = table(
      ["Clause", "Typical value", "What it does to the offer"],
      [["<b>Maximum cashout</b>", "NZ$50&ndash;NZ$100",
        "Caps your withdrawal regardless of how much you win. Turn 20 spins into NZ$3,000 and you collect "
        "NZ$100. This single clause defines the entire category."],
       ["<b>Wagering on winnings</b>", "40x&ndash;50x",
        "Applied to what the spins produce, not to a bonus amount. Win NZ$20 from your spins at 50x and "
        "you owe NZ$1,000 of turnover before withdrawing a cent."],
       ["Maximum bet while wagering", "NZ$5",
        "Exceed it once and the operator may void everything. Easy to breach by accident after the free "
        "spins convert to a cash balance."],
       ["Game restriction", "One named title",
        "Spins are usually locked to a single pokie chosen by the operator &mdash; frequently a "
        "high-volatility title where most sessions return nothing."],
       ["Expiry", "24 hours &ndash; 7 days",
        "Much shorter than a deposit bonus. Unused spins and unmet wagering both vanish."],
       ["One per household", "Strictly enforced",
        "Tied to IP, device fingerprint and payment method as well as identity. Multiple accounts is the "
        "fastest route to confiscated winnings and a closed account."]],
      caption="The six clauses that turn a no deposit bonus NZ players see advertised as free money into "
              "something worth well under a dollar. All six are disclosed; none of them are prominent.")

    body = f"""
{sec(f'''{sechead("What a no deposit bonus is actually worth",
  "We are about to argue ourselves out of commission. The arithmetic is the arithmetic.", 2, "worth")}
<div class="prose">
<p>A no deposit bonus is the only genuinely free thing in this industry. You register, you receive spins or
a small credit, you risk nothing of your own. That much is true and it is why the category is searched so
heavily.</p>
<p>What is also true is that the typical offer is worth <b>less than a dollar</b>, and the headline number
is roughly ten times its realistic value. Here is why, on the standard structure.</p>
<p>Take 20 free spins at NZ$0.20 &mdash; a common no deposit sign up bonus NZ side. Face value NZ$4. Those
spins return about 96% on average, so call it NZ$3.84 of expected winnings. Now the winnings carry 50x
wagering: to withdraw NZ$3.84 you must stake <b>NZ$192</b>. Generating NZ$192 of turnover from a NZ$3.84
balance means surviving roughly fifty spins at NZ$0.20 without going broke, which the maths says you will
usually not. Discount for that, then cap the outcome at the NZ$100 maximum cashout, and the offer is worth
about <b>forty cents</b>.</p>
</div>
{value}
<div class="prose">
{note('<p><b>So should you take one? Yes.</b> Forty cents of expected value for five minutes and an email '
      'address is a fine trade, and occasionally somebody does clear one and collect the cap. What you '
      'should not do is <b>choose a casino</b> because of it. You are selecting a site you may deposit at '
      'for years on the basis of an offer worth less than a coffee. Pick the casino on payout terms and '
      'licensing, then take the no deposit bonus if there happens to be one.</p>', "info")}
</div>''', ident="worth")}

{sec(f'''{sechead("Maximum cashout: the clause that defines the category", None, 2, "cashout")}
<div class="prose">
<p>If you read one section here, read this one. It is the source of nearly every complaint we see about
this category, and in almost every case the casino has done nothing wrong.</p>
<p><b>A maximum cashout caps what you may withdraw from bonus-derived winnings, regardless of how much you
actually won.</b> On a no deposit offer it is typically NZ$50 to NZ$100.</p>
<p>Consider what that means. You take 20 free spins. The game runs hot and you finish with NZ$3,000. You
grind out the wagering requirement, which is genuinely difficult, and request a withdrawal. You receive
<b>NZ$100</b>. The remaining NZ$2,900 is removed from your balance, as the terms you accepted said it
would be.</p>
<p>Players describe this as theft. It is not &mdash; it is disclosed, enforceable and standard across the
industry. But it is also the reason a no deposit bonus can never be a route to a meaningful win, and why
the honest framing is &ldquo;a free look at a casino&rdquo; rather than &ldquo;free money&rdquo;.</p>
{note('<p><b>The one thing to check before you claim.</b> Find the maximum cashout figure in the bonus '
      'terms. If it is not stated, assume it exists and is low. An offer with <i>no</i> maximum cashout is '
      'genuinely rare and genuinely valuable &mdash; and worth far more than one with twice the spins.</p>',
      "warn")}
</div>''', ident="cashout", haze=True)}

{sec(f'''{sechead("Every clause in a no deposit offer, and what it does")}
{mechanics}
<div class="prose">
<p>Note the second row particularly, because it is the one people misread. On a deposit bonus, wagering is
applied to the bonus amount. On free spins, it is applied to <b>what the spins win</b> &mdash; which means
a lucky outcome makes the requirement <i>larger</i>. Win NZ$200 from your spins at 50x and you must stake
NZ$10,000 before touching it. The better your luck, the further away the money gets.</p>
</div>''', ident="clauses")}

{sec(f'''{sechead("How to claim a no deposit bonus properly")}
{steps([
  ("Register with accurate details, the first time",
   "Your name must match the identity document you will eventually upload. A mismatch is the most common "
   "reason a no deposit win is refused at verification, and it cannot be corrected afterwards without "
   "raising exactly the question you do not want raised."),
  ("Look for the offer in the cashier, not the inbox",
   "Most no deposit bonuses activate automatically or sit under a Bonuses tab. A minority need a code, "
   "which will be shown with the offer. Codes republished on affiliate sites expire constantly, and an "
   "expired code can consume the qualifying registration."),
  ("Read the maximum cashout before you spin",
   "Thirty seconds, and it tells you the ceiling on the entire exercise. If it is NZ$50, you now know the "
   "best possible outcome and can treat the rest as entertainment."),
  ("Check which game the spins are locked to",
   "Almost always a single title. If it is a high-volatility pokie, most sessions will return nothing at "
   "all &mdash; that is the mechanic working as designed, not bad luck."),
  ("Respect the maximum bet after the spins convert",
   "Once free spin winnings become a wagering-restricted cash balance, the maximum bet rule applies "
   "&mdash; usually NZ$5. Breaching it once, even by accident on autoplay, voids everything."),
  ("Complete verification early",
   "If you do clear the wagering and reach the cap, the operator will verify before paying. Doing it "
   "upfront turns a multi-day wait into a same-day withdrawal."),
])}''', ident="claim", haze=True)}

{sec(f'''{sechead("Are no deposit bonuses legitimate?")}
<div class="prose">
<p>At licensed operators, yes &mdash; with a precise definition of &ldquo;legitimate&rdquo; that is worth
stating.</p>
<p><b>The offers are real.</b> The spins credit, the winnings are genuine, and if you clear the wagering
within the cap you will be paid. We have tested this and it works.</p>
<p><b>The terms are heavily restrictive and fully disclosed.</b> Maximum cashout, high wagering on
winnings, a single eligible game and a short expiry are not hidden &mdash; they are in the bonus terms,
which almost nobody opens. The gap between what players expect and what they receive is a gap of attention,
not of honesty.</p>
<p><b>Where it does go wrong</b> is at the margins: offers republished on affiliate sites long after they
expired, &ldquo;exclusive&rdquo; codes that were never exclusive, and a small number of unlicensed sites
that use a no deposit offer purely to harvest identity documents. The defence is the same as everywhere
else on this site &mdash; check that the operator names a company, holds a licence that resolves on the
regulator&rsquo;s own register, and publishes its withdrawal terms.</p>
{note('<p><b>Our disclosure on this specific category.</b> We are paid when you register through a link '
      'here, including on a no deposit offer where you never deposit a cent. That is a direct commercial '
      'incentive for us to overstate what these bonuses are worth, and it is precisely why this page opens '
      'by pricing them at about forty cents. If an affiliate page tells you a no deposit bonus is a good '
      'reason to pick a casino, weigh that against who is paying them.</p>', "info")}
</div>''', ident="legit")}

{sec(f'''{sechead("What to do after you clear one")}
<div class="prose">
<p>Rarely covered, and it is the moment the offer has actually done its job &mdash; on both sides.</p>
<p>If you cleared the wagering and collected the cap, you now know something genuinely useful: this casino
pays. You have watched a withdrawal go through end to end without risking your own money, which is a better
test of an operator than any review, including ours.</p>
<p>If you are going to deposit next, that is the moment to think about the welcome offer properly &mdash;
and in most cases, to decline it. A no deposit bonus is worth taking because it is free. A deposit bonus
demands turnover you must pay for, and on our pricing most of them cost more than they give.
<a href="/online-casinos/bonuses/">The full ledger</a> has every offer converted into what it actually
costs to clear.</p>
<p>And if the casino did not pay, you have learned that for the price of an email address, which is the
cheapest possible way to find out.</p>
</div>''', ident="after")}

{sec(f'''{sechead("Free spins no deposit NZ: every variant, priced", None, 2, "variants")}
<div class="prose">
<p>A casino no deposit bonus New Zealand players are offered comes in a handful of standard shapes. Here is
what each is realistically worth once the wagering and the cap are applied.</p>
<h3>20 and 25 free spins no deposit NZ</h3>
<p>The most common offers. 20 free spins no deposit NZ side at NZ$0.20 a spin is NZ$4 of face value and
about forty cents of realistic value. 25 free spins no deposit NZ offers are the same structure with a
slightly better number.</p>
<h3>50 and 100 free spins no deposit NZ</h3>
<p>50 free spins no deposit NZ offers usually pair a larger count with a lower spin value or a tighter cap,
so the realistic value rises far less than the headline suggests. 100 free spins no deposit NZ side is
almost always NZ$0.10 spins &mdash; the same NZ$10 of face value as a fifty-spin offer at NZ$0.20.</p>
<h3>$5 and $10 no deposit bonus NZ</h3>
<p>A $5 no deposit bonus NZ side, sometimes called a free chip no deposit casino NZ offer, is cash rather
than spins, which means you choose the game &mdash; a genuine advantage. A $10 no deposit bonus NZ offer is
the larger version. Both typically carry 50x wagering and a NZ$50 to NZ$100 cap.</p>
<h3>No deposit free spins on registration NZ</h3>
<p>No deposit free spins on registration NZ side credit automatically when the account is created, with no
card required. Free spins no deposit no card details NZ offers are the same thing described from the other
direction, and they are common.</p>
<h3>Real money no deposit bonus NZ and &ldquo;keep what you win&rdquo;</h3>
<p>A real money no deposit bonus NZ offer produces genuine withdrawable winnings, subject to the wagering
and the cap. No deposit bonus keep what you win NZ side should mean zero wagering; in practice the phrase
is applied loosely, so find the multiplier before believing it. Can you withdraw no deposit bonus winnings
NZ side? Yes &mdash; up to the cap, after clearing the wagering.</p>
<h3>New, exclusive and 2026 offers</h3>
<p>A new no deposit bonus NZ side appears regularly and free spins no deposit NZ 2026 listings go stale
fast. We do not republish exclusive no deposit bonus codes NZ we have not confirmed live, because an
expired code can consume the single registration you get. The best no deposit bonus NZ 2026 offer is
whichever one is actually live and carries the highest cap &mdash; and no deposit bonus pokies NZ offers
are all locked to a game the operator chose.</p>
<p>No deposit bonus max cashout explained, and no deposit bonus wagering requirements NZ side, are covered
in full <a href="#cashout">above</a> &mdash; they are the two clauses that decide everything.</p>
</div>''', ident="variants")}
"""

    return shell(P, T, H1[P],
      "<p>A no deposit bonus NZ players can claim is the only genuinely free offer in this industry, and "
      "the typical one is worth about <b>forty cents</b>. Face value NZ$4, wagering of 50x applied to the "
      "winnings, and a NZ$100 maximum cashout waiting at the end of it.</p>"
      "<p>Take one &mdash; free is free. Just never choose a casino because of one. Below: every offer "
      "priced honestly, the six clauses that do the damage, and how to claim without voiding it.</p>",
      [("~NZ$0.40", "Realistic value, 20 free spins"), ("50x", "Typical wagering on winnings"),
       ("NZ$100", "Usual maximum cashout"), ("1 per", "Household, strictly enforced")],
      f"No deposit bonuses &middot; {MONTH_YEAR}", A, C,
      [("What one is actually worth", "worth"),
       ("Maximum cashout explained", "cashout"),
       ("Every clause, decoded", "clauses"),
       ("How to claim one properly", "claim"),
       ("Are they legitimate?", "legit"),
       ("What to do after you clear one", "after")],
      body,
      [("What free spins no deposit NZ offers are actually available?",
        "<p>Free spins no deposit NZ side are offered by a minority of the operators we cover, most "
        "reliably as a 20-spin package on registration. A casino no deposit bonus New Zealand players can "
        "claim is genuinely free and genuinely small &mdash; worth roughly forty cents once the 50x "
        "wagering on winnings and the NZ$100 maximum cashout are applied.</p>"),
       ("What is the best no deposit bonus NZ players can get right now?",
        "<p>The most reliable standing offer among the sites we cover is "
        "<a href='/casino-reviews/lucky7even/'>Lucky7even</a>&rsquo;s 20 no-deposit spins, which carry 50x "
        "wagering on winnings. Priced honestly that is worth roughly forty cents &mdash; genuinely free, "
        "and genuinely small. Take it if you were considering the casino anyway; do not pick a casino for "
        "it.</p>"),
       ("Can you actually withdraw no deposit bonus winnings in NZ?",
        "<p>Yes, but only up to the maximum cashout, and only after clearing the wagering requirement on "
        "the winnings. The cap is typically NZ$50 to NZ$100. If your spins produce NZ$3,000 and the cap is "
        "NZ$100, you withdraw NZ$100 and the balance is removed. That is disclosed in the terms and it is "
        "enforceable.</p>"),
       ("What does no deposit bonus keep what you win mean?",
        "<p>It should mean no wagering requirement on your winnings, which would make the offer worth its "
        "face value. In practice the phrase is often applied loosely to offers that still carry a maximum "
        "cashout, and sometimes to ones that still carry wagering. Find the two numbers &mdash; the "
        "multiplier and the cap &mdash; before believing the phrase.</p>"),
       ("How do no deposit bonus wagering requirements work?",
        "<p>Differently from a deposit bonus, and worse. On a deposit bonus the multiplier applies to the "
        "bonus amount. On free spins it applies to <i>what the spins win</i>, so a lucky result increases "
        "the requirement. Win NZ$20 at 50x and you owe NZ$1,000 of turnover; win NZ$200 and you owe "
        "NZ$10,000.</p>"),
       ("Do I need a code to claim a no deposit bonus in NZ?",
        "<p>Usually not &mdash; most offers activate on registration or sit in the cashier under a bonus "
        "tab. Where a code is required it is displayed with the offer at the operator. We do not "
        "republish no deposit bonus codes NZ side that we have not verified live from a New Zealand IP, "
        "because an expired code can consume the one registration you get.</p>"),
       ("Are free spins no deposit offers available without card details?",
        "<p>Frequently, yes. A true no deposit offer requires only registration, and many sites do not ask "
        "for a payment method until you deposit. Some request card details at signup purely for identity "
        "purposes, which is legitimate but worth knowing before you start. You will always need to "
        "complete verification before withdrawing.</p>")],
      [("Why do casinos give away no deposit bonuses?",
        "<p>Because they are an extremely cheap way to acquire a verified, engaged account. The offer "
        "costs the operator a few dollars of credit that mostly never converts to a withdrawal, and a "
        "meaningful proportion of the people who claim one go on to deposit. The maximum cashout caps the "
        "operator's downside precisely; that is the clause the whole model rests on.</p>"),
       ("Can I claim more than one no deposit bonus?",
        "<p>One per person, per household, per device, and operators enforce it with IP, device "
        "fingerprinting and payment-method matching as well as identity checks. Attempting multiple "
        "accounts is the single fastest route to confiscated winnings and a permanently closed account, "
        "and it is detected at verification rather than at signup.</p>"),
       ("Are no deposit bonuses better than deposit bonuses?",
        "<p>They are better value in the sense that they are free and cannot cost you anything. They are "
        "far smaller, far more restricted, and capped at an amount that makes a large win impossible. A "
        "deposit bonus can be worth more in absolute terms &mdash; but on our pricing most of them have a "
        "negative expected value, so 'better' depends on whether you are measuring size or cost.</p>"),
       ("Do no deposit free spins work on any pokie?",
        "<p>Almost never. Spins are normally locked to one title the operator has chosen, frequently a "
        "high-volatility game where the majority of short sessions return nothing. That is not bad luck, "
        "it is the expected behaviour of the game selected, and it is part of why the realistic value of "
        "these offers is so far below the face value.</p>")],
      top, priority=0.9,
      toplist_h2="No deposit bonus NZ offers &mdash; priced honestly",
      toplist_intro=("Our commercial order, disclosed as always. Every offer below is checked live from a "
                     "New Zealand IP; where a maximum cashout or a wagering multiplier applies, it is "
                     "named rather than buried."),
      toplist_html=leaderboard(top, cta="Claim Offer"))


def build():
    pokies(); highpayout(); fastpayout(); crypto(); live(); bonuses(); nodeposit()
