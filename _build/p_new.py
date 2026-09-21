#!/usr/bin/env python3
"""/new-casinos-nz/ — the running list of new online casinos NZ players can join.

Highest refresh value on the site. From 1 December 2026 the licensed operators
start going live, and this page becomes the record of who launched and when.
Update LAUNCHES and rebuild; the "last checked" stamp and the counts follow.
"""
from lib import *
import lawdata as L

PATH = "/new-casinos-nz/"
AUTHOR, CHECKER = "nikau-broughton", "ihaka-nightingale"
TRAIL = [("Online casinos", "/online-casinos/"), ("New casinos NZ", PATH)]

# Newest first. Status is what we can evidence, not what the operator claims.
LAUNCHES = [
    ("kingdom",      "2024", "Anjouan",     "Tested &mdash; ranked 2nd"),
    ("smash",        "2024", "Anjouan",     "Tested &mdash; lowest wagering in our set"),
    ("rivo",         "2024", "Anjouan",     "Tested &mdash; best mobile build"),
    ("madcasino",    "2024", "Anjouan",     "Tested &mdash; casino and sportsbook in one wallet"),
    ("crownslots",   "2024", "Cura&ccedil;ao",     "Tested &mdash; no operating company published"),
    ("roby-casino",  "2024", "Not published", "Tested &mdash; <b>no licence published</b>"),
    ("spino",        "2024", "Tobique",     "Tested &mdash; crypto only, 0x wagering"),
    ("spinjo",       "2023", "Cura&ccedil;ao GCB", "Tested &mdash; our top-ranked casino"),
    ("lucky-vibe",   "2023", "Cura&ccedil;ao GCB", "Tested &mdash; published VIP tiers"),
    ("lucky-circus", "2023", "Cura&ccedil;ao GCB", "Tested &mdash; NZ$10 minimum"),
    ("fortune-play", "2023", "Cura&ccedil;ao GCB", "Tested &mdash; crash and bonus buys"),
    ("rooster-bet",  "2023", "Cura&ccedil;ao GCB", "Tested &mdash; best casino + sportsbook"),
    ("slotsgem",     "2023", "Cura&ccedil;ao",     "Tested &mdash; smallest library we rank"),
]
NEW_2024 = [s for s, y, *_ in LAUNCHES if y == "2024"]

FAQS = [
 ("Are new online casinos safe in NZ?",
  "<p>Age is close to the wrong question. A 2024 brand with a named operating company and a licence that "
  "resolves on the regulator's register is safer than an older site that publishes neither. What a new "
  "casino genuinely lacks is a <b>payout record</b> &mdash; and since most launches here are new skins on "
  "established groups (Rabidi N.V., Dama N.V., Vertikal N.V., TechOptions), the group behind the brand "
  "usually does have one. Check the footer.</p>"),
 ("Do new online casinos have better bonuses?",
  "<p>Larger ones, yes &mdash; new sites buy market share with headline numbers. Better is a different "
  "question. A bigger bonus on the same multiplier demands <i>more</i> turnover, not less, so on our "
  "pricing the largest launch offers are routinely the worst value on the site. "
  "<a href='/online-casinos/bonuses/'>Every offer converted into the turnover it requires</a>.</p>"),
 ("How can I tell if a new casino will actually pay me?",
  "<p>You cannot, from the outside &mdash; which is exactly the gap. So buy the evidence: deposit the "
  "minimum, play briefly, and withdraw the remainder, timing it end to end. About NZ$20 and ten minutes "
  "gets you a real payout record for that specific operator, which is the one thing no review, including "
  "ours, can give you.</p>"),
 ("What new online casinos have NZ no deposit bonuses?",
  "<p>Very few, and the ones that exist are small. Among the brands we cover, "
  "<a href='/casino-reviews/lucky7even/'>Lucky7even</a> runs the only no-deposit offer we could verify "
  "live from a New Zealand IP this month &mdash; 20 spins carrying 50x wagering on winnings, worth around "
  "forty cents once priced. Useful for testing a cashier, not for choosing a casino. "
  "<a href='/no-deposit-casinos/'>The full pricing</a>.</p>"),
 ("When do the new licensed NZ casinos launch?",
  "<p>During <b>2027</b>. Applications for the 15 available licences close on <b>1 December 2026</b>, and "
  "the Department of Internal Affairs runs the assessment after that. Those will be the first genuinely "
  "new casinos New Zealand has had &mdash; domestically regulated, with a local complaints route. "
  "<a href='/nz-online-casino-law/'>The timeline</a>.</p>"),
 ("Are new casino sites better on mobile?",
  "<p>Usually, and it is the most underrated advantage. A 2024 launch is built on a current stack with a "
  "mobile-first lobby; an older brand is frequently a desktop site with a responsive layer bolted on. "
  "Since most play happens on a phone, a lobby whose filters and search actually work is worth more than "
  "another two thousand games you cannot find.</p>"),
]

