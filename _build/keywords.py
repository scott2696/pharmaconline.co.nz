#!/usr/bin/env python3
"""The keyword map, as data, so coverage can be checked rather than asserted.

Supplied targets use a different URL scheme (magnumsports.co.nz's). This maps
each cluster onto the equivalent page on this site — see MAPPED_FROM — and
check_keywords.py fails the build if a Tier 1 term is missing from its page.

Rules encoded here:
  * The HOMEPAGE keeps the head term "best online casino sites NZ".
    /online-casinos/ owns "online casinos nz" and "real money casino nz" so
    the two do not cannibalise.
  * "no deposit" and "free spins no deposit" belong to /no-deposit-casinos/
    ONLY. /online-casinos/bonuses/ must not target them — see FORBIDDEN.
"""

# supplied-path -> path on this site
MAPPED_FROM = {
    "/online-casinos/":            "/online-casinos/",
    "/licensed-online-casinos/":   "/nz-online-casino-law/",
    "/casino-bonus/":              "/online-casinos/bonuses/",
    "/casino-payout-percentages/": "/high-payout-casinos/",
    "/fast-payout-casinos/":       "/fast-payout-casinos/",
    "/casino-payment-methods/":    "/payment-methods/",
    "/online-pokies/":             "/online-pokies/",
    "/live-casino/":               "/live-casinos/",
    "/how-we-rate-casinos/":       "/how-we-rate/",
    "/no-deposit-bonus/":          "/no-deposit-casinos/",
    "/new-casinos-nz/":            "/new-casinos-nz/",
    "/crypto-casinos-nz/":         "/best-crypto-casinos/",
    "/instant-withdrawals/":       "/instant-withdrawals/",   # 301 stub
}

