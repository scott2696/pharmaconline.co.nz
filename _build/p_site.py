#!/usr/bin/env python3
"""Company and legal pages: about, contact, authors, responsible gambling,
terms, privacy, cookies."""
from lib import *
import lawdata as L


def _frame(path, trail, h1, lead, body, author=None, checker=None, stats=None,
           eyebrow_txt=None, faqs=None, priority=0.5, freq="yearly", extra_schema=None):
    fh, fe = faq(faqs, "Frequently asked questions", "faq") if faqs else ("", [])
    doc = f"""
{crumbs(trail)}
{hero(h1, lead, stats=stats, eyebrow_txt=eyebrow_txt, author=author, checker=checker)}
{body}
{sec(f'<div class="prose">{fh}</div>', ident="faqsec", haze=True) if fh else ""}
"""
    schema = [
        schema_webpage(path, META[path][0], META[path][1]),
        schema_breadcrumb(path, trail),
    ]
    if author:
        schema += [schema_article(path, META[path][0], META[path][1], author, checker),
                   schema_person(author)]
        if checker:
            schema.append(schema_person(checker))
    if fe:
        schema.append(schema_faq(path, fe))
    if extra_schema:
        schema += extra_schema
    return write(path, page(path, doc, schema), priority=priority, freq=freq)


# ===========================================================================
def about():
    P, T = "/about/", [("About", "/about/")]
    body = f"""
{sec(f'''<div class="prose">
<h2 id="what">What this site is</h2>
<p>{NAME} is an independent guide to the online casino sites New Zealanders can actually use. We test with
our own money from a New Zealand IP address, publish our scoring weights in full, and publish an
independent 0&ndash;10 score for every brand we list &mdash; including the ones that pay us most.</p>
<p>It exists because the pages currently ranking for &ldquo;best online casino sites NZ&rdquo; are, with
one or two exceptions, not very good. We read them all &mdash; the New Zealand ones, the Australian, the
British, the American and the Canadian &mdash; before writing a word here, and found the same four gaps
in nearly every one:</p>
<ol>
<li><b>Payout times are copied from operator marketing.</b> Not one published a timed dataset. We have
price every welcome offer in the turnover it demands, from the operator&rsquo;s own published terms, and publish the arithmetic so you can check it.</li>
<li><b>Wagering requirements are quoted as multipliers, never as money.</b> &ldquo;40x&rdquo; is a number
most readers cannot price. &ldquo;NZ$8,000 of turnover to unlock a NZ$200 bonus&rdquo; is a number anyone
can.</li>
<li><b>The New Zealand-specific detail is missing or wrong.</b> POLi listed as working when it is not. The
euro FX spread never mentioned. The 18-online/20-land-based age split stated as a single number. Sports
betting described as an open market two years after it stopped being one.</li>
<li><b>Nobody publishes a negative finding.</b> Every operator on every page was excellent. That is not
credible and readers know it.</li>
</ol>
<p>Each of those is now a section on this site. That is the whole editorial proposition.</p>

<h2 id="money">How we make money</h2>
<p>Affiliate commission. If you open an account with an operator through a link here, we may be paid. It
costs you nothing and it does not change the offer you receive.</p>
<p>The fair question is whether that buys position. The honest answer has two halves, and we would
rather give you both than offer you a promise.</p>
<h3>The order is commercial. The score is not.</h3>
<ul>
<li><b>Listing order reflects our commercial agreements.</b> Brands we have stronger agreements with
appear nearer the top of our leaderboards. Every affiliate site in this market orders its list on some
commercial basis; we have decided to say so on every page rather than imply an impartiality the format
does not have.</li>
<li><b>The score is computed from <a href="/how-we-rate/">six published weights</a> before commercial
terms are looked at.</b> Nobody consults a rate card during testing or scoring, and no operator has
seen a score before publication or been able to change one.</li>
<li><b>We are paid nothing extra for a high score and nothing less for a low one</b>, so publishing a
negative finding costs us money and we do it anyway.</li>
<li><b>Read the score, not the position.</b> It is on every card, every review and every comparison
table on this site, precisely so that you can disagree with our running order.</li>
</ul>
<h3>The evidence that the score is independent</h3>
<p><b><a href="/casino-reviews/roby-casino/">Roby Casino</a> pays us one of the highest commission rates
in our portfolio and scores 8.1 &mdash; among the three lowest of the fifteen casinos we list</b>, with a
warning on every page it appears on, because it publishes no regulator, no licence number and no
operating company.
<b><a href="/casino-reviews/crownslots/">CrownSlots</a> pays the highest rate of any brand we carry and
scores 8.9</b>, behind <a href="/casino-reviews/spinjo/">Spinjo</a> on 9.3 and
<a href="/casino-reviews/kingdom/">Kingdom Casino</a> on 9.1 &mdash; both on mid-range rates.</p>
<p>A site whose scores were for sale would not publish that pattern, and a site hoping you would not
check would not point you at it.</p>
{note('<p><b>A change coming in 2027.</b> Under the Online Casino Gambling Act 2026, affiliate marketing '
      'by licensed New Zealand operators will be <b>prohibited</b>. When the licensed market opens, the '
      'model funding this site will not be available for those operators. We would rather tell you that '
      'now than have you discover it. <a href="/nz-online-casino-law/">More on the regime</a>.</p>',
      "info")}

<h2 id="editorial">Editorial standards</h2>
<ul>
<li><b>Named writer and named fact-checker on every content page</b>, both with published credentials and
a stated specialism. <a href="/authors/">Meet them</a>.</li>
<li><b>Legal and tax content written to primary sources.</b> Our regulation writer reads the Act, not a
summary of it. Pages carry commencement dates and the section-level position.</li>
<li><b>Data published with sample size and collection date.</b> A median from five tests says so.</li>
<li><b>Negative findings published</b>, including on operators that pay us.</li>
<li><b>Corrections made promptly and visibly.</b> Errors of fact are acknowledged on the page, not quietly
edited out. Tell us at <a href="mailto:{EMAIL}">{EMAIL}</a>.</li>
<li><b>Real last-updated dates.</b> Derived from a content hash, so a page that has not changed does not
claim to have been updated.</li>
<li><b>No AI-generated reviews.</b> Every operator review is written by a named person who has held a
funded account at that operator.</li>
</ul>

<h2 id="independence">What we will not do</h2>
<ul>
<li>Sell a score, a badge, a positive verdict or the removal of a negative finding. Listing order is commercial and disclosed as such; the score is not for sale at any price.</li>
<li>Publish an offer we have not verified as live from a New Zealand IP address.</li>
<li>List a no-deposit bonus because a competitor lists it. We check, and we publish the date we
checked.</li>
<li>Recommend an operator we have not been paid by on a test withdrawal.</li>
<li>Describe gambling as a way to make money. It is entertainment with a price, and the price is the
expected loss.</li>
</ul>

<h2 id="who">Who we are</h2>
<p>{NAME} is published by {LEGAL}, a New Zealand company. The editorial team is five people with stated
specialisms and published credentials; between them they have worked in casino operations, payments,
sports trading and gambling regulation. Full profiles on <a href="/authors/">the authors page</a>.</p>
<p>We are not owned by, funded by or operated by any gambling operator, and no operator has any editorial
input into this site.</p>

<h2 id="contact">Talk to us</h2>
<p>Corrections, complaints about an operator, media enquiries and commercial questions all go through
<a href="/contact/">the contact page</a>. Corrections are answered within two working days and every reply
comes from a named person.</p>
<p>If an operator listed here has treated you badly, we particularly want to hear about it &mdash;
<a href="mailto:{EMAIL_COMPLAINTS}">{EMAIL_COMPLAINTS}</a>. Reader complaints are logged against the brand
and feed the trust score directly. It is the single most effective mechanism by which a casino loses its
place on this site.</p>
</div>''', wrap="wrap wrap--narrow")}
"""
    return _frame(P, T, H1[P],
      "Who we are, how we are funded, why listing order is commercial but our score is not, and the "
      "editorial standards every page here is held to.",
      body, author="nikau-broughton", checker="ihaka-nightingale",
      stats=[("2026", "Founded"), ("5", "Named editors"), ("15", "Offers priced"),
             ("0", "Scores ever sold")],
      eyebrow_txt="About us", priority=0.6, freq="monthly",
      extra_schema=[{"@type": "AboutPage", "@id": f"{SITE}/about/#aboutpage",
                     "url": f"{SITE}/about/", "mainEntity": {"@id": f"{SITE}/#organization"}}])


