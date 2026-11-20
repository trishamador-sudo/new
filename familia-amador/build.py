#!/usr/bin/env python3
"""Família Amador Construções: static site generator.

Run `python3 build.py`. It writes the full PT + EN site into site/.
Change the domain in DOMAIN below (one place), then rebuild.
Copy lives in content.py.
"""
import html
import json
import re
import shutil
from datetime import date
from pathlib import Path

from content import SERVICES, AREAS, VILLAGES, ALL_TOWNS, HOME_FAQ

# ------------------------------------------------------------------ Config
DOMAIN = "https://familiaamador.com"
FORMSPREE = "https://formspree.io/f/mrpqkrva"
BRAND = "Família Amador Construções"
PEOPLE = {
    "ricardo": {"name": "Ricardo", "tel": "+351969164772", "show": "+351 969 164 772", "wa": "351969164772",
                "langs": {"pt": "PT / EN", "en": "PT / EN"}, "knows": ["pt", "en"]},
    "trishta": {"name": "Trishta", "tel": "+351961909846", "show": "+351 961 909 846", "wa": "351961909846",
                "langs": {"pt": "EN", "en": "EN"}, "knows": ["en"]},
}
ROOT = Path(__file__).parent
OUT = ROOT / "site"
TODAY = date.today().isoformat()

# ------------------------------------------------------------------ Labels
L = {
    "pt": {
        "nav": [("/servicos/", "Serviços"), ("/zonas/", "Zonas"), ("/projetos/", "Projetos"), ("/sobre-nos/", "Sobre nós"), ("/contacto/", "Contacto")],
        "quote": "Pedir orçamento", "quote_free": "Pedir orçamento grátis", "wa_talk": "Falar no WhatsApp",
        "menu": "Abrir menu", "close": "Fechar menu", "home": "Início", "more": "Saiba mais",
        "wa_msg": "Olá, gostaria de pedir um orçamento", "wa_title": "Fale connosco no WhatsApp",
        "trust": ["Respondemos em poucas horas", "Equipa familiar", "Falamos português e inglês"],
        "before": "Antes", "after": "Depois", "skip": "Saltar para o conteúdo",
        "lang_name": "Português", "other_lang": "EN", "other_label": "English",
        "services": "Serviços", "areas": "Zonas", "footer_desc": "Empresa familiar de obras e remodelações em Montemor-o-Novo, Alentejo. Pai e filha, qualidade à medida e respostas rápidas e honestas.",
        "no_electric": "Não fazemos trabalhos elétricos.",
    },
    "en": {
        "nav": [("/en/services/", "Services"), ("/en/areas/", "Areas"), ("/en/projects/", "Projects"), ("/en/about/", "About"), ("/en/contact/", "Contact")],
        "quote": "Get a quote", "quote_free": "Get a free quote", "wa_talk": "Chat on WhatsApp",
        "menu": "Open menu", "close": "Close menu", "home": "Home", "more": "Find out more",
        "wa_msg": "Hi, I'd like a quote", "wa_title": "Chat with us on WhatsApp",
        "trust": ["We reply within hours", "Family team", "We speak English"],
        "before": "Before", "after": "After", "skip": "Skip to content",
        "lang_name": "English", "other_lang": "PT", "other_label": "Português",
        "services": "Services", "areas": "Areas", "footer_desc": "Family-run renovation and building company in Montemor-o-Novo, Alentejo. Dad and daughter, bespoke quality, and fast, honest replies in English.",
        "no_electric": "We do not do electrical work.",
    },
}

# ------------------------------------------------------------------ Icons
ICONS = {
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "out": '<path d="M7 17 17 7M8 7h9v9"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "x": '<path d="M6 6l12 12M18 6 6 18"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "wa": '<path fill="currentColor" stroke="none" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "heart": '<path d="M19 14c1.5-1.5 3-3.2 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.8 0-3 .5-4.5 2-1.5-1.5-2.7-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4 3 5.5l7 7Z"/>',
    "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
    "home": '<path d="m3 10 9-7 9 7v10a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z"/>',
    "bath": '<path d="M4 12h16v3a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5z"/><path d="M6 12V5a2 2 0 0 1 3.5-1.3M7 20l-1 2M17 20l1 2"/>',
    "kitchen": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M4 10h16M8 6.5h2M8 14v3"/>',
    "brush": '<path d="M18 3l3 3-9 9-3-3z"/><path d="M9 12c-3 0-5 2-5 5 0 1.5-1 3-2 3 4 1 9 0 9-5"/>',
    "saw": '<path d="M3 14 14 3l7 7-11 11H3z"/><path d="m7 14 2 2M10 11l2 2M13 8l2 2"/>',
    "drop": '<path d="M12 2.7S5 10 5 15a7 7 0 0 0 14 0c0-5-7-12.3-7-12.3z"/>',
    "roof": '<path d="M2 12 12 4l10 8M5 10v10h14V10"/><path d="M16 6V3h3v5.5"/>',
    "damp": '<path d="M7 3S3 8 3 11a4 4 0 0 0 8 0c0-3-4-8-4-8z"/><path d="M17 9s-3 4-3 6a3 3 0 0 0 6 0c0-2-3-6-3-6z"/>',
    "ceiling": '<path d="M3 4h18M5 4v4h14V4M8 8v3M16 8v3M3 20h18"/>',
    "tools": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
}
SPRITE = '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>' + "".join(
    f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items()) + "</defs></svg>"


def ic(name, cls="ic"):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'


def esc(s):
    return html.escape(s, quote=True)


IMG = {  # name: (width, height) of the generated files
    "hero": (1376, 768), "hallway-before": (800, 960), "hallway-after": (800, 960),
    "bathroom-vanity": (700, 1244), "bathroom-shower": (700, 1244),
}


LAZY = ' loading="lazy" decoding="async"'
EAGER = ' fetchpriority="high"'


def picture(name, alt, cls="", lazy=True, sizes="(min-width: 900px) 33vw, 100vw"):
    w, h = IMG[name]
    load = LAZY if lazy else EAGER
    if name == "hero":
        srcw = "/assets/img/hero-768.webp 768w, /assets/img/hero.webp 1376w"
        srcj = "/assets/img/hero-768.jpg 768w, /assets/img/hero.jpg 1376w"
        return (f'<picture><source type="image/webp" srcset="{srcw}" sizes="{sizes}">'
                f'<img class="{cls}" src="/assets/img/hero.jpg" srcset="{srcj}" sizes="{sizes}" width="{w}" height="{h}" alt="{esc(alt)}"'
                f'{load}></picture>')
    return (f'<picture><source type="image/webp" srcset="/assets/img/{name}.webp">'
            f'<img class="{cls}" src="/assets/img/{name}.jpg" width="{w}" height="{h}" alt="{esc(alt)}"'
            f'{LAZY if lazy else ""}></picture>')


# ------------------------------------------------------------------ URLs
def svc_url(s, lang):
    return f"/servicos/{s['pt_slug']}/" if lang == "pt" else f"/en/services/{s['en_slug']}/"


def area_url(a, lang):
    return f"/zonas/{a['pt_slug']}/" if lang == "pt" else f"/en/areas/{a['en_slug']}/"


def town_name(a, lang):
    return a.get("town_en", a["town"]) if lang == "en" else a["town"]


SVC = {s["key"]: s for s in SERVICES}
ALT_TEXT = {
    "pt": {
        "hero": "Cozinha moderna com ilha em pedra, armários pretos e pavimento de madeira",
        "hallway-before": "Hall antes da remodelação, com mosaico antigo e paredes por acabar",
        "hallway-after": "Hall remodelado em Montemor-o-Novo, com pavimento efeito madeira, painel ripado e pintura nova",
        "bathroom-shower": "Remodelação de casa de banho com microcimento e duche walk-in com resguardo de vidro",
        "bathroom-vanity": "Casa de banho em microcimento com móvel de lavatório por medida e bancada em granito",
    },
    "en": {
        "hero": "Modern kitchen with a stone island, black cabinets and wooden flooring",
        "hallway-before": "Hallway before the renovation, with old tiles and unfinished walls",
        "hallway-after": "Renovated hallway in the Alentejo with wood-effect flooring, a slatted feature wall and fresh paint",
        "bathroom-shower": "Bathroom renovation with microcement walls and floor and a walk-in shower with a glass screen",
        "bathroom-vanity": "Microcement bathroom with a custom-made vanity unit and granite worktop",
    },
}

