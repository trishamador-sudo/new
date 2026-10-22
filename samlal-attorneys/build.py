#!/usr/bin/env python3
"""Sahil Samlal Attorneys Inc.: website mock-up generator.

Run `python3 build.py` to rebuild every page from the shared header, footer and
content below. Pages use .html links so the mock-up also works when opened
straight from a folder or a zip.
"""
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
DOMAIN = "https://samlalattorneys.com"
TODAY = date.today().isoformat()

FIRM = "Sahil Samlal Attorneys Inc."
TEL, TEL_LINK = "(034) 315 5315", "+27343155315"
CELL, CELL_LINK = "082 762 5716", "+27827625716"
WA = "https://wa.me/27827625716?text=" + "Hello%20Sahil%20Samlal%20Attorneys%2C%20I%27d%20like%20to%20book%20a%20consultation."
EMAIL = "info@samlalattorneys.com"
ADDRESS_LINES = ["Office Suite 2", "54 Bird Street", "Newcastle, 2940", "KwaZulu-Natal"]
GEO = (-27.763156207698277, 29.92802789846893)
MAPS = f"https://www.google.com/maps/search/?api=1&query={GEO[0]},{GEO[1]}"
LPC = "73764"

ICONS = {
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "wa": '<path fill="currentColor" stroke="none" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "arrow": '<path d="M5 12h14M13 5l7 7-7 7"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
    "x": '<path d="M18 6 6 18M6 6l12 12"/>',
    "cal": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "video": '<path d="m22 8-6 4 6 4V8Z"/><rect x="2" y="6" width="14" height="12" rx="2"/>',
    "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "heart": '<path d="M19 14c1.5-1.5 3-3.2 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.8 0-3 .5-4.5 2-1.5-1.5-2.7-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4 3 5.5l7 7Z"/>',
    "chat": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "alert": '<circle cx="12" cy="12" r="10"/><path d="M12 8v4M12 16h.01"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "scale": '<path d="m16 16 3-8 3 8c-.9.6-1.9 1-3 1s-2.1-.4-3-1Z"/><path d="m2 16 3-8 3 8c-.9.6-1.9 1-3 1s-2.1-.4-3-1Z"/><path d="M7 21h10M12 3v18M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>',
    "pulse": '<path d="M19 14c1.5-1.5 3-3.2 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.8 0-3 .5-4.5 2-1.5-1.5-2.7-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4 3 5.5l7 7Z"/><path d="M3.2 12h6.3l.5-1 2 4.5 2-7 1.5 3.5h5.3"/>',
    "car": '<path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><path d="M9 17h6"/><circle cx="17" cy="17" r="2"/>',
    "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
    "coins": '<circle cx="8" cy="8" r="6"/><path d="M18.1 10.4A6 6 0 1 1 10.3 18M7 6h1v4M16.7 13.9l.7.7-2.8 2.8"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
    "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M16 13H8M16 17H8M10 9H8"/>',
    "badge": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M15 8h2M15 12h2M7 16h10"/>',
    "home": '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
    "gavel": '<path d="m14 13-7.5 7.5a2.1 2.1 0 0 1-3-3L11 10M16 16l6-6M8 8l6-6M9 7l8 8M21 11l-8-8"/>',
}


def ic(name, cls="ic"):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'


SPRITE = '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>' + "".join(
    f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items()) + "</defs></svg>"

# ------------------------------------------------------------------ Content
AREAS = [
    ("criminal-litigation", "Criminal Litigation", "shield",
     "From bail applications to trials, if you face criminal charges you need a strong legal defence. We represent you in court and work to protect your rights and your future."),
    ("civil-litigation", "Civil Litigation", "scale",
     "We handle disputes between individuals, businesses and organisations, and pursue or defend claims efficiently to secure practical, cost-effective outcomes."),
    ("personal-injury", "Personal Injury", "pulse",
     "We act for people injured through negligence, workplace incidents or accidents, and pursue the compensation you are entitled to for your losses."),
    ("road-accident-fund", "Road Accident Fund (RAF)", "car",
     "We help victims of motor vehicle accidents claim from the Road Accident Fund for medical expenses, loss of income, and pain and suffering."),
    ("commercial-corporate", "Commercial &amp; Corporate Law", "briefcase",
     "We guide businesses through company formation, compliance and commercial agreements, so you can operate legally, ethically and efficiently."),
    ("debt-collection", "Debt Collection", "coins",
     "We recover outstanding debts lawfully and effectively through negotiation, letters of demand and litigation, protecting your financial interests."),
    ("family-law", "Family Law", "users",
     "Compassionate, discreet assistance in family matters, including maintenance, child custody, protection orders and divorce proceedings."),
    ("divorce", "Divorces", "file",
     "We manage divorce proceedings with professionalism and care, helping you reach fair settlements on property, maintenance and children."),
    ("labour-law", "Labour Law", "badge",
     "Advice and representation on workplace disputes, unfair dismissals, disciplinary hearings and employment contracts, for employers and employees."),
    ("estates-trusts", "Estates &amp; Trusts", "home",
     "We draft wills, administer deceased estates and establish trusts, to safeguard your assets and your loved ones' financial security."),
]

# Anti-GBV section: wording and layout kept exactly as on the firm's current site.
GBV_PLEDGE = (f"Sahil Samlal Attorneys Inc. stands unequivocally against Gender-Based Violence (GBV). We commit our time, talent, "
              "and resources to protect survivors, hold perpetrators accountable, and advance a justice system that is "
              "survivor-centred, trauma-informed, and rights-based.")
