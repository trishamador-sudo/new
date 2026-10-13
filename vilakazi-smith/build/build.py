#!/usr/bin/env python3
"""Generates the Vilakazi Smith Inc. static site from build/content.py.

    python3 build/build.py               # writes the live site into this folder
    python3 build/build.py --preview DIR # writes a copy whose links end in index.html (for previewing without a web server)

No dependencies beyond the Python standard library.
"""
import json
import os
import shutil
import sys
from html import escape

sys.path.insert(0, os.path.dirname(__file__))
from content import ABOUT, DOMAIN, FIRM, HOME_FAQS, LASTMOD, MISSION, OFFICES, PRACTICE, TEAM, TESTIMONIALS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREVIEW = False

FIRM_ID = f"{DOMAIN}/#firm"
SITE_ID = f"{DOMAIN}/#website"
MAIN_OFFICE = OFFICES[0]


def e(s):
    return escape(s, quote=True)


# ---------------------------------------------------------------- links

def link(cur, target):
    """Relative link from page path `cur` (e.g. 'practice-areas/family-law/') to `target`."""
    depth = cur.count("/")
    href = "../" * depth + target
    if PREVIEW and (target == "" or target.endswith("/")):
        href += "index.html"
    return href or "./"


def asset(cur, path):
    return "../" * cur.count("/") + path


# ---------------------------------------------------------------- shared bits

ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="i-phone" viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
<symbol id="i-left" viewBox="0 0 24 24"><path d="M19 12H5M11 6l-6 6 6 6"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><path d="M20 6 9 17l-5-5"/></symbol>
<symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></symbol>
<symbol id="i-x" viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12"/></symbol>
<symbol id="i-down" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></symbol>
<symbol id="i-calendar" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></symbol>
<symbol id="i-scale" viewBox="0 0 24 24"><path d="M12 3v18M7 21h10M3 7h18M6 7l-3 7a3 3 0 0 0 6 0zM18 7l-3 7a3 3 0 0 0 6 0z"/></symbol>
<symbol id="i-shield" viewBox="0 0 24 24"><path d="M20 13c0 5-3.5 7.5-7.7 9a1 1 0 0 1-.7 0C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.2-2.7a1.2 1.2 0 0 1 1.6 0C14.5 3.8 17 5 19 5a1 1 0 0 1 1 1z"/></symbol>
<symbol id="i-plus" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></symbol>
<symbol id="i-file" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/></symbol>
<symbol id="i-user" viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></symbol>
<symbol id="i-pen" viewBox="0 0 24 24"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/></symbol>
</defs></svg>"""


def ic(name, cls="ic"):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'


def tel(num):
    return "+27" + num.replace(" ", "")[1:]


def header(cur, active):
    def nl(target, label, key):
        cur_attr = ' aria-current="page"' if active == key else ""
        return f'<a class="nav__link" href="{link(cur, target)}"{cur_attr}>{label}</a>'

    pa_links = "".join(f'<a href="{link(cur, "practice-areas/" + p["slug"] + "/")}">{e(p["name"])}</a>' for p in PRACTICE)
    off_links = "".join(f'<a href="{link(cur, "attorneys-" + o["slug"] + "/")}">{e(o["name"])}</a>' for o in OFFICES)
    pa_cur = ' aria-current="page"' if active == "practice" else ""
    off_cur = ' aria-current="page"' if active == "offices" else ""
    return f"""
<a class="skip-link" href="#main">Skip to main content</a>
{ICONS}
<div class="topbar">
  <div class="container topbar__inner">
    <a href="tel:{tel(MAIN_OFFICE['phones'][0][0])}">{ic('phone')}<span>Pretoria {MAIN_OFFICE['phones'][0][0]}</span></a>
    <a class="topbar__hide-sm" href="tel:{tel(OFFICES[1]['phones'][0][0])}">{ic('phone')}<span>Sandton {OFFICES[1]['phones'][0][0]}</span></a>
    <span class="topbar__push topbar__hide-sm">Founded in {FIRM['founded']}, B-BBEE Level 2</span>
  </div>
</div>
<header class="header">
  <div class="container header__inner">
    <a class="brand" href="{link(cur, '')}" aria-label="{e(FIRM['name'])}, home">
      <img class="brand__mark" src="{asset(cur, 'assets/img/mark-white.png')}" width="160" height="60" alt="">
      <span class="brand__name">{e(FIRM['name'])}</span>
    </a>
    <nav class="nav" id="site-nav" aria-label="Main">
      <div class="nav__group">
        <a class="nav__link" href="{link(cur, 'practice-areas/')}"{pa_cur}>Practice areas {ic('down', 'ic nav__caret')}</a>
        <div class="nav__sub">{pa_links}</div>
      </div>
      <div class="nav__group">
        <a class="nav__link" href="{link(cur, 'attorneys-pretoria/')}"{off_cur}>Offices {ic('down', 'ic nav__caret')}</a>
        <div class="nav__sub">{off_links}</div>
      </div>
      {nl('about/', 'About', 'about')}
      {nl('blog/', 'Blog', 'blog')}
      {nl('contact/', 'Contact', 'contact')}
      <a class="btn btn--light nav__cta" href="{link(cur, 'contact/')}">Book a consultation</a>
    </nav>
    <a class="header__call" href="tel:{tel(MAIN_OFFICE['phones'][0][0])}" aria-label="Call Vilakazi Smith Inc.">{ic('phone')}</a>
    <button class="menu-toggle" type="button" aria-controls="site-nav" aria-expanded="false" aria-label="Open menu">
      {ic('menu', 'ic ic--open')}{ic('x', 'ic ic--close')}
    </button>
  </div>