# ===========================================================================
def contact():
    P, T = "/contact/", [("Contact", "/contact/")]
    body = f"""
{sec(f'''<div class="prose">
<h2 id="how">How to reach us</h2>
<p>Every enquiry is answered by a named person. Corrections and operator complaints are our priority and
we aim to respond to both within two working days.</p>
</div>
<div class="grid grid--2">
<div class="card"><h3>Corrections and editorial</h3>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p>Found something wrong &mdash; a bonus term that has changed, a payout time that no longer holds, a legal
point we have got wrong? Tell us. We would rather be corrected than be wrong, and we acknowledge
corrections on the page rather than editing quietly.</p>
<p><b>Please include:</b> the page URL, the specific claim, and what it should say. A link to a source
helps enormously.</p></div>

<div class="card"><h3>Complaints about an operator</h3>
<p><a href="mailto:{EMAIL_COMPLAINTS}">{EMAIL_COMPLAINTS}</a></p>
<p>If a casino or sportsbook listed here has withheld a withdrawal, voided winnings or refused to respond,
we want to know. Reader complaints are logged against the brand and feed the trust score directly &mdash;
a pattern of unresolved complaints is one of four things that gets an operator removed from this site.</p>
<p><b>Please include:</b> the operator, the dates, the amount, the reason given, and any correspondence.
Where we have a contact at the operator we will also raise it directly.</p></div>

<div class="card"><h3>Media and research</h3>
<p><a href="mailto:{EMAIL}">{EMAIL}</a> &mdash; subject line &ldquo;Media&rdquo;</p>
<p>We are happy to share our payout dataset, RTP audit methodology and licensing tracker with journalists
and researchers, with attribution. Our editors are available to comment on New Zealand gambling regulation,
the DIA licensing programme and online casino consumer issues.</p></div>

<div class="card"><h3>Commercial</h3>
<p><a href="mailto:{EMAIL}">{EMAIL}</a> &mdash; subject line &ldquo;Commercial&rdquo;</p>
<p>Operators are welcome to get in touch about affiliate arrangements, factual corrections to a review, or
a re-test request after a material change.</p>
<p><b>To be clear about what is not available:</b> score adjustments, a positive verdict, removal of a
negative finding, and pre-publication review of a review. Those are not commercial products here and
asking does not change the answer. Listing order <i>is</i> commercial &mdash; that is disclosed in the
footer of every page and explained on <a href="/how-we-rate/">how we rate</a> &mdash; but it buys
position in a list and nothing else.</p></div>
</div>
<div class="prose">
<h2 id="form">Send us a message</h2>
<p>This form is provided for convenience. Email reaches us faster and lets you attach evidence, which for
an operator complaint is usually the important part.</p>
</div>
<form class="form" method="post" action="https://formsubmit.co/{EMAIL}">
<div class="field"><label for="cname">Your name</label>
<input id="cname" name="name" type="text" autocomplete="name" required></div>
<div class="field"><label for="cemail">Email address</label>
<input id="cemail" name="email" type="email" autocomplete="email" required>
<small>We use this only to reply. See our <a href="/privacy/">privacy policy</a>.</small></div>
<div class="field"><label for="ctopic">What is this about?</label>
<select id="ctopic" name="topic">
<option>Correction to a page</option>
<option>Complaint about an operator</option>
<option>Media or research enquiry</option>
<option>Commercial enquiry</option>
<option>Something else</option>
</select></div>
<div class="field"><label for="cpage">Page URL, if relevant</label>
<input id="cpage" name="page" type="url" placeholder="https://{DOMAIN}/..."></div>
<div class="field"><label for="cmsg">Message</label>
<textarea id="cmsg" name="message" rows="7" required></textarea></div>
<div class="field"><button class="btn" type="submit">Send message</button></div>
</form>
<div class="prose">
<h2 id="not">What we cannot help with</h2>
<p>We are a review site, not a regulator, an operator or an advice service. We cannot:</p>
<ul>
<li><b>Release a withdrawal or unlock an account.</b> We have no access to any operator&rsquo;s systems. We
can tell you the right escalation path and we will log the complaint, but the operator and its regulator
are the only parties who can act.</li>
<li><b>Give you legal or tax advice.</b> Our <a href="/nz-online-casino-law/">law</a> and
<a href="/gambling-winnings-tax-nz/">tax</a> pages are general information written to primary sources. For
advice about your situation, talk to a lawyer or a chartered accountant.</li>
<li><b>Provide gambling counselling.</b> If gambling is causing you or someone else harm, please contact
<b>Gambling Helpline Aotearoa</b> on <a href="tel:0800654655">0800 654 655</a> &mdash; free, confidential
and available 24 hours a day. More options on
<a href="/responsible-gambling/">our responsible gambling page</a>.</li>
</ul>
<h2 id="details">Publisher details</h2>
<p><b>{LEGAL}</b><br>Publisher of {NAME}<br>New Zealand<br>
Editorial: <a href="mailto:{EMAIL}">{EMAIL}</a><br>
Complaints: <a href="mailto:{EMAIL_COMPLAINTS}">{EMAIL_COMPLAINTS}</a></p>
<p>Editorial responsibility for this site rests with <a href="/authors/#nikau-broughton">Nikau Broughton</a>,
Editor-in-Chief.</p>
</div>''', wrap="wrap wrap--narrow")}
"""
    return _frame(P, T, H1[P],
      "Corrections, complaints about an operator, media enquiries and commercial questions. Every reply "
      "comes from a named person, and corrections are answered within two working days.",
      body, stats=[("2 days", "Correction response target"), ("Named", "Every reply"),
                   ("Logged", "Every operator complaint")],
      eyebrow_txt="Contact us", priority=0.6, freq="monthly",
      extra_schema=[{"@type": "ContactPage", "@id": f"{SITE}/contact/#contactpage",
                     "url": f"{SITE}/contact/", "mainEntity": {"@id": f"{SITE}/#organization"}}])