GBV_COMMITMENTS = [
    ("Survivor-centred practice", "Your safety, dignity, and informed choice come first. We explain options in plain language and you decide the path."),
    ("Confidentiality &amp; POPIA compliance", "Sensitive information is handled with strict privacy safeguards and need-to-know access only."),
    ("Accessible services", "Discreet consultations (in-person or virtual), flexible hours for urgent matters, and language support (e.g., isiZulu/English)."),
]
GBV_SERVICES = [
    ("Protection Orders (Domestic Violence)", "Drafting, filing, and arguing for interim/final Protection Orders; variations and enforcement for breaches."),
    ("Harassment Protection Orders", "Applications under the Protection from Harassment framework, including digital/online harassment and stalking."),
    ("Urgent Interdicts", "After-hours and urgent applications for immediate protection and access to children or property."),
    ("Criminal Process Support", "Opening cases, statement taking, liaison with SAPS/NPA, opposing or supporting bail, and court accompaniment for complainants."),
    ("Family Law Remedies", "Divorce, parental responsibilities and rights, care/contact variations, Rule 43/58 interim relief, and supervised contact where appropriate."),
    ("Maintenance &amp; Financial Relief", "New applications, arrears enforcement, garnishee orders, and financial disclosure."),
    ("Workplace GBV &amp; Harassment", "Grievances, investigations, CCMA referrals, unfair discrimination/harassment claims, and employer compliance advisory."),
    ("Civil Claims for Damages", "Delictual claims for assault, emotional shock, and related harms; institutional/employer liability where applicable."),
    ("Evidence &amp; Case Building", "Preservation of digital evidence (messages, emails, social media), subpoenas/discovery, affidavits, medico-legal documentation coordination."),
    ("Safety Planning &amp; Risk Management", "Tailored plans addressing protection, housing, children, communication boundaries, and safe digital practices."),
]
GBV_PROMISE = ("We will treat you with respect, believe you, protect your privacy, and pursue remedies swiftly and strategically. "
               "Fighting GBV is core to our mission and to the values of a just South Africa")

FAQS = [
    ("Where is your office?", "Our offices are at Office Suite 2, 54 Bird Street, Newcastle, 2940, KwaZulu-Natal."),
    ("What are your office hours?", "Monday to Friday from 08h00 to 12h00 and from 13h00 to 16h30 (closed for lunch from 12h00 to 13h00). We are closed on weekends and public holidays."),
    ("Can I have a consultation online?", "Yes. When you book, choose a consultation at our offices or a virtual consultation, and tell us when you are available."),
    ("How do I book a consultation?", "Use the booking form, call (034) 315 5315 or 082 762 5716, or send us a WhatsApp. Selected dates and times are subject to our consulting team's availability."),
    ("Which courts do you appear in?", "Magistrates' district and regional courts in Newcastle, Madadeni, Utrecht, uMnambithi (Ladysmith), Endumeni (Dundee), Dannhauser, Glencoe and Volksrust, and the KwaZulu-Natal High Courts in Durban and Pietermaritzburg."),
    ("What areas of law do you handle?", "Criminal and civil litigation, personal injury, Road Accident Fund claims, commercial and corporate law, debt collection, family law, divorces, labour law, and estates and trusts."),
    ("I need help with a gender-based violence matter. Is it confidential?", "Yes. Sensitive information is handled with strict privacy safeguards and need-to-know access only. We offer discreet consultations in person or virtually, and urgent applications for protection."),
    ("Do you offer language support?", "Yes. Our services for GBV matters include language support, for example isiZulu and English."),
]

# Google reviews: paste real reviews here as (text, name). Leave empty to show the placeholder cards.
REVIEWS = []
GOOGLE_REVIEWS_URL = "https://www.google.com/maps/search/?api=1&query=Sahil+Samlal+Attorneys+Inc+54+Bird+Street+Newcastle"

INSIGHTS = [
    ("Road Accident Fund", "How to claim from the Road Accident Fund", "What you need to lodge an RAF claim for medical expenses, loss of income, and pain and suffering."),
    ("Family law", "Protection orders: how they work", "The difference between interim and final protection orders, and how to apply for one."),
    ("Labour law", "Dismissed? Your first steps", "What to do after an unfair dismissal, from disciplinary hearings to the CCMA."),
    ("Estates &amp; trusts", "Why every adult needs a valid will", "How a will protects your loved ones, and what happens to an estate without one."),
]

MAGISTRATES = ["Newcastle", "Madadeni", "Utrecht", "uMnambithi (Ladysmith)", "Endumeni (Dundee)", "Dannhauser", "Glencoe", "Volksrust"]
HIGH_COURTS = ["Durban", "Pietermaritzburg"]

NAV = [("index.html", "Home", "home"), ("practice-areas.html", "Practice Areas", "areas"),
       ("anti-gbv.html", "Anti-GBV", "gbv"), ("about.html", "About", "about"), ("index.html#faq", "FAQ", "faq"),
       ("index.html#insights", "Insights", "insights"), ("contact.html", "Contact", "contact")]


# ------------------------------------------------------------------ Shared parts
def head(p):
    canonical = DOMAIN + "/" + ("" if p["file"] == "index.html" else p["file"])
    schema = json.dumps({"@context": "https://schema.org", "@graph": p["schema"]}, ensure_ascii=False, indent=2)
    robots = '  <meta name="robots" content="noindex">\n' if p.get("noindex") else ""
    preload = '  <link rel="preload" as="image" href="assets/img/hero-monogram.webp">\n' if p["file"] == "index.html" else ""
    return f"""<!doctype html>
<html lang="en-ZA">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{p['title']}</title>
  <meta name="description" content="{p['description']}">
{robots}  <meta name="theme-color" content="#0B1730">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="en_ZA">
  <meta property="og:site_name" content="{FIRM}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:title" content="{p['title']}">
  <meta property="og:description" content="{p['description']}">
  <meta property="og:image" content="{DOMAIN}/assets/img/og.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png">
  <link rel="apple-touch-icon" href="apple-touch-icon.png">
  <link rel="preload" href="assets/fonts/manrope.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="assets/fonts/cormorant.woff2" as="font" type="font/woff2" crossorigin>
{preload}  <link rel="stylesheet" href="styles.css">
  <script src="main.js" defer></script>
  <script type="application/ld+json">
{schema}
  </script>
</head>
"""