</header>"""


def footer(cur):
    pa = "".join(f'<li><a href="{link(cur, "practice-areas/" + p["slug"] + "/")}">{e(p["name"])}</a></li>' for p in PRACTICE)
    offices = "".join(
        f'<div><strong><a href="{link(cur, "attorneys-" + o["slug"] + "/")}">{e(o["name"])}</a></strong>'
        f'{"<br>".join(e(l) for l in o["lines"])}<br>'
        + " / ".join(f'<a href="tel:{t}">{n}</a>' for n, t in o["phones"])
        + "</div>"
        for o in OFFICES
    )
    return f"""
<footer class="footer">
  <div class="container footer__grid">
    <div>
      <img class="footer__logo" src="{asset(cur, 'assets/img/logo-white.png')}" width="428" height="196" alt="{e(FIRM['name'])}" loading="lazy">
      <p>Attorneys in Pretoria and Sandton, Gauteng. Founded in {FIRM['founded']}. {e(FIRM['bbbee'])}.</p>
    </div>
    <div>
      <h2>Offices</h2>
      <address>{offices}<div><strong>Postal address</strong>{e(FIRM['postal'])}</div></address>
    </div>
    <div>
      <h2>Practice areas</h2>
      <ul role="list">{pa}</ul>
    </div>
    <div>
      <h2>The firm</h2>
      <ul role="list">
        <li><a href="{link(cur, 'about/')}">About us</a></li>
        <li><a href="{link(cur, 'blog/')}">Blog</a></li>
        <li><a href="{link(cur, 'contact/')}">Book a consultation</a></li>
        <li><a href="{asset(cur, 'assets/docs/privacy-policy.pdf')}">Privacy policy</a></li>
        <li><a href="{asset(cur, 'assets/docs/paia-manual.pdf')}">PAIA manual</a></li>
        <li><a href="{asset(cur, 'assets/docs/bbbee-certificate.pdf')}">B-BBEE certificate</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer__base">
    <span>© <span data-year>2026</span> {e(FIRM['legal_name'])}. All rights reserved.</span>
    <span>The information on this website is general and is not legal advice.</span>
  </div>
</footer>"""


def cta_band(cur, heading="Take action on your legal matter.", text="Book a consultation at our Pretoria or Sandton office."):
    return f"""
<section class="cta-band" aria-labelledby="cta-title">
  <div class="container cta-band__inner">
    <div>
      <h2 class="h2" id="cta-title">{e(heading)}</h2>
      <p>{e(text)}</p>
    </div>
    <div class="cta-band__btns">
      <a class="btn btn--light btn--lg" href="{link(cur, 'contact/')}">{ic('calendar')}Book a consultation</a>
      <a class="btn btn--outline-light btn--lg" href="tel:{tel(MAIN_OFFICE['phones'][0][0])}">{ic('phone')}{MAIN_OFFICE['phones'][0][0]}</a>
    </div>
  </div>
</section>"""


def faq_html(items, heading_id="faq-title", heading="Frequently asked questions", lead=None):
    rows = "".join(
        f'<details><summary>{e(q)}{ic("plus")}</summary><div class="faq__a"><p>{e(a)}</p></div></details>' for q, a in items
    )
    lead_html = f"<p>{e(lead)}</p>" if lead else ""
    return f"""<div class="section-head"><span class="stroke" aria-hidden="true"></span><h2 class="h2" id="{heading_id}">{e(heading)}</h2>{lead_html}</div>
