# Swift Deals 18 Construction: website

A static one-page site (HTML + CSS + a little JavaScript). No build step. Open `index.html` or upload the `site/` folder to any web host.

## Edit your details

Open `main.js`. At the very top is `SITE`:

| Setting | What it does |
|---|---|
| `phone` / `phoneLink` | Phone number shown on the site / digits used for tap-to-call |
| `email` | Contact email shown in the footer |
| `serviceArea`, `hours` | Shown in the top bar and footer |
| `formEndpoint` | Your Formspree form URL. Estimate requests are emailed to the account that owns the form |
| `leadEmail` | Only used while `formEndpoint` is empty: the form opens the visitor's email app addressed here |

### Connect the estimate form (Formspree, free)

1. Go to [formspree.io](https://formspree.io) and sign up with **trishamador@gmail.com**. Confirm the email Formspree sends you.
2. Create a new form (name it "Free estimate").
3. Copy its endpoint, which looks like `https://formspree.io/f/abcdwxyz`.
4. Paste it into `formEndpoint` in `main.js`. Each request (project type, name, phone, details) then arrives in your inbox.

The form is connected to `https://formspree.io/f/xvkgblbq`.

## Still to add

- **Reviews:** replace the three dashed placeholder cards in the `REVIEWS` section of `index.html`.
- **Photos:** to add a service card (e.g. Plumbing) once you have a photo, copy one of the `<article class="svc">` blocks in `index.html` and change the image and text. Put images in `assets/img/`.

## Files

- `index.html`: page content
- `styles.css`: design (brand colours are at the top as CSS variables)
- `main.js`: settings, estimate form, menu, video
- `assets/img`, `assets/video`: logo, project photos and video (optimised WebP / MP4)