CUR = ' aria-current="page"'


def header(active):
    links = "\n".join(
        f'        <a href="{href}"{CUR if key == active else ""}>{label}</a>'
        for href, label, key in NAV)
    return f"""<body>
  <a class="skip-link" href="#main">Skip to content</a>
  {SPRITE}
  <div class="topbar">
    <div class="container topbar__inner">
      <a href="{MAPS}" target="_blank" rel="noopener" class="topbar__hide-sm">{ic('pin')}54 Bird Street, Newcastle, KZN</a>
      <a href="tel:{TEL_LINK}">{ic('phone')}{TEL}</a>
      <a href="tel:{CELL_LINK}" class="topbar__hide-sm">{ic('phone')}Cell {CELL}</a>
      <span class="topbar__push topbar__hide-sm">{ic('clock')}Mon–Fri 08h00–16h30</span>
    </div>
  </div>
  <header class="header">
    <div class="container header__inner">
      <a class="brand" href="index.html" aria-label="{FIRM}, home">
        <span class="brand__name">Sahil Samlal</span>
        <span class="brand__sub">Attorneys Inc.</span>
      </a>
      <nav class="nav" id="site-nav" aria-label="Main">
{links}
        <a class="btn btn--light nav__cta-mobile" href="contact.html#book">{ic('cal')}Book a consultation</a>
      </nav>
      <div class="header__actions">
        <a class="icon-btn" href="tel:{TEL_LINK}" aria-label="Call {TEL}">{ic('phone')}</a>
        <a class="btn btn--light header__cta" href="contact.html#book">Book a consultation</a>
        <button class="icon-btn menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">
          {ic('menu', 'ic ic-open')}{ic('x', 'ic ic-close')}
        </button>
      </div>
    </div>
  </header>
"""


def cta_band(title="Need legal advice? Speak to an attorney today.",
             text="Book a consultation at our Newcastle offices or online. We'll confirm a time that suits you."):
    return f"""    <section class="cta-band">
      <div class="container cta-band__inner">
        <div>
          <h2 class="cta-band__title">{title}</h2>
          <p>{text}</p>
        </div>
        <div class="cta-band__actions">
          <a class="btn btn--light btn--lg" href="contact.html#book">{ic('cal')}Book a consultation</a>
          <a class="btn btn--outline btn--lg" href="tel:{TEL_LINK}">{ic('phone')}Call {TEL}</a>
          <a class="btn btn--outline btn--lg" href="{WA}" target="_blank" rel="noopener">{ic('wa')}WhatsApp us</a>
        </div>
      </div>
    </section>
"""


def footer():
    areas = "".join(f'<li><a href="practice-areas.html#{slug}">{name}</a></li>' for slug, name, _, _ in AREAS[:6])
    return f"""  <footer class="footer">
    <div class="container footer__grid">
      <div class="footer__brand">
        <a class="brand brand--footer" href="index.html"><span class="brand__name">Sahil Samlal</span><span class="brand__sub">Attorneys Inc.</span></a>
        <p class="footer__tag">Dedicated to Results. Driven by Excellence.</p>
        <p>LPC Firm Number: {LPC}</p>
        <a class="btn btn--light" href="contact.html#book">{ic('cal')}Book a consultation</a>
      </div>
      <div>
        <h2>Practice areas</h2>
        <ul>{areas}<li><a href="practice-areas.html">All practice areas →</a></li></ul>
      </div>
      <div>
        <h2>Contact</h2>
        <ul class="footer__contact">
          <li>{ic('phone')}<a href="tel:{TEL_LINK}">Tel: {TEL}</a></li>
          <li>{ic('phone')}<a href="tel:{CELL_LINK}">Cell: {CELL}</a></li>
          <li>{ic('wa')}<a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></li>
          <li>{ic('mail')}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{ic('pin')}<a href="{MAPS}" target="_blank" rel="noopener">{'<br>'.join(ADDRESS_LINES)}</a></li>
        </ul>
      </div>
      <div>
        <h2>Office hours</h2>
        <dl class="hours">
          <div><dt>Mon–Fri</dt><dd>08h00–12h00</dd></div>
          <div><dt>Lunch</dt><dd>12h00–13h00</dd></div>
          <div><dt>Mon–Fri</dt><dd>13h00–16h30</dd></div>
          <div><dt>Weekends &amp; public holidays</dt><dd>Closed</dd></div>
        </dl>
      </div>
    </div>
    <div class="container footer__popia" id="popia">
      <h2>Protection of Personal Information (POPIA)</h2>
      <p>{FIRM} processes personal information in line with the Protection of Personal Information Act 4 of 2013. Information you share through this website, by phone, WhatsApp or email is used only to respond to your enquiry and, if you instruct us, to provide legal services. We do not sell it, and we share it only where needed to provide our services or where the law requires. You may ask to access, correct or delete your information by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
      <p class="footer__disclaimer">The information on this website is general information, not legal advice. Contact us for advice on your specific matter.</p>
    </div>
    <div class="container footer__bottom">
      <p>© <span data-year>2026</span> {FIRM} All rights reserved. LPC Firm Number: {LPC}.</p>
      <a href="#main">Back to top ↑</a>
    </div>
  </footer>

  <a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp {FIRM}">{ic('wa')}</a>
  <nav class="mbar" aria-label="Quick contact">
    <a href="tel:{TEL_LINK}">{ic('phone')}Call</a>
    <a href="{WA}" target="_blank" rel="noopener">{ic('wa')}WhatsApp</a>
    <a class="mbar__primary" href="contact.html#book">{ic('cal')}Book</a>
  </nav>
</body>
</html>
"""