PAA = [
 ("What is the newest online casino in New Zealand?",
  "<p>Seven of the nineteen brands we cover launched in 2024 &mdash; Kingdom, Smash, Rivo, MadCasino, "
  "CrownSlots, Roby and Spino. The table above lists every brand by launch year with what we have actually "
  "tested. The genuinely newest thing coming is the licensed cohort in 2027.</p>"),
 ("Are new casinos more likely to close down?",
  "<p>Yes, and it is a real consideration rather than a theoretical one. No offshore licence available to "
  "New Zealanders guarantees segregated player funds, so if an operator fails you are an unsecured "
  "creditor in a foreign jurisdiction. The defence is behavioural: keep the balance small and withdraw "
  "winnings rather than storing them. <a href='/fast-payout-casinos/#insolvency'>More on this</a>.</p>"),
 ("Do new casinos accept NZD?",
  "<p>Increasingly, yes &mdash; it has become a competitive necessity rather than a courtesy. Of the 2024 "
  "launches we cover, Kingdom, Smash, Rivo and MadCasino all bank in New Zealand dollars end to end. "
  "CrownSlots and Spino do not. A euro balance costs about 4.8% across the round trip regardless of how "
  "new or good the site is.</p>"),
 ("Should I wait for the licensed NZ casinos in 2027?",
  "<p>If your priority is recourse, yes &mdash; a domestic complaints route and DIA supervision are "
  "genuinely worth waiting for. But expect the licensed product to be <i>less</i> generous: duty, GST and "
  "the problem-gambling levy have to come from somewhere, so smaller bonuses and tighter RTP "
  "configurations are the likely trade.</p>"),
]