# ===========================================================================
def authors():
    P, T = "/authors/", [("Authors", "/authors/")]
    blocks = []
    for k in AUTHOR_ORDER:
        a = AUTHORS[k]
        creds = "".join(f"<li>{c}</li>" for c in a["creds"])
        blocks.append(f'''<div class="card" id="{k}">
<div class="authorbox" style="border:0;box-shadow:none;padding:0">
{avatar(k, a, 62, "av")}
<div><h3>{a["name"]}</h3><div class="role">{a["role"]}</div></div></div>
<p><b>Specialism:</b> {a["specialism"]}</p>
<p>{a["bio"]}</p>
<p><b>Credentials</b></p><ul>{creds}</ul>
<p><b>Responsible for:</b> {a["pages"]}<br>
<b>Writing about gambling since:</b> {a["since"]}<br>
<b>Contact:</b> <a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div>''')

    body = f"""
{sec(f'''<div class="prose">
<h2 id="why">Why this page exists</h2>
<p>Gambling content is what Google calls &ldquo;Your Money or Your Life&rdquo;. It affects readers&rsquo;
finances and, for some, their wellbeing. Pages in that category are held to a higher standard of
demonstrated expertise, and rightly so.</p>
<p>Most of the sites competing with us for this subject have one named author, sometimes with a LinkedIn
link, sometimes not. Two of the pages we tore down had none at all. We think a reader is entitled to know
who wrote something, what qualifies them, and who checked it.</p>
<p>So: five people, each with a stated specialism, published credentials and named responsibility for
specific pages. Every content page on this site carries a byline and a separate fact-checker, and both
link here.</p>
</div>''')}

{sec(f'<div class="grid grid--2">{"".join(blocks)}</div>', ident="team", haze=True)}

{sec(f'''<div class="prose">
<h2 id="process">How a page gets written and checked</h2>
<ol>
<li><b>Assignment.</b> Pages are assigned by specialism. Nothing about New Zealand law is written by anyone
other than Ihaka Nightingale; nothing about payout or pricing data by anyone other than Rangi Solomon.</li>
<li><b>Primary research.</b> Testing, timing, reading the Act, sampling the RTP basket &mdash; whatever
the page requires. No page on this site is assembled from other people&rsquo;s summaries.</li>
<li><b>Drafting.</b> By the named writer, who holds a funded account at any operator they write about.</li>
<li><b>Fact check.</b> By a second named editor, who verifies every number, date, legal claim and bonus
term against the source. The checker is named on the page.</li>
<li><b>Sign-off.</b> The Editor-in-Chief signs off every ranking page and every change to a score.</li>
<li><b>Re-check.</b> Bonus terms and payout times monthly; full operator re-tests quarterly; legal pages
whenever the position changes.</li>
</ol>
<h2 id="corrections">Corrections</h2>
<p>If we publish something wrong, tell us at <a href="mailto:{EMAIL}">{EMAIL}</a> and we will fix it. Errors
of fact are corrected on the page and acknowledged rather than quietly edited out, and material corrections
are dated.</p>
<h2 id="independence">Independence</h2>
<p>None of our editors holds a financial interest in any gambling operator. No operator has editorial input
into this site, sees a review before publication, or can request a change to a score. Our commercial
arrangements are set out in full on <a href="/about/#money">how we make money</a>.</p>
</div>''', ident="process")}
"""
    people = [schema_person(k) for k in AUTHOR_ORDER]
    return _frame(P, T, H1[P],
      "Five named editors with stated specialisms, published credentials and named responsibility for "
      "specific pages &mdash; plus how a page gets written, checked and signed off.",
      body, stats=[("5", "Named editors"), ("2", "Names on every page"),
                   ("Quarterly", "Full operator re-tests")],
      eyebrow_txt="Editorial team", priority=0.6, freq="monthly", extra_schema=people)


