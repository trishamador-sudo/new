# Família Amador Construções: website

A fast, bilingual static website (European Portuguese and English) for Família Amador Construções, a dad-and-daughter renovation company in Montemor-o-Novo. It uses plain HTML, CSS and a little JavaScript, with no framework.

- **Portuguese:** the default language, at `/`.
- **English:** at `/en/`.
- **Deploy folder:** `site/` (upload this to Cloudflare Pages).
- **47 pages:** 23 in Portuguese, 23 in English, plus a bilingual 404 page.

## Files

| Path | What it is |
|---|---|
| `build.py` | The generator: page templates, the PT/EN page map, schema, sitemap. **The domain constant is here.** |
| `content.py` | All the copy: services, areas, FAQs (PT and EN) |
| `site/` | The generated website: upload this folder |
| `site/assets/css/styles.css` | Design. Brand colours are variables at the top. |
| `site/assets/js/main.js` | Mobile menu, WhatsApp chooser, quote form |
| `site/assets/pagemap.json` | PT ↔ EN page map, generated from `build.py` |
| `source-images/` | The original photos, logo and inspiration screenshots. These are not uploaded. |

**To change any text:** edit `content.py` or `build.py`, then run `python3 build.py`. Do not edit the HTML in `site/` by hand; it is overwritten on every build.

## Change the domain

The domain is not known yet. The site uses the placeholder **`https://familiaamador.pt`**.

1. In `build.py`, change `DOMAIN = "https://familiaamador.pt"` to the real address (no slash at the end).
2. Run `python3 build.py`.

That one change updates every canonical tag, hreflang link, Open Graph URL, schema, `sitemap.xml` and `robots.txt`.

## Pages

| Portuguese | English |
|---|---|
| `/` | `/en/` |
| `/servicos/` + 10 service pages | `/en/services/` + 10 service pages |
| `/zonas/` + 6 area pages | `/en/areas/` + 6 area pages |
| `/projetos/` | `/en/projects/` |
| `/sobre-nos/` | `/en/about/` |
| `/contacto/` | `/en/contact/` |
| `/obrigado/` (noindex) | `/en/thank-you/` (noindex) |

- **Language switcher:** every page carries hreflang links to its pair (pt-PT, en, x-default → PT). The PT | EN switcher always goes to the equivalent page.
- **Small towns:** Lavre, Santiago do Escoural, Cabrela and Ciborro are covered on the Montemor-o-Novo page and in the area chips.

## Add a review

Reviews are hidden until there are real ones. Never add invented reviews.

1. In `build.py`, find `<!-- REVIEWS:` in the `home()` function.
2. Add one `<figure class="review">` for each review, with the exact text and the reviewer's name.
3. Remove `hidden` from `<section class="section" id="reviews" hidden ...>`.
4. Run `python3 build.py`.

## Add a project

1. Put the photos in `source-images/`. Convert them to WebP and JPG at about 800 px wide in `site/assets/img/`, and add their size to `IMG` in `build.py`.
2. In `projects_block()` in `build.py`, copy one `<article class="proj">` block and change the photos, labels and text.
3. Add alt text for both languages in `ALT_TEXT`.
4. Optional: replace the `<!-- PROJECT LOCATION -->` comment with the town.
5. Run `python3 build.py`.

## Add the email address

The email is left out for now. Search `build.py` for `EMAIL:`. There are placeholders in the footer and on the contact page. Also add `"email"` to `business_schema()`.

## Quote form

- **Where it sends:** the form posts to Formspree, `https://formspree.io/f/mrpqkrva`.
- **How it sends:** with JavaScript, it sends in the background and opens `/obrigado/` or `/en/thank-you/`. Without JavaScript, it still posts to Formspree normally.
- **Email subject:** "Novo pedido de orçamento - [service] - [town]". The page URL and language are included.
- **Spam:** a hidden `_gotcha` field blocks simple spam.

## Deploy to Cloudflare Pages

1. **Upload:** Cloudflare → Workers & Pages → Create → Pages → upload the **`site`** folder. You can also connect the GitHub repo with build output directory `familia-amador/site` and no build command.
2. **Custom domain:** add the domain, plus the `www` version if you use one.
3. **One version of the address:**
   - Turn on SSL/TLS → Edge Certificates → **Always Use HTTPS**.
   - Add a 301 Redirect Rule so that only one version is used. For example, send `www.` to the bare domain if `DOMAIN` has no `www`.
4. **Extras included:** `_headers` adds HSTS, security headers and long caching for `/assets/`. `404.html` is the bilingual not-found page.

## After launch: checklist

- [ ] Change `DOMAIN` in `build.py` to the real domain, rebuild and redeploy.
- [ ] Google Search Console: add the site and submit `https://<domain>/sitemap.xml`.
- [ ] Google Business Profile: create it in Montemor-o-Novo, with these service areas:
  - Montemor-o-Novo, Arraiolos, Vendas Novas, Lavre;
  - Santiago do Escoural, Cabrela, Ciborro;
  - Viana do Alentejo, Évora, Lisboa.

  Add both phone numbers and the website. Do not add electrical services.
- [ ] Formspree: send a test quote from the live site and click the confirmation link that Formspree emails to the form owner.
- [ ] Add the email address (see above).
- [ ] Add real Google reviews when you have them (see above).
- [ ] Run Lighthouse (Chrome DevTools) on the live homepage and a service page on mobile.

## SEO built in
- **Every page:**
  - a unique title (under 60 characters) and meta description (under 155 characters);
  - one H1, canonical, hreflang, Open Graph and Twitter tags;
  - `lang="pt-PT"` or `lang="en"`.
- **Schema (JSON-LD):**
  - `HomeAndConstructionBusiness`, with both phones, `areaServed`, `knowsLanguage` and `priceRange`;
  - `Person` nodes for Ricardo and Trishta;
  - `WebSite`;
  - `Service` on each service page;
  - `FAQPage` wherever there are FAQs;
  - `BreadcrumbList` on inner pages.
- **`sitemap.xml`:** lists the 44 indexable pages, with `xhtml:link` hreflang alternates. `robots.txt` points to it.
- **Page content:**
  - Area pages have their own content: typical properties, most-requested services, distance from Montemor-o-Novo and a local FAQ.
  - Every service page links to every area page, and every area page to every service.
  - The footer lists all services and areas.
- **Images:** WebP with a JPG fallback, width and height set, lazy-loaded below the fold. The hero image and both fonts are preloaded, and the fonts (Outfit, Inter) are self-hosted.
- **Accessibility:**
  - Gold text on light backgrounds uses a darker gold (`#7A6000`, 5.5:1 contrast).
  - The bright logo gold (`#CCA300`) is used only on black or behind black text.
  - The menu, FAQ accordion and WhatsApp chooser all work with the keyboard.