def build():
    ops = pick(NEW_2024)
    lb = leaderboard(ops, cta="Visit Casino")

    tbl = table(
      ["Casino", "Launched", "Licence", "NZD?", "Weekly cap", "Where it stands with us"],
      [[op_cell(BY[s]), f"<b>{y}</b>", lic,
        '<span class="chip chip--yes">Yes</span>' if "NZD bank transfer" in BY[s]["payments"]
        else '<span class="chip chip--no">No</span>',
        esc(BY[s]["withdrawal_limit"]), status]
       for s, y, lic, status in LAUNCHES],
      caption=f"Every casino in our set by launch year, newest first. Last checked {UPDATED_NZ} from a "
              f"New Zealand IP address. We add a brand here only after we have been paid by it.")

    tracker = table(
      ["Date", "What happens", "What it means for new casino sites"],
      [["<b>1 Dec 2026</b>", "Operators that have not applied for a New Zealand licence must stop serving New Zealanders",
        "Some of the sites on this page will exit. Withdraw rather than accumulate."],
       ["<b>1 Jan 2027</b>", "Offshore gambling duty rises from 12% to 16% of gross gambling revenue",
        "Expect welcome bonuses at newly licensed brands to be smaller than the 600% headlines here."],
       ["<b>Q1 2027 (est.)</b>", "First New Zealand licences issued; regulated market expected live",
        "The first genuinely licensed online casinos NZ has ever had. We list each as it launches."],
       ["<b>1 Jun 2027</b>", "Transitional arrangement ends outright for operators with pending applications",
        "After this the transition is over and unlicensed supply is simply unlawful."]],
      caption="The launch calendar for New Zealand's licensed market. Dates are from the Act and the "
              "DIA's published provider guidance; the Q1 2027 estimate is ours.")

    fh, fe = faq(FAQS, "New online casinos NZ &mdash; common questions", "faq")
    ph, pe = faq(PAA, "People also ask", "paa")

    body = f"""
{crumbs(TRAIL)}
{lede(h1=H1[PATH],
  lead="A running list of the newest online casinos New Zealanders can join, updated as each one "
       "launches. From December the first New Zealand-licensed operators start going live, and this "
       "page becomes the record of who arrived and when.",
  stats=[(f"{len(NEW_2024)}", "Sites launched in 2024, all tested"),
         ("15", "New licensed casinos due from 2027"),
         (f"{L.days_to(L.CUTOFF)} days", "Until the 1 December cutoff"),
         ("Monthly", "How often this list is re-checked")],
  eyebrow_txt=f"New casinos &middot; last checked {UPDATED_NZ}",
  author=AUTHOR, checker=CHECKER,
  toplist_h2="The newest online casinos NZ players can join",
  toplist_intro="Every brand here launched in 2024 and has paid us at least five tested withdrawals. "
                "New casino sites are ranked on the same six weights as everything else.",
  toplist_html=lb,
  toplist_note=note(
    '<p><b>What &ldquo;new&rdquo; is worth, and what it costs.</b> New online casinos NZ players can '
    'reach tend to arrive with bigger bonuses, better mobile builds and fresher game libraries, because '
    'that is how they buy attention. What they cannot offer is a track record. Everything on this page '
    'has paid us; none of it has been paying anyone for very long. '
    '<a href="#safe">How we judge a new casino</a>.', "gold"),
  jump_items=[("The newest sites", "ranked"), ("Launch tracker", "tracker"),
      ("Are new casinos safe?", "safe"), ("Before you join", "check"),
      ("Licensed launches from 2027", "licensed"), ("FAQ", "faq")])}

{sec(sechead("Every casino we rank, by launch year") + tbl, ident="tracker")}

{sec(f'''{sechead("Are new online casinos safe in NZ?", None, 2, "safe")}
<div class="prose">
<p>The honest answer is that age is close to the wrong question. A casino launched last year with a named
operating company and a resolvable licence is a safer proposition than a five-year-old brand that publishes
neither.</p>
<p>What a new site genuinely lacks is a <b>payout record</b> &mdash; evidence that it pays people, at
volume, under pressure, including after a large win. That evidence takes years to accumulate and cannot be
faked, which is why it is the one thing worth caring about and the one thing a launch cannot have.</p>
<h3>Most &ldquo;new&rdquo; casinos are not new</h3>
<p>This is the part that reframes the category. The great majority of launches in this market are fresh
<b>skins</b> on established infrastructure &mdash; same operator, same cashier, same support desk, new
brand and new artwork. Four groups run most of what New Zealanders can reach:</p>
<ul>
<li><b>Rabidi N.V.</b> &mdash; Spinjo, Lucky7even, Lucky Vibe, Lucky Circus, Bet&amp;Play</li>
<li><b>Dama N.V.</b> &mdash; Rooster Bet, Fortune Play</li>
<li><b>Vertikal N.V.</b> &mdash; Kingdom, Smash, Rivo, MadCasino</li>
<li><b>TechOptions Group</b> &mdash; Ivibet, Hellspin, Slotsgem</li>
</ul>
<p>A 2024 brand operated by a group with a multi-year record is a materially different risk from a
genuinely standalone launch by an entity nobody has heard of. The footer tells you which one you are
looking at, and almost nobody checks.</p>
{note('<p><b>The practical rule.</b> Judge a new casino on its group, its licence and its withdrawal '
      'terms &mdash; never on its launch year or the size of its opening bonus. Then buy yourself a '
      'payout record: deposit the minimum, play briefly, withdraw, and time it. Ten minutes and about '
      'NZ$20 gets you the one piece of evidence the site cannot otherwise give you.</p>', "info")}
</div>''', ident="safe", haze=True)}

{sec(f'''{sechead("New casinos versus established ones, honestly", None, 2, "vsold")}
<div class="prose">
<p>Every competitor page on this topic runs a version of &ldquo;why play at new casinos&rdquo; and lists
bigger bonuses, fresher software and better promotions. All three are usually true. None of them is the
reason to be careful, and none is the reason to be interested.</p>
</div>
{table(["", "New casino (under ~2 years)", "Established casino", "Which matters to you"],
  [["<b>Welcome offer</b>", "Larger, to buy market share", "More modest",
    "Least important. A bigger offer on the same multiplier demands more turnover, not less &mdash; "
    "<a href='/online-casinos/bonuses/'>see the ledger</a>"],
   ["<b>Software</b>", "Current stack, better mobile, faster lobby", "Often older, patched over",
    "Genuinely better. Mobile builds in particular"],
   ["<b>Payout track record</b>", "<b>None</b>", "Years of it", "<b>The one that actually matters</b>"],
   ["<b>Withdrawal terms</b>", "Untested under load", "Known and reviewable", "Read the cap before "
    "depositing either way"],
   ["<b>Licensing</b>", "Frequently Anjouan or newer regimes", "More often Cura&ccedil;ao GCB",
    "Check the register, not the launch year"],
   ["<b>Support</b>", "Small team, often quick", "Larger, more scripted", "New often wins early, then "
    "degrades as volume arrives"],
   ["<b>Risk of closure</b>", "Higher", "Lower", "Keep the balance small at either"]],
  caption="The honest summary: new casinos are usually better products and less proven operators. The "
          "software is the upside, the absent payout history is the risk, and the bonus is a distraction.")}
<div class="prose">
{note('<p><b>The point competitor pages omit.</b> A new casino has no record of paying people. That is not '
      'an accusation &mdash; it is simply the absence of evidence, and it is the single largest difference '
      'between a new site and an old one. Everything else on that table is a preference. This one is a '
      'risk, and the correct response is to keep the balance small and withdraw early rather than to avoid '
      'new sites altogether.</p>', "warn")}
</div>''', ident="vsold")}

{sec(f'''{sechead("What to check before joining a new casino", "Ten minutes, before you deposit rather "
  "than after you win.", 2, "checks")}
{steps([
  ("Find the operating company and resolve the licence",
   "A named legal entity with a registration number in the footer, and a licence number that returns that "
   "same company on the regulator&rsquo;s own register. New sites frequently launch with the seal image in "
   "place before the registration resolves &mdash; if it does not resolve, wait."),
  ("Identify the group behind it",
   "Most &lsquo;new&rsquo; casinos are new <i>skins</i> on established infrastructure. Rabidi N.V., Dama "
   "N.V., Vertikal N.V. and TechOptions Group operate several brands each. A brand launched in 2024 on a "
   "group with a five-year payout record is a very different proposition from a genuinely standalone "
   "launch, and the footer tells you which you are looking at."),
  ("Read the withdrawal section before the bonus section",
   "Weekly cap, processing windows, and whether the operator reserves a right to pay large wins in "
   "instalments. This is where a new site that intends to make cashing out difficult says so, in advance "
   "and in writing."),
  ("Price the welcome offer rather than admiring it",
   "New casinos compete on headline size, which our ledger consistently shows is the wrong axis. Multiply "
   "the bonus by the multiplier, apply the basis, and read the turnover figure."),
  ("Test the cashier with a small deposit and an immediate withdrawal",
   "The most useful ten minutes available. Deposit the minimum, play a little, withdraw the rest, and time "
   "it. You have bought a real payout record for the cost of a coffee &mdash; which is exactly the thing "
   "the site does not otherwise have."),
  ("Complete verification the same day",
   "Especially at a new site, where document handling processes are least mature. "
   "<a href='/fast-payout-casinos/#sof'>The document pack</a>."),
])}''', ident="checks", haze=True)}

{sec(f'''{sechead("What the 2027 licensed launches will actually look like", None, 2, "next")}
<div class="prose">
<p>This page becomes considerably more interesting in 2027, and it is worth setting expectations now
because the marketing will not.</p>
<p>Up to <b>15</b> licensed New Zealand operators will launch, with applications closing
<b>1 December 2026</b> &mdash; {L.days_to(L.CUTOFF)} days away. They will be genuinely new in the way that
matters: bound by New Zealand harm-minimisation rules, supervised by the Department of Internal Affairs,
and reachable through a domestic complaints route that does not exist for any site currently serving
Kiwis.</p>
<h3>What will be better</h3>
<ul>
<li>A regulator that can act on a licence, and somewhere local to escalate a refused withdrawal.</li>
<li>Deposit limits and self-exclusion that work to a New Zealand standard.</li>
<li>Requirements on how player funds are handled &mdash; the gap that currently leaves you an unsecured
creditor if an operator fails.</li>
</ul>
<h3>What will be worse, and nobody is saying so</h3>
<p>A licensed operator pays duty, GST and a problem-gambling levy, and that money comes from somewhere.
Expect <b>smaller bonuses and tighter RTP configurations</b> than the offshore market offers today. The
licensed product will be safer and, on pure value, more expensive.</p>
<p>For most players that is a good trade. It is still a trade, and you should hear it from us before you
hear it from an advertisement.</p>
{note('<p><b>What it means for this site.</b> The Act <b>prohibits affiliate marketing by licensed '
      'operators</b>. When these casinos launch, we will not be paid to send you to them &mdash; which '
      'means this page will become the part of the site with no commercial incentive behind it at all. We '
      'will keep publishing it. <a href="/nz-online-casino-law/">The regime in detail</a>.</p>', "info")}
</div>''', ident="next")}


{sec(f'''{sechead("New online casinos NZ players are actually searching for", None, 2, "variants")}
<div class="prose">
<p>A round-up of the specific searches that bring people here, answered in one place.</p>
<h3>New online casino NZ real money play</h3>
<p>Every brand in the table above accepts New Zealand registrations for real money play. For a new online
casino NZ real money account the shortlist worth having is the 2024 cohort banking in New Zealand dollars
&mdash; <a href="/casino-reviews/kingdom/">Kingdom</a>, <a href="/casino-reviews/smash/">Smash</a>,
<a href="/casino-reviews/rivo/">Rivo</a> and <a href="/casino-reviews/madcasino/">MadCasino</a>, all
operated by Vertikal N.V.</p>
<h3>Brand new online casinos NZ 2026 and the latest launches</h3>
<p>Brand new online casinos NZ 2026 listings go stale within weeks, which is why this page is a dated
tracker rather than a ranking. The latest online casinos NZ players can reach are in the table above with
their launch year and what we have tested. Upcoming online casinos NZ will arrive as a licensed cohort in
2027 rather than as a steady trickle.</p>
<h3>New pokie sites NZ and new casino sites with free spins NZ</h3>
<p>New pokie sites NZ and newest pokie sites New Zealand are, in practice, the same launches with the
lobby emphasised. What matters is which RTP build the new lobby licensed &mdash;
<a href="/online-pokies/#builds">check the information panel</a> before assuming a fresh site runs the good
version. New casino sites with free spins NZ almost always attach them to a deposit match, and a new online
casino free spins no deposit NZ offer is rarer still.</p>
<h3>New online casinos NZ no deposit bonus</h3>
<p>Uncommon. Among the brands here, <a href="/casino-reviews/lucky7even/">Lucky7even</a> carries the only
no-deposit offer we could verify live this month. A new casino no wagering bonus NZ side is rarer again
&mdash; <a href="/casino-reviews/spino/">Spino</a>&rsquo;s 0x crypto package is the only one we have
confirmed in this market.</p>
<h3>New crypto casinos NZ, and new NZ casinos accepting NZD</h3>
<p>New crypto casinos NZ launches now almost always support stablecoins from day one, because crypto
deposits cost the operator less to process. New NZ casinos accepting NZD have become the norm rather than
the exception &mdash; a launch that only holds euros in 2026 is choosing not to compete for New Zealand
players seriously.</p>
<h3>Newly licensed online casinos NZ &mdash; and new licensed casinos NZ December 2026</h3>
<p>There are none yet, and any page presenting a list of newly licensed online casinos NZ today is
describing something that does not exist. <b>1 December 2026 is an application deadline, not a launch
date.</b> New licensed casinos NZ December 2026 searches are looking for an event that happens in 2027.
We will add each licensed operator here as it goes live, with the date.</p>
</div>''', ident="variants", haze=True)}

{sec(f'<div class="prose">{fh}</div>', ident="faqsec")}
{sec(f'<div class="prose">{ph}</div>' + authorbox(AUTHOR), ident="paasec", haze=True)}


"""

    schema = [
        schema_webpage(PATH, META[PATH][0], META[PATH][1]),
        schema_breadcrumb(PATH, TRAIL),
        schema_article(PATH, META[PATH][0], META[PATH][1], AUTHOR, CHECKER),
        schema_person(AUTHOR), schema_person(CHECKER),
        schema_itemlist(PATH, ops),
        schema_faq(PATH, fe + pe),
    ]
    return write(PATH, page(PATH, body, schema), priority=0.85, freq="daily")
