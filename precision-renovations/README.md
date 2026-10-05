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

## SEO files
- `robots.txt` and `sitemap.xml` sit next to `index.html`.
- The schema (JSON-LD: GeneralContractor and WebSite) is in the `<head>` of `index.html`.
- The domain is **assumed** to be `https://www.precisionrenovations.co.za/`. Update it in `index.html` (canonical, og tags and schema), `robots.txt` and `sitemap.xml` once the real domain is known.

## Still to add
- **Reviews:** replace the three placeholder cards in the `REVIEWS` section of `index.html`.
- **Formspree** link.
- Business hours and a street address, if wanted. They would also go in the schema.

## Files
- `assets/img`: logo (cut out from the supplied logo, with a white version for the footer), hero, and optimised project photos (WebP).
- `assets/references`: the original hero, logo, wordmark and palette. These are not needed on the live site.
- Brand colours: deep teal `#133643`, forest green `#35523F`, bronze `#807253`, tan `#AB9D78`, cream `#E3DBB5`. They are tokens at the top of `styles.css`.
