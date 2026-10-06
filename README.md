# JTB 293 Alliance Board

Read-only dashboard for the JTB alliance (Last Z: Survival Shooter, server 293): leadership, roster strength, Canyon Clash teams, trends and rules.

**Strength measure.** Since 2026-10-05 the board ranks members and balances Canyon teams on **arena power**, following the "Starters chosen by" cell (Canyon Teams `C9`) in the tracker. The page reads `meta.by` and switches with the sheet, so changing that cell back to *Hero + vehicle* changes the board on the next export. Growth charts (trends, movers, the alliance line) stay on hero + mod vehicle power, which is the only measure with history before 2026-10-05.

`index.html` is generated from the JTB 293 Power Tracker after each weekly roster capture. Do not edit it by hand; it is overwritten on the next publish.

## Layout
- `index.html` - the published board (generated; do not edit).
- `board_template.html` - the page source; `/*__DATA__*/`, `/*__READONLY__*/`, `/*__TITLE__*/` and `/*__API_URL__*/` are filled in by `build_board.py` (kept with the private data store).
- `worker/` - the Cloudflare Worker that takes availability / slot changes from the page and hands them to the tracker's Apps Script; `node worker/test.mjs` runs its unit tests, `worker/e2e.mjs` drives the page against it with Playwright.

## How the team split works
One-session voters are placed first, then members who can make either session, each group strongest first on the chosen measure. Only the top `C7` starters per team count toward the balance - subs never do. A member who could play either side goes where they would make the starting lineup, then to the team with the weaker starters, and finally to the team with fewer players. The page mirrors that rule in `recompute()` so an edit previews instantly; the sheet's `W17` array formula is the source of truth.
