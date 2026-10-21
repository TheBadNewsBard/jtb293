// Drives the page's "Clear all votes" flow against the Worker (in-memory KV) with Playwright.
import http from 'node:http'; import fs from 'node:fs'; import { chromium } from 'playwright';
import w from './worker.js';
const kv = new Map();
const BOARD = { get: async (k, t) => { const v = kv.get(k); return v === undefined ? null : (t === 'json' ? JSON.parse(v) : v); }, put: async (k, v) => { kv.set(k, v); }, delete: async k => { kv.delete(k); }, list: async ({ prefix }) => ({ keys: [...kv.keys()].filter(k => k.startsWith(prefix)).map(name => ({ name })) }) };
const env = { BOARD, SYNC_KEY: 'sync', OFFICER_CODE: 'off123', MEMBER_CODE: 'mem456' };
const data = JSON.parse(fs.readFileSync(process.env.DATA || '../data.json', 'utf8'));
kv.set('data', JSON.stringify(data));
const page = fs.readFileSync(process.env.PAGE || '../index.html', 'utf8').replace(/API_URL = '[^']*'/, "API_URL = 'http://127.0.0.1:8788'");
const srv = http.createServer(async (req, res) => {
  if (req.url === '/page') { res.setHeader('Content-Type', 'text/html'); return res.end(page); }
  let body = ''; for await (const c of req) body += c;
  const r = await w.fetch(new Request('http://127.0.0.1:8788' + req.url, { method: req.method, headers: req.headers, body: ['GET','HEAD','OPTIONS'].includes(req.method) ? undefined : body }), env);
  res.writeHead(r.status, Object.fromEntries(r.headers)); res.end(await r.text());
}).listen(8788);
let fails = 0; const ok = (c, m) => { if (!c) { fails++; console.log('FAIL', m); } else console.log('ok  ', m); };
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--headless=new'] });
const p = await b.newPage({ viewport: { width: 1200, height: 900 } }); const errs = []; p.on('pageerror', e => errs.push(e.message));
await p.goto('http://127.0.0.1:8788/page'); await p.waitForTimeout(1500);
await p.click('.tab[data-view=canyon]'); await p.waitForTimeout(300);
const voted = data.canyon.filter(c => c.avail).length;
ok(await p.isVisible('#clear-open'), 'Clear all votes button shown');
await p.click('#clear-open'); await p.waitForTimeout(200);
ok((await p.textContent('#clr-go')).includes('Clear ' + voted + ' votes'), 'button counts ' + voted + ' votes: ' + await p.textContent('#clr-go'));
await p.screenshot({ path: process.env.SHOT || 'clear.png', clip: await p.$eval('#clearbox', e => { const r = e.closest('.panel').getBoundingClientRect(); return { x: r.x, y: r.y, width: r.width, height: r.height }; }) });
await p.fill('#clr-code', 'mem456'); await p.click('#clr-go'); await p.waitForTimeout(500);
ok((await p.textContent('#toast')).includes('officer code') && (await BOARD.list({ prefix: 'edit:' })).keys.length === 0, 'member code refused: ' + await p.textContent('#toast'));
await p.fill('#clr-code', 'off123'); await p.fill('#clr-by', 'Joe'); await p.click('#clr-go'); await p.waitForTimeout(800);
const q = (await BOARD.list({ prefix: 'edit:' })).keys.map(k => JSON.parse(kv.get(k.name)));
ok(q.length === voted && q.every(e => e.avail === '' && e.slot === undefined && /Joe/.test(e.by)), 'queued ' + q.length + ' clears');
const legend = await p.textContent('#view-canyon .legend');
ok(legend.includes('No vote · ' + data.canyon.length), 'board shows everyone as No vote: ' + legend);
ok(!(await p.isVisible('#clearbox')), 'form closed'); ok(/syncing/.test(await p.textContent('#sync')), 'sync pill: ' + await p.textContent('#sync'));
// a member votes right after the reset; it must queue after the clears
await p.click('.nudge [data-member]'); await p.waitForTimeout(300);
const who = await p.$eval('#drawer [data-member], #drawer h2, #drawer h3', e => e.textContent).catch(() => '');
await p.selectOption('#ed-avail', 'Both'); await p.waitForTimeout(2500);
const q2 = (await w.fetch(new Request('http://x/edits', { headers: { 'X-Sync-Key': 'sync' } }), env).then(r => r.json())).edits;
ok(q2.length === voted + 1 && q2[q2.length - 1].avail === 'Both', 'new vote after the reset is last in the queue');
// sheet catches up: the export shows everyone cleared except the new vote -> pending drains
const fresh = JSON.parse(JSON.stringify(data)); fresh.generated = new Date().toISOString();
fresh.canyon.forEach(c => { c.avail = ''; }); const last = q2[q2.length - 1]; fresh.canyon.find(c => c.name === last.name).avail = 'Both';
kv.set('data', JSON.stringify(fresh)); await p.evaluate(() => document.dispatchEvent(new Event('visibilitychange'))); await p.waitForTimeout(800);
ok(/Live/.test(await p.textContent('#sync')), 'pending drained after the export: ' + await p.textContent('#sync'));
ok(!errs.length, 'no page errors ' + errs.join(' | '));
await b.close(); srv.close();
console.log(fails ? fails + ' FAILURES' : 'CLEAR E2E PASSED');
