#!/usr/bin/env python3
"""Bit Byte Tech: builds the one-page site (index.html) from shared parts.

Run `python3 build.py` after editing. Content comes from the client's three
posters in assets/references/. Contact details are shown as text and icons only:
nothing links out. The contact form sends to Formspree (see main.js).
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
DOMAIN = "https://www.bitbytetech.co.za"
PHONE = "076 803 0406"
TEL = "tel:+27768030406"
WA = "https://wa.me/27768030406?text=" + "Hi%20Bit%20Byte%20Tech%2C%20I%27d%20like%20a%20quote."
EMAIL = "riccomdr@gmail.com"
AREA = "Welkom and surrounding areas"
HOURS = "9:00 to 18:00"
KEYWORDS = ("computer repairs Welkom, laptop repairs Welkom, computer upgrades Welkom, PC repairs Welkom, "
            "computer technician Welkom, computer repairs Free State, "
            "computer repairs, laptop repairs, PC repairs, computer technician, CompTIA A+ technician, "
            "hardware diagnostics, data recovery, blue screen repair, SSD upgrade, RAM upgrade, graphics card upgrade, "
            "custom gaming PC, gaming PC build, workstation build, refurbished computers, PC components")

ICONS = {
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "x": '<path d="M6 6l12 12M18 6 6 18"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "wa": '<path fill="currentColor" stroke="none" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "laptop": '<rect x="4" y="4" width="16" height="11" rx="1.5"/><path d="M2 19h20"/>',
    "desktop": '<rect x="3" y="3" width="7" height="18" rx="1"/><rect x="14" y="3" width="7" height="18" rx="1"/><path d="M5.5 7h2M16.5 7h2M5.5 10h2M16.5 10h2"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    "gauge": '<path d="M4 18a8 8 0 1 1 16 0"/><path d="m12 18 4-6"/>',
    "gamepad": '<path d="M6 9h12a4 4 0 0 1 4 4v1a3 3 0 0 1-5.4 1.8L15 14H9l-1.6 1.8A3 3 0 0 1 2 14v-1a4 4 0 0 1 4-4z"/><path d="M7 11.5v3M5.5 13h3"/><circle cx="16.5" cy="12" r=".6"/><circle cx="18" cy="13.5" r=".6"/>',
    "chip": '<rect x="5" y="5" width="14" height="14" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/>',
    "cart": '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.6 11.2a2 2 0 0 0 2 1.6h7.7a2 2 0 0 0 2-1.5L21 7H6"/>',
    "trophy": '<path d="M8 21h8M12 17v4M7 4h10v5a5 5 0 0 1-10 0z"/><path d="M7 6H4a3 3 0 0 0 3 4M17 6h3a3 3 0 0 1-3 4"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    "dollar": '<circle cx="12" cy="12" r="10"/><path d="M15 9a3 2.5 0 0 0-3-2c-1.7 0-3 .9-3 2.2s1.3 2 3 2.3 3 1 3 2.3-1.3 2.2-3 2.2a3 2.5 0 0 1-3-2M12 5.5v13"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/>',
    "gear": '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>',
    "upload": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 16V8M8.5 11.5 12 8l3.5 3.5"/>',
    "monitor": '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/>',
    "tag": '<path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L2 12V2h10l8.6 8.6a2 2 0 0 1 0 2.8z"/><circle cx="7" cy="7" r="1.5"/>',
    "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    "headset": '<path d="M3 14v-2a9 9 0 0 1 18 0v2"/><path d="M21 15a2 2 0 0 1-2 2h-1v-6h1a2 2 0 0 1 2 2zM3 15a2 2 0 0 0 2 2h1v-6H5a2 2 0 0 0-2 2z"/><path d="M19 17v1a3 3 0 0 1-3 3h-3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
}
SPRITE = '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>' + "".join(
    f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items()) + "</defs></svg>"


def ic(name, cls="ic"):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'


NAV = [("#services", "Services"), ("#diagnosis", "Diagnosis"), ("#new-computer", "New computers"),
       ("#why", "Why me"), ("#faq", "FAQ"), ("#contact", "Contact")]

SERVICES = [
    ("Computer and laptop repairs", "Computers that won't switch on or keep restarting, blue screens and Windows problems, overheating, cracked screens, keyboards and charging ports, for laptops and desktop PCs."),
    ("Hardware diagnostics", "Finding the actual fault and explaining it without the jargon, with a written price before any work starts."),
    ("Data recovery", "Getting files and photos off a dying drive."),
    ("Software troubleshooting", "Fixing Windows problems, blue screens and software faults."),
    ("PC and laptop upgrades", "SSD and RAM upgrades, graphics cards, power supplies, cooling solutions and motherboards."),
    ("Custom gaming and workstation builds", "PCs built to your budget for gaming, business, graphic design, video editing and everyday home use."),
    ("PC components and accessories", "Help choosing the right components for your budget and needs."),
    ("New and refurbished computer sales", "New and refurbished computers and full systems."),
]
FIRM = {
    "@type": "ProfessionalService", "@id": DOMAIN + "/#business", "name": "Bit Byte Tech",
    "alternateName": "Bit Byte Tech: Your Friendly Neighbourhood Geek",
    "slogan": "Your Tech. Our Priority.",
    "description": "Computer and laptop repairs and upgrades in Welkom and surrounding areas: hardware diagnostics, data recovery, upgrades, and custom gaming and workstation PC builds by a CompTIA A+ certified technician. Quotes are free and you get a written price before any work starts.",
    "url": DOMAIN + "/", "logo": DOMAIN + "/assets/img/icon-512.png", "image": DOMAIN + "/assets/img/og.jpg",
    "telephone": "+27768030406", "email": EMAIL,
    "address": {"@type": "PostalAddress", "addressLocality": "Welkom", "addressRegion": "Free State", "addressCountry": "ZA"},
    "areaServed": [{"@type": "City", "name": "Welkom"}, {"@type": "AdministrativeArea", "name": "Welkom and surrounding areas, Free State"}],
    "contactPoint": {"@type": "ContactPoint", "contactType": "customer service", "telephone": "+27768030406", "email": EMAIL, "availableLanguage": "English"},
    "knowsAbout": ["Computer repair", "Laptop repair", "Hardware diagnostics", "Data recovery", "SSD upgrades", "RAM upgrades", "Graphics cards", "Gaming PC builds", "Workstation builds", "CompTIA A+"],
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Computer services", "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "description": d}} for n, d in SERVICES]},
}
WEBSITE = {"@type": "WebSite", "@id": DOMAIN + "/#website", "url": DOMAIN + "/", "name": "Bit Byte Tech",
           "inLanguage": "en-ZA", "publisher": {"@id": DOMAIN + "/#business"}}


def head(p):
    url = DOMAIN + "/" + ("" if p["file"] == "index.html" else p["file"])
    schema = json.dumps({"@context": "https://schema.org", "@graph": p["schema"]}, ensure_ascii=False, indent=2)
    robots = "noindex, follow" if p.get("noindex") else "index, follow, max-image-preview:large"
    preload = ('  <link rel="preload" as="image" href="assets/img/logo-880.webp" imagesrcset="assets/img/logo-480.webp 480w, assets/img/logo-880.webp 880w" imagesizes="(min-width: 1020px) 440px, 90vw" fetchpriority="high">\n'
               if p["file"] == "index.html" else "")
    base = '  <base href="/">\n' if p.get("noindex") else ""
    canon = "" if p.get("noindex") else f'  <link rel="canonical" href="{url}">\n'
    return f"""<!doctype html>
