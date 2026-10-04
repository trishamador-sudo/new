# Minnaar Attorneys website

A static site: plain `index.html`, `styles.css` and `main.js` with no build step. Upload the folder to any static host, such as Cloudflare Pages.

## Edit contact details
Change the `SITE` block at the top of `main.js`. The phone number, WhatsApp, email, area and form endpoint update across the whole page.

## Consultation form
The form is connected to Formspree (`formEndpoint` in `main.js`: https://formspree.io/f/xoevogrd), which delivers to louise@lawgical.co.za.

The first live submission triggers a Formspree confirmation email. Click the link in it to activate the form.

## Add a blog article (Insights)
In `index.html`, find the `Insights` section. It contains a commented-out example `<article class="post">` card.
1. Paste one card per article inside `.posts`.
2. Delete the `.posts__empty` "Articles coming soon" block.

The layout switches to a grid automatically.

## Files
- `assets/img/`: hero (`hero.webp`, `hero-960.webp`), logo (`logo.png`), M mark (`mark.png`, `mark-white.png`), favicons, social image (`og.jpg`), Louise's photo.
- `assets/fonts/`: self-hosted Manrope and Cinzel (wordmark only), under the SIL Open Font License.
- `assets/references/`: original uploads (hero, logo, email signature, inspiration). These are not needed on the live site.

## Brand
See `copy/brand-kit.md` (October 2026 questionnaire).
- Dark, moody palette from the logo and hero image.
- Manrope type.
- Slogan "Moving beyond conflict."

## Placeholders to confirm
- Office hours are carried over from Lawgical Labour.
- Only "Krugersdorp" is shown, with no street address.

## SEO files
- `robots.txt` and `sitemap.xml` sit next to `index.html`.
- The schema (JSON-LD: Attorney, Person, WebSite) is in the `<head>` of `index.html`.
- All three use `https://www.minnaar-law.co.za/`. If the domain changes, update it in all three places.
- When blog articles are added, list each article URL in `sitemap.xml`.
