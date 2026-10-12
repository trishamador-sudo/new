# Precision Renovations: website

A static one-page site (HTML, CSS and a little JavaScript) built on the Swift Deals 18 template. There is no build step: upload this folder to any web host, such as Cloudflare Pages.

## Edit the details
At the top of `main.js` is `SITE`, which holds:
- the phone and WhatsApp number;
- the email address;
- the service area;
- `formEndpoint`, the Formspree link.

### Connect the estimate form (Formspree)
1. Create a form at https://formspree.io that delivers to the right inbox.
2. Paste its endpoint (e.g. `https://formspree.io/f/abcdwxyz`) into `formEndpoint`.

Until then, the form opens the visitor's email app, addressed to `leadEmail` (jean.pepler@gmail.com).

## Estimate form
- **Service area:** free estimates within a 45 km radius of Centurion. This is stated in the form box and in the schema (a 45 km GeoCircle around Centurion).
- **Required fields:** name, phone, project location (suburb or area), and a POPIA consent tick box. The location and consent are included in every request.
- **POPIA:** the full privacy notice is in the footer (`#popia`), and the consent box links to it.

## Photos
- Click any service, before/after or gallery photo to open it in full, uncropped.
- Before/after photos are shown at their natural shape, not cropped.
- **Bathroom 1:** `bathroom1-before` and `bathroom1-after`.
- **Bathroom 2:** `bathroom2-before` and `bathroom2-after`.

## SEO files
- `robots.txt` and `sitemap.xml` sit next to `index.html`.
- The canonical link (`<link rel="canonical">`) and the schema (JSON-LD: GeneralContractor and WebSite) are in the `<head>` of `index.html`.
- The domain is **assumed** to be `https://www.precisionrenovations.co.za/`. Update it in `index.html` (canonical, og tags and schema), `robots.txt` and `sitemap.xml` once the real domain is known.

## Still to add
- **Reviews:** replace the three placeholder cards in the `REVIEWS` section of `index.html`.
- **Formspree** link.
- Business hours and a street address, if wanted. They would also go in the schema.

## Files
- `assets/img`: logo (cut out from the supplied logo, with a white version for the footer), hero, and optimised project photos (WebP).
- `assets/references`: the original hero, logo, wordmark and palette. These are not needed on the live site.
- Facebook ("View our work on Facebook") links: header icon, hero pill, under the gallery and in the footer. Change the link in `SITE.facebook` in `main.js`.
- Brand colours: deep teal `#133643`, forest green `#35523F`, bronze `#807253`, tan `#AB9D78`, cream `#E3DBB5`. They are tokens at the top of `styles.css`.