<html lang="en-ZA">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
{base}  <title>{p['title']}</title>
  <meta name="description" content="{p['description']}">
  <meta name="keywords" content="{KEYWORDS}">
  <meta name="robots" content="{robots}">
  <meta name="theme-color" content="#070C13">
  <meta name="format-detection" content="telephone=no">
{canon}  <meta property="og:type" content="website">
  <meta property="og:locale" content="en_ZA">
  <meta property="og:site_name" content="Bit Byte Tech">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{p.get('og_title', p['title'])}">
  <meta property="og:description" content="{p['description']}">
  <meta property="og:image" content="{DOMAIN}/assets/img/og.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Bit Byte Tech logo: Your Tech. Our Priority.">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{p.get('og_title', p['title'])}">
  <meta name="twitter:description" content="{p['description']}">
  <meta name="twitter:image" content="{DOMAIN}/assets/img/og.jpg">
  <link rel="icon" href="favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <link rel="manifest" href="site.webmanifest">
  <link rel="preload" href="assets/fonts/exo2-italic.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="assets/fonts/manrope.woff2" as="font" type="font/woff2" crossorigin>
{preload}  <link rel="stylesheet" href="styles.css">
  <script src="main.js" defer></script>
  <script type="application/ld+json">
{schema}
  </script>
