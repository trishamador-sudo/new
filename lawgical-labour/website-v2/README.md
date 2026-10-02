# Lawgical Labour: website version 2

A light, editorial alternative to `../website/` (the scroll-video version), inspired by the layout of bloomlegalcoach.com and built in Lawgical Labour's own brand (`../copy/brand-kit.md`): Lawgical Navy, Quill Turquoise, white, and Manrope throughout.

Built with **Vite + vanilla JavaScript**, **GSAP ScrollTrigger** (gentle reveals and arch parallax) and **Lenis** (smooth scroll). No background video.

## Run it locally

You need [Node.js](https://nodejs.org) 18 or newer.

```bash
cd lawgical-labour/website-v2
npm install
npm run dev
```

## Build for hosting

```bash
npm run build -- --base=./
```

Upload the **contents** of `dist/` to Cloudflare Pages (or any static host). Preview the build with `npx serve dist`.

## Edit contact details and the form

Open `src/main.js`. At the top is `SITE`: phone, WhatsApp number and message, email and `formEndpoint` (paste a Formspree URL to receive consultation requests by email; until then the form opens the visitor's email app).

Working hours and the address line are written in `index.html` (top bar, contact tiles, footer).

## Sections

Top bar → Nav → Hero (overlapping arch photos, "Prevent. Protect. Resolve.", slogan) → Intro + consultation form → At a glance → Services slider → Meet Louise (pill portrait, vertical name) → Qualifications band → Why choose us → Testimonials (placeholder) → Blog slider over a full-width image → Every way to reach us → Footer (contact box, hours, banking-details fraud warning).

## Files

- `index.html`: all markup, icons and the line-drawn feather (`#feather` symbol)
- `src/style.css`: brand tokens and all styles
- `src/main.js`: settings, smooth scroll, services slider, blog slider, reveals, form
- `public/img/`: logo, Louise's headshot and photos cut from the brand video
