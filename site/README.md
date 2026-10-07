# Swift Deals 18 Construction: website

A static one-page site (HTML, CSS and a little JavaScript) with no build step. To publish, upload everything in this folder to a web host such as Cloudflare Pages. `index.html`, `robots.txt` and `sitemap.xml` must sit together at the top level.

**Live domain:** https://swiftdeals18.com/

## Edit your details

Open `main.js`. At the very top is `SITE`:

| Setting | What it does |
|---|---|
| `phone` / `phoneLink` | Phone number shown on the site / digits used for tap-to-call |
| `email` | Contact email shown in the footer |
| `serviceArea`, `hours` | Shown in the top bar and footer |
| `formEndpoint` | Your Formspree form URL. Estimate requests are emailed to the account that owns the form. |
| `leadEmail` | Only used while `formEndpoint` is empty: the form opens the visitor's email app addressed here |

### Estimate form (Formspree)

The form is connected to `https://formspree.io/f/xvkgblbq`, which delivers to the Formspree account for **trishamador@gmail.com**. Each request (project type, name, phone, details) arrives by email.

To use a different form:
1. Create a form at [formspree.io](https://formspree.io).
2. Paste its endpoint into `formEndpoint`.

## SEO files

- **`robots.txt`:** allows all search engines and points them to the sitemap.
- **`sitemap.xml`:** lists the page for Google. Update `<lastmod>` (YYYY-MM-DD) when the site changes, and add any new pages.
- **Canonical link:** the `<head>` of `index.html` points to `https://swiftdeals18.com/`.

If the domain changes, update it in all three places: `index.html`, `robots.txt` and `sitemap.xml`.

After the site is live, add it to [Google Search Console](https://search.google.com/search-console) and submit `https://swiftdeals18.com/sitemap.xml` so Google finds it quickly.

## Still to add

- **Reviews:** replace the three dashed placeholder cards in the `REVIEWS` section of `index.html`.
- **Photos:** to add a service card (e.g. Plumbing) once you have a photo:
  1. Copy one of the `<article class="svc">` blocks in `index.html`.
  2. Change its image and text.
  3. Put the image in `assets/img/`.

## Files

| Path | What it is |
|---|---|
| `index.html` | Page content and SEO tags |
| `styles.css` | Design. Brand colours are CSS variables at the top. |
| `main.js` | Settings, estimate form, menu and video |
| `robots.txt`, `sitemap.xml` | Search engine files |
| `assets/img`, `assets/video` | Logo, project photos and video (optimised WebP / MP4) |