</head>
"""


def header(active, prefix=""):
    links = "\n".join(f'        <a href="{prefix}{h}"{CUR if h == active else ""}>{t}</a>' for h, t in NAV)
    return f"""<body>
  <a class="skip-link" href="#main">Skip to content</a>
  {SPRITE}
  <header class="header">
    <div class="container header__inner">
      <a class="brand" href="{prefix or '#top'}" aria-label="Bit Byte Tech, home">
        <img src="assets/img/logo-mark.webp" width="200" height="74" alt="">
        <span class="brand__name">Bit Byte Tech</span>
      </a>
      <nav class="nav" id="site-nav" aria-label="Main">
{links}
        <a class="btn btn--blue nav__cta" href="{prefix}#quote">Get a free quote</a>
      </nav>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">
        {ic('menu', 'ic ic-open')}{ic('x', 'ic ic-close')}
      </button>
    </div>
  </header>
"""


CUR = ' aria-current="page"'


def contact_tiles(compact=False):
    return f"""        <ul class="ctiles{' ctiles--compact' if compact else ''}">
          <li><a class="ctile" href="{TEL}"><span class="ctile__ic">{ic('phone')}</span><span><small>Call</small>{PHONE}</span></a></li>
          <li><a class="ctile" href="{WA}" target="_blank" rel="noopener"><span class="ctile__ic ctile__ic--wa">{ic('wa')}</span><span><small>WhatsApp</small>{PHONE}</span></a></li>
          <li><a class="ctile" href="mailto:{EMAIL}"><span class="ctile__ic">{ic('mail')}</span><span><small>Email</small>{EMAIL}</span></a></li>
          <li class="ctile ctile--info"><span class="ctile__ic">{ic('pin')}</span><span><small>Service area</small>Welkom &amp; surrounding areas</span></li>
          <li class="ctile ctile--info"><span class="ctile__ic">{ic('clock')}</span><span><small>Hours</small>9:00 to 18:00</span></li>
        </ul>"""


QR = """          <div class="qr">
            <img src="assets/img/whatsapp-qr.png" width="480" height="480" alt="QR code to chat with Bit Byte Tech on WhatsApp" loading="lazy">
            <p><strong>Scan to chat</strong>on WhatsApp</p>
          </div>"""


def footer(prefix=""):
    return f"""  <section class="pledge" aria-label="Our promise">
    <div class="container">
      <p class="pledge__line">Reliable tech. Better solutions. Stronger tomorrows.</p>
      <ul class="pledge__list">
        <li>{ic('shield')}Local support</li>
        <li>{ic('bolt')}Fast service</li>
        <li>{ic('headset')}Honest advice</li>
      </ul>
    </div>
  </section>
  <footer class="footer">
    <div class="container footer__inner">
      <a class="brand" href="{prefix or '#top'}"><img src="assets/img/logo-mark.webp" width="200" height="74" alt="" loading="lazy"><span class="brand__name">Bit Byte Tech</span></a>
      <ul class="footer__contact">
        <li><a href="{TEL}">{ic('phone')}{PHONE}</a></li>
        <li><a href="{WA}" target="_blank" rel="noopener">{ic('wa')}WhatsApp</a></li>
        <li><a href="mailto:{EMAIL}">{ic('mail')}{EMAIL}</a></li>
      </ul>
      <div class="footer__meta">
        <p class="footer__area">{ic('pin')}Welkom &amp; surrounding areas · {ic('clock')}9:00 to 18:00</p>
        <p class="footer__cert">CompTIA A+ certified technician</p>
      </div>
    </div>
    <div class="container footer__bottom">
      <p>© <span data-year>2026</span> Bit Byte Tech. All rights reserved.</p>
      <p class="footer__tag">Your Tech. Our Priority.</p>
    </div>
  </footer>
  <nav class="mbar" aria-label="Quick contact">
    <a href="{TEL}">{ic('phone')}Call</a>
    <a href="{WA}" target="_blank" rel="noopener">{ic('wa')}WhatsApp</a>
    <a class="mbar__primary" href="{prefix}#quote">{ic('arrow')}Free quote</a>
  </nav>
