# Apex Lead Advisors: website

A static one-page site (HTML, CSS and a little JavaScript), built on the Swift Deals 18 layout. There is no build step: upload everything in this folder to any web host, such as Cloudflare Pages. `index.html`, `robots.txt` and `sitemap.xml` must sit together at the top level.

## Page sections
1. **Top bar:** audience line, email and WhatsApp number.
2. **Header:** logo, menu, a WhatsApp button and "Book a free audit" (Calendly).
3. **Hero:** headline, "Book a free audit" and "WhatsApp me", and the 2-step free audit form.
4. **Trust strip.**
5. **Who I help:** law firms in South Africa and contractors.
6. **Services:** Websites & Web Optimisation, SEO, Google Business Profile Optimisation and Meta Ads (all for law firms), plus Lead Capture and Campaign Reporting.
7. **Work:** screen recordings of six websites (`assets/video/`), with a short SEO-focused description each. Videos play muted while on screen.
8. **About:** Trish's profile, law degrees and the story behind the business.
9. **Contact band:** call, WhatsApp, email and form.
10. **Footer.**

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

## Adding a website to the Work section
1. Export a short screen recording as MP4 and a still image (WebP) of its first frame into `assets/video/`.
2. Copy one `<article class="work-card">` block in `index.html` and change the video, poster, name and description.
3. Add a matching `VideoObject` to the schema in the `<head>`.

## Analytics, favicon and 404
- **Google Analytics 4** (`G-7RCQE05LLV`) is in the `<head>` of `index.html` and `404.html`. The footer says the site uses Google Analytics.
- **Favicon:** `favicon.ico` (16/32/48), `assets/img/favicon-32.png` and `apple-touch-icon.png` (180×180), made from `assets/img/mark-white.png` on navy `#062B66`.
- **404 page:** `404.html` in the site root. Cloudflare Pages serves it automatically for missing pages. It is set to `noindex`.

## SEO files
- **`robots.txt`** and **`sitemap.xml`** sit next to `index.html`.
- **Schema (JSON-LD)** is in the `<head>` of `index.html`: ProfessionalService, Person (founder) and WebSite.
- **Domain:** `https://www.apexleadadvisors.com/` (www is the main address). If it changes, update it in:
  - `index.html` (canonical link, `og:` tags and schema);
  - `robots.txt`;
  - `sitemap.xml`.

## Files
- `assets/img/`: logo, header lockup, white footer logo, mark, favicon, profile photo and share image.
- `assets/references/`: the original uploads. These are not needed on the live site.
- Brand colours: red `#EF0C28`, blue `#004AAD`, navy `#062B66`.
- Fonts: Outfit (headings) and Figtree (body).

## Hosting (Cloudflare Pages)
- Publish the contents of this folder. If the Pages project is connected to the GitHub repo, every push redeploys the site.
- **HSTS and security headers** are set in `_headers`.
- **Canonical www address:** in Cloudflare, turn on SSL/TLS > Edge Certificates > **Always Use HTTPS**. Then add a **Redirect Rule** sending `apexleadadvisors.com/*` to `https://www.apexleadadvisors.com/${1}` (301). Add both domains to the Pages project.
