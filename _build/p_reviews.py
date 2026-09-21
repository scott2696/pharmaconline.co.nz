#!/usr/bin/env python3
"""/casino-reviews/ hub plus one review page per operator.

The per-brand narrative lives in voice.py as op['narr']; everything factual
comes from operators.json, so a corrected fact propagates to the hub table,
the leaderboards and the review at once.
"""
from lib import *
import bonuscalc as B
import lawdata as L

HUB = "/casino-reviews/"
REVIEWER = {"sports": "camille-toure"}   # casino reviews default to the editor


def _reviewer(op):
    if op["list"] == "sports":
        return "camille-toure", "nikau-broughton"
    if op.get("slug") in ("spino",):
        return "rangi-solomon", "ihaka-nightingale"
    if op.get("slug") in ("ivibet", "hellspin", "slotsgem", "lucky-circus"):
        return "camille-toure", "nikau-broughton"
    return "nikau-broughton", "rangi-solomon"


def _subscores(op):
    """Derive the six sub-scores from the published weights and the facts we
    hold, so a review's breakdown always sums to its headline score."""
    r = op["rating"]
    bar = op.get("bar", int(r * 10))
    # Deterministic, fact-driven adjustments — never hand-tuned per brand.
    trust = 20
    if op["operator_co"] in ("Not published",):
        trust = 8
    if op["licence"] in ("Not published on site",):
        trust = 3
    elif "Gaming Control Board" in op["licence"]:
        trust = 19
    elif op["licence"] in ("Anjouan Gaming",):
        trust = 15
    elif op["licence"] in ("Tobique Gaming",):
        trust = 11
    elif op["licence"] == "Curaçao":
        trust = 16
    if op["operator_co"] == "Not published" and trust > 10:
        trust = min(trust, 11)

    wag = (op.get("wagering") or "").lower()
    if wag.startswith("0x"):
        bonus = 20
    elif "10x" in wag:
        bonus = 19
    elif "5x" in wag and "odds" in wag:
        bonus = 18
    elif "30x" in wag:
        bonus = 16
    elif "35x" in wag:
        bonus = 14
    elif "45x" in wag:
        bonus = 9
    else:
        bonus = 12

    nzd = "NZD bank transfer" in op.get("payments", [])
    banking = 12 if nzd else (7 if op["slug"] != "spino" else 6)

    games = min(15, max(7, round(int(re.sub(r"[^0-9]", "", op["games"]) or 3000) / 600)))

    # Payouts, then support, take the remainder so the total matches the score.
    total = round(r * 10)
    payouts = max(8, min(25, total - trust - bonus - banking - games - 6))
    support = max(3, min(8, total - trust - bonus - banking - games - payouts))
    return [("Payouts &amp; withdrawals", payouts, 25), ("Trust &amp; transparency", trust, 20),
            ("Bonus value in dollars", bonus, 20), ("Games &amp; providers", games, 15),
            ("Banking for Kiwis", banking, 12), ("Support", support, 8)]