<div class="faq">{rows}</div>"""


def faq_schema(items, page_url):
    return {
        "@type": "FAQPage",
        "@id": page_url + "#faq",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items],
    }


def breadcrumb_schema(trail, page_url):
    return {
        "@type": "BreadcrumbList",
        "@id": page_url + "#breadcrumb",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": DOMAIN + "/" + path} for i, (name, path) in enumerate(trail)
        ],
    }


def breadcrumb_html(cur, trail):
    items = []
    for i, (name, path) in enumerate(trail):
        if i == len(trail) - 1:
            items.append(f'<li aria-current="page">{e(name)}</li>')
        else:
            items.append(f'<li><a href="{link(cur, path)}">{e(name)}</a></li>')
    return f'<nav class="breadcrumb container" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'


def office_postal(o):
    return {
        "@type": "PostalAddress",
        "streetAddress": o["street"],
        "addressLocality": o["locality"],
        "addressRegion": "Gauteng",
        "postalCode": o["postcode"],
        "addressCountry": "ZA",
    }


def firm_node(full=True):
    if not full:
        return {"@id": FIRM_ID}
    node = {
        "@type": "Attorney",
        "@id": FIRM_ID,
        "name": FIRM["name"],
        "legalName": FIRM["legal_name"],
        "alternateName": FIRM["short"],
        "url": DOMAIN + "/",
        "logo": DOMAIN + "/assets/img/logo.png",
        "image": DOMAIN + "/assets/img/og.jpg",
        "slogan": FIRM["slogan"],
        "description": "Law firm with offices in Pretoria and Sandton, Gauteng: family, banking and finance, wills and estates, commercial, labour, criminal, insurance and conveyancing law.",
        "foundingDate": FIRM["founded"],
        "telephone": tel(FIRM["main_phone"]),
        "faxNumber": tel(MAIN_OFFICE["fax"]),
        "address": office_postal(MAIN_OFFICE),
        "areaServed": [{"@type": "City", "name": n} for n in ["Pretoria", "Midrand", "Sandton", "Johannesburg"]]
        + [{"@type": "AdministrativeArea", "name": "Gauteng"}],
        "department": [{"@id": f"{DOMAIN}/attorneys-{o['slug']}/#office"} for o in OFFICES],
        "knowsAbout": [p["name"] for p in PRACTICE],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Practice areas",
            "itemListElement": [
                {
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Service",
                        "name": p["name"],
                        "description": p["short"],
                        "url": f"{DOMAIN}/practice-areas/{p['slug']}/",
                    },
                }
                for p in PRACTICE
            ],
        },
    }
    if FIRM["email"]:
        node["email"] = FIRM["email"]
    if FIRM["social"]:
        node["sameAs"] = FIRM["social"]
    # TBC: add a `founder`/`employee` Person node (linked by @id) once the team details are confirmed.
    return node


def office_node(o):
    return {
        "@type": "Attorney",
        "@id": f"{DOMAIN}/attorneys-{o['slug']}/#office",
        "name": f"{FIRM['name']}: {o['name']} office",
        "url": f"{DOMAIN}/attorneys-{o['slug']}/",
        "image": DOMAIN + "/assets/img/og.jpg",
        "logo": DOMAIN + "/assets/img/logo.png",
        "telephone": tel(o["phones"][0][0]),
        "faxNumber": tel(o["fax"]),
        "address": office_postal(o),
        "areaServed": [{"@type": "City", "name": n} for n in o["areas"]],
        "parentOrganization": {"@id": FIRM_ID},
        "hasMap": "https://www.google.com/maps/search/?api=1&query=" + o["map_q"].replace(" ", "+"),
    }


def website_node():
    return {"@type": "WebSite", "@id": SITE_ID, "url": DOMAIN + "/", "name": FIRM["name"], "publisher": {"@id": FIRM_ID}, "inLanguage": "en-ZA"}


def page(cur, *, title, desc, body, graph, active=None, preload_hero=False, noindex=False):
    url = DOMAIN + "/" + cur
    graph = [website_node()] + graph
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    robots = '\n<meta name="robots" content="noindex">' if noindex else ""
    preload = ""
    if preload_hero:
        preload = (
            f'\n<link rel="preload" as="image" href="{asset(cur, "assets/img/hero.webp")}" '
            f'imagesrcset="{asset(cur, "assets/img/hero-mobile.webp")} 919w, {asset(cur, "assets/img/hero-960.webp")} 960w, {asset(cur, "assets/img/hero.webp")} 1919w" '
            'imagesizes="100vw" fetchpriority="high">'
        )
    return f"""<!doctype html>
<html lang="en-ZA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">{robots}
<meta name="theme-color" content="#0b1339">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(FIRM['name'])}">
<meta property="og:locale" content="en_ZA">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{DOMAIN}/assets/img/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(FIRM['name'])} logo beside a lion's eye">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{DOMAIN}/assets/img/og.jpg">
<link rel="icon" type="image/png" href="{asset(cur, 'assets/img/favicon.png')}">
<link rel="apple-touch-icon" href="{asset(cur, 'assets/img/apple-touch-icon.png')}">
<link rel="preload" href="{asset(cur, 'assets/fonts/manrope.woff2')}" as="font" type="font/woff2" crossorigin>
{preload}
<link rel="stylesheet" href="{asset(cur, 'assets/fonts/fonts.css')}">
<link rel="stylesheet" href="{asset(cur, 'styles.css')}">
<script src="{asset(cur, 'main.js')}" defer></script>
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
{header(cur, active)}
<main id="main">
{body}
</main>
{footer(cur)}
</body>
</html>
"""


def webpage_node(cur, name, desc, extra=None):
    node = {
        "@type": "WebPage",
        "@id": DOMAIN + "/" + cur + "#webpage",
        "url": DOMAIN + "/" + cur,
        "name": name,
        "description": desc,
        "isPartOf": {"@id": SITE_ID},
        "about": {"@id": FIRM_ID},
        "inLanguage": "en-ZA",
        "dateModified": LASTMOD,
    }
    if extra:
        node.update(extra)
    return node


# ---------------------------------------------------------------- components

def pa_cards(cur, items, heading_level=3):
    out = []
    for p in items:
        out.append(f"""<a class="pa-card" href="{link(cur, 'practice-areas/' + p['slug'] + '/')}">
  <div class="pa-card__img"><img src="{asset(cur, 'assets/img/' + p['img'])}" width="367" height="273" alt="{e(p['img_alt'])}" loading="lazy" decoding="async"></div>
  <h{heading_level}>{e(p['name'])}</h{heading_level}>
  <p>{e(p['short'])}</p>
  <span class="pa-card__more">More about {e(p['name'].lower())} {ic('arrow')}</span>
</a>""")
    return '<div class="pa-grid">' + "".join(out) + "</div>"


def office_cards(cur, heading_level=3):
    out = []
    for o in OFFICES:
        phones = "<br>".join(f'<a href="tel:{t}">{n}</a>' for n, t in o["phones"])
        maps = "https://www.google.com/maps/search/?api=1&query=" + o["map_q"].replace(" ", "+")
        out.append(f"""<article class="office">
  <h{heading_level}>{e(o['name'])}</h{heading_level}>
  <dl>
    <div><dt>Address</dt><dd>{'<br>'.join(e(l) for l in o['lines'])}</dd></div>
    <div><dt>Telephone</dt><dd>{phones}</dd></div>
    <div><dt>Fax</dt><dd>{o['fax']}</dd></div>
  </dl>
  <div class="office__links">
    <a class="btn btn--navy" href="{link(cur, 'attorneys-' + o['slug'] + '/')}">{e(o['name'])} office</a>
    <a class="btn btn--outline" href="{maps}" target="_blank" rel="noopener">{ic('pin')}Directions</a>
  </div>
