# Plumber Steve: website

A static one-page site (HTML + CSS + a little JavaScript). No build step. Upload this folder to Cloudflare Pages (or any host).

## Edit details

Open `main.js`. At the top is `SITE`: phone, email, service area, hours and `formEndpoint`.

### Connect the quote form (Formspree)

1. In Formspree, create a new form (e.g. "Plumber Steve quotes").
2. Copy its endpoint, e.g. `https://formspree.io/f/abcdwxyz`.
3. Paste it into `formEndpoint` in `main.js`.

Until then, the form opens the visitor's email app addressed to plumbersteves@gmail.com.

## Still to add

- **Reviews:** replace the three dashed placeholder cards in the `REVIEWS` section of `index.html`.

## Files

- `index.html`: page content (copy follows `brand-voice.md` from the client pack)
- `styles.css`: design (brand colours at the top as CSS variables)
- `main.js`: settings, quote form, menu, project carousel
- `assets/img`: logo and project photos (WebP)