# ------------------------------------------------------------------ Schema
BUSINESS_ID = DOMAIN + "/#business"


def business_schema():
    return {
        "@type": "HomeAndConstructionBusiness", "@id": BUSINESS_ID, "name": BRAND,
        "url": DOMAIN + "/", "logo": DOMAIN + "/assets/img/icon-512.png", "image": DOMAIN + "/assets/img/og.jpg",
        "description": "Empresa familiar de obras e remodelações em Montemor-o-Novo, Alentejo: casas de banho, cozinhas, pintura, carpintaria, canalização, telhados, infiltrações e pequenas reparações.",
        "telephone": PEOPLE["ricardo"]["tel"],
        "contactPoint": [
            {"@type": "ContactPoint", "contactType": "customer service", "telephone": p["tel"], "name": p["name"],
             "availableLanguage": ["Portuguese", "English"] if "pt" in p["knows"] else ["English"]}
            for p in PEOPLE.values()],
        "address": {"@type": "PostalAddress", "addressLocality": "Montemor-o-Novo", "addressRegion": "Évora", "addressCountry": "PT"},
        "areaServed": [{"@type": "City", "name": t} for t in ALL_TOWNS],
        "knowsLanguage": ["pt", "en"], "priceRange": "€€",
        "employee": [{"@id": DOMAIN + "/#ricardo"}, {"@id": DOMAIN + "/#trishta"}],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Serviços", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["pt"]["name"], "url": DOMAIN + svc_url(s, "pt")}} for s in SERVICES]},
    }


def people_schema():
    return [{"@type": "Person", "@id": DOMAIN + f"/#{k}", "name": p["name"], "worksFor": {"@id": BUSINESS_ID},
             "knowsLanguage": p["knows"]} for k, p in PEOPLE.items()]


def website_schema(lang):
    return {"@type": "WebSite", "@id": DOMAIN + "/#website", "url": DOMAIN + "/", "name": BRAND,
            "inLanguage": ["pt-PT", "en"], "publisher": {"@id": BUSINESS_ID}}


def faq_schema(faq):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def crumbs_schema(items):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + u} for i, (n, u) in enumerate(items)]}


# ------------------------------------------------------------------ Shared blocks
def head(p):
    url = DOMAIN + p["path"]
    alts = ""
    if p.get("alt"):
        pt_path, en_path = (p["path"], p["alt"]) if p["lang"] == "pt" else (p["alt"], p["path"])
        alts = (f'  <link rel="alternate" hreflang="pt-PT" href="{DOMAIN}{pt_path}">\n'
                f'  <link rel="alternate" hreflang="en" href="{DOMAIN}{en_path}">\n'
                f'  <link rel="alternate" hreflang="x-default" href="{DOMAIN}{pt_path}">\n')
    robots = "noindex, follow" if p.get("noindex") else "index, follow, max-image-preview:large"
    canon = "" if p.get("nocanonical") else f'  <link rel="canonical" href="{url}">\n'
    preload = ('  <link rel="preload" as="image" type="image/webp" href="/assets/img/hero.webp" imagesrcset="/assets/img/hero-768.webp 768w, /assets/img/hero.webp 1376w" imagesizes="(min-width: 1240px) 1200px, 100vw">\n'
               if p.get("hero") else "")
    schema = json.dumps({"@context": "https://schema.org", "@graph": p["schema"]}, ensure_ascii=False, indent=1)
    lang_attr = "pt-PT" if p["lang"] == "pt" else "en"
    return f"""<!doctype html>
<html lang="{lang_attr}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(p['title'])}</title>
  <meta name="description" content="{esc(p['desc'])}">
  <meta name="robots" content="{robots}">
  <meta name="theme-color" content="#0A0A0A">
{canon}{alts}  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{BRAND}">
  <meta property="og:locale" content="{'pt_PT' if p['lang'] == 'pt' else 'en_GB'}">
  <meta property="og:locale:alternate" content="{'en_GB' if p['lang'] == 'pt' else 'pt_PT'}">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{esc(p['title'])}">
  <meta property="og:description" content="{esc(p['desc'])}">
  <meta property="og:image" content="{DOMAIN}/assets/img/og.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(p['title'])}">
  <meta name="twitter:description" content="{esc(p['desc'])}">
  <meta name="twitter:image" content="{DOMAIN}/assets/img/og.jpg">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="preload" href="/assets/fonts/outfit.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
{preload}  <link rel="stylesheet" href="/assets/css/styles.css">
  <script src="/assets/js/main.js" defer></script>
  <script type="application/ld+json">
{schema}
  </script>
</head>
"""


def header(p):
    lang = p["lang"]; t = L[lang]
    nav = "\n".join(f'        <a href="{h}"{CUR if p.get("section") == h else ""}>{n}</a>' for h, n in t["nav"])
    quote_href = "#orcamento" if p.get("form") else ("/contacto/" if lang == "pt" else "/en/contact/")
    alt = p.get("alt") or ("/en/" if lang == "pt" else "/")
    other_hreflang = "en" if lang == "pt" else "pt-PT"
    return f"""<body>
  <a class="skip-link" href="#main">{t['skip']}</a>
  {SPRITE}
  <header class="header">
    <div class="container header__inner">
      <a class="brand" href="{'/' if lang == 'pt' else '/en/'}" aria-label="{BRAND}, {t['home']}">
        <img src="/assets/img/logo-icon.png" width="150" height="106" alt="">
        <span class="brand__text"><span class="brand__name">Família Amador</span><span class="brand__sub">Construções</span></span>
      </a>
      <nav class="nav" id="site-nav" aria-label="{'Principal' if lang == 'pt' else 'Main'}">
{nav}
        <a class="nav__phone" href="tel:{PEOPLE['ricardo']['tel']}">{ic('phone')}{PEOPLE['ricardo']['show']}</a>
        <a class="btn btn--gold nav__cta-m" href="{quote_href}">{t['quote']}</a>
      </nav>
      <div class="header__actions">
        <a class="lang" href="{alt}" hreflang="{other_hreflang}" lang="{other_hreflang}" title="{t['other_label']}"><span aria-hidden="true">{'PT' if lang == 'pt' else 'EN'} | </span><strong>{t['other_lang']}</strong><span class="sr-only">{t['other_label']}</span></a>
        <a class="btn btn--gold header__cta" href="{quote_href}">{t['quote']} {ic('out', 'ic ic--sm')}</a>
        <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="{t['menu']}" data-label-open="{t['menu']}" data-label-close="{t['close']}">{ic('menu', 'ic ic-open')}{ic('x', 'ic ic-close')}</button>
      </div>
    </div>
  </header>
"""


CUR = ' aria-current="page"'


def wa_link(person, lang, extra=""):
    msg = L[lang]["wa_msg"] + (f" {extra}" if extra else "") + "."
    return f"https://wa.me/{PEOPLE[person]['wa']}?text=" + re.sub(r"[^A-Za-z0-9\-_.~]", lambda m: "".join(f"%{b:02X}" for b in m.group(0).encode()), msg)