</article>""")
    return '<div class="offices">' + "".join(out) + "</div>"


def team_cards(heading_level=3):
    out = []
    for name, role, bio in TEAM:
        out.append(f"""<article class="person">
  <div class="person__photo" role="img" aria-label="Photo to follow">{ic('user')}</div>
  <h{heading_level} class="placeholder">{e(name)}</h{heading_level}>
  <p class="person__role placeholder">{e(role)}</p>
  <p class="placeholder">{e(bio)}</p>
</article>""")
    return '<div class="team-grid">' + "".join(out) + "</div>"


def testimonials():
    slides = "".join(
        f'<figure class="quote"><blockquote><p>{e(q)}</p></blockquote><figcaption><strong>{e(n)}</strong>{e(r)}</figcaption></figure>'
        for q, n, r in TESTIMONIALS
    )
    return f"""<section class="section section--navy" aria-labelledby="testimonials-title">
  <div class="container">
    <div class="section-head"><span class="stroke" aria-hidden="true"></span><h2 class="h2" id="testimonials-title">What our clients say</h2></div>
    <div class="carousel" data-carousel>
      <div class="carousel__track" tabindex="0" aria-label="Client testimonials">{slides}</div>
      <div class="carousel__nav">
        <button class="carousel__btn" type="button" data-dir="prev" aria-label="Previous testimonial">{ic('left')}</button>
        <button class="carousel__btn" type="button" data-dir="next" aria-label="Next testimonial">{ic('arrow')}</button>
      </div>
    </div>
  </div>
</section>"""


def blog_empty(cur):
    return f"""<div class="empty">
  {ic('pen')}
  <div>
    <h3>Articles coming soon</h3>
    <p>We'll publish plain-language guides to common legal questions here, such as how evictions work and what a Section 129 notice means.</p>
  </div>
</div>"""


# ---------------------------------------------------------------- pages

def home():
    cur = ""
    desc = ("Law firm in Pretoria and Sandton: family and divorce, commercial, labour, criminal, insurance, banking, "
            "conveyancing, wills and estates. Call 012 492 5505.")
    title = "Attorneys in Pretoria & Sandton | Vilakazi Smith Inc."
    body = f"""
<section class="hero" aria-labelledby="hero-title">
  <picture class="hero__media">
    <source media="(max-width: 760px)" srcset="assets/img/hero-mobile.webp">
    <img src="assets/img/hero.webp" srcset="assets/img/hero-960.webp 960w, assets/img/hero.webp 1919w" sizes="100vw" width="1919" height="682" alt="Close-up of a lion's eyes in deep navy tones" fetchpriority="high">
  </picture>
  <div class="container hero__inner">
    <div class="hero__copy">
      <h1 class="h1" id="hero-title"><span class="hero__slogan">Take action.</span><span class="hero__kw">Attorneys in Pretoria &amp; Sandton for individuals and businesses</span></h1>
      <p class="hero__sub">Tailored guidance and decisive advocacy in family, commercial, labour, criminal, insurance, property and estate law.</p>
      <div class="hero__ctas">
        <a class="btn btn--light btn--lg" href="{link(cur, 'contact/')}">{ic('calendar')}Book a consultation</a>
        <a class="btn btn--outline-light btn--lg" href="tel:{tel(FIRM['main_phone'])}">{ic('phone')}{FIRM['main_phone']}</a>
      </div>
    </div>
  </div>
</section>

<section class="facts" aria-label="About the firm at a glance">
  <ul class="container facts__grid" role="list">
    <li>{ic('scale')}<div><strong>Founded in {FIRM['founded']}</strong><span>{e(FIRM['legal_name'])}</span></div></li>
    <li>{ic('shield')}<div><strong>B-BBEE Level 2</strong><span>125% procurement recognition</span></div></li>
    <li>{ic('pin')}<div><strong>Pretoria &amp; Sandton</strong><span>Files managed centrally in Pretoria</span></div></li>
  </ul>
</section>

<section class="section" aria-labelledby="practice-title">
  <div class="container">
    <div class="section-head">
      <span class="stroke" aria-hidden="true"></span>
      <h2 class="h2" id="practice-title">Practice areas</h2>
      <p class="lead muted">Legal services for individuals, families and businesses across Gauteng. Choose an area to see how we help and answers to common questions.</p>
    </div>
    {pa_cards(cur, PRACTICE)}
  </div>
</section>

<section class="section section--mist" aria-labelledby="mission-title">
  <div class="container split">
    <div class="split__aside">
      <span class="stroke" aria-hidden="true"></span>
      <h2 class="h2" id="mission-title">{e(MISSION[0])}</h2>
      <a class="text-link" href="{link(cur, 'about/')}">About Vilakazi Smith Inc.</a>
    </div>
    <div>
      <p class="lead">{e(MISSION[1])}</p>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="team-title">
  <div class="container">
    <div class="section-head">
      <span class="stroke" aria-hidden="true"></span>
      <h2 class="h2" id="team-title">Our attorneys</h2>
      <p class="lead muted">Meet the people who will handle your matter.</p>
    </div>
    {team_cards()}
  </div>
</section>

{testimonials()}

<section class="section section--mist" aria-labelledby="offices-title">
  <div class="container">
    <div class="section-head">
      <span class="stroke" aria-hidden="true"></span>
      <h2 class="h2" id="offices-title">Our offices</h2>
      <p class="lead muted">See us in Pretoria or Sandton. Postal address for both offices: {e(FIRM['postal'])}.</p>
    </div>
    {office_cards(cur)}
  </div>