def page_hero(eyebrow, h1, lead, crumb):
    return f"""  <main id="main">
    <section class="page-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span>{crumb}</nav>
        <p class="eyebrow">{eyebrow}</p>
        <h1 class="page-hero__title">{h1}</h1>
        <p class="page-hero__lead">{lead}</p>
        <div class="page-hero__ctas">
          <a class="btn btn--light btn--lg" href="contact.html#book">{ic('cal')}Book a consultation</a>
          <a class="btn btn--outline btn--lg" href="tel:{TEL_LINK}">{ic('phone')}{TEL}</a>
        </div>
      </div>
    </section>
"""


def crumbs(name, file):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": f"{DOMAIN}/{file}"}]}


def plain(t):
    return t.replace("&amp;", "&")


FIRM_SCHEMA = {
    "@type": ["Attorney", "LegalService"],
    "@id": DOMAIN + "/#firm",
    "name": FIRM,
    "url": DOMAIN + "/",
    "logo": DOMAIN + "/assets/img/icon-512.png",
    "image": DOMAIN + "/assets/img/og.jpg",
    "slogan": "Dedicated to Results. Driven by Excellence.",
    "description": "Law firm in Newcastle, KwaZulu-Natal: criminal and civil litigation, family law and divorce, labour law, personal injury and RAF claims, commercial law, debt collection, and estates and trusts.",
    "telephone": TEL_LINK,
    "email": EMAIL,
    "address": {"@type": "PostalAddress", "streetAddress": "Office Suite 2, 54 Bird Street", "addressLocality": "Newcastle",
                "postalCode": "2940", "addressRegion": "KwaZulu-Natal", "addressCountry": "ZA"},
    "geo": {"@type": "GeoCoordinates", "latitude": GEO[0], "longitude": GEO[1]},
    "areaServed": [{"@type": "City", "name": c} for c in MAGISTRATES + HIGH_COURTS],
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "12:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "13:00", "closes": "16:30"},
    ],
    "founder": {"@id": DOMAIN + "/#sahil-samlal"},
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Practice areas", "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": plain(n), "description": plain(d)}} for _, n, _, d in AREAS]},
}
PERSON_SCHEMA = {
    "@type": "Person", "@id": DOMAIN + "/#sahil-samlal", "name": "Sahil Ishan Samlal",
    "jobTitle": "Director and Founder", "honorificSuffix": "LLB, LLM",
    "image": DOMAIN + "/assets/img/sahil-samlal.webp", "worksFor": {"@id": DOMAIN + "/#firm"},
}
WEBSITE_SCHEMA = {"@type": "WebSite", "@id": DOMAIN + "/#website", "url": DOMAIN + "/", "name": FIRM,
                  "inLanguage": "en-ZA", "publisher": {"@id": DOMAIN + "/#firm"}}


# ------------------------------------------------------------------ Pages
def area_cards(link_to_detail=True):
    out = []
    for slug, name, icon, desc in AREAS:
        href = f"practice-areas.html#{slug}" if link_to_detail else f"contact.html?area={slug}#book"
        out.append(f"""          <article class="area">
            <span class="area__icon">{ic(icon)}</span>
            <h3>{name}</h3>
            <p>{desc}</p>
            <a class="area__link" href="contact.html?area={slug}#book">Discuss your matter {ic('arrow')}</a>
          </article>""")
    return "\n".join(out)


def courts_block():
    mags = "".join(f"<li>{c}</li>" for c in MAGISTRATES)
    highs = "".join(f"<li>{c}</li>" for c in HIGH_COURTS)
    return f"""        <div class="courts">
          <div class="courts__lists">
            <div>
              <h3>Magistrates' district &amp; regional courts</h3>
              <p class="courts__region">KwaZulu-Natal</p>
              <ul class="courts__list">{mags}</ul>
            </div>
            <div>
              <h3>High Courts</h3>
              <p class="courts__region">KwaZulu-Natal</p>
              <ul class="courts__list">{highs}</ul>
            </div>
          </div>
          <figure class="courts__map">
            <img src="assets/img/kzn-courts-map.webp" width="357" height="405" alt="Map of KwaZulu-Natal showing the courts where Sahil Samlal Attorneys appears: Volksrust, Utrecht, Newcastle, Madadeni, Dannhauser, Dundee, Glencoe and Ladysmith, with High Courts in Pietermaritzburg and Durban" loading="lazy">
          </figure>
        </div>"""


def gbv_original():
    commits = "".join(f'''<article class="gbvo__commit"><img src="assets/img/gbv-heart.png" width="63" height="55" alt="" loading="lazy"><h4>{t}</h4><p>{d}</p></article>''' for t, d in GBV_COMMITMENTS)
    services = "".join(f"<li><strong>{t}:</strong><br>{d}</li>" for t, d in GBV_SERVICES)
    return f"""    <section class="gbvo" id="gbv" aria-labelledby="gbv-title">
      <div class="gbvo__inner">
        <h2 id="gbv-title" class="gbvo__title">Anti-GBV Pledge</h2>
        <p class="gbvo__intro">{GBV_PLEDGE}</p>
        <h3 class="gbvo__red">Our Commitments</h3>
        <div class="gbvo__commits">{commits}</div>
        <h3 class="gbvo__red">Legal Services for GBV Matters</h3>
        <ul class="gbvo__services">{services}</ul>
        <div class="gbvo__promise">
          <img src="assets/img/our-promise.webp" width="195" height="190" alt="Our Promise" loading="lazy">
          <p>{GBV_PROMISE}</p>
        </div>
      </div>
    </section>
"""