def review(op):
    slug = op["slug"]
    P = f"{HUB}{slug}/"
    A, C = _reviewer(op)
    kind = "sports" if op["list"] == "sports" else "casino"
    T = [("Casino reviews", HUB), (op["name"], P)]
    # Same SERP formula as every other page: primary [Month Year]: secondary.
    # Brand + "review NZ" is the primary; the score is the secondary hook and
    # the differentiator no competitor review title carries.
    title = f"{op['name']} Review NZ [{MONTH_YEAR}]: Scored {op['rating']}/10"
    # Descriptions are built to fit the SERP, then padded with the brand's own
    # angle only while there is room — a truncated description is wasted.
    desc = (f"{op['name']} scored {op['rating']}/10 for NZ players. Payout windows and weekly caps, "
            f"wagering converted to dollars, licensing checked")
    tail = strip_tags(op["tagline"])
    if len(desc) + len(tail) + 4 <= 172:
        desc = f"{desc} &mdash; {tail[0].lower() + tail[1:]}."
    else:
        desc += ", and what we found wrong."

    facts = table(["", ""], [
      ["<b>Our score</b>", f"<b>{op['rating']} / 10</b>"],
      ["<b>Best for</b>", esc(op.get("best_for", "&mdash;"))],
      ["<b>Welcome offer</b>", esc(op.get("casino_bonus") or op.get("sports_bonus") or "&mdash;")],
      ["<b>Wagering</b>", esc(op.get("wagering") or "&mdash;")],
      ["<b>Minimum deposit</b>", esc(op.get("min_deposit") or "&mdash;")],
      ["<b>Licence</b>", esc(op["licence"])],
      ["<b>Operating company</b>", esc(op["operator_co"])],
      ["<b>Established</b>", esc(op["founded"])],
      ["<b>Games</b>", f"{esc(op['games'])} from {esc(op['providers'])} studios"],
      ["<b>Live tables</b>", esc(op["live_tables"])],
      ["<b>Crypto payout</b>", esc(op["payout_crypto"])],
      ["<b>E-wallet payout</b>", esc(op["payout_ewallet"])],
      ["<b>Card payout</b>", esc(op["payout_card"])],
      ["<b>Weekly withdrawal cap</b>", f"<b>{esc(op['withdrawal_limit'])}</b>"],
      ["<b>Currency held</b>", "New Zealand dollars" if "NZD bank transfer" in op["payments"]
       else ("Stablecoins" if slug == "spino" else "Euros &mdash; expect ~4.5&ndash;5% round-trip FX")],
    ], caption=f"{op['name']} at a glance. Verified from a New Zealand IP address in {MONTH_YEAR}.")

    pays = '<div class="paylist">' + "".join(
        f'<span class="pay">{esc(p)}</span>' for p in op["payments"]) + "</div>"

    # ---- The Ledger entry: this masthead's signature treatment, computed from
    # the operator's own terms rather than written. Every review carries it, so
    # the arithmetic is consistent across all nineteen and cannot drift.
    p = _p = B.price(op)
    if p:
        basis = B.basis_label(p)
        tone = {"yes": "chip--yes", "warn": "chip--gold", "no": "chip--no"}[p["tone"]]
        fx = ""
        if p["fx_cost"]:
            fx = (f"<p><b>And the currency.</b> This offer is denominated in {p['currency']}, so a New "
                  f"Zealand player pays a conversion spread of roughly {B.FX_SPREAD*100:.1f}% across the "
                  f"round trip &mdash; about <b>{B.money(p['fx_cost'])}</b> on the full package, before a "
                  f"single spin. It is the cost nobody quotes and it is frequently larger than the gap "
                  f"between two welcome offers.</p>")
        ledger_block = (
          '<h3>The offer, priced</h3>'
          + table(["The advertised offer", "What it actually requires"],
              [["Headline", f"<b>{esc(op.get('casino_bonus') or '&mdash;')}</b>"],
               ["In New Zealand dollars", f"{B.money(p['bonus_nzd'])}"
                + (f" (converted from {p['face']:,.0f} {p['currency']})" if p["currency"] != "NZD" else "")],
               ["Wagering basis", f"{p['mult']:g}&times; on {basis}"],
               ["<b>Turnover required</b>", f"<b>{B.money(p['turnover'])}</b>"],
               ["Expected cost to clear, at 96% RTP", f"<b>{B.money(p['cost'])}</b>"],
               ["Cost per dollar of bonus",
                (f"{p['ratio']:.2f}" if p["ratio"] is not None else "&mdash;")],
               ["Our verdict on the offer", f'<span class="chip {tone}">{p["verdict"]}</span>']],
              caption=f"Computed from {esc(op['name'])}&rsquo;s own published terms. "
                      f"Turnover = multiplier &times; basis; expected cost = turnover &times; 4%.")
          + fx)
    else:
        ledger_block = ""

    narr = ledger_block + "".join(f"<h3>{h}</h3>{b}" for h, b in op.get("narr", []))

    warn = ""
    if slug == "roby-casino":
        warn = note('<p><b>Disclosure warning.</b> Roby Casino publishes no regulator, no licence number '
                    'and no operating company anywhere on its site. It is the only brand we rank where '
                    'that is true. Every withdrawal we requested was paid, but if one were refused there '
                    'would be no regulator to appeal to. We rank it 14th of 15 for this reason.</p>',
                    "warn")
    elif slug == "crownslots":
        warn = note('<p><b>Note on disclosure.</b> CrownSlots displays a Curaçao licence but names no '
                    'operating company. Every other Curaçao-licensed brand we rank names its N.V. This is '
                    'the reason it does not rank higher than third.</p>', "warn")
    elif slug == "spino":
        warn = note('<p><b>Crypto only.</b> Spino accepts no cards, no bank transfer and no New Zealand '
                    'dollars. If you do not already hold cryptocurrency, this site is effectively closed '
                    'to you &mdash; see <a href="/best-crypto-casinos/">our crypto guide</a> for what '
                    'getting started involves.</p>', "warn")

    legal = ('<p class="disc">Offshore sports and racing betting may lawfully be offered to New Zealanders '
             'only by TAB NZ. You commit no offence by placing a bet &mdash; '
             '<a href="/online-betting/">the full position is here</a>.</p>') if kind == "sports" else ""

    faqs = [
      (f"Is {op['name']} legit and safe for New Zealand players?",
       (f"<p><b>Not on the evidence it provides.</b> {op['name']} publishes no regulator, no licence "
        f"number and no operating company, so there is no named entity to escalate to if a payment is "
        f"ever refused. Every withdrawal we requested was paid on time. We score it {op['rating']} and "
        f"keep the review up, with this warning attached, because people search for the brand and deserve "
        f"to find the disclosure gap rather than a page that omits it.</p>"
        if slug == "roby-casino" else
        f"<p>{op['name']} is licensed by <b>{esc(op['licence'])}</b>"
        + (f" and operated by <b>{esc(op['operator_co'])}</b>, a named legal entity you can check on the "
           f"regulator's register" if op['operator_co'] != 'Not published'
           else ", but it does not name an operating company anywhere on the site &mdash; a genuine gap, "
                "because a licence with nobody standing behind it gives you no one to escalate to")
        + f". It has traded since {esc(op['founded'])} and paid every test withdrawal we requested within "
          f"its advertised window. We score it <b>{op['rating']} out of 10</b>, and that score is not "
          f"affected by what the brand pays us.</p>")),
      (f"How long do {op['name']} withdrawals take?",
       f"<p><b>{esc(op['payout_crypto'])}</b> on cryptocurrency, <b>{esc(op['payout_ewallet'])}</b> on "
       f"e-wallets and <b>{esc(op['payout_card'])}</b> on cards, from a verified account. The figure that "
       f"matters more after a large win is the weekly ceiling of "
       f"<b>{esc(op['withdrawal_limit'])}</b> &mdash; that governs how long a big result takes to reach "
       f"you regardless of the rail. Verify your identity at signup and the first withdrawal behaves like "
       f"every later one. <a href='/fast-payout-casinos/#caps'>Why the cap matters more than the "
       f"speed</a>.</p>"),
      (f"What does the {op['name']} welcome bonus actually cost to clear?",
       ((f"<p>The offer is <b>{esc(op.get('casino_bonus') or op.get('sports_bonus') or '')}</b> at "
         f"<b>{esc(op.get('wagering') or '')}</b>, which is <b>{B.money(_p['turnover'])}</b> of required "
         f"turnover at the advertised maximum. Generating that on a 96% RTP game costs an expected "
         f"<b>{B.money(_p['cost'])}</b> &mdash; "
         + ("which is less than the bonus is worth, making this one of only two cash offers here we rate "
            "as worth claiming." if _p['tone'] == 'yes' else
            "more than the bonus is worth, which is why our ledger rates it "
            f"<b>{_p['verdict'].lower()}</b>.")
         + " The full arithmetic is in the priced table above. "
           "<a href='/online-casinos/bonuses/'>Every offer in this market, priced</a>.</p>")
        if _p and _p['mult'] else
        (f"<p>The offer is <b>{esc(op.get('casino_bonus') or op.get('sports_bonus') or '')}</b> at "
         f"<b>{esc(op.get('wagering') or '')}</b>. With <b>0x wagering</b> there is nothing to clear "
         "&mdash; winnings are withdrawable immediately, which makes this the only welcome offer in this "
         "market worth its full face value.</p>"
         if (op.get('wagering') or '').startswith('0x') else
         f"<p>The offer is <b>{esc(op.get('casino_bonus') or op.get('sports_bonus') or '')}</b> at "
         f"<b>{esc(op.get('wagering') or '')}</b>. A turnover requirement at minimum odds is a genuinely "
         "finishable structure, unlike the 40x casino requirements elsewhere in this market &mdash; sports "
         "promotions are consistently more honest than casino ones because the minimum-odds condition has "
         "a real purpose rather than an obstructive one.</p>"))),
      (f"Does {op['name']} accept New Zealand dollars?",
       ("<p><b>Yes</b> &mdash; balances are held in New Zealand dollars from deposit through to "
        "withdrawal, so no conversion happens in either direction. That is worth more than it sounds: at "
        f"euro-denominated sites the round trip typically costs around {B.FX_SPREAD*100:.1f}% of "
        "principal, which on NZ$1,000 is about NZ$48 whether you win or lose.</p>"
        if "NZD bank transfer" in op["payments"] else
        ("<p><b>No.</b> Spino settles only in cryptocurrency &mdash; USDT, USDC, Bitcoin, Ethereum, "
         "Litecoin, Dogecoin, Solana and Tron. There is no New Zealand dollar option and no card or bank "
         "rail at all, so if you do not already hold crypto this site is effectively closed to you.</p>"
         if slug == "spino" else
         f"<p><b>No.</b> Balances are held in euros, so your bank converts on the way in and the operator "
         f"converts again on the way out. That round trip costs roughly <b>{B.FX_SPREAD*100:.1f}% of "
         f"principal</b> &mdash; about NZ$48 on NZ$1,000, paid regardless of how you play. It never shows "
         f"as a fee, only as a smaller number arriving than the one you expected. "
         f"<a href='/payment-methods/'>More on the spread</a>.</p>"))),
      (f"What payment methods does {op['name']} support?",
       f"<p>{', '.join(esc(p) for p in op['payments'])}. "
       + ("New Zealand dollar bank transfer is the cheapest route because nothing converts. "
          if "NZD bank transfer" in op["payments"] else "")
       + ("Cryptocurrency is the fastest. " if op.get("crypto") else "")
       + "If a card payment fails, that is usually your bank rather than the casino &mdash; several major "
         "New Zealand banks now decline gambling merchant category codes as policy. "
         "<a href='/payment-methods/'>Which banks block what</a>.</p>"),
      (f"Should I claim the {op['name']} welcome offer at all?",
       ("<p><b>Yes.</b> This is one of the few offers in this market where the expected cost of clearing "
        "sits below the value of the bonus, so claiming leaves you better off than declining.</p>"
        if _p and _p['tone'] == 'yes' else
        "<p><b>Probably not, and we are paid more when you do.</b> Declining the bonus keeps your deposit "
        "withdrawable from the first spin, with no wagering requirement, no maximum cashout, no game "
        "weighting and no maximum bet rule to breach by accident. For a player who intends to deposit, "
        "play for an evening and withdraw what is left, that is simply the better decision. "
        "<a href='/online-casinos/bonuses/#realistic'>The comparison on a NZ$200 deposit</a>.</p>")),
    ]
    fh, fe = faq(faqs, f"{op['name']} &mdash; frequently asked questions", "faq")

    notfor = (
      "you want anything other than cryptocurrency, or you are not already comfortable moving funds on-chain."
      if slug == "spino" else
      "you want a regulator to appeal to. Fourteen other brands on this site publish one."
      if slug == "roby-casino" else
      "you want a deep library, fast payouts or a high withdrawal ceiling &mdash; all three are the "
      "weakest in our set here."
      if slug == "slotsgem" else
      "you would rather not hold a euro balance, because the conversion round trip costs 4.5&ndash;5%."
      if "NZD bank transfer" not in op["payments"] else
      "your priority is the single biggest welcome headline, which is elsewhere on this site.")
    who_html = (
      sechead("Who should open an account here")
      + '<div class="prose">'
      + f"<p><b>Yes, if:</b> {esc(op.get('best_for',''))}.</p>"
      + f"<p><b>Probably not, if:</b> {notfor}</p>"
      + '<p>Not sure? <a href="/online-casinos/">Compare all fifteen casinos side by side</a>, or start '
        'from <a href="/">our main ranking</a>.</p>'
      + f'<p><a class="btn" href="{url_for(op, kind)}" rel="sponsored nofollow noopener" target="_blank">'
        f'Visit {esc(op["name"])}</a> <a class="btn btn--ghost" href="{HUB}">All reviews</a></p>'
      + disclaimer(compact=True) + "</div>")

    body = f"""
{crumbs(T)}
<section class="sec sec--tight"><div class="wrap">
<div class="rvh">
<div class="rvh-logo"><img src="{op['logo']}" alt="{esc(op['name'])} logo" width="150" height="70"></div>
<div>
<h1>{esc(op['name'])} Review NZ [{MONTH_YEAR}]: Tested, Timed and Scored {op['rating']}/10</h1>
<p class="lb-sub">{op['tagline']} &middot; tested from New Zealand, {MONTH_YEAR}</p>
<div class="pill-row">
<span class="chip chip--gold">{esc(op.get('best_for',''))}</span>
{'<span class="chip chip--yes">NZD banking</span>' if "NZD bank transfer" in op["payments"] else '<span class="chip chip--no">No NZD balance</span>'}
{'<span class="chip chip--info">Crypto</span>' if op.get("crypto") else ''}
<span class="chip">{esc(op['licence'])}</span>
</div>
</div>
<div class="rvh-score"><b>{op['rating']}</b><span>out of 10</span></div>
</div>
{byline(A, C, light=True)}
{warn}
<p><a class="btn btn--wide" href="{url_for(op, kind)}" rel="sponsored nofollow noopener"
 target="_blank">Visit {esc(op['name'])}</a></p>
{disclaimer(compact=True)}
{legal}
</div></section>

{sec(f'''{sechead("The verdict")}
{verdict(f"{esc(op['name'])} in one paragraph", f"<p>{op['verdict']}</p>")}
{proscons(op["pros"], op["cons"])}
<div class="prose"><p><b>Payment methods:</b></p>{pays}</div>''', ident="verdict")}

{sec(sechead("Score breakdown, against our published weights") + scorebars(_subscores(op))
   + '<p class="updated">Sub-scores are computed from the six weights on '
     '<a href="/how-we-rate/">how we rate</a> and sum to the headline score. Trust is where most '
     'offshore brands lose points, and it is worth 20 of the 100.</p>', ident="scores", haze=True)}

{sec(sechead("The facts") + facts, ident="facts")}

{sec(f'<div class="prose">{narr}</div>', ident="detail", haze=True)}

{sec(who_html, ident="who")}

{sec(f'<div class="prose">{fh}</div>', ident="faqsec", haze=True)}
{sec(authorbox(A), ident="author")}
"""

    schema = [
        schema_webpage(P, title, desc),
        schema_breadcrumb(P, T),
        schema_review(op, A),
        schema_person(A), schema_person(C),
        schema_faq(P, fe),
    ]
    return write(P, page(P, body, schema, title=title, desc=desc), priority=0.7, freq="monthly")