</section>

<section class="section" aria-labelledby="blog-title">
  <div class="container">
    <div class="section-head">
      <span class="stroke" aria-hidden="true"></span>
      <h2 class="h2" id="blog-title">Legal insights</h2>
    </div>
    {blog_empty(cur)}
  </div>
</section>

<section class="section section--mist" aria-labelledby="faq-title">
  <div class="container">
    {faq_html(HOME_FAQS)}
  </div>
</section>

{cta_band(cur)}
"""
    graph = [firm_node(), webpage_node(cur, title, desc), faq_schema(HOME_FAQS, DOMAIN + "/")] + [office_node(o) for o in OFFICES]
    return cur, page(cur, title=title, desc=desc, body=body, graph=graph, preload_hero=True)


def practice_index():
    cur = "practice-areas/"
    title = "Practice Areas | Vilakazi Smith Inc. Attorneys"
    desc = "Family, banking, wills and estates, commercial, labour, criminal, insurance and conveyancing law. Vilakazi Smith Inc., attorneys in Pretoria and Sandton."
    trail = [("Home", ""), ("Practice areas", cur)]
    body = f"""
<section class="page-hero page-hero--plain" aria-labelledby="page-title">
  {breadcrumb_html(cur, trail)}
  <div class="container page-hero__inner">
    <div>
      <h1 class="h1" id="page-title">Practice areas</h1>
      <p class="page-hero__lead">Eight areas of law, handled from our offices in Pretoria and Sandton. Each page explains what we do and answers the questions clients ask most.</p>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">{pa_cards(cur, PRACTICE, heading_level=2)}</div>
</section>
{cta_band(cur, "Not sure which area your matter falls under?", "Call us and we'll point you to the right attorney.")}
"""
    graph = [firm_node(False), webpage_node(cur, title, desc, {"@type": "CollectionPage", "breadcrumb": {"@id": DOMAIN + "/" + cur + "#breadcrumb"}}),
             breadcrumb_schema(trail, DOMAIN + "/" + cur)]
    return cur, page(cur, title=title, desc=desc, body=body, graph=graph, active="practice")


def practice_page(p):
    cur = f"practice-areas/{p['slug']}/"
    url = DOMAIN + "/" + cur
    trail = [("Home", ""), ("Practice areas", "practice-areas/"), (p["name"], cur)]
    services = "".join(f'<li>{ic("check")}<div><strong>{e(s)}</strong><span>{e(d)}</span></div></li>' for s, d in p["services"])
    body_p = "".join(f"<p>{e(x)}</p>" for x in p["body"])
    others = [x for x in PRACTICE if x["slug"] != p["slug"]]
    i = PRACTICE.index(p)
    related = [others[(i + k) % len(others)] for k in range(3)]
    related_html = "".join(
        f'<a href="{link(cur, "practice-areas/" + r["slug"] + "/")}"><strong>{e(r["name"])}</strong><span>{e(r["short"])}</span></a>' for r in related
    )
    offices = "".join(
        f'<div><strong>{e(o["name"])}</strong>' + " / ".join(f'<a href="tel:{t}">{n}</a>' for n, t in o["phones"]) + "</div>" for o in OFFICES
    )
    body = f"""
<section class="page-hero" aria-labelledby="page-title">
  {breadcrumb_html(cur, trail)}
  <div class="container page-hero__inner">
    <div>
      <h1 class="h1" id="page-title">{e(p['h1'])}</h1>
      <p class="page-hero__lead">{e(p['lead'])}</p>
      <div class="hero__ctas">
        <a class="btn btn--light" href="{link(cur, 'contact/')}">{ic('calendar')}Book a consultation</a>
        <a class="btn btn--outline-light" href="tel:{tel(FIRM['main_phone'])}">{ic('phone')}{FIRM['main_phone']}</a>
      </div>
    </div>
    <div class="page-hero__img"><img src="{asset(cur, 'assets/img/' + p['img'])}" width="367" height="273" alt="{e(p['img_alt'])}" fetchpriority="high"></div>
  </div>
</section>

<section class="section">
  <div class="container article">
    <div class="prose">
      <h2>{e(p['name'])}: how we help</h2>
      {body_p}
      <h3>Our {e(p['name'].lower())} services</h3>
      <ul class="services" role="list">{services}</ul>
    </div>
    <aside class="aside-card" aria-labelledby="aside-title">
      <h2 id="aside-title">Speak to an attorney</h2>
      <p>Tell us briefly what your matter is about, and we'll arrange a consultation at the office that suits you.</p>
      <a class="btn btn--light" href="{link(cur, 'contact/')}">Book a consultation</a>
      <div class="aside-card__offices">{offices}</div>
    </aside>
  </div>
</section>

<section class="section section--mist" aria-labelledby="faq-title">
  <div class="container">
    {faq_html(p['faqs'], heading=p['name'] + ": common questions", lead="General information only. Every matter is different, so speak to us about yours.")}
  </div>
</section>

<section class="section section--tight" aria-labelledby="related-title">
  <div class="container">
    <div class="section-head"><h2 class="h3" id="related-title">Related practice areas</h2></div>
    <div class="related">{related_html}</div>
  </div>
</section>

