# Bit Byte Tech: website mock-up

A one-page mock-up for Bit Byte Tech (computer repairs, upgrades and new builds). It is a static site (HTML, CSS and a little JavaScript). All the content comes from the client's poster (`assets/references/poster.pdf`).

## Design
- **Colours (from the logo):** near-black navy `#070C13`, electric blue `#39A9F5` / `#37B8FF`, and white. The whole site is dark.
- **Fonts:** all three are self-hosted in `assets/fonts/`.
  - Exo 2 (italic) for headings, matching the logo lettering.
  - Manrope for body text.
  - Yellowtail for "Your Friendly Neighbourhood Geek".
- **Logo:** extracted from the poster, with a transparent background.

## Sections
1. **Hero:** the logo, "Computer giving you trouble?" and free-quote buttons.
2. **Services:** Repairs, Upgrades and New builds, plus "Quotes cost nothing".
3. **How it works:** four steps.
4. **Why me:** CompTIA A+ certified, one technician, written price first, honest advice.
5. **Contact:** phone, email, the WhatsApp QR code and a contact form.

## Mock-up only
- **Contact form:** not connected. It checks the fields and shows a thank-you message, but sends nothing. To make it live, point it at Formspree or similar.
- **Contact details:** the phone number and email are shown as text, not as tap-to-call or email links. All buttons scroll to the contact section.
- **Domain:** assumed to be `https://www.bitbytetech.co.za`. Update it in `index.html` (canonical, Open Graph and schema), `robots.txt` and `sitemap.xml` once the real domain is known.
- **Not on the poster, left out:** the owner's name, address, service area and hours. Add them to the page and the schema when confirmed.