def wa_chooser(p):
    lang = p["lang"]; t = L[lang]; extra = p.get("wa_extra", "")
    items = "".join(f'<a class="wa-pick" href="{wa_link(k, lang, extra)}" target="_blank" rel="noopener">{ic("wa")}<span><strong>{v["name"]}</strong> ({v["langs"][lang]})</span></a>' for k, v in PEOPLE.items())
    return f"""  <div class="wa" data-wa>
    <div class="wa__panel" id="wa-panel" hidden>
      <p class="wa__title">{t['wa_title']}</p>
      {items}
    </div>
    <a class="wa__btn" href="{wa_link('ricardo', lang, extra)}" target="_blank" rel="noopener" aria-controls="wa-panel" aria-expanded="false" data-wa-toggle aria-label="{t['wa_title']}">{ic('wa')}</a>
  </div>
"""


def footer(p):
    lang = p["lang"]; t = L[lang]
    svcs = "".join(f'<li><a href="{svc_url(s, lang)}">{s[lang]["name"]}</a></li>' for s in SERVICES)
    areas = "".join(f'<li><a href="{area_url(a, lang)}">{town_name(a, lang)}</a></li>' for a in AREAS)
    people = "".join(f'<li><a href="{wa_link(k, lang, p.get("wa_extra", ""))}" target="_blank" rel="noopener">{ic("wa")}{v["name"]} ({v["langs"][lang]}): {v["show"]}</a></li>' for k, v in PEOPLE.items())
    alt = p.get("alt") or ("/en/" if lang == "pt" else "/")
    pt_href, en_href = (p["path"], alt) if lang == "pt" else (alt, p["path"])
    if p["path"] == "/404.html":
        pt_href, en_href = "/", "/en/"
    # <!-- EMAIL: add once known, e.g. <li><a href="mailto:...">...</a></li> -->
    return f"""  <footer class="footer">
    <div class="container footer__grid">
      <div class="footer__brand">
        <img src="/assets/img/logo-full.png" width="480" height="383" alt="{BRAND}" loading="lazy">
        <p>{t['footer_desc']}</p>
        <ul class="footer__contact">{people}<li>{ic('pin')}Montemor-o-Novo, Évora, Portugal</li><!-- EMAIL: add here once known --></ul>
      </div>
      <div><h2>{t['services']}</h2><ul>{svcs}</ul></div>
      <div><h2>{t['areas']}</h2><ul>{areas}</ul><p class="footer__villages">{'Também' if lang == 'pt' else 'Also'}: {', '.join(VILLAGES)}</p></div>
    </div>
    <div class="container footer__bottom">
      <p>© <span data-year>{date.today().year}</span> {BRAND}. {t['no_electric']}</p>
      <p class="footer__lang"><a href="{pt_href}" lang="pt-PT" hreflang="pt-PT"{' aria-current="true"' if lang == 'pt' else ''}>Português</a> · <a href="{en_href}" lang="en" hreflang="en"{' aria-current="true"' if lang == 'en' else ''}>English</a></p>
    </div>
  </footer>
{wa_chooser(p)}</body>
</html>
"""


def eyebrow(text, light=False):
    return f'<p class="eyebrow{" eyebrow--light" if light else ""}">{text}</p>'


def section_head(lang, eb, h, text="", light=False, hid=""):
    right = f'<div class="shead__text"><p>{text}</p></div>' if text else ""
    return f"""        <div class="shead">
          <div>{eyebrow(eb, light)}<h2 class="h2"{f' id="{hid}"' if hid else ''}>{h}</h2></div>
          {right}
        </div>"""


def faq_block(lang, faq, title=None, eb=None, dark=False):
    items = "\n".join(f'          <details class="faq__item"><summary>{q}</summary><div class="faq__a"><p>{a}</p></div></details>' for q, a in faq)
    title = title or ("Perguntas frequentes" if lang == "pt" else "Frequently asked questions")
    eb = eb or ("Perguntas frequentes" if lang == "pt" else "Questions people ask")
    return f"""    <section class="section{' section--dark' if dark else ''}" aria-labelledby="faq-title">
      <div class="container faq">
        <div>{eyebrow(eb, dark)}<h2 class="h2" id="faq-title">{title}</h2>
          <p class="faq__more">{'Não encontra a sua pergunta? Fale connosco no' if lang == 'pt' else "Can't see your question? Message us on"} <a href="#" data-wa-open>WhatsApp</a>.</p></div>
        <div class="faq__list">
{items}
        </div>
      </div>
    </section>
"""


def chips(lang, current=None):
    out = []
    for a in AREAS:
        cur = ' aria-current="page"' if current == a["key"] else ""
        out.append(f'<a class="chip" href="{area_url(a, lang)}"{cur}>{ic("pin", "ic ic--sm")}{town_name(a, lang)}</a>')
    mon = next(a for a in AREAS if a["key"] == "montemor")
    for v in VILLAGES:
        out.append(f'<a class="chip chip--sub" href="{area_url(mon, lang)}">{v}</a>')
    return '<div class="chips">' + "".join(out) + "</div>"


def form_section(p, preset_service=None, preset_town=None):
    lang = p["lang"]; pt = lang == "pt"
    towns = "".join(f'<option{" selected" if preset_town == t else ""}>{t}</option>' for t in ALL_TOWNS) + f'<option>{"Outro" if pt else "Other"}</option>'
    svcs = "".join(f'<option value="{s[lang]["name"]}"{" selected" if preset_service == s["key"] else ""}>{s[lang]["name"]}</option>' for s in SERVICES) + f'<option>{"Outro" if pt else "Other"}</option>'
    thanks = "/obrigado/" if pt else "/en/thank-you/"
    return f"""    <section class="section section--dark cta" id="orcamento" aria-labelledby="form-title">
      <div class="container cta__grid">
        <div class="cta__intro">
          {eyebrow('Orçamento grátis' if pt else 'Free quote', True)}
          <h2 class="h2" id="form-title">{'Peça o seu orçamento grátis' if pt else 'Ask for your free quote'}</h2>
          <p>{'Conte-nos o que precisa. Respondemos em poucas horas, com uma resposta honesta sobre se e quando podemos ajudar.' if pt else 'Tell us what you need. We reply within a few hours, with an honest answer about if and when we can help.'}</p>
          <ul class="cta__people">
            {''.join(f'<li><a href="{wa_link(k, lang, p.get("wa_extra", ""))}" target="_blank" rel="noopener">{ic("wa")}<span><strong>{v["name"]}</strong> ({v["langs"][lang]})<br>{v["show"]}</span></a></li>' for k, v in PEOPLE.items())}
          </ul>
        </div>
        <form class="form" action="{FORMSPREE}" method="POST" data-quote data-thanks="{thanks}" data-lang="{lang}">
          <input type="hidden" name="_subject" value="{'Novo pedido de orçamento' if pt else 'New quote request'}">
          <input type="hidden" name="page" value="{DOMAIN}{p['path']}">
          <input type="hidden" name="language" value="{'Português' if pt else 'English'}">
          <div class="hp" aria-hidden="true"><label>Não preencher / Leave empty<input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label></div>
          <div class="form__grid">
            <div class="field"><label for="f-name">{'Nome' if pt else 'Name'} *</label><input id="f-name" name="name" autocomplete="name" required></div>
            <div class="field"><label for="f-phone">{'Telemóvel / WhatsApp' if pt else 'Phone / WhatsApp'} *</label><input id="f-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required></div>
            <div class="field field--full"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email"></div>
            <div class="field"><label for="f-town">{'Localidade' if pt else 'Town'}</label><select id="f-town" name="town">{towns}</select></div>
            <div class="field"><label for="f-service">{'Serviço' if pt else 'Service'}</label><select id="f-service" name="service">{svcs}</select></div>
            <div class="field field--full"><label for="f-msg">{'Descreva o trabalho' if pt else 'Describe the job'} *</label><textarea id="f-msg" name="message" rows="4" required></textarea></div>
            <div class="field field--full"><label for="f-lang">{'Idioma preferido' if pt else 'Preferred language'}</label><select id="f-lang" name="preferred_language"><option{' selected' if pt else ''}>Português</option><option{'' if pt else ' selected'}>English</option></select></div>
          </div>
          <button class="btn btn--gold btn--lg btn--block" type="submit">{'Pedir orçamento grátis' if pt else 'Send my quote request'} {ic('arrow')}</button>
          <p class="form__status" role="status" aria-live="polite"></p>
          <p class="form__note">{'Respondemos em poucas horas. Pode também enviar fotos do trabalho por WhatsApp.' if pt else 'We reply within a few hours. You can also send photos of the job on WhatsApp.'}</p>
        </form>
      </div>
    </section>
"""


