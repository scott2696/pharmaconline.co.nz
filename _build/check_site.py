#!/usr/bin/env python3
"""Build guard. Fails loudly on the mistakes that are expensive to find later:
broken internal links, missing or duplicate metas, non-self-referencing
canonicals, invalid JSON-LD, .html in a URL, thin pages, missing R18/affiliate
disclosure, and SERP titles wider than Google will render."""
import os, re, json, sys, glob, html
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "_build"))
import lib
from lib import SITE

# Google truncates titles on rendered width, not characters. Arial 20px
# advance widths, normalised — good enough to catch a title that will clip.
W = {' ':5.0,'!':5.6,'"':7.1,'#':10,'$':10,'%':16,'&':13.3,"'":3.8,'(':6.7,')':6.7,
     '*':7,'+':10.5,',':5,'-':6,'.':5,'/':5.6,'0':10,'1':10,'2':10,'3':10,'4':10,
     '5':10,'6':10,'7':10,'8':10,'9':10,':':5.6,';':5.6,'<':10.5,'=':10.5,'>':10.5,
     '?':10,'@':18.3,'A':13.3,'B':13.3,'C':14.4,'D':14.4,'E':13.3,'F':12.2,'G':15.5,
     'H':14.4,'I':5.6,'J':10,'K':13.3,'L':11.1,'M':16.6,'N':14.4,'O':15.5,'P':13.3,
     'Q':15.5,'R':14.4,'S':13.3,'T':12.2,'U':14.4,'V':13.3,'W':18.9,'X':13.3,'Y':13.3,
     'Z':12.2,'[':5.6,']':5.6,'a':11.1,'b':11.1,'c':10,'d':11.1,'e':11.1,'f':5.6,
     'g':11.1,'h':11.1,'i':4.4,'j':4.4,'k':10,'l':4.4,'m':16.6,'n':11.1,'o':11.1,
     'p':11.1,'q':11.1,'r':6.7,'s':10,'t':5.6,'u':11.1,'v':10,'w':14.4,'x':10,
     'y':10,'z':10,'|':4.7,'’':3.8,'—':20,'–':10,'·':3.9,'&':13.3}
TITLE_PX = 580


def px(s):
    return sum(W.get(c, 11.0) for c in s)


