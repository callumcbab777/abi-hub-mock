# ABI Group hub: MOCK site (local working draft)

Static HTML/CSS/JS with no backend. Open `index.html`, or run `python3 -m http.server --directory /workspace/abi-hub-mock 8080`.
Pages are generated from `build.py`. Edit content there and run `python3 build.py`. The output is plain HTML.
Not published. `noindex,nofollow` and `robots.txt` (Disallow: /) are already in place for any future preview.

- Tokens and fonts: `assets/css/site.css` (`:root`). Free Google fonts, self-hosted: Montserrat (headings, nav, buttons, labels), Newsreader (body), Inter fallback. See `assets/fonts/README.md`.
- AMBAR theme: `.theme-ambar` (AMBAR page content) plus `.card-ambar` and `.ambar-accent` use the AMBAR green and gold from the ambar-orlando-market-analysis styles.css.
- Interactions: `assets/js/site.js` (currency toggle with example rates, Isla script, 3D viewer sample data, floor plans, modal, mock notes).
- Logo variants: `assets/img/` (logo-navy / logo-gold / logo-stone as .svg and .png, logo-mark.svg uses currentColor, logo-original.png, favicon.svg/.ico/-32/-512, apple-touch-icon).
- Mock notes: the "Phase N · notes" pill at bottom-left (or Alt+N) shows each page's phase, purpose, components and data from the build plan.