{cta_band(cur)}
"""
    service = {
        "@type": "Service",
        "@id": url + "#service",
        "name": p["name"],
        "serviceType": p["name"],
        "description": p["lead"],
        "url": url,
        "provider": {"@id": FIRM_ID},
        "areaServed": [{"@type": "City", "name": n} for n in ["Pretoria", "Sandton", "Johannesburg"]],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": p["name"],
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s, "description": d}} for s, d in p["services"]],
        },
    }
    graph = [firm_node(False), webpage_node(cur, p["meta_title"], p["meta_desc"], {"breadcrumb": {"@id": url + "#breadcrumb"}, "mainEntity": {"@id": url + "#service"}}),
             service, faq_schema(p["faqs"], url), breadcrumb_schema(trail, url)]
    return cur, page(cur, title=p["meta_title"], desc=p["meta_desc"], body=body, graph=graph, active="practice")


def office_page(o):
    cur = f"attorneys-{o['slug']}/"
    url = DOMAIN + "/" + cur
    trail = [("Home", ""), (f"{o['name']} office", cur)]
    phones = "<br>".join(f'<a href="tel:{t}">{n}</a>' for n, t in o["phones"])
    maps = "https://www.google.com/maps/search/?api=1&query=" + o["map_q"].replace(" ", "+")
    intro = "".join(f"<p>{e(x)}</p>" for x in o["intro"])
    other = [x for x in OFFICES if x["slug"] != o["slug"]][0]
    pa_list = "".join(
        f'<li>{ic("check")}<div><strong><a href="{link(cur, "practice-areas/" + p["slug"] + "/")}">{e(p["name"])}</a></strong><span>{e(p["short"])}</span></div></li>'
        for p in PRACTICE
    )
    body = f"""
<section class="page-hero page-hero--plain" aria-labelledby="page-title">
  {breadcrumb_html(cur, trail)}
  <div class="container page-hero__inner">
    <div>
      <h1 class="h1" id="page-title">{e(o['title'])}</h1>
      <p class="page-hero__lead">{e(FIRM['name'])}, {e(', '.join(o['lines']))}.</p>
      <div class="hero__ctas">
        <a class="btn btn--light" href="tel:{o['phones'][0][1]}">{ic('phone')}{o['phones'][0][0]}</a>
        <a class="btn btn--outline-light" href="{link(cur, 'contact/')}">{ic('calendar')}Book a consultation</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container contact-grid">
    <div class="prose">
      <h2>Our {e(o['name'])} office</h2>
      {intro}
      <div class="offices" style="grid-template-columns:1fr;margin-top:28px">
        <article class="office" style="background:var(--mist)">
          <dl>
            <div><dt>Address</dt><dd>{'<br>'.join(e(l) for l in o['lines'])}</dd></div>
            <div><dt>Telephone</dt><dd>{phones}</dd></div>
            <div><dt>Fax</dt><dd>{o['fax']}</dd></div>
            <div><dt>Postal address</dt><dd>{e(FIRM['postal'])}</dd></div>
          </dl>
          <div class="office__links"><a class="btn btn--outline" href="{maps}" target="_blank" rel="noopener">{ic('pin')}Get directions</a></div>
        </article>
      </div>
    </div>
    <div class="map">
      <div>
        <p>The map loads from Google Maps when you open it.</p>
        <button class="btn btn--navy" type="button" data-map="{e(o['map_q'])}" data-title="Map of the {e(o['name'])} office">{ic('pin')}Show map</button>
      </div>
    </div>
  </div>
</section>

<section class="section section--mist" aria-labelledby="pa-title">
  <div class="container">
    <div class="section-head"><span class="stroke" aria-hidden="true"></span><h2 class="h2" id="pa-title">Legal services at our {e(o['name'])} office</h2>
    <p class="lead muted">Consult a {e(o['name'])} attorney about any of our practice areas.</p></div>
    <ul class="services" role="list" style="max-width:860px">{pa_list}</ul>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <p class="lead">Closer to {e(other['name'])}? <a class="text-link" href="{link(cur, 'attorneys-' + other['slug'] + '/')}">Visit our {e(other['name'])} office</a>.</p>
  </div>
</section>

{cta_band(cur, f"Speak to an attorney in {o['name']}.", f"Call {o['phones'][0][0]} or book a consultation online.")}
"""
    graph = [firm_node(False), office_node(o), webpage_node(cur, o["meta_title"], o["meta_desc"], {"breadcrumb": {"@id": url + "#breadcrumb"}, "mainEntity": {"@id": url + "#office"}}),
             breadcrumb_schema(trail, url)]
    return cur, page(cur, title=o["meta_title"], desc=o["meta_desc"], body=body, graph=graph, active="offices")


def about():
    cur = "about/"
    url = DOMAIN + "/" + cur
    title = "About Us | Vilakazi Smith Incorporated, Attorneys Since 2020"
    desc = "Vilakazi Smith Incorporated (VSI), founded in 2020, B-BBEE Level 2. Offices in Pretoria and Sandton, with all files managed centrally in Pretoria."
    trail = [("Home", ""), ("About", cur)]
    about_p = "".join(f"<p>{e(x)}</p>" for x in ABOUT)
    body = f"""
<section class="page-hero page-hero--plain" aria-labelledby="page-title">
  {breadcrumb_html(cur, trail)}
  <div class="container page-hero__inner">
    <div>
      <h1 class="h1" id="page-title">Get to know Vilakazi Smith Inc.</h1>
      <p class="page-hero__lead">A Gauteng law firm founded in {FIRM['founded']}, with offices in Pretoria and Sandton.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="split__aside"><span class="stroke" aria-hidden="true"></span><h2 class="h2">About the firm</h2></div>
    <div class="prose">{about_p}</div>
  </div>
</section>