HOW = {
    "pt": [("Contacto", "Fale connosco por WhatsApp, telefone ou formulário. Se puder, envie fotos do trabalho."),
           ("Visita", "Vamos ver o trabalho ao local, para perceber o que é preciso de verdade."),
           ("Orçamento honesto", "Recebe um preço claro e grátis. Ou dizemos-lhe com honestidade que a nossa agenda não permite."),
           ("Trabalho feito", "Fazemos o trabalho com cuidado e deixamos tudo limpo. Só está concluído quando estiver bem feito.")],
    "en": [("Get in touch", "Message us on WhatsApp, call or use the form. If you can, send a few photos of the job."),
           ("Site visit", "We come and look at the job in person, so we understand what is really needed."),
           ("Honest quote", "You get a clear, free quote. Or we tell you honestly that our schedule cannot fit your job."),
           ("Job done", "We do the work carefully and leave everything clean. It is only finished when it is done properly.")],
}


def how_block(lang):
    steps = "".join(f'<li><span class="step__n">0{i + 1}</span><h3>{h}</h3><p>{d}</p></li>' for i, (h, d) in enumerate(HOW[lang]))
    return f"""    <section class="section section--white" aria-labelledby="how-title">
      <div class="container">
{section_head(lang, 'Como trabalhamos' if lang == 'pt' else 'How we work', 'Do primeiro contacto ao trabalho feito' if lang == 'pt' else 'From first message to job done', hid='how-title')}
        <ol class="steps">{steps}</ol>
      </div>
    </section>
"""


def page_hero(p, eb, h1, lead, crumbs_list, img=None):
    lang = p["lang"]
    bc = '<nav class="crumbs" aria-label="Breadcrumb">' + '<span aria-hidden="true"> / </span>'.join(
        (f'<a href="{u}">{n}</a>' if i < len(crumbs_list) - 1 else f'<span aria-current="page">{n}</span>') for i, (n, u) in enumerate(crumbs_list)) + "</nav>"
    media = f'<div class="phero__media">{picture(img, ALT_TEXT[lang][img], lazy=False, sizes="(min-width: 900px) 40vw, 100vw")}</div>' if img else ""
    return f"""  <main id="main">
    <section class="phero">
      <div class="container phero__inner{' phero__inner--media' if img else ''}">
        <div>
          {bc}
          {eyebrow(eb, True)}
          <h1 class="phero__title">{h1}</h1>
          <p class="phero__lead">{lead}</p>
          <div class="btn-row">
            <a class="btn btn--gold btn--lg" href="#orcamento">{L[lang]['quote_free']} {ic('arrow')}</a>
            <a class="btn btn--ghost btn--lg" href="{wa_link('ricardo', lang, p.get('wa_extra', ''))}" target="_blank" rel="noopener" data-wa-open>{ic('wa')}{L[lang]['wa_talk']}</a>
          </div>
          <ul class="trust">{''.join(f'<li>{ic("check", "ic ic--sm")}{x}</li>' for x in L[lang]['trust'])}</ul>
        </div>
        {media}
      </div>
    </section>
"""


def svc_card(s, lang, big=False):
    c = s[lang]
    media = (f'<div class="card__media">{picture(s["img"], ALT_TEXT[lang][s["img"]])}</div>' if s["img"]
             else f'<div class="card__icon">{ic(s["icon"])}</div>')
    ticks = "".join(f'<li>{ic("check", "ic ic--sm")}{x}</li>' for x in c["ticks"])
    return f"""          <article class="card{' card--big' if big else ''}{'' if s['img'] else ' card--noimg'}">
            {media}
            <div class="card__body">
              <h3><a href="{svc_url(s, lang)}">{c['name']}</a></h3>
              <p>{c['card']}</p>
              <ul class="ticks">{ticks}</ul>
              <span class="more" aria-hidden="true">{L[lang]['more']} {ic('arrow', 'ic ic--sm')}</span>
            </div>
          </article>"""


def services_grid(lang):
    return '<div class="cards">\n' + "\n".join(svc_card(s, lang, big=(i < 2)) for i, s in enumerate(SERVICES)) + "\n        </div>"


def projects_block(lang, full=False):
    pt = lang == "pt"
    t = L[lang]
    hall = f"""          <article class="proj">
            <!-- PROJECT LOCATION: add the town here, e.g. <p class="proj__place">Montemor-o-Novo</p> -->
            <div class="proj__pair">
              <figure>{picture('hallway-before', ALT_TEXT[lang]['hallway-before'])}<figcaption class="tag">{t['before']}</figcaption></figure>
              <figure>{picture('hallway-after', ALT_TEXT[lang]['hallway-after'])}<figcaption class="tag tag--gold">{t['after']}</figcaption></figure>
            </div>
            <div class="proj__body">
              <ul class="pills"><li>{'Remodelação' if pt else 'Renovation'}</li><li>{'Carpintaria' if pt else 'Carpentry'}</li><li>{'Pintura' if pt else 'Painting'}</li></ul>
              <h3>{'Hall: de mosaico antigo a pavimento efeito madeira' if pt else 'Hallway: from old tiles to wood-effect flooring'}</h3>
              <p>{'Tirámos o mosaico antigo, colocámos pavimento efeito madeira, criámos um painel ripado com prateleira suspensa e pintámos as paredes.' if pt else 'We lifted the old tiles, laid wood-effect flooring, built a slatted feature wall with a floating shelf and repainted the walls.'}</p>
            </div>
          </article>"""
    bath = f"""          <article class="proj">
            <!-- PROJECT LOCATION: add the town here -->
            <div class="proj__pair">
              <figure>{picture('bathroom-shower', ALT_TEXT[lang]['bathroom-shower'])}<figcaption class="tag tag--gold">{'Duche walk-in' if pt else 'Walk-in shower'}</figcaption></figure>
              <figure>{picture('bathroom-vanity', ALT_TEXT[lang]['bathroom-vanity'])}<figcaption class="tag tag--gold">{'Móvel por medida' if pt else 'Custom vanity'}</figcaption></figure>
            </div>
            <div class="proj__body">
              <ul class="pills"><li>{'Casa de banho' if pt else 'Bathroom'}</li><li>{'Microcimento' if pt else 'Microcement'}</li><li>{'Carpintaria' if pt else 'Carpentry'}</li></ul>
              <h3>{'Casa de banho em microcimento com duche walk-in' if pt else 'Microcement bathroom with a walk-in shower'}</h3>
              <p>{'Microcimento nas paredes e no chão, duche walk-in com resguardo de vidro e um móvel de lavatório feito por medida.' if pt else 'Microcement on the walls and floor, a walk-in shower with a glass screen and a vanity unit made to measure.'}</p>
            </div>
          </article>"""
    return f'<div class="projs">\n{hall}\n{bath}\n        </div>'