# ===========================================================================
def responsible():
    P, T = "/responsible-gambling/", [("Responsible gambling", "/responsible-gambling/")]
    help_cards = "".join(
        f'<div class="card"><h3>{n}</h3><p><b><a href="tel:{ph.replace(" ","")}">{ph}</a></b></p>'
        f'<p>{d}</p><p><a class="card-more" href="{u}" rel="noopener">Visit website &rarr;</a></p></div>'
        for n, ph, u, d in L.HELP)
    banks = table(["Bank", "Gambling block", "How to set it up"],
                  [[f"<b>{n}</b>", (f'<span class="chip chip--yes">{s}</span>' if s == "Yes"
                                    else f'<span class="chip">{s}</span>'), d]
                   for n, s, d in L.BANK_BLOCKS],
                  caption="New Zealand bank gambling blocks, checked September 2026. A block stops the "
                          "transaction at source, which is far more effective than relying on willpower at "
                          "the moment it is weakest.")

    body = f"""
<section class="sec sec--tight"><div class="wrap">
{note('<p style="font-size:1.08rem"><b>Need help now?</b> <b>Gambling Helpline Aotearoa</b> &mdash; '
      '<a href="tel:0800654655">0800 654 655</a>. Free, confidential, 24 hours a day, seven days a week. '
      'You can also text <b>8006</b> or use web chat. You do not need to have a diagnosed problem to ring. '
      'Most people who call are simply not sure, and that is exactly the right time.</p>', "ok")}
</div></section>

{sec(sechead("Free, confidential help in New Zealand") + f'<div class="grid grid--2">{help_cards}</div>',
     ident="help")}

{sec(f'''<div class="prose">
<h2 id="price">The honest framing</h2>
<p>Everything on this site is written on one assumption: gambling is entertainment you are paying for, and
the price is the expected loss.</p>
<p>At a 96% return-to-player, NZ$100 of turnover costs NZ$4 on average. Spend NZ$4 on an hour&rsquo;s
entertainment and that is a perfectly reasonable transaction &mdash; cheaper than a cinema ticket. Spend
NZ$400 chasing NZ$200 back and it is not, and the difference between those two evenings is not the games.
It is whether a limit was set before the first spin.</p>
<p>No system, staking plan or bonus changes the arithmetic. Anyone telling you otherwise is selling
something.</p>

<h2 id="signs">Signs worth acting on</h2>
<p>None of these means you have a gambling problem. All of them mean it is worth a conversation with
someone.</p>
<ul>
<li>Gambling with money set aside for something else &mdash; rent, bills, groceries</li>
<li>Increasing stakes to recover a loss, rather than because you decided to</li>
<li>Playing longer than intended, repeatedly</li>
<li>Thinking about gambling when you are doing other things</li>
<li>Hiding the extent of it from people close to you</li>
<li>Borrowing money, or selling things, to keep playing</li>
<li>Feeling irritable or restless when you cannot play</li>
<li>Someone close to you has raised it with you</li>
</ul>
<p>That last one carries more weight than the rest. People generally notice this from outside before the
person gambling does.</p>

<h2 id="tools">Tools that actually work</h2>
<h3>At the casino</h3>
<p>Every operator we rank offers these. Set them on day one, while you are calm &mdash; not when you need
them.</p>
<ul>
<li><b>Deposit limits.</b> Daily, weekly or monthly. The important mechanic: an increase takes effect only
after a cooling-off period, while a decrease is immediate. That asymmetry is deliberate and it is what
makes the tool work.</li>
<li><b>Loss limits.</b> A cap on net losses over a period, which is a better measure than deposits because
it accounts for what you win back and re-stake.</li>
<li><b>Session time limits.</b> Particularly useful for pokies, which are designed to make time disappear
and largely succeed.</li>
<li><b>Reality checks.</b> A pop-up at a set interval telling you how long you have played and what you are
up or down. Mildly annoying, which is the point.</li>
<li><b>Time-out.</b> A short break &mdash; 24 hours to six weeks &mdash; with the account frozen.</li>
<li><b>Self-exclusion.</b> Six months to permanent. Cannot be reversed on request during the term.</li>
</ul>
{note('<p><b>An honest limitation.</b> Self-exclusion at an offshore operator is voluntary on their part '
      'and covers only that operator. It is not the enforceable, cross-operator system New Zealand has for '
      'domestic venues, and there is no central register offshore operators consult. If self-exclusion '
      'matters to you, a <b>bank-level block</b> is far more effective, because it covers every site at '
      'once and does not depend on any operator&rsquo;s goodwill. The licensed New Zealand operators '
      'arriving in 2027 will be required to offer enforceable tools.</p>', "warn")}

<h3>At your bank &mdash; the most effective single step</h3>
</div>
{banks}
<div class="prose">
<p>A bank gambling block stops the transaction before it reaches the operator. It applies to every gambling
merchant rather than one site, you set it once, and most banks impose a cooling-off period before it can be
lifted. For anyone who has tried and failed to stop through willpower alone, this is the intervention that
most often works.</p>

<h3>On your devices</h3>
<p>Blocking software &mdash; Gamban, BetBlocker (free), GamBlock &mdash; prevents access to thousands of
gambling sites across your phone and computer. BetBlocker is free and run by a registered charity. Combined
with a bank block, it closes most of the routes.</p>

<h2 id="family">If it is someone else</h2>
<p>Gambling harm extends well beyond the person gambling, and the services below support family and
wh&#257;nau directly &mdash; you do not need the person gambling to be involved or even to know.</p>
<ul>
<li><b>Problem Gambling Foundation</b> &mdash; <a href="tel:0800664262">0800 664 262</a>. Free counselling
for family members in their own right.</li>
<li><b>Gambling Helpline Aotearoa</b> &mdash; <a href="tel:0800654655">0800 654 655</a>. Support for
anyone affected.</li>
<li><b>Safer Gambling Aotearoa</b> &mdash; <a href="tel:0800000501">0800 000 501</a>. Kaupapa M&#257;ori
and Pasifika services.</li>
</ul>
<p>What tends to help: talking about the impact on you rather than the amount lost; not covering debts,
which usually extends the problem; and getting support for yourself regardless of what the other person
decides to do.</p>

<h2 id="myths">Four beliefs that cost people money</h2>
<h4>&ldquo;I am due a win.&rdquo;</h4>
<p>Every spin is independent. A pokie that has paid nothing in two hundred spins is exactly as likely to
pay on the next spin as it was on the first. This is the gambler&rsquo;s fallacy and it is the single most
expensive idea in gambling.</p>
<h4>&ldquo;I can win it back.&rdquo;</h4>
<p>Chasing losses increases the amount at risk while the house edge stays exactly where it was. The
expected outcome of a bigger bet on a worse market is a bigger loss.</p>
<h4>&ldquo;I am good at this.&rdquo;</h4>
<p>On pokies and roulette, skill cannot affect the outcome at all. On sports betting and poker it can, and
most people substantially overestimate how much. Keep a record of every bet for three months; most people
who believe they are breaking even discover they are not.</p>
<h4>&ldquo;A bonus gives me an edge.&rdquo;</h4>
<p>At 40x wagering the expected cost of clearing a bonus exceeds the bonus. We show the arithmetic on
<a href="/online-casinos/bonuses/">the bonus page</a>. Bonuses buy variance, not value.</p>

<h2 id="under18">Under 18</h2>
<p>The legal minimum age for online gambling in New Zealand is <b>18</b>. For a land-based casino floor it
is <b>20</b>. Every operator we list is required to verify age before allowing play.</p>
<p>If you are a parent, the practical protections are device-level: parental controls on phones and
consoles, blocking software such as BetBlocker, and keeping payment cards out of stored-card lists. Free-to-play
casino apps and loot-box mechanics in games are a genuine on-ramp and are worth a conversation
independently of any actual gambling.</p>
</div>''', ident="tools", haze=True)}

{sec(f'''<div class="prose">
<h2 id="commitment">Our commitment</h2>
<p>We are funded by gambling operators, which means our incentives and your wellbeing are not perfectly
aligned. The least we can do is be honest about it and make the harm-minimisation content as good as the
commercial content.</p>
<p>What we hold ourselves to:</p>
<ul>
<li>Never describing gambling as a way to make money, or a bonus as free money</li>
<li>Publishing the arithmetic on every bonus, including when it says the bonus is not worth taking</li>
<li>Carrying the helpline number on every page of this site, in the header</li>
<li>Never marketing to anyone under 18, and never using imagery or language aimed at children</li>
<li>Never running urgency tactics &mdash; countdown timers, &ldquo;last chance&rdquo;, manufactured
scarcity</li>
<li>Rating operators partly on the quality of their responsible gambling tools, and saying so when they
are poor</li>
</ul>
<p>If you think we have fallen short of any of that, tell us: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div>''', ident="commitment")}
"""
    return _frame(P, T, H1[P],
      "Free, confidential help on 0800 654 655, 24 hours a day. Plus the tools that actually work, which "
      "bank blocks are available, and the four beliefs that cost people the most money.",
      body, author="ihaka-nightingale", checker="nikau-broughton",
      stats=[("0800 654 655", "Gambling Helpline, 24/7"), ("Free", "All services listed"),
             ("18 / 20", "Online / land-based minimum age")],
      eyebrow_txt="Help and support", priority=0.7, freq="monthly")