<section class="section section--mist" aria-labelledby="mission-title">
  <div class="container split">
    <div class="split__aside"><span class="stroke" aria-hidden="true"></span><h2 class="h2" id="mission-title">Our why</h2></div>
    <div><p class="lead"><strong>{e(MISSION[0])}</strong></p><p>{e(MISSION[1])}</p></div>
  </div>
</section>

<section class="section" aria-labelledby="team-title">
  <div class="container">
    <div class="section-head"><span class="stroke" aria-hidden="true"></span><h2 class="h2" id="team-title">Our attorneys</h2></div>
    {team_cards()}
  </div>
</section>

<section class="section section--mist" aria-labelledby="docs-title">
  <div class="container">
    <div class="section-head"><span class="stroke" aria-hidden="true"></span><h2 class="h2" id="docs-title">Compliance documents</h2></div>
    <div class="docs">
      <a href="{asset(cur, 'assets/docs/bbbee-certificate.pdf')}">{ic('file')}<span>B-BBEE certificate<small>Level 2, PDF</small></span></a>
      <a href="{asset(cur, 'assets/docs/paia-manual.pdf')}">{ic('file')}<span>PAIA manual<small>PDF</small></span></a>
      <a href="{asset(cur, 'assets/docs/privacy-policy.pdf')}">{ic('file')}<span>Privacy policy<small>PDF</small></span></a>
    </div>
  </div>
</section>

{cta_band(cur)}
"""
    graph = [firm_node(False), webpage_node(cur, title, desc, {"@type": "AboutPage", "breadcrumb": {"@id": url + "#breadcrumb"}}), breadcrumb_schema(trail, url)]
    return cur, page(cur, title=title, desc=desc, body=body, graph=graph, active="about")


def blog():
    cur = "blog/"
    url = DOMAIN + "/" + cur
    title = "Legal Insights Blog | Vilakazi Smith Inc. Attorneys"
    desc = "Plain-language articles on South African law from the attorneys at Vilakazi Smith Inc. in Pretoria and Sandton."
    trail = [("Home", ""), ("Blog", cur)]
    body = f"""
<section class="page-hero page-hero--plain" aria-labelledby="page-title">
  {breadcrumb_html(cur, trail)}
  <div class="container page-hero__inner">
    <div>
      <h1 class="h1" id="page-title">Legal insights</h1>
      <p class="page-hero__lead">Plain-language answers to common legal questions, written by our attorneys.</p>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <!-- Add one <article class="post"> per published article inside .posts, newest first, then delete the .empty block.
    <div class="posts">
      <article class="post">
        <time datetime="2026-11-01">1 November 2026</time>
        <h2 class="h3"><a href="how-evictions-work/">How does the eviction process work in South Africa?</a></h2>
        <p>One-sentence summary of the article.</p>
        <a class="text-link" href="how-evictions-work/">Read the article</a>
      </article>
    </div>
    -->
    {blog_empty(cur)}
  </div>
</section>
{cta_band(cur)}
"""
    graph = [firm_node(False), webpage_node(cur, title, desc, {"@type": "CollectionPage", "breadcrumb": {"@id": url + "#breadcrumb"}}),
             {"@type": "Blog", "@id": url + "#blog", "name": "Legal insights", "url": url, "publisher": {"@id": FIRM_ID}, "inLanguage": "en-ZA"},
             breadcrumb_schema(trail, url)]
    return cur, page(cur, title=title, desc=desc, body=body, graph=graph, active="blog")


def contact():
    cur = "contact/"
    url = DOMAIN + "/" + cur
    title = "Contact Us & Book a Consultation | Vilakazi Smith Inc."
    desc = "Book a consultation with Vilakazi Smith Inc. Pretoria: 012 492 5505. Sandton: 010 979 4130. Or send a consultation request online."
    trail = [("Home", ""), ("Contact", cur)]
    pa_opts = "".join(f"<option>{e(p['name'])}</option>" for p in PRACTICE)
    off_opts = "".join(f"<option>{e(o['name'])}</option>" for o in OFFICES)
    body = f"""
<section class="page-hero page-hero--plain" aria-labelledby="page-title">
  {breadcrumb_html(cur, trail)}
  <div class="container page-hero__inner">
    <div>
      <h1 class="h1" id="page-title">Book a consultation</h1>
      <p class="page-hero__lead">Call the office nearest to you, or send a request below and we'll contact you to arrange a time.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container contact-grid">
    <form class="form" data-enquiry novalidate>
      <div class="field"><label for="f-name">Full name</label><input id="f-name" name="name" autocomplete="name" required></div>
      <div class="field"><label for="f-phone">Phone number</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" required></div>
      <div class="field field--full"><label for="f-email">Email address</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
      <div class="field"><label for="f-area">Type of matter</label><select id="f-area" name="practice_area" required><option value="">Choose one</option>{pa_opts}<option>Something else</option></select></div>
      <div class="field"><label for="f-office">Preferred office</label><select id="f-office" name="office" required><option value="">Choose one</option>{off_opts}</select></div>
      <div class="field field--full"><label for="f-msg">Briefly, what is your matter about? <span class="hint">(optional)</span></label><textarea id="f-msg" name="message"></textarea></div>
      <div class="hp" aria-hidden="true"><label>Leave this empty<input name="_gotcha" tabindex="-1" autocomplete="off"></label></div>
      <label class="consent"><input type="checkbox" name="popia_consent" value="yes" required><span>I consent to Vilakazi Smith Inc. processing my personal information to respond to this request, as set out in the <a href="{asset(cur, 'assets/docs/privacy-policy.pdf')}">privacy policy</a> (POPIA).</span></label>
      <div class="form__actions">
        <button class="btn btn--navy btn--lg" type="submit">Send consultation request</button>
        <p class="form__status" role="status" aria-live="polite"></p>
      </div>
    </form>
    <div>
      {office_cards(cur, heading_level=2)}
      <p class="muted" style="margin-top:20px">Postal address: {e(FIRM['postal'])}</p>
    </div>
  </div>
