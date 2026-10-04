# Client websites: house rules

Each client site lives in its own folder (e.g. `site/`, `plumber-steve/`, `minnaar-attorneys/`). For Vite projects, the deploy root is `public/`, which is copied to `dist/`.

## Every website must ship with these files (next to `index.html`, in the deploy root)
1. **`robots.txt`**: allow all crawlers, plus a `Sitemap:` line with the absolute sitemap URL.
   ```
   User-agent: *
   Allow: /

   Sitemap: https://www.<domain>/sitemap.xml
   ```
2. **`sitemap.xml`**: every real page, with absolute URLs and `<lastmod>` (YYYY-MM-DD). One-page sites list just `/`; add each blog post or page as it is created.
3. **Schema (JSON-LD)**: a `<script type="application/ld+json">` in the `<head>` of `index.html`, using an `@graph` that contains:
   - **the business**, as the most specific schema.org type: `Attorney`/`LegalService`, `Plumber`, `GeneralContractor`, etc. Include name, url, logo, image, telephone, email, address (or region if there is no street address), `areaServed`, `openingHoursSpecification`, `sameAs` (social links) and a services `OfferCatalog`.
   - **the owner/key person** as a `Person`, linked by `@id`.
   - **a `WebSite`** node.
   - Add `BlogPosting` on each article page once a blog has posts.

Also include in the `<head>`: a canonical link, and Open Graph tags with **absolute** `og:url`/`og:image`, plus a `twitter:card`.

Only state facts the client has confirmed. Leave out unknown fields; never invent addresses or reviews. If the domain is not yet known, use the planned domain and note in the README that it must be updated in `index.html`, `robots.txt` and `sitemap.xml`.