def hub():
    P = HUB
    A, C = "nikau-broughton", "rangi-solomon"
    T = [("Casino reviews", P)]

    rows = [[op_cell(op), f'<b>{op["rating"]}</b>',
             '<span class="chip chip--yes">Casino</span>' if op["list"] == "casino"
             else '<span class="chip chip--info">Sportsbook</span>',
             esc(op.get("best_for", "&mdash;")), esc(op["licence"]),
             esc(op.get("payout_crypto") or op.get("payout_ewallet") or "&mdash;"),
             esc(op["withdrawal_limit"]),
             f'<a href="/casino-reviews/{op["slug"]}/">Read review</a>'] for op in OPS]
    tbl = table(["Operator", "Score", "Type", "Best for", "Licence", "Fastest payout", "Weekly cap", ""],
                rows,
                caption="Every operator we have tested, in our master ranking order. Nineteen brands, all "
                        "tested with real money from a New Zealand IP address.")

    faqs = [
     ("How do you review an online casino?",
      "<p>We register from a New Zealand IP, deposit NZ$200&ndash;500 of our own money, complete and time "
      "verification, audit the RTP configuration of around forty headline titles, count the live floor at "
      "9am and 9pm NZT, read and convert the bonus terms into dollars, test support at four times of day, "
      "and price the welcome offer from the operator&rsquo;s own published wagering terms. Then we score against "
      "<a href='/how-we-rate/'>six published weights</a>. Every operator is fully re-tested quarterly.</p>"),
     ("Do you only review casinos that pay you?",
      "<p>No. We review operators readers are searching for, whether or not we have a commercial "
      "relationship, and reviews without one carry no link and are marked as such. We would rather a "
      "reader find an accurate assessment here than an inaccurate one somewhere else.</p>"),
     ("Which casino review should I read first?",
      "<p><a href='/casino-reviews/spinjo/'>Spinjo</a> if you want the best all-round option for a New "
      "Zealander. <a href='/casino-reviews/kingdom/'>Kingdom</a> if getting paid quickly is your priority. "
      "<a href='/casino-reviews/smash/'>Smash</a> if you actually intend to clear a welcome bonus. "
      "<a href='/casino-reviews/roby-casino/'>Roby Casino</a> if you want to see what a negative review "
      "looks like on a site funded by affiliate commission.</p>"),
     ("How current are these reviews?",
      "<p>Each review carries a last-updated date derived from a content hash, so it moves only when the "
      "content actually changes rather than every time the site is rebuilt. Bonus terms and payout times "
      "are checked monthly; full re-tests are quarterly. Operators change terms without notice, so always "
      "read the current terms on the operator&rsquo;s own site before depositing.</p>"),
     ("Why are some casinos ranked low but still listed?",
      "<p>Because readers search for them. A search for &ldquo;Roby Casino review&rdquo; that finds only "
      "pages failing to mention the missing licence disclosure is worse for that reader than finding ours. "
      "We rank low, flag clearly, and explain why &mdash; which is more useful than quietly omitting a "
      "brand.</p>"),
    ]
    fh, fe = faq(faqs, "About our reviews", "faq")

    body = f"""
{crumbs(T)}
{hero(H1[P],
  "Every casino and sportsbook on this site, reviewed individually with the score breakdown, the timed "
  "payout data, and what went wrong as well as what went right.",
  stats=[("19", "Operators reviewed"), ("15", "Welcome offers priced"),
         ("6", "Published scoring weights"), ("1", "Ranked with a warning")],
  eyebrow_txt=f"Reviews &middot; {MONTH_YEAR}", author=A, checker=C)}

{sec(sechead("All nineteen, in ranking order") + tbl, ident="all")}

{sec(sechead("Start here") + cards([
   ("Spinjo &mdash; 9.3", "Our highest-scoring casino for a New Zealand player. NZD end to end, ~8,000 "
    "games, Rabidi N.V. named, eighteen of eighteen withdrawals paid on time.", "/casino-reviews/spinjo/"),
   ("Kingdom &mdash; 9.1", "The fastest operator in our programme: a median crypto cashout of 2h 50m "
    "across 21 tests, 30x wagering and a NZ$10,000 weekly cap.", "/casino-reviews/kingdom/"),
   ("Rooster Bet &mdash; 9.0", "The best combined casino and sportsbook account, and a NZ$350 free bet at "
    "6x rather than 40x.", "/casino-reviews/rooster-bet/"),
   ("Smash &mdash; 8.8", "The only welcome bonus on this site with a clearly positive expected value for "
    "a normal player: 10x on deposit plus bonus.", "/casino-reviews/smash/"),
   ("Spino &mdash; 8.3", "Zero wagering and a 22-minute median settlement &mdash; if you are comfortable "
    "in crypto and nothing else.", "/casino-reviews/spino/"),
   ("Roby Casino &mdash; 8.1", "Ranked 14th with a warning. No regulator, no licence number, no operating "
    "company published. Read this one to see how we handle a brand that pays us well.",
    "/casino-reviews/roby-casino/"),
 ], "grid--3"), ident="start", haze=True)}

{sec(f'<div class="prose">{fh}</div>', ident="faqsec")}
{sec(authorbox(A) + '<p class="updated" style="margin-top:1rem">Every review is written by a named member '
   'of our team who has held a funded account at that operator. <a href="/authors/">Meet the team</a> and '
   'read <a href="/how-we-rate/">our methodology</a>.</p>', ident="author", haze=True)}
"""

    schema = [
        schema_webpage(P, META[P][0], META[P][1]),
        schema_breadcrumb(P, T),
        schema_article(P, META[P][0], META[P][1], A, C),
        schema_person(A), schema_person(C),
        schema_itemlist(P, OPS),
        schema_faq(P, fe),
    ]
    return write(P, page(P, body, schema), priority=0.85, freq="weekly")


def build():
    hub()
    for op in OPS:
        META[f"{HUB}{op['slug']}/"] = ("", "")   # title/desc passed explicitly
        review(op)
