#!/usr/bin/env python3
"""Orchestrator. Regenerates every page, sitemap.xml, robots.txt and the
web manifest. Output is written in place — this directory is the site."""
import os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib
from lib import ROOT, SITE, NAME, PAGES, save_lastmod

MODULES = ["p_home", "p_casinos", "p_categories", "p_betting",
           "p_guides", "p_reviews", "p_site", "p_new"]


# 301s cannot be emitted from HTML. A static host has to do it, so we ship the
# config for the common ones AND a meta-refresh page as the fallback, which
# Google treats as a permanent redirect when the delay is 0 and the canonical
# points at the target. REDIRECTS is the single source for all of it.
REDIRECTS = {
    "/instant-withdrawals/": "/fast-payout-casinos/",
}


def redirects():
    from lib import SITE, NAME
    for src, dst in REDIRECTS.items():
        html = f"""<!doctype html>
<html lang="en-NZ">
<head>
<meta charset="utf-8">
<title>Redirecting to {dst}</title>
<meta http-equiv="refresh" content="0; url={dst}">
<link rel="canonical" href="{SITE}{dst}">
<meta name="robots" content="noindex,follow">
</head>
<body>
<p>This page has moved to <a href="{dst}">{SITE}{dst}</a>.</p>
<script>location.replace("{dst}");</script>
</body>
</html>
"""
        out = os.path.join(ROOT, src.strip("/"), "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w").write(html)

    # Netlify / Cloudflare Pages
    open(os.path.join(ROOT, "_redirects"), "w").write(
        "".join(f"{s}  {d}  301\n" for s, d in REDIRECTS.items()))
    # Apache
    open(os.path.join(ROOT, ".htaccess"), "w").write(
        "# 301s for retired URLs. Apache/LiteSpeed only — see docs/DEPLOY-REDIRECTS.md\n"
        "RewriteEngine On\n"
        + "".join(f"RewriteRule ^{s.strip('/')}/?$ {d} [R=301,L]\n"
                  for s, d in REDIRECTS.items()))
    return len(REDIRECTS)


def sitemap():
    rows = []
    for path, date, pri, freq in sorted(PAGES, key=lambda p: (-p[2], p[0])):
        rows.append(f"  <url>\n    <loc>{SITE}{path}</loc>\n"
                    f"    <lastmod>{date}</lastmod>\n"
                    f"    <changefreq>{freq}</changefreq>\n"
                    f"    <priority>{pri:.1f}</priority>\n  </url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(xml)
    return len(rows)


# SEO-tool crawlers are blocked at the user-agent level as requested. They
# consume crawl budget and hand a competitor a map of the site for nothing in
# return. Search engines and the AI crawlers we want indexing us are allowed.
BLOCKED = ["AhrefsBot", "SemrushBot", "MJ12bot", "DotBot", "Rogerbot",
           "serpstatbot", "SistrixBot", "BLEXBot", "DataForSeoBot",
           "Barkrowler", "ZoominfoBot", "PetalBot", "SEOkicks",
           "LinkpadBot", "spbot", "Cliqzbot", "Screaming Frog SEO Spider"]


def robots():
    out = [f"# robots.txt for {SITE}", f"# {NAME} — updated {datetime.date.today().isoformat()}", ""]
    for ua in BLOCKED:
        out += [f"User-agent: {ua}", "Disallow: /", ""]
    out += ["# Everything else is welcome.",
            "User-agent: *",
            "Allow: /",
            # site.css is served with a ?v= cache-buster, so the blanket
            # query-string rule below would hide the only stylesheet from
            # Googlebot's renderer. Google renders pages to index them and
            # penalises blocked CSS, so /assets/ is allowed explicitly. This
            # wins on longest-match (8 chars vs 3) and is listed first for
            # crawlers that take the first match instead.
            "Allow: /assets/",
            "Disallow: /_build/",
            "Disallow: /docs/",
            "Disallow: /*?",
            "", f"Sitemap: {SITE}/sitemap.xml", ""]
    open(os.path.join(ROOT, "robots.txt"), "w").write("\n".join(out))


def manifest():
    import json
    m = {"name": NAME, "short_name": NAME, "start_url": "/",
         "display": "standalone", "background_color": "#FCFBF9",
         "theme_color": "#131C2E", "lang": "en-NZ",
         "icons": [{"src": f"/favicon-{s}x{s}.png", "sizes": f"{s}x{s}",
                    "type": "image/png",
                    "purpose": "any maskable" if s >= 192 else "any"}
                   for s in (48, 96, 144, 192, 512)]}
    json.dump(m, open(os.path.join(ROOT, "site.webmanifest"), "w"), indent=1)


def main():
    for name in MODULES:
        try:
            mod = __import__(name)
        except ImportError:
            print(f"  .. {name} not present yet, skipping")
            continue
        mod.build()
        print(f"  ok {name}")
    r = redirects()
    n = sitemap()
    robots()
    manifest()
    save_lastmod()
    print(f"\n{n} pages written, {r} redirect stub(s). "
          f"sitemap.xml, robots.txt, site.webmanifest, _redirects, .htaccess updated.")


if __name__ == "__main__":
    main()