</body>
</html>
"""


FAQS = [
    ("How much does a quote cost?", "Nothing. Tell me what your computer is doing, or what you want to spend and what you need it for, and I'll price the parts and the labour. You get the price in writing, and nothing happens until you say go ahead."),
    ("Will you tell me if my computer isn't worth fixing?", "Yes. If it's not worth fixing, or buying new works out cheaper, I'll tell you that rather than take the repair job."),
    ("Do I have to bring my computer in?", "You can drop it off, or I can fetch it if you're nearby."),
    ("Do you repair laptops and desktop PCs?", "Yes. I repair computers that won't switch on or keep restarting, blue screens and Windows problems, overheating and loud fans, cracked screens, keyboards and charging ports."),
    ("Can you get my files and photos off a broken computer?", "Yes. Data recovery, including getting files off a dying drive, is one of the repairs I do."),
    ("What upgrade will make my computer faster?", "An SSD is the biggest speed jump you can buy. More RAM helps if it chokes with tabs open, and a new graphics card helps with games and rendering."),
    ("Can you build me a gaming PC?", "Yes. I build gaming PCs to your budget, as well as office, home, editing and design machines. If you're building it yourself, I can just advise on parts."),
    ("Which areas do you cover?", "I do computer and laptop repairs and upgrades in Welkom and surrounding areas. I can fetch your computer if you're nearby."),
    ("What are your hours?", "I'm available from 9:00 to 18:00. You can also send a WhatsApp or fill in the quote form at any time, and I'll get back to you."),
    ("Are you qualified?", "Yes. I'm a CompTIA A+ certified technician, and I work on my own, so you deal with the same person from start to finish."),
]


def faq_section():
    items = "\n".join(f"""          <details class="faq__item"><summary>{q}</summary><p>{a}</p></details>""" for q, a in FAQS)
    return f"""    <section class="section section--alt" id="faq" aria-labelledby="faq-title">
      <div class="container faq">
        <div class="faq__head">
          <p class="eyebrow">FAQ</p>
          <h2 class="h2" id="faq-title">Computer repair questions, answered</h2>
          <p>Still not sure? Ask me directly. Quotes cost nothing.</p>
          <a class="btn btn--blue btn--lg" href="#quote">Get a free quote {ic('arrow')}</a>
        </div>
        <div class="faq__list">
{items}
        </div>
      </div>
    </section>
