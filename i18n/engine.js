// ---------- i18n: English / Español / Français / ไทย
// Works on the rendered page: every text node, placeholder, title and aria-label is looked up in the
// dictionary below after numbers and dates are swapped for {0}, {1}… placeholders. Player and alliance
// names are never translated. Copied text (Discord posts, lineups) stays English on purpose.
window.I18N = (() => {
  const LANGS = [['en','English'], ['es','Español'], ['fr','Français'], ['th','ไทย']];
  const LOC = { en: 'en-US', es: 'es-ES', fr: 'fr-FR', th: 'th-TH' };
  const D = /*__I18N_DICT__*/{};
  const G = /*__I18N_GLOSS__*/{};
  const ok = l => LANGS.some(x => x[0] === l);
  let saved = null; try { saved = localStorage.getItem('jtb-lang'); } catch (e) {}
  const sys = () => { for (const l of (navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || 'en'])) { const b = String(l).toLowerCase().split(/[-_]/)[0]; if (ok(b)) return b; } return 'en'; };
  let lang = ok(saved) ? saved : sys();

  const MON = 'Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec', WD = 'Mon|Tue|Wed|Thu|Fri|Sat|Sun';
  const TOK = new RegExp([
    `(?:(?:${WD}), )?(?:${MON}) \\d{1,2}(?:, \\d{4})?(?!\\d)`,
    `\\d{1,2} (?:${MON}) \\d{4}`,
    `\\d{4}-\\d{2}-\\d{2}(?: \\d{2}:\\d{2}(?:[–-]\\d{2}:\\d{2})?(?: [A-Za-z]{2,4})?)?`,
    `(?<![\\w.])[~+\\-−]?\\d+(?:,\\d{3})*(?:\\.\\d+)?(?::\\d{2})?[KMB%]?(?![\\w])`
  ].join('|'), 'g');
  const MI = MON.split('|');
  const fmtTok = t => { // en-US dates → the chosen language; numbers and ISO stamps unchanged
    let m = t.match(new RegExp(`^(?:(${WD}), )?(${MON}) (\\d{1,2})(?:, (\\d{4}))?$`)) || null, y, mo, d, wd;
    if (m) { wd = !!m[1]; mo = MI.indexOf(m[2]); d = +m[3]; y = m[4] ? +m[4] : null; }
    else if ((m = t.match(new RegExp(`^(\\d{1,2}) (${MON}) (\\d{4})$`)))) { d = +m[1]; mo = MI.indexOf(m[2]); y = +m[3]; }
    else return t;
    const dt = new Date(y || new Date().getFullYear(), mo, d, 12);
    const o = { month: 'short', day: 'numeric' }; if (y) o.year = 'numeric'; if (wd) o.weekday = 'short';
    try { return dt.toLocaleDateString(LOC[lang], o); } catch (e) { return t; }
  };
  const NAMES = new Set();
  try {
    const walk = v => { if (Array.isArray(v)) v.forEach(walk); else if (v && typeof v === 'object') { for (const k in v) { if (k === 'name' && typeof v[k] === 'string') NAMES.add(v[k]); else walk(v[k]); } } };
    const j = id => { const e = document.getElementById(id); try { return e ? JSON.parse(e.textContent) : null; } catch (x) { return null; } };
    walk(j('data'));
    const cd = j('cddata'); if (cd) { (cd.cd || []).forEach(r => { NAMES.add(r[1]); NAMES.add(r[3]); }); (cd.alliances || []).forEach(r => NAMES.add(r[2])); }
    const rv = j('rivdata'); if (rv) (rv.players || []).forEach(r => NAMES.add(r[2]));
  } catch (e) {}
  const PAT = {}; for (const l in D) PAT[l] = Object.keys(D[l]).filter(k => k.includes('{*}')).map(k => [new RegExp('^' + k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&').replace(/\\\{\\\*\\\}/g, '(.+?)') + '$'), D[l][k]]);
  const gKeys = Object.keys(G).sort((a, b) => b.length - a.length);
  const gRe = gKeys.length ? new RegExp('(?<![\\p{L}\\d])(' + gKeys.map(k => k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|') + ')(?![\\p{L}\\d])', 'gu') : null;
  const one = s => { // s is trimmed
    const dl = D[lang]; if (!dl) return null;
    if (dl[s] != null) return dl[s];
    const toks = []; const k = s.replace(TOK, m => { toks.push(m); return '{' + (toks.length - 1) + '}'; });
    const fill = v => v.replace(/\{(\d+)\}/g, (_, i) => toks[+i] != null ? fmtTok(toks[+i]) : '');
    if (dl[k] != null) return fill(dl[k]);
    if (!/\p{L}/u.test(k)) return toks.length ? fill(k) : null; // bare dates / numbers (chart axes)
    for (const [re, v] of (PAT[lang] || [])) { const m = k.match(re); if (m) { let i = 1; return fill(v.replace(/\{\*\}/g, () => m[i++])); } } // keys with a free-text {*} slot (names)
    if (gRe && G[lang] !== undefined) { // whole string made only of glossary words, numbers and punctuation
      const out = k.replace(gRe, w => '\u0001' + w + '\u0002');
      if (!/\p{L}/u.test(out.replace(/\u0001[^\u0002]*\u0002/g, '').replace(/\{\d+\}/g, '')) && out.includes('\u0001'))
        return fill(out.replace(/\u0001([^\u0002]*)\u0002/g, (_, w) => (G[lang][w] ?? w)));
    }
    return null;
  };
  const tr = raw => {
    if (lang === 'en' || !raw) return raw;
    const s = raw.replace(/\s+/g, ' ').trim();
    if (!s || !/\p{L}/u.test(s) || NAMES.has(s)) return raw;
    let v = one(s);
    if (v == null) { const m = s.match(/^((?:· )?)(.*?)((?: ·)?)$/); if (m && (m[1] || m[3]) && m[2]) { const t = one(m[2]); if (t != null) v = m[1] + t + m[3]; } }
    if (v == null && s.includes(' · ')) { let hit = false; v = s.split(' · ').map(p => { if (NAMES.has(p)) return p; const t = one(p); if (t != null) { hit = true; return t; } return p; }).join(' · '); if (!hit) v = null; }
    if (v == null) return raw;
    const lead = raw.match(/^\s*/)[0], trail = raw.match(/\s*$/)[0];
    return (lead ? ' ' : '') + v + (trail ? ' ' : '');
  };

  // ---- DOM layer: remember each node's English source so switching language is instant and lossless
  const SRC = new WeakMap(), OUT = new WeakMap(), ASRC = new WeakMap(), ATTRS = ['placeholder', 'title', 'aria-label'];
  const skip = el => !el || el.closest('script,style,textarea,[translate="no"],#lang');
  const doText = n => {
    const cur = n.nodeValue;
    if (OUT.get(n) !== cur) SRC.set(n, cur);            // new English text written by the app
    if (skip(n.parentElement)) return;
    const v = tr(SRC.get(n)); if (v !== cur) n.nodeValue = v; OUT.set(n, n.nodeValue);
  };
  const doAttrs = el => {
    if (skip(el)) return; let m = ASRC.get(el);
    for (const a of ATTRS) { if (!el.hasAttribute(a)) continue; const cur = el.getAttribute(a); if (!m) ASRC.set(el, m = {});
      if (!m[a] || m[a][1] !== cur) m[a] = [cur, cur];
      const v = tr(m[a][0]); if (v !== cur) el.setAttribute(a, v); m[a][1] = el.getAttribute(a); }
  };
  const walk = root => {
    if (root.nodeType === 3) return doText(root);
    if (root.nodeType !== 1) return;
    doAttrs(root); root.querySelectorAll && root.querySelectorAll('[placeholder],[title],[aria-label]').forEach(doAttrs);
    const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT); let n; while ((n = w.nextNode())) doText(n);
  };
  const mo = new MutationObserver(list => { for (const r of list) {
    if (r.type === 'characterData') doText(r.target);
    else if (r.type === 'attributes') doAttrs(r.target);
    else r.addedNodes.forEach(walk);
  } });
  const start = () => { walk(document.body); mo.observe(document.body, { subtree: true, childList: true, characterData: true, attributes: true, attributeFilter: ATTRS }); };
  const setLang = l => {
    if (!ok(l)) return; lang = l; try { localStorage.setItem('jtb-lang', l); } catch (e) {}
    document.documentElement.lang = l; const s = document.getElementById('lang'); if (s) s.value = l;
    walk(document.body);
  };
  // English text of an element as the app wrote it (sorting logic reads headers)
  const src = el => { let t = ''; const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT); let n; while ((n = w.nextNode())) t += SRC.has(n) ? SRC.get(n) : n.nodeValue; return t; };
  const t = s => { const v = tr(String(s)); return v; };
  for (const f of ['confirm', 'alert', 'prompt']) { const orig = window[f]; if (orig) window[f] = (m, ...r) => orig.call(window, t(m), ...r); }
  // switcher in the top bar
  const sel = document.getElementById('lang');
  if (sel) { sel.innerHTML = LANGS.map(([k, n]) => `<option value="${k}">${n}</option>`).join(''); sel.value = lang; sel.onchange = e => setLang(e.target.value); }
  document.documentElement.lang = lang;
  start();
  return { t, src, set: setLang, get lang() { return lang; }, langs: LANGS.map(x => x[0]) };
})();
