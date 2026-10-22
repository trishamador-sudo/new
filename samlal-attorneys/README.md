# Sahil Samlal Attorneys Inc.: website mock-up

This is a redesign mock-up based on the current site (samlalattorneys.com). It is a static multi-page site (HTML, CSS and a little JavaScript) in navy, grey and white, with the SAS monogram photo as the hero.

## Pages
| File | Page |
|---|---|
| `index.html` | Home: hero, quick-contact bar, 10 practice areas, director teaser, Anti-GBV pledge, how it works, areas of jurisdiction |
| `practice-areas.html` | Every practice area, each with its own booking and call buttons |
| `anti-gbv.html` | Anti-GBV pledge, commitments, legal services for GBV matters, our promise, emergency numbers |
| `about.html` | About the firm, full director profile, areas of jurisdiction |
| `contact.html` | Booking form (the same questions as the current site, plus type of matter and POPIA consent), contact details, directions, office hours |
| `404.html` | Not-found page |

## Calls to action
- "Book a consultation" in the header and in every page hero.
- Call and WhatsApp buttons in every page hero.
- A "Discuss your matter" link on every practice area. It opens the booking form with that area already selected.
- CTA bands between sections.
- A floating WhatsApp button on desktop.
- A Call / WhatsApp / Book bar fixed to the bottom of the screen on phones.

## Editing
Content lives in `build.py`. Run `python3 build.py` to rebuild every page, `sitemap.xml` and `robots.txt`.

**Booking form:** paste a Formspree URL into `formEndpoint` at the top of `main.js` to receive bookings by email. While it is empty (mock-up), the form shows a thank-you message without sending anything.

## To confirm with the firm
- WhatsApp is linked to the cell number 082 762 5716. Confirm that this number uses WhatsApp.
- On the current site the Criminal Litigation and Civil Litigation descriptions are swapped. They are corrected here.
- The GBV page adds emergency numbers: SAPS 10111 and the GBV Command Centre 0800 428 428.
- The domain is assumed to be `https://samlalattorneys.com`. Update `DOMAIN` in `build.py` if it differs.
- Images (hero, director photo and court map) were cropped from screenshots of the current site. Replace them with the original files for full quality.