G = '<svg class="g-logo" viewBox="0 0 24 24" aria-hidden="true"><path fill="#4285F4" d="M23.5 12.3c0-.8-.1-1.6-.2-2.3H12v4.5h6.5a5.6 5.6 0 0 1-2.4 3.6v3h3.9c2.3-2.1 3.5-5.2 3.5-8.8z"/><path fill="#34A853" d="M12 24c3.2 0 6-1.1 8-2.9l-3.9-3c-1.1.7-2.5 1.2-4.1 1.2-3.1 0-5.8-2.1-6.7-5H1.3v3.1A12 12 0 0 0 12 24z"/><path fill="#FBBC05" d="M5.3 14.3a7.2 7.2 0 0 1 0-4.6V6.6H1.3a12 12 0 0 0 0 10.8l4-3.1z"/><path fill="#EA4335" d="M12 4.8c1.8 0 3.3.6 4.6 1.8l3.4-3.4A12 12 0 0 0 1.3 6.6l4 3.1c.9-2.9 3.6-4.9 6.7-4.9z"/></svg>'


def reviews_block():
    stars = '<span class="stars" aria-label="5 out of 5 stars">★★★★★</span>'
    if REVIEWS:
        cards = "\n".join(f"""          <figure class="review">{stars}<blockquote>“{t}”</blockquote><figcaption>{G}<span><strong>{n}</strong>Google review</span></figcaption></figure>""" for t, n in REVIEWS)
    else:
        cards = "\n".join(f"""          <figure class="review review--placeholder">{stars}<blockquote>Client review from Google appears here: the client's own words about their experience with the firm.</blockquote><figcaption>{G}<span><strong>Client name</strong>Google review</span></figcaption></figure>""" for _ in range(3))
    return f"""    <section class="section section--soft" id="reviews" aria-labelledby="reviews-title">
      <div class="container">
        <div class="section-head section-head--split">
          <div>
            <p class="eyebrow">Google reviews</p>
            <h2 class="h2" id="reviews-title">What our clients say</h2>
          </div>
          <div class="reviews__actions">
            <p>Read what clients say about working with {FIRM}, or share your own experience.</p>
            <div class="btn-row">
              <a class="btn btn--light" href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener">{G}Read our Google reviews</a>
              <a class="btn btn--outline" href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener">Leave a review</a>
            </div>
          </div>
        </div>
        <div class="review-grid">
{cards}
        </div>
        <div class="center-cta"><a class="btn btn--light btn--lg" href="contact.html#book">{ic('cal')}Book a consultation</a></div>
      </div>
    </section>
"""


def faq_block():
    items = "\n".join(f"""          <details class="faq__item"><summary>{q}</summary><p>{a}</p></details>""" for q, a in FAQS)
    return f"""    <section class="section section--soft" id="faq" aria-labelledby="faq-title">
      <div class="container faq">
        <div class="faq__head">
          <p class="eyebrow">FAQ</p>
          <h2 class="h2" id="faq-title">Frequently asked questions</h2>
          <p>Can't find your answer? Speak to us directly.</p>
          <div class="btn-col">
            <a class="btn btn--light btn--lg" href="contact.html#book">{ic('cal')}Book a consultation</a>
            <a class="btn btn--outline btn--lg" href="tel:{TEL_LINK}">{ic('phone')}Call {TEL}</a>
            <a class="btn btn--outline btn--lg" href="{WA}" target="_blank" rel="noopener">{ic('wa')}Ask on WhatsApp</a>
          </div>
        </div>
        <div class="faq__list">
{items}
        </div>
      </div>
    </section>
"""


def insights_block():
    cards = "\n".join(f"""          <article class="insight">
            <p class="insight__tag">{tag}</p>
            <h3>{title}</h3>
            <p>{text}</p>
            <span class="insight__soon">Article coming soon</span>
          </article>""" for tag, title, text in INSIGHTS)
    return f"""    <section class="section section--light" id="insights" aria-labelledby="insights-title">
      <div class="container">
        <div class="section-head section-head--split">
          <div>
            <p class="eyebrow">Insights</p>
            <h2 class="h2" id="insights-title">Legal insights &amp; guides</h2>
          </div>
          <div>
            <p>Plain-language guides to common legal questions in South Africa. New articles are on the way. In the meantime, ask us about your matter.</p>
            <a class="btn btn--light" href="contact.html#book">{ic('cal')}Book a consultation</a>
          </div>
        </div>
        <div class="insight-grid">
{cards}
        </div>
      </div>
    </section>
"""