def why_block(lang):
    pt = lang == "pt"
    cards = [("bolt", "Rápidos" if pt else "Fast", "Respondemos em poucas horas. Não tem de esperar dias por uma resposta." if pt else "We reply within a few hours. You should not have to wait days for an answer."),
             ("shield", "Fiáveis" if pt else "Reliable", "Fazemos o que combinamos, quando combinamos, e mantemos o contacto durante a obra." if pt else "We do what we agree, when we agree it, and keep you updated throughout."),
             ("heart", "Honestos" if pt else "Honest", "Dizemos-lhe a verdade sobre preços, prazos e o que vale ou não a pena fazer." if pt else "We tell you the truth about prices, timings and what is or is not worth doing."),
             ("users", "Equipa familiar" if pt else "Family team", "Pai e filha. O Ricardo fala português e inglês, a Trishta fala inglês." if pt else "Dad and daughter. Ricardo speaks Portuguese and English, Trishta speaks English.")]
    row = "".join(f'<article class="why__card">{ic(i)}<h3>{h}</h3><p>{d}</p></article>' for i, h, d in cards)
    return f"""    <section class="section section--dark" aria-labelledby="why-title">
      <div class="container">
{section_head(lang, 'Porquê escolher-nos' if pt else 'Why choose us', 'Rápidos, fiáveis e honestos' if pt else 'Fast, reliable and honest', 'Ou ajudamos a um preço justo, ou dizemos-lhe com honestidade que a nossa agenda não permite o seu trabalho.' if pt else "We either help you at a fair price, or tell you honestly that our schedule can't fit your job.", True, 'why-title')}
        <div class="why">{row}</div>
        <div class="why__wide">
          <article class="why__gold"><h3>{'Respondemos em poucas horas, com uma resposta honesta sobre se e quando podemos ajudar.' if pt else 'We reply within a few hours, with an honest answer about if and when we can help.'}</h3><a class="btn btn--dark" href="#" data-wa-open>{ic('wa')}{L[lang]['wa_talk']}</a></article>

        </div>
      </div>
    </section>
"""


# ------------------------------------------------------------------ Pages
PAGES = []


def add(p):
    PAGES.append(p)


def home(lang):
    pt = lang == "pt"; t = L[lang]
    p = {"lang": lang, "path": "/" if pt else "/en/", "alt": "/en/" if pt else "/", "hero": True, "form": True, "section": None}
    p["title"] = "Obras em Montemor-o-Novo, Évora e Lisboa | Família Amador" if pt else "English-Speaking Builder in the Alentejo | Família Amador"
    p["desc"] = ("Obras e remodelações em Montemor-o-Novo, Évora e Lisboa: casas de banho, cozinhas, pintura, canalização. Resposta em poucas horas. Orçamento grátis."
                 if pt else "English-speaking builder, plumber, carpenter and painter in the Alentejo and Lisbon. Family team, reply within hours. Free quote.")
    h1 = "Obras e Remodelações em Montemor-o-Novo, Évora e Lisboa" if pt else "English-speaking builder in the Alentejo and Lisbon"
    sub = ("Somos uma equipa familiar de pai e filha. Respondemos em poucas horas e dizemos-lhe com honestidade se e quando podemos ajudar."
           if pt else "We are a dad-and-daughter renovation team based in Montemor-o-Novo. We reply within a few hours and tell you honestly if and when we can help.")
    body = f"""  <main id="main">
    <section class="hero" aria-labelledby="hero-title">
      <div class="container">
        <div class="hero__frame">
          {picture('hero', ALT_TEXT[lang]['hero'], cls='hero__img', lazy=False, sizes='(min-width: 1240px) 1200px, 100vw')}
          <div class="hero__content">
            {eyebrow('Remodelações e construção' if pt else 'Renovations and building', True)}
            <h1 id="hero-title" class="hero__title">{h1}</h1>
            <p class="hero__lead">{sub}</p>
            <div class="btn-row">
              <a class="btn btn--gold btn--lg" href="#orcamento">{t['quote_free']} {ic('arrow')}</a>
              <a class="btn btn--ghost btn--lg" href="{wa_link('ricardo', lang)}" target="_blank" rel="noopener" data-wa-open>{ic('wa')}{t['wa_talk']}</a>
            </div>
            <ul class="trust">{''.join(f'<li>{ic("check", "ic ic--sm")}{x}</li>' for x in t['trust'])}</ul>
          </div>
        </div>
      </div>
    </section>

{form_section(p)}
    <section class="section" aria-label="{'Sobre nós' if pt else 'About us'}">
      <div class="container intro">
        <p class="intro__big">{'A Família Amador Construções é uma empresa familiar de obras e remodelações em Montemor-o-Novo, gerida por pai e filha: o Ricardo e a Trishta.' if pt else 'Família Amador Construções is a family renovation company in Montemor-o-Novo, run by a dad-and-daughter team: Ricardo and Trishta.'}</p>
        <div class="intro__text">
          <p>{'Fazemos tudo com qualidade à medida e temos paixão por criar casas confortáveis e bonitas. Trabalhamos em casas, apartamentos, montes e espaços comerciais, do Alentejo a Lisboa.' if pt else 'We do everything with bespoke quality, and we are passionate about creating comfortable, beautiful homes. As English-speaking builders, plumbers, carpenters and painters in the Alentejo and Lisbon, we work on houses, quintas, apartments and commercial properties.'}</p>
          <p>{'E acreditamos que não tem de esperar uma eternidade por uma resposta.' if pt else 'And we believe you should not have to wait forever for a reply.'}</p>
          <a class="link" href="{'/sobre-nos/' if pt else '/en/about/'}">{'Conheça-nos' if pt else 'Meet the team'} {ic('arrow', 'ic ic--sm')}</a>
        </div>
      </div>
    </section>

    <section class="section section--tight" aria-labelledby="svc-title">
      <div class="container">
{section_head(lang, 'O que fazemos' if pt else 'What we do', 'Tudo o que a sua casa precisa, de uma só equipa' if pt else 'Everything your house needs, from one team', 'Remodelações, casas de banho, cozinhas, pintura, carpintaria, canalização, telhados, humidade e pequenas reparações. Não fazemos trabalhos elétricos.' if pt else 'Renovations, bathrooms, kitchens, painting, carpentry, plumbing, roofs, damp and general repairs. We do not do electrical work.', hid='svc-title')}
        {services_grid(lang)}
      </div>
    </section>

{why_block(lang)}
    <section class="section" aria-labelledby="proj-title">
      <div class="container">
{section_head(lang, 'Os nossos projetos' if pt else 'Our projects', 'Veja o trabalho completo, não só o resultado' if pt else 'See the whole job, not just the finish', 'Qualquer um mostra uma foto bonita no fim. Nós preferimos mostrar o antes e o depois.' if pt else 'Anyone can show a nice photo at the end. We would rather show you the before and after.', hid='proj-title')}
        {projects_block(lang)}
        <a class="btn btn--outline" href="{'/projetos/' if pt else '/en/projects/'}">{'Ver todos os projetos' if pt else 'See all projects'} {ic('out', 'ic ic--sm')}</a>
      </div>
    </section>

    <section class="section section--white" aria-labelledby="areas-title">
      <div class="container">
{section_head(lang, 'Zonas que servimos' if pt else 'Areas we cover', 'Obras em Montemor-o-Novo, Évora, Lisboa e arredores' if pt else 'Builders in Montemor-o-Novo, Évora, Lisbon and around', 'Estamos em Montemor-o-Novo e trabalhamos em Arraiolos, Vendas Novas, Lavre, Santiago do Escoural, Cabrela, Ciborro, Viana do Alentejo, Évora e Lisboa. Se não tem a certeza se chegamos até si, pergunte.' if pt else 'We are based in Montemor-o-Novo and work across Arraiolos, Vendas Novas, Lavre, Santiago do Escoural, Cabrela, Ciborro, Viana do Alentejo, Évora and Lisbon. Not sure if we cover you? Just ask.', hid='areas-title')}
        {chips(lang)}
      </div>
    </section>

{faq_block(lang, HOME_FAQ[lang])}
    <!-- REVIEWS: add real Google reviews here, then remove the hidden attribute.
         Copy one <figure class="review"> per review. Do not invent reviews. -->
    <section class="section" id="reviews" hidden aria-labelledby="reviews-title">
      <div class="container">
{section_head(lang, 'Avaliações' if pt else 'Reviews', 'O que dizem os nossos clientes' if pt else 'What our customers say', hid='reviews-title')}
        <div class="reviews">
          <!-- <figure class="review"><blockquote><p>Review text</p></blockquote><figcaption>Name, Town</figcaption></figure> -->
        </div>
      </div>
    </section>
  </main>
"""
    p["body"] = body
    p["schema"] = [business_schema(), *people_schema(), website_schema(lang), faq_schema(HOME_FAQ[lang])]
    add(p)


