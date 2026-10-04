# Lawgical Labour: scroll-driven website

A single-page, scroll-driven site for Lawgical Labour, built with **Vite + vanilla JavaScript**, **GSAP ScrollTrigger** and **Lenis**. The Higgsfield-generated video is a fixed full-screen background that scrubs frame by frame as you scroll; the content scrolls over it on navy glass panels.

Built from `../copy/brand-kit.md` following the project skill `.claude/skills/BRAND-landing/SKILL.md`.

## Run it locally

You need [Node.js](https://nodejs.org) 18 or newer.

```bash
cd lawgical-labour/website
npm install
npm run dev
```

Open the address Vite prints (usually http://localhost:5173).

## Build for hosting

```bash
npm run build -- --base=./
```

This creates `dist/`. Upload the **contents** of `dist/` to Cloudflare Pages (or any static host).

Preview the build over HTTP (not by double-clicking the file):

```bash
npx serve dist
```

## Edit contact details

Open `src/main.js`. At the top is `SITE`: phone, WhatsApp number and pre-filled messages, the public email (specialist@), area, `formEndpoint` and `formEmail` (louise@, where consultation requests go).

**Consultation form:** create a form at [formspree.io](https://formspree.io) that delivers to **louise@lawgical.co.za**, paste its endpoint into `formEndpoint`, and requests arrive by email. Until then, the form opens the visitor's email app addressed to `louise@lawgical.co.za`.

Working hours (Mon–Thu 08:00–16:00, Fri 08:00–15:00) are written in `index.html` (At a glance, Every way to reach us, footer).

## Swap the background video

From the `lawgical-labour` folder:

```bash
scripts/swap-bg-video.sh assets/videos/<new-video>.mp4
```

This re-encodes it to all-keyframe H.264 (needed for smooth scrubbing), removes audio, and writes `website/public/bg.mp4` plus a poster frame at `website/public/img/poster.jpg`. Requires `ffmpeg`.

## How it works

| Layer | What |
|---|---|
| `#bgv` (z 0) | Fixed video, `currentTime` mapped to scroll progress |
| `.bg-tint` (z 1) | Navy gradient for text readability |
| `#page` (z 10) | Sections, on navy glass panels |

- **Video scrub:** `scrubVideo()` in `src/main.js`. The video slows during the pinned section so its three phases (still life → close-up → workspace) line up with the page story.
- **Pinned section:** the promise statement (word-by-word reveal).
- **Phones and reduced motion:** the video is replaced by a still poster, pins are switched off and the cards stack.

## Sections

Hero → Our promise → Services (disputes) → Services (prevention) → Every detail → Meet Louise → How it works & at a glance → Blog (labour law updates) → Book a consultation & every way to reach us → Footer (with banking-details fraud warning and POPIA note).

## Files

- `index.html`: all section markup and the Google Fonts link (Manrope)
- `src/main.js`: settings, Lenis, ScrollTrigger, video scrub, pins, reveals, form
- `src/style.css`: brand tokens, layout, sections, video layers
- `src/glass.css`: glass panels, buttons, chips
- `public/bg.mp4`: all-keyframe background video; `public/img/`: logo, headshot, poster, favicon

## Kamohelo's photo and bio
In `index.html`, find the `<!-- KAMOHELO -->` comment in the "Our team" section.
1. Add the photo as `public/img/kamohelo.webp` (portrait, about 900 px wide).
2. Swap the "K" placeholder for the `<img>` tag shown in the comment.
3. Replace "Kamohelo's profile is coming soon." with his bio, and add his surname to the heading.
4. Also update the `#kamohelo` Person in the JSON-LD schema in the `<head>`.

## SEO files
- `public/robots.txt` and `public/sitemap.xml` are copied next to `index.html` on build.
- The JSON-LD schema (LegalService, two people, WebSite, FAQPage) is in the `<head>` of `index.html`.
- All of them assume the domain **https://www.lawgical.co.za/**. Update it in those three places if it changes.
- If you change the FAQ text, update the FAQPage answers in the schema too.