def main():
    pages = {}
    for f in glob.glob(os.path.join(ROOT, "**", "index.html"), recursive=True):
        if "/_build/" in f or "/docs/" in f:
            continue
        if 'http-equiv="refresh"' in open(f, encoding="utf-8").read(2000):
            continue   # redirect stub, not a page
        rel = os.path.relpath(f, ROOT)
        path = "/" if rel == "index.html" else "/" + rel[:-len("index.html")]
        pages[path] = open(f, encoding="utf-8").read()

    errs, warns = [], []
    titles, descs = defaultdict(list), defaultdict(list)
    total_words = 0

    for path, doc in sorted(pages.items()):
        def one(pat, label):
            m = re.search(pat, doc, re.S)
            if not m:
                errs.append(f"{path}: missing {label}")
                return None
            return m.group(1)

        t = one(r"<title>(.*?)</title>", "<title>")
        d = one(r'<meta name="description" content="(.*?)">', "meta description")
        canon = one(r'<link rel="canonical" href="(.*?)">', "canonical")

        if t:
            titles[t].append(path)
            w = px(html.unescape(t))
            if w > TITLE_PX:
                warns.append(f"{path}: title {w:.0f}px > {TITLE_PX}px — will truncate: {t[:70]}")
        if d:
            descs[d].append(path)
            n = len(html.unescape(d))
            if not (110 <= n <= 175):
                warns.append(f"{path}: description {n} chars (want 110-175)")
        if canon and canon != f"{SITE}{path}":
            errs.append(f"{path}: canonical not self-referencing -> {canon}")

        # JSON-LD must parse, and every @id must be absolute
        for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
            try:
                g = json.loads(blk)
            except Exception as e:
                errs.append(f"{path}: invalid JSON-LD — {e}")
                continue
            if "@graph" not in g:
                errs.append(f"{path}: JSON-LD has no @graph")

        # duplicate element ids — invalid HTML, and it breaks anchor links
        ids = re.findall(r'\sid="([^"]+)"', doc)
        seen = {}
        for i in ids:
            seen[i] = seen.get(i, 0) + 1
        dups = sorted(k for k, v in seen.items() if v > 1)
        if dups:
            errs.append(f"{path}: duplicate id(s) {dups}")

        # headings
        h1 = re.findall(r"<h1[^>]*>", doc)
        if len(h1) != 1:
            errs.append(f"{path}: {len(h1)} <h1> elements (want exactly 1)")

        # word count
        txt = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", doc, flags=re.S)
        words = len(re.sub(r"<[^>]+>", " ", txt).split())
        total_words += words
        if words < 450:
            warns.append(f"{path}: only {words} words")

        # compliance furniture that must appear on every page
        if "0800 654 655" not in doc:
            errs.append(f"{path}: no responsible-gambling helpline")
        if "R18" not in doc and "18+" not in doc:
            errs.append(f"{path}: no age statement")
        if "Affiliate disclosure" not in doc:
            errs.append(f"{path}: no affiliate disclosure")

        # nav must carry About and Contact, as required
        nav = re.search(r'<nav class="nav"[^>]*>(.*?)</nav>', doc, re.S)
        if not nav or '/about/' not in nav.group(1) or '/contact/' not in nav.group(1):
            errs.append(f"{path}: About/Contact missing from main nav")

        # internal links: resolve every one
        for href in re.findall(r'href="(/[^"#?]*)', doc):
            if href.endswith((".xml", ".txt", ".png", ".svg", ".ico", ".css", ".webmanifest")):
                if not os.path.exists(os.path.join(ROOT, href.lstrip("/"))):
                    errs.append(f"{path}: broken asset link {href}")
                continue
            if ".html" in href:
                errs.append(f"{path}: URL contains .html -> {href}")
            if href not in pages:
                errs.append(f"{path}: broken internal link {href}")

        # outbound operator links must be rel=sponsored nofollow
        for m in re.finditer(r'<a ([^>]*href="https?://(?!(?:www\.)?(?:dia|legislation|ird|privacy)\.)[^"]*"[^>]*)>', doc):
            attrs = m.group(1)
            if "gamblinghelpline" in attrs or "pgf.nz" in attrs or "safergambling" in attrs \
               or "asianfamilyservices" in attrs or "privacy.org.nz" in attrs or "formsubmit" in attrs:
                continue
            if "sponsored" not in attrs:
                warns.append(f"{path}: outbound link without rel=sponsored")

    for t, ps in titles.items():
        if len(ps) > 1:
            errs.append(f"duplicate <title> on {ps}: {t[:60]}")
    for d, ps in descs.items():
        if len(ps) > 1:
            errs.append(f"duplicate description on {ps}")

    # sitemap must list exactly the pages that exist
    sm = open(os.path.join(ROOT, "sitemap.xml")).read()
    listed = {u.replace(SITE, "") for u in re.findall(r"<loc>(.*?)</loc>", sm)}
    for miss in sorted(set(pages) - listed):
        errs.append(f"sitemap missing {miss}")
    for extra in sorted(listed - set(pages)):
        errs.append(f"sitemap lists non-existent {extra}")

    # robots.txt must block the named crawlers and carry the sitemap
    rb = open(os.path.join(ROOT, "robots.txt")).read()
    for ua in ["AhrefsBot", "SemrushBot", "MJ12bot", "DotBot", "Rogerbot",
               "serpstatbot", "SistrixBot"]:
        if f"User-agent: {ua}" not in rb:
            errs.append(f"robots.txt: {ua} not blocked")
    if f"Sitemap: {SITE}/sitemap.xml" not in rb:
        errs.append("robots.txt: sitemap URL missing")

    # Every page must be tagged for indexing. A page that is not a redirect
    # stub and carries noindex is almost always an accident, and it is the
    # kind that costs a month of traffic before anyone notices.
    for rel, doc in sorted(pages.items()):
        m = re.search(r'<meta name="robots" content="([^"]*)"', doc)
        if not m:
            errs.append(f"{rel}: no robots meta")
        elif "noindex" in m.group(1):
            errs.append(f"{rel}: robots meta says noindex")
        elif not m.group(1).startswith("index,follow"):
            errs.append(f"{rel}: robots meta is {m.group(1)!r}, want index,follow")

    # JSON-LD must carry plain text. An HTML entity inside a JSON string is
    # not markup to a schema consumer — it is nine literal characters.
    def ld_strings(node, path=""):
        if isinstance(node, dict):
            for k, v in node.items():
                yield from ld_strings(v, f"{path}.{k}")
        elif isinstance(node, list):
            for v in node:
                yield from ld_strings(v, path + "[]")
        elif isinstance(node, str):
            yield path, node

    for rel, doc in sorted(pages.items()):
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>',
                                doc, re.S):
            try:
                data = json.loads(block)
            except ValueError as e:
                errs.append(f"{rel}: invalid JSON-LD ({e})")
                continue
            for field, text in ld_strings(data):
                ent = re.search(r"&[a-zA-Z][a-zA-Z0-9]{1,10};|&#\d+;", text)
                if ent:
                    errs.append(f"{rel}: HTML entity {ent.group(0)} in JSON-LD {field}")

    # robots.txt must not hide the assets Google needs in order to render the
    # page it is indexing. Longest-match wins, as Googlebot resolves it.
    def blocked(url):
        star = rb.split("User-agent: *", 1)[-1]
        best, verdict = -1, True
        for line in star.splitlines():
            line = line.strip()
            for kind in ("Allow", "Disallow"):
                if line.startswith(kind + ":"):
                    pat = line.split(":", 1)[1].strip()
                    rx = "^" + re.escape(pat).replace(r"\*", ".*").replace(r"\$", "$")
                    if re.match(rx, url) and len(pat) > best:
                        best, verdict = len(pat), (kind == "Disallow")
        return verdict

    for asset in re.findall(r'(?:href|src)="(/assets/[^"]+)"', pages["/"]):
        if blocked(asset):
            errs.append(f"robots.txt blocks {asset} — Googlebot renders pages "
                        f"before indexing them and needs this")

    # every page must be reachable from the full-site menu, so "all pages in
    # the hamburger" cannot quietly stop being true when a page is added
    menu_urls = {u for _, links in lib.menu_groups() for _, u in links}
    for miss in sorted(set(pages) - menu_urls):
        errs.append(f"{miss}: not in the site menu")
    for extra in sorted(menu_urls - set(pages)):
        errs.append(f"site menu links to non-existent {extra}")

    # required favicon sizes, each a multiple of 48
    for s in (48, 96, 144, 192):
        if not os.path.exists(os.path.join(ROOT, f"favicon-{s}x{s}.png")):
            errs.append(f"missing favicon-{s}x{s}.png")

    print(f"{len(pages)} pages · {total_words:,} words · "
          f"{total_words // max(1, len(pages)):,} avg")
    if warns:
        print(f"\n{len(warns)} warning(s):")
        for w in warns[:40]:
            print("  ⚠ " + w)
    if errs:
        print(f"\n{len(errs)} ERROR(S):")
        for e in errs[:60]:
            print("  ✗ " + e)
        sys.exit(1)
    print("\n✓ all checks passed")


if __name__ == "__main__":
    main()