def home():
    body = f"""  <main id="main">
    <section class="hero" aria-labelledby="hero-title">
      <div class="container hero__grid">
        <div class="hero__copy">
        <p class="eyebrow">Attorneys in Newcastle, KwaZulu-Natal</p>
        <h1 id="hero-title" class="hero__title">Dedicated to Results.<br><em>Driven by Excellence.</em></h1>
        <p class="hero__lead">Efficient, affordable legal solutions, custom-tailored for every client. Criminal and civil litigation, family and divorce, labour, RAF and estate matters across KwaZulu-Natal.</p>
        <div class="hero__ctas">
          <a class="btn btn--light btn--lg" href="contact.html#book">{ic('cal')}Book a consultation</a>
          <a class="btn btn--outline btn--lg" href="tel:{TEL_LINK}">{ic('phone')}Call {TEL}</a>
          <a class="btn btn--outline btn--lg" href="{WA}" target="_blank" rel="noopener">{ic('wa')}WhatsApp</a>
        </div>
        <ul class="hero__facts">
          <li>{ic('gavel')}<span><strong>Magistrates' &amp; High Court</strong>litigation</span></li>
          <li>{ic('video')}<span><strong>In-office or virtual</strong>consultations</span></li>
          <li>{ic('shield')}<span><strong>LPC Firm No. {LPC}</strong>registered law firm</span></li>
        </ul>
        </div>
        <figure class="hero__logo">
          <img src="assets/img/hero-monogram.webp" srcset="assets/img/hero-monogram-360.webp 432w, assets/img/hero-monogram.webp 720w" sizes="(min-width: 960px) 560px, 90vw" width="720" height="556" alt="The SAS monogram of Sahil Samlal Attorneys Inc." fetchpriority="high">
        </figure>
      </div>
    </section>

    <section class="quickbar" aria-label="Contact us">
      <div class="container quickbar__grid">
        <a class="qtile" href="tel:{TEL_LINK}">{ic('phone')}<span><small>Office</small>{TEL}</span></a>
        <a class="qtile" href="tel:{CELL_LINK}">{ic('phone')}<span><small>Cell</small>{CELL}</span></a>
        <a class="qtile" href="mailto:{EMAIL}">{ic('mail')}<span><small>Email</small>{EMAIL}</span></a>
        <a class="qtile" href="{MAPS}" target="_blank" rel="noopener">{ic('pin')}<span><small>Office</small>54 Bird Street, Newcastle</span></a>
      </div>
    </section>

    <section class="section section--light" id="practice" aria-labelledby="practice-title">
      <div class="container">
        <div class="section-head section-head--split">
          <div>
            <p class="eyebrow eyebrow--dark">Areas of practice</p>
            <h2 class="h2" id="practice-title">Legal help for individuals, families and businesses</h2>
          </div>
          <div>
            <p>Whether you're navigating a sensitive family dispute, a labour conflict or a high-stakes litigation matter, we provide clear legal direction and tenacious representation.</p>
            <a class="btn btn--navy" href="practice-areas.html">See all practice areas {ic('arrow')}</a>
          </div>
        </div>
        <div class="area-grid">
{area_cards()}
          <article class="area area--cta">
            <h3>Not sure where your matter fits?</h3>
            <p>Tell us what happened and we'll point you in the right direction.</p>
            <a class="btn btn--light" href="contact.html#book">{ic('cal')}Book a consultation</a>
            <a class="btn btn--outline" href="tel:{TEL_LINK}">{ic('phone')}{TEL}</a>
          </article>
        </div>
      </div>
    </section>

{cta_band()}
    <section class="section section--soft" id="about" aria-labelledby="about-title">
      <div class="container director">
        <figure class="director__photo">
          <img src="assets/img/sahil-samlal.webp" width="324" height="309" alt="Sahil Ishan Samlal, Director and Founder of Sahil Samlal Attorneys Inc." loading="lazy">
          <figcaption><strong>Sahil Ishan Samlal</strong> LLB, LLM<span>Director, Founder</span></figcaption>
        </figure>
        <div class="director__copy">
          <p class="eyebrow eyebrow--dark">About the firm</p>
          <h2 class="h2" id="about-title">We don't merely advise. We partner with our clients.</h2>
          <blockquote class="pull">Efficient, affordable legal solutions, custom-tailored for every client.</blockquote>
          <p>At {FIRM}, we guide our clients through complex legal challenges with precision and foresight. Sahil Samlal practises across Magistrates' Court and High Court litigation, Labour Court matters, family and matrimonial law, criminal defence and broader civil litigation.</p>
          <p>We pride ourselves on legal services that are responsive, accountable and always in pursuit of your best interests.</p>
          <div class="btn-row">
            <a class="btn btn--navy" href="about.html">Read the director profile {ic('arrow')}</a>
            <a class="btn btn--ghost-dark" href="contact.html#book">{ic('cal')}Book a consultation</a>
          </div>
        </div>
      </div>
    </section>

{reviews_block()}
{gbv_original()}
{cta_band("Need confidential help with a GBV matter?", "Consultations are discreet, in person or virtual. Speak to us today.")}
    <section class="section section--soft" id="jurisdiction" aria-labelledby="jur-title">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow eyebrow--dark">Areas of jurisdiction</p>
          <h2 class="h2" id="jur-title">Representing clients across northern KwaZulu-Natal</h2>
        </div>
{courts_block()}
      </div>
    </section>

{faq_block()}
{insights_block()}
{cta_band("Dedicated to results. Let's discuss your matter.", "Office hours: Monday to Friday, 08h00–16h30 (closed 12h00–13h00 and on public holidays).")}  </main>
"""
    return {"file": "index.html", "active": "home",
            "title": "Sahil Samlal Attorneys Inc. | Attorneys in Newcastle, KwaZulu-Natal",
            "description": "Attorneys in Newcastle, KZN: criminal and civil litigation, divorce and family law, labour law, RAF and personal injury claims, and estates. Book a consultation.",
            "schema": [FIRM_SCHEMA, PERSON_SCHEMA, WEBSITE_SCHEMA, {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}], "body": body}


def practice():
    blocks = "\n".join(f"""        <article class="practice" id="{slug}">
          <span class="practice__icon">{ic(icon)}</span>
          <div class="practice__body">
            <h2>{name}</h2>
            <p>{desc}</p>
          </div>
          <div class="practice__ctas">
            <a class="btn btn--navy" href="contact.html?area={slug}#book">{ic('cal')}Book a consultation</a>
            <a class="btn btn--ghost-dark" href="tel:{TEL_LINK}">{ic('phone')}Call us</a>
          </div>
        </article>""" for slug, name, icon, desc in AREAS)
    body = page_hero("Areas of practice", "Practice areas",
                     "From urgent court applications to long-term estate planning, we handle a wide range of matters for individuals, families and businesses across KwaZulu-Natal.",
                     "Practice areas") + f"""
    <section class="section section--light">
      <div class="container practice-list">
{blocks}
      </div>
    </section>

{cta_band("Not sure which practice area applies?", "Describe your matter and we'll advise on the next steps.")}  </main>
"""
    return {"file": "practice-areas.html", "active": "areas",
            "title": "Practice Areas | Sahil Samlal Attorneys Inc., Newcastle KZN",
            "description": "Criminal and civil litigation, personal injury, RAF claims, commercial law, debt collection, family law, divorce, labour law, and estates and trusts in Newcastle, KZN.",
            "schema": [crumbs("Practice areas", "practice-areas.html")], "body": body}