def service_page(s, lang):
    pt = lang == "pt"; c = s[lang]
    other = "en" if pt else "pt"
    p = {"lang": lang, "path": svc_url(s, lang), "alt": svc_url(s, other), "form": True,
         "section": "/servicos/" if pt else "/en/services/", "title": c["title"], "desc": c["desc"],
         "wa_extra": ("para " if pt else "for ") + c["name"].split(":")[0].lower()}
    crumbs_list = [(L[lang]["home"], "/" if pt else "/en/"), (L[lang]["services"], p["section"]), (c["name"].split(":")[0], p["path"])]
    lead = c["intro"][0]
    includes = "".join(f'<li>{ic("check", "ic ic--sm")}{x}</li>' for x in c["includes"])
    intro_rest = "".join(f"<p>{x}</p>" for x in c["intro"][1:])
    img_block = f'<figure class="svc__img">{picture(s["img"], ALT_TEXT[lang][s["img"]], sizes="(min-width: 900px) 40vw, 100vw")}</figure>' if s["img"] else ""
    area_links = "".join(f'<li><a href="{area_url(a, lang)}">{(c["name"].split(":")[0]) + (" em " if pt else " in ") + town_name(a, lang)}</a></li>' for a in AREAS)
    others = "".join(f'<li><a href="{svc_url(o, lang)}">{o[lang]["name"]}</a></li>' for o in SERVICES if o["key"] != s["key"])
    body = page_hero(p, "Serviço" if pt else "Service", c["h1"], lead, crumbs_list) + f"""
    <section class="section">
      <div class="container svc">
        <div class="svc__main prose">
          {intro_rest}
          <h2>{'O que inclui' if pt else "What's included"}</h2>
          <ul class="ticks ticks--lg">{includes}</ul>
          <p>{c['extra']}</p>
        </div>
        <aside class="svc__aside">
          {img_block}
          <div class="aside-card">
            <h2>{'Outros serviços' if pt else 'Other services'}</h2>
            <ul class="linklist">{others}</ul>
          </div>
        </aside>
      </div>
    </section>

{how_block(lang)}
{faq_block(lang, c['faq'], title=('Perguntas sobre ' if pt else 'Questions about ') + c['name'].split(':')[0].lower())}
    <section class="section section--white" aria-labelledby="where-title">
      <div class="container">
{section_head(lang, 'Onde trabalhamos' if pt else 'Where we work', (c['name'].split(':')[0] + (' no Alentejo e em Lisboa' if pt else ' in the Alentejo and Lisbon')), ('Com base em Montemor-o-Novo, fazemos este serviço em todas as zonas abaixo.' if pt else 'From our base in Montemor-o-Novo, we offer this service in all the areas below.'), hid='where-title')}
        <ul class="arealinks">{area_links}</ul>
        {chips(lang)}
      </div>
    </section>

{form_section(p, preset_service=s['key'])}  </main>
"""
    p["body"] = body
    p["schema"] = [
        {"@type": "Service", "name": c["name"], "serviceType": c["name"].split(":")[0], "description": c["desc"], "url": DOMAIN + p["path"],
         "provider": {"@id": BUSINESS_ID}, "areaServed": [{"@type": "City", "name": t} for t in ALL_TOWNS], "availableLanguage": ["pt", "en"]},
        business_ref(), faq_schema(c["faq"]), crumbs_schema(crumbs_list)]
    add(p)


def business_ref():
    return {"@type": "HomeAndConstructionBusiness", "@id": BUSINESS_ID, "name": BRAND, "url": DOMAIN + "/",
            "telephone": PEOPLE["ricardo"]["tel"], "address": {"@type": "PostalAddress", "addressLocality": "Montemor-o-Novo", "addressRegion": "Évora", "addressCountry": "PT"}}


def area_page(a, lang):
    pt = lang == "pt"; c = a[lang]; other = "en" if pt else "pt"
    town = town_name(a, lang)
    p = {"lang": lang, "path": area_url(a, lang), "alt": area_url(a, other), "form": True,
         "section": "/zonas/" if pt else "/en/areas/", "title": c["title"], "desc": c["desc"],
         "wa_extra": ("em " if pt else "in ") + town}
    crumbs_list = [(L[lang]["home"], "/" if pt else "/en/"), (L[lang]["areas"], p["section"]), (town, p["path"])]
    popular = "".join(svc_card(SVC[k], lang) for k in c["popular"][:4])
    all_svc = "".join(f'<li><a href="{svc_url(s, lang)}">{s[lang]["name"].split(":")[0]}{(" em " if pt else " in ") + town}</a></li>' for s in SERVICES)
    villages = ""
    if a["key"] == "montemor":
        villages = f"""<div class="villages"><h3>{'Freguesias e aldeias à volta' if pt else 'Parishes and villages around it'}</h3><ul class="chips">{''.join(f'<li class="chip chip--sub">{ic("pin", "ic ic--sm")}{v}</li>' for v in VILLAGES)}</ul></div>"""
    body = page_hero(p, ("Zona" if pt else "Area") + f": {town}", c["h1"], c["intro"][0], crumbs_list) + f"""
    <section class="section">
      <div class="container svc">
        <div class="svc__main prose">
          {''.join(f'<p>{x}</p>' for x in c['intro'][1:])}
          <h2>{('Casas típicas em ' if pt else 'Typical properties in ') + town}</h2>
          <p>{c['props']}</p>
          <h2>{'Distância e deslocação' if pt else 'Distance and travel'}</h2>
          <p>{c['travel']}</p>
          {villages}
        </div>
        <aside class="svc__aside">
          <div class="aside-card aside-card--dark">
            <h2>{('Todos os serviços em ' if pt else 'All services in ') + town}</h2>
            <ul class="linklist">{all_svc}</ul>
          </div>
        </aside>
      </div>
    </section>

    <section class="section section--white" aria-labelledby="pop-title">
      <div class="container">
{section_head(lang, 'Mais pedidos' if pt else 'Most requested', ('Os trabalhos mais pedidos em ' if pt else 'Most requested jobs in ') + town, hid='pop-title')}
        <div class="cards cards--even">{popular}</div>
      </div>
    </section>

{faq_block(lang, c['faq'], title=('Perguntas sobre obras em ' if pt else 'Questions about work in ') + town, dark=True)}
    <section class="section" aria-labelledby="other-areas">
      <div class="container">
{section_head(lang, 'Outras zonas' if pt else 'Other areas', 'Também trabalhamos em' if pt else 'We also work in', hid='other-areas')}
        {chips(lang, a['key'])}
      </div>
    </section>

{form_section(p, preset_town=a['town'])}  </main>
"""
    p["body"] = body
    p["schema"] = [business_ref(), faq_schema(c["faq"]), crumbs_schema(crumbs_list)]
    add(p)