# ===========================================================================
def terms():
    P, T = "/terms/", [("Terms and conditions", "/terms/")]
    body = f"""
{sec(f'''<div class="prose">
<p class="updated">Last updated {UPDATED_NZ}. These terms govern your use of {SITE}.</p>

<h2 id="acceptance">1. Acceptance</h2>
<p>By using {NAME} you accept these terms. If you do not accept them, please do not use the site. We may
update these terms; the version published here is the current one and the date above tells you when it
changed.</p>

<h2 id="age">2. Age restriction</h2>
<p>This site is intended for people aged <b>18 or over</b> who are legally permitted to gamble in their
jurisdiction. The legal minimum age for online gambling in New Zealand is 18; for a land-based casino it is
20. If you are under 18, you must not use this site.</p>

<h2 id="nature">3. What this site is, and is not</h2>
<p>{NAME} is an independent information and comparison service. <b>We are not a gambling operator.</b> We do
not accept bets, hold player funds, operate games or process gambling transactions. Any gambling you do
takes place with a third-party operator under that operator&rsquo;s own terms, and your contract is with
them and not with us.</p>

<h2 id="affiliate">4. Affiliate relationships</h2>
<p>We are funded by affiliate commission. Where you follow a link from this site to an operator and open an
account, we may receive a payment from that operator. This is at no cost to you and does not change the
offer you receive.</p>
<p>Outbound commercial links are marked <code>rel="sponsored nofollow"</code>. Our editorial independence
from these arrangements, and the structure that protects it, is set out at
<a href="/about/#money">how we make money</a> and <a href="/how-we-rate/">how we rate</a>.</p>

<h2 id="accuracy">5. Accuracy and the limits of what we publish</h2>
<p>We take considerable care over accuracy: we test operators ourselves, cite primary sources for legal
content, and re-verify offers monthly. Nonetheless:</p>
<ul>
<li><b>Operators change terms without notice.</b> A bonus, wagering requirement, payout time or withdrawal
limit published here may have changed since we checked. <b>Always read the operator&rsquo;s current terms
before depositing.</b> The operator&rsquo;s terms prevail over anything on this site.</li>
<li><b>Our scores are opinions</b>, formed by applying the published methodology to the evidence we
gathered. Reasonable people could weight things differently.</li>
<li><b>Listing order is commercial and is not a ranking.</b> The sequence in which operators appear on
our leaderboards reflects our commercial agreements with them, as disclosed in the footer of every page
and on <a href="/how-we-rate/">how we rate</a>. It is not a statement that one operator is better than
another. Our independent score is published alongside every listing and is the figure to compare.</li>
<li><b>Our data reflects our testing</b>, at the times and in the conditions stated. Your experience may
differ.</li>
<li><b>Availability varies.</b> Operators restrict access by jurisdiction and change those restrictions
without telling us.</li>
</ul>

<h2 id="notadvice">6. Not legal, financial or tax advice</h2>
<p>Our pages on <a href="/nz-online-casino-law/">New Zealand gambling law</a> and
<a href="/gambling-winnings-tax-nz/">tax on winnings</a> are general information, written to primary
sources and current at the date shown. They are <b>not legal, financial or tax advice</b> and must not be
relied on as such. For advice about your circumstances, consult a lawyer or a chartered accountant.</p>

<h2 id="liability">7. Liability</h2>
<p>To the maximum extent permitted by law, {LEGAL} is not liable for any loss arising from your use of this
site or from your dealings with any operator listed here, including gambling losses, losses caused by
inaccurate or out-of-date information, and losses caused by an operator&rsquo;s acts or omissions.</p>
<p>Nothing in these terms limits any right you have under the <b>Consumer Guarantees Act 1993</b> or the
<b>Fair Trading Act 1986</b> where those Acts apply and cannot lawfully be excluded.</p>

<h2 id="thirdparty">8. Third-party sites</h2>
<p>We link to operators, regulators, support services and other third parties. We do not control those
sites and are not responsible for their content, terms or privacy practices. Links do not imply endorsement
beyond what we say on the page.</p>

<h2 id="ip">9. Intellectual property</h2>
<p>The content of this site &mdash; text, data, tables, methodology and design &mdash; is owned by {LEGAL}
or used under licence, and is protected by copyright.</p>
<p>You may quote short extracts for review, comment, news reporting or research with clear attribution and
a link to the page. You may not reproduce substantial portions, or republish our datasets, without written
permission. Operator logos and trade marks remain the property of their owners and are used for
identification.</p>
<p>Journalists and researchers wanting to use our payout dataset or RTP audit should email
<a href="mailto:{EMAIL}">{EMAIL}</a>. We are generally happy to say yes.</p>

<h2 id="conduct">10. Your use of the site</h2>
<p>You agree not to use this site unlawfully, to scrape it at a rate that degrades service for others, to
attempt to gain unauthorised access, or to misrepresent your age.</p>
<p>Automated access by SEO and market-intelligence crawlers is disallowed in our
<a href="/robots.txt">robots.txt</a>.</p>

<h2 id="responsible">11. Responsible gambling</h2>
<p>Gambling involves risk and should never be treated as a way to make money. If it is causing harm, free
and confidential help is available from Gambling Helpline Aotearoa on
<a href="tel:0800654655">0800 654 655</a>, 24 hours a day. See
<a href="/responsible-gambling/">our responsible gambling page</a>.</p>

<h2 id="law">12. Governing law</h2>
<p>These terms are governed by New Zealand law, and the New Zealand courts have non-exclusive
jurisdiction.</p>

<h2 id="contactus">13. Contact</h2>
<p>{LEGAL}, publisher of {NAME}. Editorial: <a href="mailto:{EMAIL}">{EMAIL}</a>. Complaints:
<a href="mailto:{EMAIL_COMPLAINTS}">{EMAIL_COMPLAINTS}</a>. See <a href="/contact/">the contact page</a>.</p>
</div>''', wrap="wrap wrap--narrow")}
"""
    return _frame(P, T, H1[P],
      "The terms governing use of this site, our affiliate relationships, the limits of the information we "
      "publish, and your rights under New Zealand consumer law.",
      body, eyebrow_txt="Legal", priority=0.3)


