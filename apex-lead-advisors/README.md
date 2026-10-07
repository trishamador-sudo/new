# Apex Lead Advisors: website

A static one-page site (HTML, CSS and a little JavaScript), built on the Swift Deals 18 layout. There is no build step: upload everything in this folder to any web host, such as Cloudflare Pages. `index.html`, `robots.txt` and `sitemap.xml` must sit together at the top level.

## Page sections
1. **Top bar:** audience line, email and WhatsApp number.
2. **Header:** logo, menu, a WhatsApp button and "Book a free audit" (Calendly).
3. **Hero:** headline, "Book a free audit" and "WhatsApp me", and the 2-step free audit form.
4. **Trust strip.**
5. **Who I help:** law firms in South Africa and contractors.
6. **Services:** the six services, plus calls to action.
7. **About:** Trish's profile, law degrees and the story behind the business.
8. **Contact band:** call, WhatsApp, email and form.
9. **Footer.**

There is also a floating WhatsApp button on larger screens, and an Email / WhatsApp / Book call bar on phones.

## Edit the details
Everything is in `SITE` at the top of `main.js`:

| Setting | What it does |
|---|---|
| `phone`, `phoneLink`, `whatsapp`, `whatsappText` | WhatsApp number and the pre-filled message |
| `email` | Contact email |
| `calendly` | Booking link used by every "Book a free audit" button |
| `formEndpoint` | Formspree form: `https://formspree.io/f/mljgjnjy` |

**Formspree:** the first live submission sends a confirmation email to the account that owns the form. Click the link in it to activate the form.

## SEO files
- **`robots.txt`** and **`sitemap.xml`** sit next to `index.html`.
- **Schema (JSON-LD)** is in the `<head>` of `index.html`: ProfessionalService, Person (founder) and WebSite.
- **Domain:** assumed to be `https://apexleadadvisors.com/`. If it differs, update it in:
  - `index.html` (canonical link, `og:` tags and schema);
  - `robots.txt`;
  - `sitemap.xml`.

## Files
- `assets/img/`: logo, header lockup, white footer logo, mark, favicon, profile photo and share image.
- `assets/references/`: the original uploads. These are not needed on the live site.
- Brand colours: red `#EF0C28`, blue `#004AAD`, navy `#062B66`.
- Fonts: Outfit (headings) and Figtree (body).