def gbv_page():
    body = page_hero("Anti-GBV pledge", "We stand against gender-based violence",
                     "Confidential, survivor-centred legal help. Consultations are discreet, in person or virtual.",
                     "Anti-GBV") + f"""
{gbv_original()}
{cta_band("Speak to us confidentially", "Discreet consultations in person or virtual, with flexible hours for urgent matters.")}  </main>
"""
    return {"file": "anti-gbv.html", "active": "gbv",
            "title": "Anti-GBV Legal Services | Protection Orders | Sahil Samlal Attorneys",
            "description": "Confidential legal help for survivors of gender-based violence in Newcastle, KZN: protection orders, urgent interdicts, maintenance, family law and damages claims.",
            "schema": [crumbs("Anti-GBV", "anti-gbv.html")], "body": body}


def about():
    skills = "".join(f"<li>{ic('check')}{s}</li>" for s in [
        "Analysing complex legal and factual matrices across multiple areas of law",
        "Drafting persuasive pleadings and heads of argument",
        "Conducting in-depth consultations and trial advocacy",
        "Cross-examining witnesses with precision and clarity",
        "Navigating urgent applications and interlocutory relief efficiently"])
    body = page_hero("About us", "Efficient, affordable legal solutions",
                     f"At {FIRM}, we don't merely advise. We partner with our clients, guiding them through complex legal challenges with precision and foresight.",
                     "About") + f"""
    <section class="section section--light">
      <div class="container about-firm">
        <p class="lead lead--dark">Whether you're navigating a sensitive family dispute, a labour conflict or a high-stakes litigation matter, we provide clear legal direction and tenacious representation.</p>
        <p>We pride ourselves on delivering legal services that are responsive, accountable and always in pursuit of your best interests.</p>
      </div>
    </section>

    <section class="section section--soft" aria-labelledby="profile-title">
      <div class="container profile">
        <aside class="profile__card">
          <img src="assets/img/sahil-samlal.webp" width="324" height="309" alt="Sahil Ishan Samlal, Director and Founder">
          <h2>Sahil Ishan Samlal</h2>
          <p class="profile__creds">LLB, LLM · Director, Founder</p>
          <a class="btn btn--navy btn--block" href="contact.html#book">{ic('cal')}Book a consultation</a>
          <a class="btn btn--ghost-dark btn--block" href="tel:{TEL_LINK}">{ic('phone')}{TEL}</a>
        </aside>
        <div class="profile__copy">
          <p class="eyebrow eyebrow--dark">Director profile</p>
          <h2 class="h2" id="profile-title">Precision, tenacity and strategic clarity</h2>
          <p>Sahil Samlal is a committed, highly skilled legal practitioner who brings precision, tenacity and strategic clarity to every matter. As the founder and director of {FIRM}, he leads a reputable and growing firm built on legal excellence, strategic litigation and client-focused results.</p>
          <p>He practises across Magistrates' Court and High Court litigation, Labour Court matters, family and matrimonial law, criminal defence and broader civil litigation. In court, he is known for assertive argumentation, meticulous preparation and tactical execution in both trial and motion proceedings.</p>
          <h3>He is particularly proficient in:</h3>
          <ul class="checks">{skills}</ul>
          <p>What distinguishes him is not only legal command but a resolute dedication to advancing clients' interests cost-effectively and without delay. He synthesises large volumes of information quickly, isolates key issues, and crafts creative, effective solutions, even in highly contentious disputes.</p>
          <p>Anchored in professional ethics and a commitment to justice, he continually adapts to South Africa's evolving legal landscape. He is passionate about the rule of law, access to justice and the development of local jurisprudence. His long-term vision includes further contribution to the profession as a senior attorney and future advocate, with matters argued before the Constitutional Court.</p>
          <p>At {FIRM}, he leads with the conviction that every client deserves focused, professional and strategic representation. Through a dynamic, analytical and principled approach, he serves as a trusted legal advisor and litigator of choice.</p>
        </div>
      </div>
    </section>

    <section class="section section--light" aria-labelledby="jur-title">
      <div class="container">
        <div class="section-head">
          <p class="eyebrow eyebrow--dark">Areas of jurisdiction</p>
          <h2 class="h2" id="jur-title">Where we appear</h2>
        </div>
{courts_block()}
      </div>
    </section>

{cta_band()}  </main>
"""
    return {"file": "about.html", "active": "about",
            "title": "About Sahil Samlal Attorneys Inc. | Director Sahil Ishan Samlal (LLB, LLM)",
            "description": "Meet Sahil Ishan Samlal (LLB, LLM), director of Sahil Samlal Attorneys Inc. in Newcastle, KZN: litigation, labour, family and criminal law, in Magistrates' and High Courts.",
            "schema": [crumbs("About", "about.html"), PERSON_SCHEMA], "body": body}