</section>
"""
    graph = [firm_node(False), webpage_node(cur, title, desc, {"@type": "ContactPage", "breadcrumb": {"@id": url + "#breadcrumb"}}), breadcrumb_schema(trail, url)]
    return cur, page(cur, title=title, desc=desc, body=body, graph=graph, active="contact")


def not_found():
    # 404 pages are served at any depth, so they use root-relative links.
    html = page("", title="Page not found | Vilakazi Smith Inc.", desc="This page could not be found.", graph=[], noindex=True, body=f"""
<section class="page-hero page-hero--plain"><div class="container page-hero__inner"><div>
  <h1 class="h1">Page not found</h1>
  <p class="page-hero__lead">The page you were looking for has moved or no longer exists. Try one of our practice areas, or call us on {FIRM['main_phone']}.</p>
  <div class="hero__ctas"><a class="btn btn--light" href="/practice-areas/">Practice areas</a><a class="btn btn--outline-light" href="/contact/">Contact us</a></div>
</div></div></section>""")
    html = html.replace('href="assets/', 'href="/assets/').replace('src="assets/', 'src="/assets/').replace('href="styles.css"', 'href="/styles.css"').replace('src="main.js"', 'src="/main.js"')
    for o in ["practice-areas/", "attorneys-pretoria/", "attorneys-sandton/", "about/", "blog/", "contact/"]:
        html = html.replace(f'href="{o}', f'href="/{o}')
    html = html.replace('href="./"', 'href="/"')
    return "404.html", html


def post_template():
    """A ready-made article page. Copy blog/_post-template.html to blog/<slug>/index.html and fill it in."""
    cur = "blog/_template/"
    url = DOMAIN + "/blog/ARTICLE-SLUG/"
    graph = [firm_node(False), {
        "@type": "BlogPosting",
        "@id": url + "#article",
        "headline": "ARTICLE TITLE",
        "description": "ARTICLE SUMMARY",
        "url": url,
        "datePublished": "YYYY-MM-DD",
        "dateModified": "YYYY-MM-DD",
        "image": DOMAIN + "/assets/img/og.jpg",
        "author": {"@type": "Person", "name": "ATTORNEY NAME", "jobTitle": "Attorney", "worksFor": {"@id": FIRM_ID}},
        "publisher": {"@id": FIRM_ID},
        "isPartOf": {"@id": DOMAIN + "/blog/#blog"},
        "inLanguage": "en-ZA",
    }]
    trail = [("Home", ""), ("Blog", "blog/"), ("ARTICLE TITLE", cur)]
    body = f"""
<section class="page-hero page-hero--plain">
  {breadcrumb_html(cur, trail)}
  <div class="container page-hero__inner"><div>
    <h1 class="h1">ARTICLE TITLE</h1>
    <p class="page-hero__lead">By ATTORNEY NAME · <time datetime="YYYY-MM-DD">DD Month YYYY</time></p>
  </div></div>
</section>
<section class="section"><div class="container article">
  <article class="prose">
    <p>Intro paragraph that answers the question directly.</p>
    <h2>Subheading</h2>
    <p>Body text.</p>
    <p class="muted"><em>This article is general information and not legal advice. Speak to us about your matter.</em></p>
  </article>
  <aside class="aside-card"><h2>Speak to an attorney</h2><p>Book a consultation at our Pretoria or Sandton office.</p><a class="btn btn--light" href="{link(cur, 'contact/')}">Book a consultation</a></aside>
</div></section>
{cta_band(cur)}
"""
    html = page(cur, title="ARTICLE TITLE | Vilakazi Smith Inc.", desc="ARTICLE SUMMARY (150–160 characters).", body=body, graph=graph, active="blog", noindex=True)
    return "blog/_post-template.html", html.replace(DOMAIN + "/blog/_template/", url)


# ---------------------------------------------------------------- write

def write(out, rel, html):
    path = os.path.join(out, rel if rel.endswith(".html") else rel + "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    global PREVIEW
    out = ROOT
    if len(sys.argv) > 2 and sys.argv[1] == "--preview":
        PREVIEW = True
        out = os.path.abspath(sys.argv[2])
        if os.path.exists(out):
            shutil.rmtree(out)
        shutil.copytree(ROOT, out, ignore=shutil.ignore_patterns("build", "references", ".git", "README.md", "*.py"))

    pages = [home(), practice_index()] + [practice_page(p) for p in PRACTICE] + [office_page(o) for o in OFFICES] + [about(), blog(), contact()]
    for rel, html in pages:
        write(out, rel, html)
    if not PREVIEW:
        rel, html = not_found()
        write(out, rel, html)
        rel, html = post_template()
        write(out, rel, html)

        urls = "".join(
            f"  <url><loc>{DOMAIN}/{rel}</loc><lastmod>{LASTMOD}</lastmod></url>\n" for rel, _ in pages
        )
        with open(os.path.join(out, "sitemap.xml"), "w", encoding="utf-8") as f:
            f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
        with open(os.path.join(out, "robots.txt"), "w", encoding="utf-8") as f:
            f.write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    print(f"Wrote {len(pages)} pages to {out}")


if __name__ == "__main__":
    main()
