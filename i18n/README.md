# Board translations (English / Español / Français / ไทย)

- `dict.py` — phrase table, one line per string: `English|Spanish|French|Thai`. `{0}`, `{1}`… stand for numbers and dates (kept from the English text; dates are re-formatted per language). `{*}` is a free-text slot (e.g. a player name).
- `engine.js` — runs in the page: translates text, placeholders, titles and aria-labels as the board renders, defaults to the device language (else English) and remembers the pick from the top-right switcher.
- `apply.py` — injects both into a board file. Idempotent: `python3 i18n/apply.py board_template.html index.html`.

Anything not in the table stays English, so new UI text just needs a new line in `dict.py` and a re-run of `apply.py`. Copied Discord/lineup text stays English on purpose.