def contact():
    opts = "".join(f'<option value="{slug}">{plain(name)}</option>' for slug, name, _, _ in AREAS) + '<option value="gbv">Gender-based violence (confidential)</option><option value="other">Other / not sure</option>'
    body = page_hero("Contact us", "Book a consultation",
                     "Fill in the form and our team will contact you to confirm a time. Note: selected dates and times are subject to our consulting team's availability.",
                     "Contact") + f"""
    <section class="section section--light" id="book" aria-labelledby="form-title">
      <div class="container contact">
        <form class="form-card" id="booking-form" novalidate>
          <h2 id="form-title">Appointment details</h2>
          <p class="form-card__sub">All fields are required.</p>
          <div class="grid-2">
            <div class="field"><label for="f-name">Full name</label><input class="input" id="f-name" name="name" autocomplete="name" required><p class="field-error" id="err-name"></p></div>
            <div class="field"><label for="f-cell">Cell number</label><input class="input" id="f-cell" name="cell" type="tel" inputmode="tel" autocomplete="tel" placeholder="082 000 0000" required><p class="field-error" id="err-cell"></p></div>
            <div class="field field--full"><label for="f-email">Email</label><input class="input" id="f-email" name="email" type="email" autocomplete="email" required><p class="field-error" id="err-email"></p></div>
            <div class="field field--full"><label for="f-area">Type of matter</label><select class="input" id="f-area" name="area" required><option value="">Select a practice area</option>{opts}</select><p class="field-error" id="err-area"></p></div>
            <div class="field field--full"><label for="f-details">Describe the legal services you need</label><textarea class="input" id="f-details" name="details" rows="4" required></textarea><p class="field-error" id="err-details"></p></div>
          </div>
          <fieldset class="field field--full choices">
            <legend>Platform for consultation</legend>
            <label class="choice"><input type="radio" name="platform" value="At our offices" required>{ic('pin')}At our offices</label>
            <label class="choice"><input type="radio" name="platform" value="Virtual">{ic('video')}Virtual</label>
            <p class="field-error" id="err-platform"></p>
          </fieldset>
          <div class="field field--full"><label for="f-avail">Your availability</label><input class="input" id="f-avail" name="availability" placeholder="e.g. Tuesday 9 AM" required><p class="hint">Office hours: 08h00–16h30 on weekdays.</p><p class="field-error" id="err-availability"></p></div>
          <label class="consent"><input type="checkbox" name="consent" required><span>I agree that {FIRM} may use these details to respond to my enquiry, in line with POPIA and the <a href="#popia">privacy notice</a>.</span></label>
          <p class="field-error" id="err-consent"></p>
          <button class="btn btn--navy btn--lg btn--block" type="submit">{ic('cal')}Request my consultation</button>
          <p class="form-status" role="status" aria-live="polite"></p>
        </form>

        <aside class="contact-card">
          <h2>Contact us today</h2>
          <ul class="contact-list">
            <li><a href="tel:{TEL_LINK}">{ic('phone')}<span><small>Tel</small>{TEL}</span></a></li>
            <li><a href="tel:{CELL_LINK}">{ic('phone')}<span><small>Cell</small>{CELL}</span></a></li>
            <li><a href="{WA}" target="_blank" rel="noopener">{ic('wa')}<span><small>WhatsApp</small>Message us</span></a></li>
            <li><a href="mailto:{EMAIL}">{ic('mail')}<span><small>Email</small>{EMAIL}</span></a></li>
          </ul>
          <h3>Our offices</h3>
          <address>{FIRM}<br>{'<br>'.join(ADDRESS_LINES)}</address>
          <a class="btn btn--light btn--block" href="{MAPS}" target="_blank" rel="noopener">{ic('pin')}Get directions</a>
          <h3>Office hours</h3>
          <dl class="hours">
            <div><dt>Mon–Fri</dt><dd>08h00–12h00</dd></div>
            <div><dt>Lunch</dt><dd>12h00–13h00</dd></div>
            <div><dt>Mon–Fri</dt><dd>13h00–16h30</dd></div>
            <div><dt>Public holidays</dt><dd>Closed</dd></div>
          </dl>
        </aside>
      </div>
    </section>
  </main>
"""
    return {"file": "contact.html", "active": "contact",
            "title": "Contact & Book a Consultation | Sahil Samlal Attorneys, Newcastle KZN",
            "description": "Book a consultation with Sahil Samlal Attorneys at 54 Bird Street, Newcastle, or online. Call (034) 315 5315, WhatsApp 082 762 5716 or email info@samlalattorneys.com.",
            "schema": [crumbs("Contact", "contact.html")], "body": body}


def notfound():
    body = f"""  <main id="main">
    <section class="page-hero page-hero--404">
      <div class="container">
        <p class="eyebrow">Error 404</p>
        <h1 class="page-hero__title">This page could not be found</h1>
        <p class="page-hero__lead">The link may be broken or the page may have moved.</p>
        <div class="page-hero__ctas">
          <a class="btn btn--light btn--lg" href="index.html">Back to the homepage</a>
          <a class="btn btn--outline btn--lg" href="contact.html#book">{ic('cal')}Book a consultation</a>
          <a class="btn btn--outline btn--lg" href="tel:{TEL_LINK}">{ic('phone')}{TEL}</a>
        </div>
      </div>
    </section>
  </main>
"""
    return {"file": "404.html", "active": None, "noindex": True, "title": "Page not found | Sahil Samlal Attorneys Inc.",
            "description": "This page could not be found.", "schema": [WEBSITE_SCHEMA], "body": body}


PAGES = [home(), practice(), gbv_page(), about(), contact(), notfound()]


def main():
    for p in PAGES:
        html = head(p) + header(p["active"]) + p["body"] + footer()
        assert html.count("<h1") == 1, f"{p['file']}: expected one <h1>"
        (ROOT / p["file"]).write_text(html, encoding="utf-8")
    urls = "\n".join(
        f"  <url>\n    <loc>{DOMAIN}/{'' if p['file'] == 'index.html' else p['file']}</loc>\n    <lastmod>{TODAY}</lastmod>\n  </url>"
        for p in PAGES if not p.get("noindex"))
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n', encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")
    print("Built:", ", ".join(p["file"] for p in PAGES))


if __name__ == "__main__":
    main()