"""


def badge():
    return """<svg class="badge" viewBox="0 0 220 250" role="img" aria-label="CompTIA A+ certified">
            <defs><linearGradient id="bg-g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#132235"/><stop offset="1" stop-color="#05090F"/></linearGradient></defs>
            <path d="M110 6 206 40v78c0 62-46 104-96 126C60 222 14 180 14 118V40z" fill="url(#bg-g)" stroke="#37B8FF" stroke-width="4"/>
            <path d="M110 20 192 49v69c0 53-38 90-82 110-44-20-82-57-82-110V49z" fill="none" stroke="#39A9F5" stroke-opacity=".35" stroke-width="1.5"/>
            <text x="110" y="92" text-anchor="middle" fill="#FF4D4D" font-family="Exo 2, sans-serif" font-weight="700" font-size="28">CompTIA</text>
            <text x="110" y="160" text-anchor="middle" fill="#FFFFFF" font-family="Exo 2, sans-serif" font-weight="800" font-size="68">A+</text>
            <text x="110" y="192" text-anchor="middle" fill="#C9D3DE" font-family="Exo 2, sans-serif" font-weight="700" font-size="15" letter-spacing="5">CERTIFIED</text>
          </svg>"""


def home():
    pro = [("shield", "CompTIA A+ certified technician"), ("laptop", "Laptop repairs"), ("desktop", "Desktop PC repairs"),
           ("search", "Hardware diagnostics"), ("gauge", "Performance upgrades"), ("gamepad", "Custom gaming &amp; workstation builds"),
           ("chip", "PC components &amp; accessories"), ("cart", "New &amp; refurbished computer sales")]
    pro_html = "\n".join(f"            <li>{ic(i)}{t}</li>" for i, t in pro)
    symptoms = ["It won't switch on", "It's gotten really slow", "The screen goes blue and it restarts", "It's hot and the fan is loud",
                "I cracked my laptop screen", "I need my photos off it", "It can't run the games I want", "I need a new computer entirely"]
    sym_html = "\n".join(f'            <li><span class="tick">{ic("check")}</span>{s}</li>' for s in symptoms)
    plan = ["Bring it in, or I'll fetch it if you're nearby.", "I find out what's actually wrong with it, and explain it without the jargon.",
            "You get the price in writing, before I start.", "Nothing happens until you say go ahead.", "You get it back fixed and tested."]
    plan_html = "\n".join(f"              <li>{p}</li>" for p in plan)
    why = [("trophy", "Professional service"), ("user", "Honest advice"), ("shield", "Quality components"),
           ("dollar", "Competitive pricing"), ("wrench", "Reliable repairs"), ("gear", "Personalised solutions")]
    why_html = "\n".join(f"          <li>{ic(i)}<span>{t}</span></li>" for i, t in why)
    body = f"""  <main id="main">
    <!-- HERO -->
    <section class="hero" id="top" aria-labelledby="hero-title">
      <div class="hero__glow" aria-hidden="true"></div>
      <div class="container hero__grid">
        <div class="hero__copy">
          <img class="hero__logo" src="assets/img/logo-880.webp" srcset="assets/img/logo-480.webp 480w, assets/img/logo-880.webp 880w" sizes="(min-width: 1020px) 440px, 90vw" width="880" height="483" fetchpriority="high" alt="Bit Byte Tech: Your Tech. Our Priority. Built on trust. Powered by technology. Connecting our community.">
          <p class="hero__script">Your Friendly Neighbourhood Geek</p>
          <h1 id="hero-title" class="hero__title"><span class="hero__kicker">Computer &amp; laptop repairs and upgrades in Welkom &amp; surrounding areas</span>Computer giving you trouble?</h1>
          <p class="hero__lead">I'm a qualified technician working on my own, so you deal with me the whole way through. You get the price in writing before I open anything. If it's not worth fixing, I'll tell you.</p>
          <div class="hero__ctas">
            <a class="btn btn--blue btn--lg" href="{TEL}">{ic('phone')}Call {PHONE}</a>
            <a class="btn btn--wa btn--lg" href="{WA}" target="_blank" rel="noopener">{ic('wa')}WhatsApp me</a>
          </div>
          <p class="hero__area">{ic('pin')}<span>In <strong>Welkom &amp; surrounding areas</strong></span><span class="hero__sep" aria-hidden="true">·</span>{ic('clock')}<span><strong>9:00 to 18:00</strong></span></p>
          <ul class="hero__badges" aria-label="At a glance">
            <li>{ic('shield')}CompTIA A+ certified</li>
            <li>{ic('check')}Written price first</li>
            <li>{ic('check')}Quotes cost nothing</li>
          </ul>
        </div>

        <form class="form hero__form" id="quote" novalidate>
          <p class="form__kicker">Free, no-obligation quote</p>
          <h2>Get a free quote</h2>
          <p class="form__sub">Tell me what's going on and I'll get back to you with a price.</p>
          <div class="form__grid">
            <div class="field"><label for="f-name">Name *</label><input id="f-name" name="name" autocomplete="name" required><p class="field__err" id="err-name"></p></div>
            <div class="field"><label for="f-phone">Phone or WhatsApp *</label><input id="f-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required><p class="field__err" id="err-phone"></p></div>
            <div class="field field--full"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email"></div>
            <div class="field"><label for="f-device">Device</label><select id="f-device" name="device"><option>Laptop</option><option>Desktop PC</option><option>New computer</option></select></div>
            <div class="field"><label for="f-problem">What's the problem?</label><select id="f-problem" name="problem"><option>It won't switch on</option><option>It's gotten really slow</option><option>Blue screen or keeps restarting</option><option>It's hot and the fan is loud</option><option>Cracked screen, keyboard or charging port</option><option>I need my files or photos off it</option><option>It can't run the games I want</option><option>I want an upgrade</option><option>I need a new computer</option><option>Parts advice</option><option>Something else</option></select></div>
            <div class="field field--full"><label for="f-msg">Tell me more *</label><textarea id="f-msg" name="message" rows="3" placeholder="What's it doing? Or your budget and what you'll use it for." required></textarea><p class="field__err" id="err-message"></p></div>
          </div>
          <div class="hp" aria-hidden="true"><label>Leave this empty<input name="_gotcha" tabindex="-1" autocomplete="off"></label></div>
          <button class="btn btn--blue btn--lg btn--block" type="submit">Send for a free quote {ic('arrow')}</button>
          <p class="form__status" role="status" aria-live="polite"></p>
          <p class="form__call">Prefer to talk? <a href="{TEL}">{ic('phone')}Call {PHONE}</a></p>
        </form>
      </div>
    </section>

    <!-- PROFESSIONAL COMPUTER SERVICES -->
    <section class="section section--alt" aria-labelledby="pro-title">
      <div class="container pro">
        <div>
          <p class="eyebrow">CompTIA A+ certified technician</p>
          <h2 class="h2" id="pro-title">Professional computer &amp; laptop repair services</h2>
          <ul class="pro__list">
{pro_html}
          </ul>
        </div>
        <div class="pro__badge">
          {badge()}
          <p>Qualified technician · CompTIA A+</p>
        </div>
      </div>
    </section>

    <!-- SERVICES WE OFFER -->
    <section class="section" id="services" aria-labelledby="services-title">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow">Services I offer</p>
          <h2 class="h2" id="services-title">Computer repairs, upgrades and custom PC builds</h2>
        </div>
        <div class="services">
          <article class="service">
            <div class="service__top"><span class="service__n">01</span>{ic('gear', 'ic service__ic')}</div>
            <h3>Computer &amp; laptop repairs</h3>
            <ul>
              <li>Slow computers</li>
              <li>Computers that won't start or keep restarting</li>
              <li>Blue screen errors and Windows problems</li>
              <li>Running hot, or the fan is screaming</li>
              <li>Cracked screens, keyboards, charging ports</li>
              <li>Data recovery from a dying drive</li>
              <li>Hardware replacement</li>
              <li>Software troubleshooting</li>
            </ul>
          </article>
          <article class="service">
            <div class="service__top"><span class="service__n">02</span>{ic('upload', 'ic service__ic')}</div>
            <h3>PC &amp; laptop upgrades</h3>
            <ul>
              <li>SSD upgrades: the biggest speed jump you can buy</li>
              <li>RAM upgrades, if it chokes with tabs open</li>
              <li>Graphics cards for games and rendering</li>
              <li>Power supplies</li>
              <li>Cooling solutions</li>
              <li>Motherboards</li>
            </ul>
          </article>
          <article class="service">
            <div class="service__top"><span class="service__n">03</span>{ic('monitor', 'ic service__ic')}</div>
            <h3>New computers &amp; gaming PCs</h3>
            <ul>
              <li>Gaming PCs built to your budget</li>
              <li>Business and office machines</li>
              <li>Graphic design and video editing workstations</li>
              <li>Everyday home use</li>
              <li>New and refurbished full systems</li>
              <li>Just parts advice if you're building it yourself</li>
            </ul>
          </article>
        </div>
      </div>
    </section>

    <!-- DIAGNOSIS SHEET -->
    <section class="section section--alt" id="diagnosis" aria-labelledby="diag-title">
      <div class="container">
        <div class="sheet">
          <div class="sheet__head">
            <h2 id="diag-title" class="sheet__title">Diagnosis Sheet</h2>
            <p class="sheet__sub">For one (1) unwell computer</p>
          </div>
          <dl class="sheet__rows">
            <div><dt>Patient</dt><dd>Your computer <em>(desktop or laptop)</em></dd></div>
            <div><dt>Presented with</dt><dd>See symptoms below: <em>tick what sounds familiar</em></dd></div>
            <div><dt>Seen by</dt><dd>Me. Only me. Same person start to finish.</dd></div>
          </dl>
          <p class="sheet__label">Symptoms</p>
          <ul class="symptoms">
{sym_html}
          </ul>
          <div class="sheet__grid">
            <div class="rx">
              <span class="rx__mark" aria-hidden="true">℞</span>
              <p class="sheet__label">Treatment plan</p>
              <ol class="rx__plan">
{plan_html}
              </ol>
              <p class="stamp" aria-label="Most cases are not terminal">Most cases<br>are not terminal</p>
            </div>
            <div class="consult">
              <div class="consult__box">
                <p class="sheet__label sheet__label--light">Consultation</p>
                <p class="consult__title">The quote costs you nothing.</p>
                <p>Tell me what it's doing, or what you want to spend and what you need it for. I'll price the parts and the labour. And if it's cheaper to replace than repair, I'll tell you that instead of taking the job.</p>
                <a class="btn btn--light" href="#quote">Book a free quote {ic('arrow')}</a>
              </div>
{QR.replace('Scan to chat', 'Book it in').replace('on WhatsApp', 'on WhatsApp: scan with your phone camera')}
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- NEED A NEW COMPUTER -->
    <section class="section" id="new-computer" aria-labelledby="new-title">
      <div class="container newpc">
        <div class="newpc__card">
          <p class="eyebrow">Need a new computer? Not sure what parts to buy?</p>
          <h2 class="h2" id="new-title">Custom gaming PCs and workstations, built to your budget</h2>
          <p>I can help you choose the right components for your budget and needs. Whether you're looking for a gaming PC, an office computer, an editing workstation or a home computer, I'll recommend the best build and give you a competitive quote.</p>
          <p class="newpc__note">Every build is tailored to your needs and budget.</p>
          <a class="btn btn--blue btn--lg" href="#quote">Contact me for a free quotation {ic('arrow')}</a>
        </div>
        <ul class="newpc__uses" aria-label="Builds for">
          <li>{ic('gamepad')}Gaming</li>
          <li>{ic('desktop')}Business</li>
          <li>{ic('monitor')}Graphic design</li>
          <li>{ic('laptop')}Video editing</li>
          <li>{ic('pin')}Everyday home use</li>
        </ul>
      </div>
    </section>

    <!-- WHY CHOOSE -->
    <section class="section section--alt" id="why" aria-labelledby="why-title">
      <div class="container">
        <div class="section-head section-head--center">
          <p class="eyebrow">Why choose Bit Byte Tech?</p>
          <h2 class="h2" id="why-title">Built on trust. Powered by technology.</h2>
        </div>
        <ul class="why">
{why_html}
        </ul>
      </div>
    </section>