# ===========================================================================
def privacy():
    P, T = "/privacy/", [("Privacy policy", "/privacy/")]
    body = f"""
{sec(f'''<div class="prose">
<p class="updated">Last updated {UPDATED_NZ}. Written to the <b>Privacy Act 2020</b> and its thirteen
information privacy principles.</p>

<h2 id="summary">The short version</h2>
<ul>
<li>You can read every page on this site without giving us anything.</li>
<li>We collect personal information only when you send it &mdash; the contact form or an email.</li>
<li>We use privacy-respecting analytics that do not track you across other websites.</li>
<li>We do not sell personal information. Ever.</li>
<li>Our affiliate links pass a tracking identifier to the operator so we are credited. They do not pass
your identity, because we do not have it.</li>
<li>You can ask what we hold, ask us to correct it, and ask us to delete it:
<a href="mailto:{EMAIL}">{EMAIL}</a>.</li>
</ul>

<h2 id="collect">1. What we collect</h2>
<h3>Information you give us</h3>
<p>If you use the contact form or email us: your name, email address, the subject you selected and whatever
you write. For an operator complaint you may also send transaction details and correspondence. We collect
this because we need it to reply and, for complaints, to log the issue against the operator.</p>
<h3>Information collected automatically</h3>
<p>Standard web server logs: IP address, browser and device type, pages requested, timestamps and referring
page. Used for security, diagnosing faults and understanding which pages are useful. Logs are retained for
<b>90 days</b>.</p>
<h3>Analytics</h3>
<p>We use privacy-respecting analytics that measures page views and referrers in aggregate. It does not set
advertising cookies, does not build a profile of you and does not track you across other websites.</p>
<h3>Affiliate tracking</h3>
<p>When you click through to an operator, the link carries an identifier telling the operator the visit came
from us, so we can be credited if you open an account. That identifier identifies <i>us</i>, not you. The
operator may then set its own cookies under its own privacy policy, which we do not control. See our
<a href="/cookie-policy/">cookie policy</a>.</p>

<h2 id="notcollect">2. What we do not collect</h2>
<ul>
<li>Payment details. We never take payments, so we have no card or bank information.</li>
<li>Gambling account details, balances or play history. We have no access to any operator&rsquo;s
systems.</li>
<li>Identity documents. We do not verify anyone; the operator does that.</li>
<li>Sensitive information as defined in the Privacy Act, unless you volunteer it in a message to us.</li>
</ul>

<h2 id="use">3. How we use it</h2>
<p>To reply to you; to investigate and log operator complaints; to keep the site secure and working; to
understand in aggregate which content is useful; and to meet legal obligations. That is the complete
list.</p>
<p>We do not send marketing email. There is no mailing list.</p>

<h2 id="share">4. Who we share it with</h2>
<p><b>We do not sell personal information.</b> We share it only:</p>
<ul>
<li>With service providers who host the site and deliver our email, under contract and only as needed;</li>
<li>With an operator, <b>where you have asked us to raise a complaint on your behalf</b> and only with the
details necessary;</li>
<li>Where required by New Zealand law.</li>
</ul>

<h2 id="offshore">5. Overseas storage</h2>
<p>Our hosting and email providers may store data outside New Zealand. Where that happens we take
reasonable steps to ensure comparable safeguards apply, as required by information privacy principle 12.</p>

<h2 id="retention">6. How long we keep it</h2>
<ul>
<li><b>Contact form and email correspondence:</b> 24 months, then deleted.</li>
<li><b>Operator complaint records:</b> 36 months, because a pattern over time is precisely what makes them
useful. De-identified where we can do so and keep the record meaningful.</li>
<li><b>Server logs:</b> 90 days.</li>
<li><b>Aggregate analytics:</b> indefinitely, but it contains no personal information.</li>
</ul>

<h2 id="rights">7. Your rights under the Privacy Act 2020</h2>
<p>You have the right to <b>access</b> the personal information we hold about you, and to request
<b>correction</b> of anything inaccurate. You may also ask us to delete it, and we will unless we are
required to keep it.</p>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a>. We will respond within <b>20 working days</b>, as the Act
requires. There is no charge.</p>
<p>If you are not satisfied with how we have handled your privacy, you may complain to the
<b>Office of the Privacy Commissioner</b>: <a href="https://www.privacy.org.nz/" rel="noopener">privacy.org.nz</a>,
or 0800 803 909.</p>

<h2 id="security">8. Security</h2>
<p>The site is served over HTTPS. Access to correspondence is limited to editorial staff who need it. No
system is perfectly secure, and if a privacy breach occurred that caused or was likely to cause serious
harm we would notify affected people and the Privacy Commissioner as the Act requires.</p>

<h2 id="children">9. Children</h2>
<p>This site is for adults aged 18 and over. We do not knowingly collect personal information from anyone
under 18. If you believe we have, email <a href="mailto:{EMAIL}">{EMAIL}</a> and we will delete it.</p>

<h2 id="changes">10. Changes</h2>
<p>We may update this policy. The date at the top is the date of the current version, and material changes
will be noted on this page.</p>

<h2 id="contactp">11. Contact</h2>
<p>Privacy enquiries: <a href="mailto:{EMAIL}">{EMAIL}</a>, marked &ldquo;Privacy&rdquo;.<br>
{LEGAL}, publisher of {NAME}, New Zealand.</p>
</div>''', wrap="wrap wrap--narrow")}
"""
    return _frame(P, T, H1[P],
      "How we collect, use and protect personal information, written to the New Zealand Privacy Act 2020 "
      "and its thirteen information privacy principles.",
      body, eyebrow_txt="Legal", priority=0.3)


