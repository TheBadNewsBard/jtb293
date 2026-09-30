# JTB 293 Alliance Board

Read-only dashboard for the JTB alliance (Last Z: Survival Shooter, server 293): leadership, roster strength (hero + mod vehicle power), Canyon Clash teams, trends and rules.

`index.html` is generated from the JTB 293 Power Tracker after each weekly roster capture. Do not edit it by hand; it is overwritten on the next publish.

## Layout
- `index.html` - the published board (generated; do not edit).
- `board_template.html` - the page source; `/*__DATA__*/`, `/*__READONLY__*/`, `/*__TITLE__*/` and `/*__API_URL__*/` are filled in by `build_board.py` (kept with the private data store).
- `worker/` - the Cloudflare Worker that takes availability / slot changes from the page and hands them to the tracker's Apps Script; `node worker/test.mjs` runs its unit tests, `worker/e2e.mjs` drives the page against it with Playwright.
