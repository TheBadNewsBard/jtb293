# JTB 293 Alliance Board

Read-only dashboard for the JTB alliance (Last Z: Survival Shooter, server 293): leadership, roster strength, Canyon Clash teams, trends and rules.

**Strength measure.** Since 2026-10-05 the board ranks members and balances Canyon teams on **arena power**, following the "Starters chosen by" cell (Canyon Teams `C9`) in the tracker. The page reads `meta.by` and switches with the sheet, so changing that cell back to *Hero + vehicle* changes the board on the next export. Growth charts (trends, movers, the alliance line) stay on hero + mod vehicle power, which is the only measure with history before 2026-10-05.

`index.html` is generated from the JTB 293 Power Tracker after each weekly roster capture. Do not edit it by hand; it is overwritten on the next publish.

## Layout
- `index.html` - the published board (generated; do not edit).
- `board_template.html` - the page source; `/*__DATA__*/`, `/*__READONLY__*/`, `/*__TITLE__*/` and `/*__API_URL__*/` are filled in by `build_board.py` (kept with the private data store).
- `worker/` - the Cloudflare Worker (also `POST /clear`, behind the Canyon tab's officer-only **Clear all votes…** button) that takes availability / slot changes from the page and hands them to the tracker's Apps Script; `node worker/test.mjs` runs its unit tests, `worker/e2e.mjs`, `worker/e2e_clear.mjs` and `worker/e2e_ledger.mjs` drive the page against it with Playwright.

## Canyon Clash ledger
After Friday's Canyon an officer opens the Canyon tab, presses **Lock in results…**, sets each rostered player's chip
(starters Show / No-show, subs Not needed / Played), optionally types each team's opponent server, alliance, total
power, both scores and points, and locks it with the officer code. The Worker keeps the ledger (`GET/POST /ledger`);
the tracker mirrors it into its Canyon Ledger tabs. **Trends → Canyon trends** shows the record, attendance and per-player
stats; any Friday can be reopened from there and saved again. Players carry their in-game UID when the roster has one;
`POST /ledger/rename` carries a rename into the ledger for members without one.

Definitions: *played* = a starter who showed or a sub who played; *no-show rate* = no-shows ÷ starts; a player's W–L only
counts matches they played; each team (Team 1 = 23:00, Team 2 = 18:00, from Canyon Teams C4/C6) has its own opponent.

## How the team split works
One-session voters are placed first, then members who can make either session, each group strongest first on the chosen measure. Only the top `C7` starters per team count toward the balance - subs never do. A member who could play either side goes where they would make the starting lineup, then to the team with the weaker starters, and finally to the team with fewer players. The page mirrors that rule in `recompute()` so an edit previews instantly; the sheet's `W17` array formula is the source of truth.