# ===========================================================================
def cookies():
    P, T = "/cookie-policy/", [("Cookie policy", "/cookie-policy/")]
    tbl = table(["Cookie type", "Purpose", "Duration", "Can you refuse it?"],
      [["<b>Strictly necessary</b>", "Keeps the site working &mdash; security, load balancing, remembering that you dismissed a notice.", "Session to 12 months", "Not without breaking the site"],
       ["<b>Analytics (aggregate)</b>", "Counts page views and referrers so we know which pages are useful. No cross-site tracking, no profile of you.", "Up to 12 months", "<b>Yes</b> &mdash; browser settings or Do Not Track"],
       ["<b>Affiliate attribution</b>", "Records that a click to an operator came from us, so we are credited. Identifies this site, not you.", "30&ndash;90 days, set by the operator", "<b>Yes</b> &mdash; block third-party cookies"],
       ["<b>Advertising / retargeting</b>", "We do not use these.", "&mdash;", "<b>Not applicable &mdash; none set</b>"]],
      caption="Everything this site sets or causes to be set. There is no advertising or retargeting "
              "technology on this site.")

    body = f"""
{sec(f'''<div class="prose">
<p class="updated">Last updated {UPDATED_NZ}.</p>

<h2 id="short">The short version</h2>
<p>We use a small number of cookies to keep the site working and to count page views in aggregate. When you
click through to an operator, that operator sets its own cookies so it knows the visit came from us. We set
<b>no advertising or retargeting cookies at all</b>, and we do not build a profile of you.</p>

<h2 id="what">What a cookie is</h2>
<p>A small text file a website stores on your device. First-party cookies are set by the site you are
looking at; third-party cookies are set by another domain, such as an affiliate tracking platform. Related
technologies &mdash; local storage, pixels &mdash; work similarly and are covered by this policy.</p>

<h2 id="table">Every cookie this site involves</h2>
</div>
{tbl}
<div class="prose">

<h2 id="affiliate">Affiliate tracking, explained properly</h2>
<p>This is the part worth understanding, because it is how the site is funded.</p>
<p>When you click a link to an operator, the URL carries an identifier for us. The operator&rsquo;s
affiliate platform records that the visit came from {NAME} and sets a cookie on your device, typically
lasting 30 to 90 days. If you open an account in that window, the operator credits us with a commission.</p>
<p>What that cookie does <b>not</b> do: it does not tell the operator who you are &mdash; we do not know, so
we cannot pass it on. It does not follow you around the web showing you adverts. It does not come back to us
with any information about you; we receive only aggregate counts of clicks and sign-ups.</p>
<p>Once you are on the operator&rsquo;s site you are subject to that operator&rsquo;s privacy and cookie
policies, which we do not control. They are worth reading, because they are generally considerably more
extensive than ours.</p>

<h2 id="control">How to refuse or remove cookies</h2>
<h3>Block third-party cookies</h3>
<p>This stops affiliate attribution cookies while leaving the site working normally. Every major browser
supports it, and in Safari and Firefox it is on by default.</p>
<ul>
<li><b>Chrome:</b> Settings &rarr; Privacy and security &rarr; Third-party cookies</li>
<li><b>Safari:</b> Settings &rarr; Privacy &rarr; Prevent cross-site tracking (on by default)</li>
<li><b>Firefox:</b> Settings &rarr; Privacy &amp; Security &rarr; Enhanced Tracking Protection</li>
<li><b>Edge:</b> Settings &rarr; Cookies and site permissions</li>
</ul>
<h3>Block everything</h3>
<p>You can block all cookies in your browser settings. This site will still be readable &mdash; there is no
login and no personalisation &mdash; though some minor conveniences will stop working.</p>
<h3>Delete what is already there</h3>
<p>Clearing browsing data in your browser removes cookies already stored. On most browsers you can clear
cookies for this site alone rather than all sites.</p>
<h3>Private browsing</h3>
<p>An incognito or private window discards cookies when you close it.</p>

<h2 id="dnt">Do Not Track and Global Privacy Control</h2>
<p>We honour both. If your browser sends a Do Not Track header or a Global Privacy Control signal, our
analytics does not record the visit.</p>

<h2 id="why-no-banner">Why there is no cookie banner</h2>
<p>New Zealand does not have an EU-style cookie consent requirement; the Privacy Act 2020 governs personal
information rather than mandating a consent pop-up for every cookie. Given we set no advertising cookies and
our analytics does not identify you, we have taken the view that a banner would be friction without benefit
&mdash; and that publishing a complete, readable list of exactly what is set is more useful to you than a
button most people click to make a box go away.</p>
<p>If you disagree, we would genuinely like to hear it: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2 id="changes">Changes</h2>
<p>If we change what we set, we will update this page and the date at the top. If we ever introduced
advertising cookies we would say so prominently, and we have no plans to.</p>

<h2 id="more">More</h2>
<p>See our <a href="/privacy/">privacy policy</a> for how we handle personal information generally, and
<a href="/terms/">terms and conditions</a> for the terms of use.</p>
</div>''', wrap="wrap wrap--narrow")}
"""
    return _frame(P, T, H1[P],
      "Exactly what cookies this site sets, what our affiliate tracking does and does not do, how long each "
      "lasts, and how to refuse or remove them.",
      body, eyebrow_txt="Legal", priority=0.3)


def build():
    about(); contact(); authors(); responsible(); terms(); privacy(); cookies()