# path -> {"t1": [...], "t2": [...], "lt": [...]}
# t1 terms are build-enforced: each must appear in the rendered page.
MAP = {

"/online-casinos/": dict(
  t1=["online casinos nz", "online casino new zealand", "nz online casinos",
      "online casino real money nz", "top online casinos nz", "real money casino nz",
      "nz casino sites", "casino online nz"],
  t2=["best casino sites nz", "safe online casinos nz", "trusted online casinos nz",
      "new online casinos nz", "online casinos that accept nzd", "nzd online casino",
      "online gambling nz", "best online gambling sites nz", "casino sites new zealand"],
  lt=["best online casino nz reddit", "which online casino pays out the most nz",
      "best online casino for kiwis", "best online casino nz low deposit",
      "online casino nz sign up bonus", "best rated online casino new zealand",
      "most trusted online casino nz", "online casino nz real money no deposit",
      "are online casinos safe nz", "best online casino nz for beginners"]),

"/nz-online-casino-law/": dict(
  t1=["licensed online casinos nz", "legal online casinos nz",
      "is online gambling legal in nz", "are online casinos legal in new zealand",
      "online gambling laws new zealand"],
  t2=["online casino gambling act 2026", "nz online casino licence",
      "regulated online casinos new zealand", "dia licensed online casino",
      "new zealand online casino licence list", "legal online casino nz 2027"],
  lt=["which online casinos are licensed in nz", "when do online casinos become legal in nz",
      "how many online casino licences nz", "department of internal affairs online casino licence",
      "is it legal to gamble online in new zealand", "offshore casinos nz legal status",
      "unlicensed online casinos nz", "what happens to offshore casinos nz december 2026",
      "nz online casino licence holders list", "do i pay tax on casino winnings nz",
      "is gambling tax free in new zealand"]),

"/online-casinos/bonuses/": dict(
  t1=["casino bonus nz", "best casino bonuses nz", "casino sign up bonus nz",
      "$1 deposit casino nz"],
  t2=["online casino bonus new zealand", "welcome bonus casino nz",
      "1 dollar deposit casino nz", "$5 deposit casino nz", "$10 deposit casino nz",
      "casino bonus codes nz"],
  lt=["no wagering casino bonus nz", "low wagering bonus nz",
      "what does 35x wagering mean", "how do casino wagering requirements work",
      "reload bonus casino nz", "cashback casino bonus nz",
      "best welcome bonus online casino nz", "minimum deposit casino bonus nz",
      "are casino bonuses worth it nz"]),

"/no-deposit-casinos/": dict(
  t1=["no deposit bonus nz", "free spins no deposit nz", "no deposit bonus codes nz",
      "casino no deposit bonus new zealand", "no deposit casino nz"],
  t2=["free spins no deposit nz 2026", "no deposit sign up bonus nz",
      "50 free spins no deposit nz", "20 free spins no deposit nz",
      "new no deposit bonus nz", "real money no deposit bonus nz",
      "no deposit free spins on registration nz"],
  lt=["100 free spins no deposit nz", "25 free spins no deposit nz",
      "$5 no deposit bonus nz", "$10 no deposit bonus nz",
      "no deposit bonus keep what you win nz",
      "can you withdraw no deposit bonus winnings nz",
      "free spins no deposit no card details nz", "no deposit bonus max cashout explained",
      "no deposit bonus wagering requirements nz", "how to claim a no deposit bonus",
      "are no deposit bonuses legit", "no deposit bonus pokies nz",
      "exclusive no deposit bonus codes nz", "best no deposit bonus nz 2026",
      "free chip no deposit casino nz"]),

"/high-payout-casinos/": dict(
  t1=["casino payout percentage", "best payout online casino nz", "highest rtp casinos nz",
      "rtp meaning casino", "what is rtp in pokies"],
  t2=["highest rtp pokies nz", "best rtp slots nz", "online casino payout percentage nz",
      "highest paying online casino nz", "return to player explained"],
  lt=["which online casino has the best payout nz", "average rtp online casino nz",
      "house edge vs rtp", "loosest online pokies nz", "how is casino rtp calculated",
      "what is a good rtp percentage", "payout rates online casinos new zealand",
      "does rtp matter in the short term", "blackjack rtp vs pokies rtp"]),

"/fast-payout-casinos/": dict(
  t1=["fast payout casinos nz", "instant withdrawal casino nz",
      "fastest paying online casino nz", "how long do casino withdrawals take nz"],
  t2=["quick withdrawal casino nz", "same day payout casino nz", "instant payout casino nz",
      "casinos with fast withdrawals nz", "withdrawal times online casino nz"],
  lt=["fastest withdrawal method online casino nz",
      "instant withdrawal casino nz bank transfer", "crypto instant withdrawal casino nz",
      "why is my casino withdrawal pending", "casino withdrawal pending time nz",
      "fast payout casino nz no verification delay",
      "online casino payout time new zealand", "instant withdrawal pokies nz",
      "casino that pays out instantly nz", "how to speed up casino withdrawal"]),

"/payment-methods/": dict(
  t1=["casino payment methods nz", "online casino deposit methods nz",
      "paysafecard casino nz", "casinos that accept poli nz", "paypal casino nz"],
  t2=["neosurf casino nz", "skrill casino nz", "neteller casino nz", "apple pay casino nz",
      "bank transfer casino nz", "visa casino nz", "mastercard casino nz",
      "casinos that accept nzd"],
  lt=["can you use paypal at online casinos nz", "best payment method for online casino nz",
      "poli payments casino nz", "minimum deposit online casino nz",
      "online casino that accepts prepaid card nz", "deposit with phone bill casino nz",
      "casino deposit no fees nz", "which casinos accept apple pay nz",
      "nzd deposits no conversion fee casino", "casino withdrawal to bank account nz"]),

"/online-pokies/": dict(
  t1=["online pokies nz", "online pokies real money nz", "best online pokies nz",
      "free pokies nz", "pokies online new zealand", "real money pokies nz"],
  t2=["play pokies online nz", "new pokies nz", "best pokie sites nz", "jackpot pokies nz",
      "mobile pokies nz", "free online pokies no download"],
  lt=["best paying pokies nz", "megaways pokies nz", "progressive jackpot pokies nz",
      "online pokies $1 deposit nz", "are online pokies legal in nz",
      "how do online pokies work", "online pokies free spins no deposit nz",
      "highest rtp online pokies nz", "free pokies no download no registration nz",
      "which online pokies pay the most nz", "online pokies with bonus buy nz"]),

"/live-casinos/": dict(
  t1=["live casino nz", "live dealer casino nz", "best live casino nz", "live roulette nz",
      "live blackjack nz"],
  t2=["live baccarat nz", "live casino real money nz", "evolution gaming casinos nz",
      "crazy time nz", "lightning roulette nz"],
  lt=["best live casino sites new zealand", "live casino minimum bet nz",
      "live dealer blackjack online nz real money", "how does live casino work",
      "live casino vs rng games", "live casino with nzd tables",
      "best live roulette site nz", "monopoly live nz", "live casino app nz"]),

"/best-crypto-casinos/": dict(
  t1=["crypto casino nz", "bitcoin casino nz", "crypto casinos new zealand",
      "best crypto casino nz", "bitcoin gambling nz"],
  t2=["ethereum casino nz", "usdt casino nz", "litecoin casino nz", "crypto pokies nz",
      "instant withdrawal crypto casino nz", "anonymous casino nz", "dogecoin casino nz"],
  lt=["best bitcoin casino nz 2026", "are crypto casinos legal in nz",
      "how to deposit bitcoin at an online casino nz", "crypto casino no deposit bonus nz",
      "fastest crypto withdrawal casino nz", "crypto casino with nzd conversion",
      "do you pay tax on crypto casino winnings nz", "provably fair casino explained",
      "crypto casino welcome bonus nz", "bitcoin pokies nz",
      "how to withdraw crypto from an online casino nz", "crypto casino minimum deposit nz",
      "crypto vs bank transfer casino withdrawals"]),

"/new-casinos-nz/": dict(
  t1=["new online casinos nz", "new casinos nz", "newest online casinos nz",
      "new casino sites nz", "new online casino nz real money"],
  t2=["brand new online casinos nz 2026", "latest online casinos nz", "new pokie sites nz",
      "new casino sites with free spins nz", "upcoming online casinos nz"],
  lt=["new online casinos nz no deposit bonus", "newly licensed online casinos nz",
      "new licensed casinos nz december 2026", "are new online casinos safe nz",
      "best new casino sites nz 2026", "new online casino free spins no deposit nz",
      "new nz casinos accepting nzd", "new casino no wagering bonus nz",
      "newest pokie sites new zealand", "what to check before joining a new casino",
      "new crypto casinos nz", "new casinos launching new zealand"]),

"/how-we-rate/": dict(
  t1=["how to choose an online casino nz", "how to tell if an online casino is legit",
      "what makes an online casino safe", "online casino review methodology"],
  t2=["casino licensing explained", "how to check if a casino is licensed nz"],
  lt=["responsible gambling nz", "gambling helpline nz"]),
}

# Terms a page must NOT target, to stop two pages competing for the same query.
FORBIDDEN = {
    "/online-casinos/bonuses/": ["no deposit bonus nz", "free spins no deposit nz",
                                 "no deposit bonus codes nz", "no deposit casino nz"],
}

# The homepage keeps the head term; /online-casinos/ must not chase it.
HOME_HEAD = "best online casino sites nz"