{faq_section()}
    <!-- CONTACT -->
    <section class="section contact" id="contact" aria-labelledby="contact-title">
      <div class="container contact__inner">
        <div>
          <p class="eyebrow">Looking for a price?</p>
          <h2 class="h2" id="contact-title">Contact me today for a no-obligation quotation</h2>
          <p class="contact__lead">Whether you need a repair, an upgrade or a completely new computer, call, WhatsApp or email me. I work in Welkom and surrounding areas, from 9:00 to 18:00.</p>
{contact_tiles()}
          <a class="btn btn--blue btn--lg" href="#quote">Fill in the quote form {ic('arrow')}</a>
        </div>
{QR}
      </div>
    </section>
  </main>
"""
    return {"file": "index.html", "active": None,
            "title": "Computer &amp; Laptop Repairs &amp; Upgrades in Welkom | Bit Byte Tech",
            "og_title": "Bit Byte Tech | Your Tech. Our Priority.",
            "description": "Computer and laptop repairs and upgrades in Welkom and surrounding areas, 9:00 to 18:00. CompTIA A+ technician. Free quotes: 076 803 0406.",
            "schema": [FIRM, WEBSITE,
                       {"@type": "WebPage", "@id": DOMAIN + "/#webpage", "url": DOMAIN + "/", "name": "Computer and laptop repairs, upgrades and custom PC builds",
                        "isPartOf": {"@id": DOMAIN + "/#website"}, "about": {"@id": DOMAIN + "/#business"}, "inLanguage": "en-ZA",
                        "primaryImageOfPage": {"@type": "ImageObject", "url": DOMAIN + "/assets/img/og.jpg"}},
                       {"@type": "FAQPage", "@id": DOMAIN + "/#faq", "mainEntity": [
                           {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}],
            "body": body}


def notfound():
    body = f"""  <main id="main">
    <section class="page-hero">
      <div class="hero__glow" aria-hidden="true"></div>
      <div class="container">
        <p class="eyebrow">Error 404</p>
        <h1 class="page-hero__title">This page could not be found</h1>
        <p class="page-hero__lead">The link may be broken or the page may have moved. Computer still giving you trouble? Quotes cost nothing.</p>
        <div class="hero__ctas nf__ctas">
          <a class="btn btn--blue btn--lg" href="/">Back to the homepage {ic('arrow')}</a>
          <a class="btn btn--ghost btn--lg" href="/#quote">Get a free quote</a>
          <a class="btn btn--wa btn--lg" href="{WA}" target="_blank" rel="noopener">{ic('wa')}WhatsApp me</a>
        </div>
      </div>
    </section>
  </main>
"""
    return {"file": "404.html", "active": None, "noindex": True, "prefix": "/",
            "title": "Page not found | Bit Byte Tech", "description": "This page could not be found. Go back to the Bit Byte Tech homepage or get a free computer repair quote.",
            "schema": [WEBSITE], "body": body}


def main():
    pages = [home(), notfound()]
    for p in pages:
        html = head(p) + header(p["active"], p.get("prefix", "")) + p["body"] + footer(p.get("prefix", ""))
        assert html.count("<h1") == 1, p["file"]
        (ROOT / p["file"]).write_text(html, encoding="utf-8")
    urls = "\n".join(f"  <url>\n    <loc>{DOMAIN}/{'' if p['file'] == 'index.html' else p['file']}</loc>\n    <lastmod>2026-11-09</lastmod>\n  </url>" for p in pages if not p.get("noindex"))
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n', encoding="utf-8")
    print("Built:", ", ".join(p["file"] for p in pages))


if __name__ == "__main__":
    main()