def services_overview(lang):
    pt = lang == "pt"
    p = {"lang": lang, "path": "/servicos/" if pt else "/en/services/", "alt": "/en/services/" if pt else "/servicos/", "form": True,
         "section": "/servicos/" if pt else "/en/services/",
         "title": "Serviços de Obras e Remodelações | Família Amador" if pt else "Building & Renovation Services | Família Amador",
         "desc": "Remodelações, casas de banho, cozinhas, pintor, carpinteiro, canalizador, telhados, humidade, pladur e pequenas reparações no Alentejo. Orçamento grátis." if pt else
                 "English-speaking builder, plumber, carpenter and painter: renovations, bathrooms, kitchens, roofs, damp and repairs in the Alentejo. Free quote."}
    crumbs_list = [(L[lang]["home"], "/" if pt else "/en/"), (L[lang]["services"], p["path"])]
    body = page_hero(p, "Serviços" if pt else "Services", "Serviços de obras e remodelações no Alentejo" if pt else "Building and renovation services in the Alentejo",
                     "Dez serviços, uma só equipa familiar. Escolha o que precisa e peça um orçamento grátis. Não fazemos trabalhos elétricos." if pt else
                     "Ten services, one family team that speaks English. Choose what you need and ask for a free quote. We do not do electrical work.", crumbs_list) + f"""
    <section class="section">
      <div class="container">
        {services_grid(lang)}
      </div>
    </section>

{how_block(lang)}
{form_section(p)}  </main>
"""
    p["body"] = body
    p["schema"] = [business_ref(), crumbs_schema(crumbs_list),
                   {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": s[lang]["name"], "url": DOMAIN + svc_url(s, lang)} for i, s in enumerate(SERVICES)]}]
    add(p)


def areas_overview(lang):
    pt = lang == "pt"
    p = {"lang": lang, "path": "/zonas/" if pt else "/en/areas/", "alt": "/en/areas/" if pt else "/zonas/", "form": True,
         "section": "/zonas/" if pt else "/en/areas/",
         "title": "Zonas: Montemor-o-Novo, Évora e Lisboa | Família Amador" if pt else "Areas: Alentejo and Lisbon | Família Amador",
         "desc": "Obras em Montemor-o-Novo, Arraiolos, Vendas Novas, Lavre, Santiago do Escoural, Cabrela, Ciborro, Viana do Alentejo, Évora e Lisboa." if pt else
                 "English-speaking builder in Montemor-o-Novo, Arraiolos, Vendas Novas, Viana do Alentejo, Évora and Lisbon. Free quote and a fast reply."}
    crumbs_list = [(L[lang]["home"], "/" if pt else "/en/"), (L[lang]["areas"], p["path"])]
    cards = "".join(f"""<article class="acard"><h2><a href="{area_url(a, lang)}">{town_name(a, lang)}</a></h2><p>{a[lang]['props']}</p><p class="acard__travel">{ic('pin', 'ic ic--sm')}{a[lang]['travel'].split('.')[0]}.</p><span class="more" aria-hidden="true">{L[lang]['more']} {ic('arrow', 'ic ic--sm')}</span></article>""" for a in AREAS)
    body = page_hero(p, "Zonas que servimos" if pt else "Areas we cover", "Obras e remodelações no Alentejo e em Lisboa" if pt else "Renovations across the Alentejo and Lisbon",
                     "Estamos em Montemor-o-Novo e trabalhamos nas vilas, aldeias e cidades à volta, até Évora e Lisboa." if pt else
                     "We are based in Montemor-o-Novo and work in the towns and villages around it, as far as Évora and Lisbon.", crumbs_list) + f"""
    <section class="section">
      <div class="container">
        {chips(lang)}
        <div class="acards">{cards}</div>
      </div>
    </section>

{form_section(p)}  </main>
"""
    p["body"] = body
    p["schema"] = [business_ref(), crumbs_schema(crumbs_list)]
    add(p)


def projects_page(lang):
    pt = lang == "pt"
    p = {"lang": lang, "path": "/projetos/" if pt else "/en/projects/", "alt": "/en/projects/" if pt else "/projetos/", "form": False,
         "section": "/projetos/" if pt else "/en/projects/",
         "title": "Projetos: Antes e Depois | Família Amador" if pt else "Projects: Before and After | Família Amador",
         "desc": "Veja os nossos projetos de remodelação no Alentejo: hall com pavimento efeito madeira e casa de banho em microcimento com duche walk-in." if pt else
                 "See our renovation projects in the Alentejo: a hallway with wood-effect flooring and a microcement bathroom with a walk-in shower."}
    crumbs_list = [(L[lang]["home"], "/" if pt else "/en/"), ("Projetos" if pt else "Projects", p["path"])]
    body = page_hero(p, "Projetos" if pt else "Projects", "Projetos de remodelação: antes e depois" if pt else "Renovation projects: before and after",
                     "Preferimos mostrar-lhe o trabalho completo, não só o resultado final." if pt else "We would rather show you the whole job, not just the finish.", crumbs_list).replace('href="#orcamento"', f'href="{"/contacto/" if pt else "/en/contact/"}"') + f"""
    <section class="section">
      <div class="container">
        {projects_block(lang, full=True)}
        <!-- ADD A PROJECT: copy one <article class="proj"> block in build.py (projects_block) and add its images to source-images/ -->
      </div>
    </section>
  </main>
"""
    p["body"] = body
    p["schema"] = [business_ref(), crumbs_schema(crumbs_list)]
    add(p)


def about_page(lang):
    pt = lang == "pt"
    p = {"lang": lang, "path": "/sobre-nos/" if pt else "/en/about/", "alt": "/en/about/" if pt else "/sobre-nos/", "form": False,
         "section": "/sobre-nos/" if pt else "/en/about/",
         "title": "Sobre Nós: Pai e Filha em Montemor-o-Novo | Família Amador" if pt else "About Us: Dad-and-Daughter Builders | Família Amador",
         "desc": "Somos o Ricardo e a Trishta, pai e filha, uma empresa familiar de obras em Montemor-o-Novo. Rápidos, fiáveis e honestos. Falamos português e inglês." if pt else
                 "We are Ricardo and Trishta, a dad-and-daughter renovation team in Montemor-o-Novo. Fast, reliable, honest, and we speak English."}
    crumbs_list = [(L[lang]["home"], "/" if pt else "/en/"), ("Sobre nós" if pt else "About", p["path"])]
    people = "".join(f"""<article class="person"><h3>{v['name']}</h3><p>{('Fala ' + ('português e inglês' if 'pt' in v['knows'] else 'inglês')) if pt else ('Speaks ' + ('Portuguese and English' if 'pt' in v['knows'] else 'English'))}</p><a class="btn btn--wa" href="{wa_link(k, lang)}" target="_blank" rel="noopener">{ic('wa')}WhatsApp {v['show']}</a></article>""" for k, v in PEOPLE.items())
    copy = ([
        "A Família Amador Construções é uma empresa familiar com base em Montemor-o-Novo, no Alentejo. Somos pai e filha: o Ricardo e a Trishta.",
        "Temos paixão por criar casas confortáveis e bonitas. Fazemos tudo com qualidade à medida, desde uma pequena reparação até à remodelação completa de uma casa, e tratamos cada obra como se fosse a nossa.",
        "Sabemos o que custa esperar dias por uma resposta de um empreiteiro. Por isso respondemos em poucas horas e dizemos-lhe com honestidade se e quando podemos ajudar. Ou fazemos o trabalho a um preço justo, ou dizemos-lhe que a nossa agenda não permite. Nunca o deixamos à espera sem resposta.",
        "Trabalhamos com clientes portugueses e com estrangeiros que escolheram viver no Alentejo e em Lisboa. O Ricardo fala português e inglês, e a Trishta fala inglês, por isso a comunicação é sempre clara.",
    ] if pt else [
        "Família Amador Construções is a family business based in Montemor-o-Novo, in the Alentejo. We are a dad and daughter: Ricardo and Trishta.",
        "We are passionate about creating comfortable, beautiful homes. We do everything with bespoke quality, from a small repair to a full house renovation, and treat every job as if it were our own home.",
        "We know how frustrating it is to wait days for a builder to reply. So we reply within a few hours and tell you honestly if and when we can help. We either do the job at a fair price, or tell you that our schedule can't fit it. We never leave you waiting without an answer.",
        "We work with Portuguese families and with people from abroad who have chosen to live in the Alentejo and Lisbon. Ricardo speaks Portuguese and English, and Trishta speaks English, so you can deal with us in English from the first message to the finished job. If you are looking for an English-speaking builder, plumber, carpenter or painter in the Alentejo, that is exactly what we are.",
    ])
    body = page_hero(p, "Sobre nós" if pt else "About us", "Uma equipa familiar de pai e filha" if pt else "A dad-and-daughter renovation team",
                     "Rápidos, fiáveis e honestos, com paixão por casas confortáveis e bonitas." if pt else "Fast, reliable and honest, and passionate about comfortable, beautiful homes.",
                     crumbs_list, img="hallway-after").replace('href="#orcamento"', f'href="{"/contacto/" if pt else "/en/contact/"}"') + f"""
    <section class="section">
      <div class="container about">
        <div class="prose">{''.join(f'<p>{x}</p>' for x in copy)}</div>
        <div class="people">{people}</div>
      </div>
    </section>
{why_block(lang)}  </main>
"""
    p["body"] = body
    p["schema"] = [business_ref(), *people_schema(), crumbs_schema(crumbs_list)]
    add(p)


def contact_page(lang):
    pt = lang == "pt"
    p = {"lang": lang, "path": "/contacto/" if pt else "/en/contact/", "alt": "/en/contact/" if pt else "/contacto/", "form": True,
         "section": "/contacto/" if pt else "/en/contact/",
         "title": "Contacto e Orçamento Grátis | Família Amador" if pt else "Contact Us for a Free Quote | Família Amador",
         "desc": "Peça um orçamento grátis para obras em Montemor-o-Novo, Évora e Lisboa. WhatsApp Ricardo 969 164 772 ou Trishta 961 909 846. Resposta em poucas horas." if pt else
                 "Get a free quote from an English-speaking builder in the Alentejo. WhatsApp Ricardo +351 969 164 772 or Trishta +351 961 909 846."}
    crumbs_list = [(L[lang]["home"], "/" if pt else "/en/"), ("Contacto" if pt else "Contact", p["path"])]
    cards = "".join(f"""<article class="ccard"><h2>{v['name']} <span>({v['langs'][lang]})</span></h2>
          <a class="ccard__row" href="{wa_link(k, lang)}" target="_blank" rel="noopener">{ic('wa')}WhatsApp: {v['show']}</a>
          <a class="ccard__row" href="tel:{v['tel']}">{ic('phone')}{'Ligar' if pt else 'Call'}: {v['show']}</a></article>""" for k, v in PEOPLE.items())
    body = page_hero(p, "Contacto" if pt else "Contact", "Peça o seu orçamento grátis" if pt else "Ask for your free quote",
                     "Respondemos em poucas horas. Pode também enviar fotos do trabalho por WhatsApp." if pt else "We reply within a few hours. You can also send photos of the job on WhatsApp.", crumbs_list) + f"""
    <section class="section">
      <div class="container ccards">
        {cards}
        <article class="ccard"><h2>{'Onde estamos' if pt else 'Where we are'}</h2><p class="ccard__row">{ic('pin')}Montemor-o-Novo, Évora, Portugal</p><p>{'Trabalhamos em todo o Alentejo central e em Lisboa.' if pt else 'We work across the central Alentejo and in Lisbon.'}</p><!-- EMAIL: add a mailto row here once the email is known --></article>
      </div>
    </section>
{form_section(p)}  </main>
"""
    p["body"] = body
    p["schema"] = [business_schema(), *people_schema(), crumbs_schema(crumbs_list), {"@type": "ContactPage", "url": DOMAIN + p["path"], "about": {"@id": BUSINESS_ID}}]
    add(p)


def thanks_page(lang):
    pt = lang == "pt"
    p = {"lang": lang, "path": "/obrigado/" if pt else "/en/thank-you/", "alt": "/en/thank-you/" if pt else "/obrigado/", "form": False, "noindex": True,
         "title": "Obrigado | Família Amador Construções" if pt else "Thank you | Família Amador Construções",
         "desc": "Recebemos o seu pedido de orçamento." if pt else "We have received your quote request."}
    body = f"""  <main id="main">
    <section class="phero phero--center">
      <div class="container">
        {eyebrow('Pedido enviado' if pt else 'Request sent', True)}
        <h1 class="phero__title">{'Obrigado! Recebemos o seu pedido.' if pt else 'Thank you! We have your request.'}</h1>
        <p class="phero__lead">{'Respondemos em poucas horas. Se quiser, envie-nos já fotos do trabalho por WhatsApp.' if pt else 'We will reply within a few hours. If you like, send us photos of the job on WhatsApp now.'}</p>
        <div class="btn-row btn-row--center">
          <a class="btn btn--gold btn--lg" href="{'/' if pt else '/en/'}">{'Voltar ao início' if pt else 'Back to the homepage'}</a>
          <a class="btn btn--ghost btn--lg" href="{wa_link('ricardo', lang)}" target="_blank" rel="noopener" data-wa-open>{ic('wa')}{L[lang]['wa_talk']}</a>
        </div>
      </div>
    </section>
  </main>
"""
    p["body"] = body
    p["schema"] = [business_ref()]
    add(p)


def notfound():
    p = {"lang": "pt", "path": "/404.html", "alt": None, "noindex": True, "nocanonical": True, "form": False,
         "title": "Página não encontrada | Page not found | Família Amador", "desc": "Página não encontrada. Page not found."}
    p["body"] = f"""  <main id="main">
    <section class="phero phero--center">
      <div class="container">
        {eyebrow('Erro 404', True)}
        <h1 class="phero__title">Página não encontrada</h1>
        <p class="phero__lead">A página que procura não existe ou mudou de lugar.</p>
        <p class="phero__lead" lang="en"><strong>Page not found.</strong> The page you are looking for does not exist or has moved.</p>
        <div class="btn-row btn-row--center">
          <a class="btn btn--gold btn--lg" href="/">Ir para o início</a>
          <a class="btn btn--ghost btn--lg" href="/en/" lang="en">Go to the English homepage</a>
          <a class="btn btn--ghost btn--lg" href="/contacto/">Pedir orçamento</a>
        </div>
      </div>
    </section>
  </main>
"""
    p["schema"] = [business_ref()]
    add(p)


# ------------------------------------------------------------------ Build
def build_all():
    for lang in ("pt", "en"):
        home(lang); services_overview(lang); areas_overview(lang)
        for s in SERVICES:
            service_page(s, lang)
        for a in AREAS:
            area_page(a, lang)
        projects_page(lang); about_page(lang); contact_page(lang); thanks_page(lang)
    notfound()


def write():
    PAGES.clear()
    build_all()
    for p in PAGES:
        html_doc = head(p) + header(p) + p["body"] + footer(p)
        assert html_doc.count("<h1") == 1, p["path"]
        assert "—" not in html_doc, f"em dash in {p['path']}"
        target = OUT / ("404.html" if p["path"] == "/404.html" else (p["path"].strip("/") + "/index.html" if p["path"] != "/" else "index.html"))
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html_doc, encoding="utf-8")
    # page map (single source for the language switcher; also handy for tools)
    pmap = {p["path"]: p["alt"] for p in PAGES if p.get("alt")}
    (OUT / "assets" / "pagemap.json").write_text(json.dumps(pmap, ensure_ascii=False, indent=1), encoding="utf-8")
    # sitemap with hreflang alternates
    urls = []
    for p in PAGES:
        if p.get("noindex"):
            continue
        pt_path, en_path = (p["path"], p["alt"]) if p["lang"] == "pt" else (p["alt"], p["path"])
        urls.append(f"""  <url>
    <loc>{DOMAIN}{p['path']}</loc>
    <lastmod>{TODAY}</lastmod>
    <xhtml:link rel="alternate" hreflang="pt-PT" href="{DOMAIN}{pt_path}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{DOMAIN}{en_path}"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{DOMAIN}{pt_path}"/>
  </url>""")
    (OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n", encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")
    print(f"Built {len(PAGES)} pages ({sum(1 for p in PAGES if not p.get('noindex'))} indexable) for {DOMAIN}")


if __name__ == "__main__":
    write()
