"""Inject the language switcher + translations into a board HTML file (template or built index). Idempotent."""
import json, re, sys
import os; HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from dict import R, GLOSS

LANGS = ['es', 'fr', 'th']
def parse(block, check=True):
    out = {l: {} for l in LANGS}
    for line in block.strip().splitlines():
        if not line.strip(): continue
        parts = line.split('|')
        assert len(parts) == 4, line
        en = parts[0]
        ph = sorted(re.findall(r'\{\d+\}', en))
        for l, v in zip(LANGS, parts[1:]):
            if check: assert sorted(re.findall(r'\{\d+\}', v)) == ph, (l, line)
            out[l][en] = v
    return out

D, G = parse(R), parse(GLOSS)
ENGINE = open(os.path.join(HERE, 'engine.js'), encoding='utf-8').read()
ENGINE = ENGINE.replace('/*__I18N_DICT__*/{}', json.dumps(D, ensure_ascii=False, separators=(',', ':')))
ENGINE = ENGINE.replace('/*__I18N_GLOSS__*/{}', json.dumps(G, ensure_ascii=False, separators=(',', ':')))
BLOCK = '<script id="i18n">\n' + ENGINE + '</script>\n'

CSS = """/* language switcher */
.lang { position: relative; display: inline-flex; align-items: center; }
.lang select { appearance: none; -webkit-appearance: none; background: var(--panel); border: 1px solid var(--line-strong); border-radius: 6px; padding: 5px 24px 5px 28px; font-size: 13px; color: var(--fg); cursor: pointer; }
.lang select:focus-visible { outline: 2px solid var(--accent); outline-offset: 1px; }
.lang svg { position: absolute; left: 8px; width: 14px; height: 14px; pointer-events: none; color: var(--fg-2); }
.lang::after { content: "▾"; position: absolute; right: 8px; font-size: 10px; color: var(--fg-3); pointer-events: none; }
.lang option { color: var(--fg); background: var(--panel); }
@media (max-width: 720px) { .lang select { width: 34px; padding: 5px 0 5px 0; color: transparent; } .lang svg { left: 10px; } .lang::after { display: none; } }
:lang(th) h1, :lang(th) h2, :lang(th) h3, :lang(th) .eyebrow, :lang(th) .tab, :lang(th) .crest .sub { letter-spacing: 0; }
:lang(th) body { font-family: "IBM Plex Sans", "Noto Sans Thai", "Leelawadee UI", "Thonburi", system-ui, sans-serif; }
"""
SWITCH = ('<label class="lang" title="Language"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true">'
          '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/></svg>'
          '<select id="lang" aria-label="Language"><option value="en">English</option></select></label>')

def apply(path):
    s = open(path, encoding='utf-8').read()
    # 1. script block (replace if present)
    if '<script id="i18n">' in s:
        s = re.sub(r'<script id="i18n">\n.*?</script>\n', lambda m: BLOCK, s, count=1, flags=re.S)
    else:
        anchor = '<script>\n'
        i = s.index(anchor, s.index('id="rivdata"'))
        s = s[:i] + BLOCK + s[i:]
    # 2. CSS
    if '/* language switcher */' in s:
        s = re.sub(r'/\* language switcher \*/\n.*?(?=</style>)', lambda m: CSS, s, count=1, flags=re.S)
    else:
        s = s.replace('</style>', CSS + '</style>', 1)
    # 3. switcher markup at the far right of the top bar
    if 'id="lang"' not in s.split('<script')[0]:
        old = '<button class="btn" id="theme" title="Light / dark">◐</button>'
        assert s.count(old) == 1
        s = s.replace(old, old + '\n    ' + SWITCH)
    # 4. Thai font
    if 'Noto+Sans+Thai' not in s:
        s = s.replace('family=IBM+Plex+Mono:wght@500', 'family=IBM+Plex+Mono:wght@500&family=Noto+Sans+Thai:wght@400;500;600', 1)
    # 5. sorting reads header text: use the English source
    s = s.replace("rankish = /^#$|rank/i.test(h.textContent.trim())", "rankish = /^#$|rank/i.test((window.I18N ? I18N.src(h) : h.textContent).trim())")
    open(path, 'w', encoding='utf-8').write(s)
    print(path, 'ok', len(s))

if __name__ == '__main__':
    for p in sys.argv[1:]: apply(p)
