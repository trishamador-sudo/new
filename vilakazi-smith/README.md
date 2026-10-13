# Vilakazi Smith Inc. website (vsinc.co.za)

A rebuild of www.vsinc.co.za as a fast, static, multi-page site. It is plain HTML, CSS and JS, with no WordPress, plugins or framework. Upload the folder (without `build/` and `assets/references/`) to a static host such as Cloudflare Pages or Netlify.

## Pages
| URL | Purpose |
|---|---|
| `/` | Home |
| `/practice-areas/` | Overview of all practice areas |
| `/practice-areas/<area>/` | One page per practice area (8 pages), each with its own services, 3 FAQs and schema |
| `/attorneys-pretoria/`, `/attorneys-sandton/` | One page per office, for local search |
| `/about/` | Firm background, mission, team, compliance documents |
| `/blog/` | Legal insights (empty until the first article is published) |
| `/contact/` | Consultation request form with POPIA consent, plus both offices |
| `/404.html` | Not-found page |

## How to edit
All copy and firm details live in `build/content.py`. After editing it, rebuild the pages:

```
python3 build/build.py
```

This rewrites every page, `sitemap.xml` and `robots.txt`. Don't hand-edit the generated `index.html` files, because the next build overwrites them.

To preview locally without a web server, run `python3 build/build.py --preview /some/folder`. This writes a copy whose links end in `index.html`.

## Before going live: to confirm with the firm
- **Team:** names, roles, one-sentence bios and photos are placeholders (the current site's team info is out of date). Edit `TEAM` in `content.py`. Once confirmed, also add a `Person` node for each director in the schema (see the note in `firm_node()` in `build.py`), and optionally a profile page for each attorney.
- **Testimonials:** the carousel shows placeholders. Use only real testimonials, with each client's written permission. Edit `TESTIMONIALS`.
- **Enquiry email and form:** the form is not connected yet. Create a Formspree form that delivers to the firm's enquiry address, and paste the endpoint into `FORM_ENDPOINT` at the top of `main.js`. The email address is deliberately not printed on the page, so spam harvesters can't collect it.
- **Office hours and social links:** unknown, so they are left off the site and schema. Add them to `FIRM` in `content.py`.
- **086 577 5456:** shown as the fax number for both offices. Confirm.
- **Contact details:** the client wasn't sure the current ones are up to date. Confirm both offices' phone numbers and addresses.
- **Compliance PDFs:** put `privacy-policy.pdf`, `paia-manual.pdf` and `bbbee-certificate.pdf` (from the current site) into `assets/docs/`. The footer, About page and form link to them.
- **Hero image:** this is the current site's lion image, with the old baked-in text removed. A new Higgsfield version can replace `assets/img/hero.webp` (1919×682), `hero-960.webp` and `hero-mobile.webp`. The Higgsfield account had 0 credits at build time.
- **Logo:** made from a small screenshot. Ask for the original vector (SVG/AI/PDF) logo, then replace `assets/img/logo*.png` and `mark*.png`.
- **Domain:** `https://www.vsinc.co.za` is used in `content.py` (`DOMAIN`), the canonical links, Open Graph tags, schema, `robots.txt` and `sitemap.xml`. If the domain changes, change `DOMAIN` and rebuild.

## Redirects from the old site
After launch, check the old WordPress URLs in Google Search Console (Pages report) and add 301 redirects in a `_redirects` file to the matching new page, for example:
```
/family-law/          /practice-areas/family-law/     301
/about-us/            /about/                         301
/contact-us/          /contact/                       301
```

## Add a blog article
1. Copy `blog/_post-template.html` to `blog/<article-slug>/index.html`.
2. Replace the ARTICLE placeholders (title, summary, author, dates, slug). Remove the `noindex` meta tag.
3. Add a card for it in the `blog()` function in `build.py` (a commented example is included), and add the URL to the `pages` list so it goes into `sitemap.xml`.

Suggested first articles, matching the practice-area FAQs and common searches:
- How does the eviction process work in South Africa?
- What is a Section 129 notice?
- How long does a divorce take in South Africa?
- My insurance claim was rejected: what now?

## What this rebuild fixes from the SEO audit
| Audit finding | Fix |
|---|---|
| No meta description | A unique description on every page |
| No social meta tags | Open Graph and Twitter tags on every page, plus a 1200×630 share image (`assets/img/og.jpg`) |
| Too many H1 tags | Exactly one H1 per page |
| Images missing alt text | Every image has descriptive alt text |
| Oversized images, no modern format | WebP images at their display size, with `srcset` for the hero, and lazy loading below the fold |
| Console errors | None: a plain script with no plugins |
| 266 KB HTML | 12–33 KB per page; CSS and JS in external files |
| 20+ HTTP requests, render-blocking resources | About 15 requests on the home page: one stylesheet, one deferred script and two self-hosted fonts. Google Maps loads only when a visitor clicks "Show map" |
| Slow TTFB / FCP, no CDN | Static files on a CDN host (Cloudflare Pages / Netlify) |
| CLS 0.24 | Width and height set on every image; fonts preloaded |
| No HSTS header | `_headers` sets Strict-Transport-Security and other security headers |
| Email address in page code | No email address in the code; enquiries go through the form |
| No structured data | JSON-LD on every page: Attorney (the firm and each office), Service, FAQPage, BreadcrumbList, WebSite |
| robots.txt with Disallow | `Allow: /` plus the sitemap |
| Repeated content blocks | Each practice area appears once, and each page has unique copy |
| No FAQs, thin practice-area content | Each practice area has its own page, services list and 3 FAQs |
| No local targeting | A dedicated page and schema for each office |
| No blog | Blog section and article template ready |

## Off-site local SEO checklist (not part of the website files)
- Claim and verify a **Google Business Profile for each office** (Pretoria and Sandton), with the same name, address and phone number as the site (NAP), the category "Law firm", and a link to that office's page.
- Submit `https://www.vsinc.co.za/sitemap.xml` in Google Search Console and Bing Webmaster Tools.
- List the firm, with identical NAP details, on Legal Practice Council / Law Society directories, Yellow Pages SA, Cylex, Brabys and Hotfrog.
- Ask satisfied clients for Google reviews (on the Business Profile, not on the website).
