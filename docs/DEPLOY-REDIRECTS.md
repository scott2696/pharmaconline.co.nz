# Redirects

## Why this file exists

A **301 cannot be emitted from HTML.** It is an HTTP status code, so the host has to send it. The
build writes three things so that whichever host you deploy to, the redirect is a real 301 where it
can be and a clean fallback where it cannot:

| File | For | Status it produces |
|---|---|---|
| `_redirects` | Netlify, Cloudflare Pages | **301** |
| `.htaccess` | Apache, LiteSpeed, cPanel | **301** |
| `<slug>/index.html` | Any static host, incl. GitHub Pages | Meta refresh + canonical |

All three are generated from one source — `REDIRECTS` in `_build/build.py`. Add a pair there and
rebuild; never hand-edit the outputs.

## Current redirects

| From | To |
|---|---|
| `/instant-withdrawals/` | `/fast-payout-casinos/` |

## If you deploy to GitHub Pages

GitHub Pages sends no custom status codes, so the meta-refresh stub is what runs. Google treats a
`<meta http-equiv="refresh" content="0; …">` combined with a self-pointing `canonical` on the target
as a permanent redirect, and it passes signals — but it is a fallback, not equivalent. The stub also
carries `noindex,follow` so it cannot compete with its own destination.

**If you want a true 301 on GitHub Pages, you need a proxy in front of it.** Cloudflare (free tier) in
front of Pages, with a Bulk Redirect or a Page Rule, gives you the real thing. That is the one change
worth making before this site takes meaningful traffic.

## nginx

```nginx
location = /instant-withdrawals/ { return 301 /fast-payout-casinos/; }
location = /instant-withdrawals  { return 301 /fast-payout-casinos/; }
```

## Cloudflare Bulk Redirects

Source `https://<domain>/instant-withdrawals/` → Target `https://<domain>/fast-payout-casinos/`,
status **301**, with *Preserve query string* on.

## Rules the build enforces

- The stub is **excluded from `sitemap.xml`** — a redirect is not a page.
- The stub is **skipped by `check_site.py`**, so it is not held to page rules it cannot meet.
- **No internal link points at it.** `grep -rl 'href="/instant-withdrawals/'` returns nothing but the
  stub itself. Every instant-withdrawal keyword variant is targeted on `/fast-payout-casinos/`
  instead, so there is nothing to split back out.
