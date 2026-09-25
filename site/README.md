# Swift Deals 18 Construction: website

A static one-page site (HTML + CSS + a little JavaScript). No build step. Open `index.html` or upload the `site/` folder to any web host.

## Edit your details

Open `main.js`. At the very top is `SITE`:

| Setting | What it does |
|---|---|
| `phone` / `phoneLink` | Phone number shown on the site / digits used for tap-to-call |
| `email` | Contact email (footer, and where estimate requests go if no form endpoint is set) |
| `serviceArea`, `hours` | Shown in the top bar and footer |
| `formEndpoint` | Where the estimate form sends leads, e.g. a [Formspree](https://formspree.io) URL. Leave empty to open the visitor's email app instead |

## Still to add

- **Reviews:** replace the three dashed placeholder cards in the `REVIEWS` section of `index.html`.
- **Photos:** the Plumbing, New builds and Repairs service cards show "photo coming soon". Swap each `svc__media--placeholder` block for an `<img>` once you have photos. Put images in `assets/img/`.

## Files

- `index.html`: page content
- `styles.css`: design (brand colours are at the top as CSS variables)
- `main.js`: settings, estimate form, menu, video
- `assets/img`, `assets/video`: logo, project photos and video (optimised WebP / MP4)
