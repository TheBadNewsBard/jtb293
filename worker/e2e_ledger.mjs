// Drives the Canyon "Lock in results" flow and the Trends -> Canyon trends view against the Worker (in-memory KV).
// DATA = a board_data.json; SHOTS = a folder for screenshots (optional).
import http from 'node:http'; import fs from 'node:fs'; import { chromium } from 'playwright';
import w from './worker.js';
const kv = new Map();
const BOARD = { get: async (k, t) => { const v = kv.get(k); return v === undefined ? null : (t === 'json' ? JSON.parse(v) : v); }, put: async (k, v) => { kv.set(k, v); }, delete: async k => { kv.delete(k); }, list: async ({ prefix }) => ({ keys: [...kv.keys()].filter(k => k.startsWith(prefix)).map(name => ({ name })) }) };
const env = { BOARD, SYNC_KEY: 'sync', OFFICER_CODE: 'off123', MEMBER_CODE: 'mem456' };
const data = JSON.parse(fs.readFileSync(process.env.DATA || '../data.json', 'utf8'));
data.meta.t1 = '23:00 session'; data.meta.t2 = '18:00 session';            // Team 1 = 23:00 since 2026-10-21
// JTB IDs as the sheet exports them: one per member, plus a member who renamed and a merged-away ID
const PID = {}; let pn = 0; data.history.forEach(h => { h.pid = PID[h.name] ||= 'J' + String(++pn).padStart(4, '0'); });
const RENAMED = data.canyon.find(c => /^T1 Starter/.test(c.final)).name, OLDNAME = RENAMED + ' (old)';
data.ids = Object.entries(PID).map(([n, id]) => [id, '', n, 'member', '', n === RENAMED ? OLDNAME : '']).concat([['J0999', '', '', 'merged', PID[RENAMED], '']]);
kv.set('data', JSON.stringify(data));
const SH = process.env.SHOTS;
const page = fs.readFileSync(process.env.PAGE || '../index.html', 'utf8').replace(/API_URL = '[^']*'/, "API_URL = 'http://127.0.0.1:8789'");
const srv = http.createServer(async (req, res) => {
  if (req.url === '/page') { res.setHeader('Content-Type', 'text/html'); return res.end(page); }
  let body = ''; for await (const c of req) body += c;
  const r = await w.fetch(new Request('http://127.0.0.1:8789' + req.url, { method: req.method, headers: req.headers, body: ['GET','HEAD','OPTIONS'].includes(req.method) ? undefined : body }), env);
  res.writeHead(r.status, Object.fromEntries(r.headers)); res.end(await r.text());
}).listen(8789);
let fails = 0; const ok = (c, m) => { if (!c) { fails++; console.log('FAIL', m); } else console.log('ok  ', m); };
// two earlier Fridays straight into the ledger (as the sync key would), so the trends have history
const uid = n => String((data.history.filter(h => h.name === n).pop() || {}).uid || '');
const pidN = n => PID[n] || '';
const names = [...new Set(data.canyon.filter(c => /^T[12] /.test(c.final)).map(c => c.name))];
const past = (date, res1, res2, miss) => ({ date, measure: 'Arena power', teams: [{ team: 'T1', session: '23:00', oppServer: '301', oppAlliance: 'WAR', oppPower: 7.4e9, score: res1 === 'W' ? 1500 : 900, oppScore: 1100, result: res1, ourPower: 6.9e9 }, { team: 'T2', session: '18:00', oppServer: '288', oppAlliance: 'KOR', oppPower: 4.1e9, score: res2 === 'W' ? 1300 : 700, oppScore: 1000, result: res2, ourPower: 4.9e9 }],
  players: names.slice(0, 50).map((n, i) => ({ pid: pidN(n), uid: uid(n), name: n, team: i % 2 ? 'T2' : 'T1', role: i < 40 ? 'Starter' : 'Sub', status: i < 40 ? (miss.includes(i) ? 'no-show' : 'show') : (i === 41 ? 'played' : 'not-needed'), points: i < 40 ? 1000 - i * 10 : null })) });
const e09 = past('2026-10-09', 'W', 'L', [3, 7]), e16 = past('2026-10-16', 'L', 'W', [3]);
// on Oct 9 the renamed member was locked under the old name with a merged-away ID; on Oct 16 by name only, no ID
const r09 = e09.players.find(p => p.name === RENAMED); if (r09) { r09.name = OLDNAME; r09.pid = 'J0999'; }
const r16 = e16.players.find(p => p.name === RENAMED); if (r16) { r16.name = OLDNAME; r16.pid = ''; r16.uid = ''; }
for (const ev of [e09, e16]) {
  const r = await w.fetch(new Request('http://x/ledger', { method: 'POST', headers: { 'X-Sync-Key': 'sync' }, body: JSON.stringify({ event: ev }) }), env); ok(r.status === 200, 'seed ' + ev.date);
}
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--headless=new'] });
const p = await b.newPage({ viewport: { width: 1280, height: 1000 } }); const errs = []; p.on('pageerror', e => errs.push(e.message));
await p.goto('http://127.0.0.1:8789/page'); await p.waitForTimeout(1500);
await p.click('.tab[data-view=canyon]'); await p.waitForTimeout(300);
const legend = await p.textContent('#view-canyon .legend');
ok(/^23:00 only/.test(legend.trim()) && (await p.textContent('#view-canyon .gap')).includes('Team 1 · 23:00'), 'Team 1 = 23:00 on the Canyon tab: ' + legend.slice(0, 40));
ok((await p.textContent('#view-canyon')).includes('Last locked: Oct 16'), 'last lock note');
await p.click('#lock-open'); await p.waitForTimeout(300);
ok(await p.inputValue('#lk-date') === '2026-10-16', 'date defaults to the last Friday (Oct 16 is locked -> edit mode)');
await p.fill('#lk-date', '2026-10-23'); await p.dispatchEvent('#lk-date', 'change'); await p.waitForTimeout(300);
const nPl = await p.$$eval('#lockbox [data-lk]', a => a.length);
ok(nPl > 0 && (await p.textContent('#lk-go')).includes('Lock in ' + nPl), 'fresh roster from the lineup: ' + nPl);
// mark: first T1 starter no-show, first T1 sub played; scores T1 1200-1000 -> W auto
const t1 = await p.$$('#lockbox .lteam.t1 [data-lk]');
await t1[0].click(); await p.waitForTimeout(150);
const subChip = await p.$$('#lockbox .lteam.t1 .lgrid:last-of-type [data-lk]'); if (subChip.length) { await subChip[0].click(); await p.waitForTimeout(150); }
await p.fill('[data-tf="T1:oppServer"]', '305'); await p.dispatchEvent('[data-tf="T1:oppServer"]', 'change');
await p.fill('[data-tf="T1:oppPower"]', '7.25B'); await p.dispatchEvent('[data-tf="T1:oppPower"]', 'change');
await p.fill('[data-tf="T1:score"]', '1200'); await p.dispatchEvent('[data-tf="T1:score"]', 'change');
await p.fill('[data-tf="T1:oppScore"]', '1,000'); await p.dispatchEvent('[data-tf="T1:oppScore"]', 'change'); await p.waitForTimeout(200);
ok(await p.inputValue('[data-tf="T1:result"]') === 'W', 'result follows the scores');
if (SH) await p.screenshot({ path: SH + '/lock.png', fullPage: false, clip: await p.$eval('#lockbox', e => { const r = e.getBoundingClientRect(); return { x: r.x, y: Math.max(0, r.y), width: r.width, height: Math.min(900, r.height) }; }) });
await p.fill('#lk-code', 'mem456'); await p.click('#lk-go'); await p.waitForTimeout(500);
ok((await p.textContent('#toast')).includes('officer code'), 'member code refused');
await p.fill('#lk-code', 'off123'); await p.fill('#lk-by', 'Joe'); await p.click('#lk-go'); await p.waitForTimeout(1200);
const L = JSON.parse(kv.get('ledger')), e = L.events.find(x => x.date === '2026-10-23');
ok(e && e.players.length === nPl && e.teams.find(t => t.team === 'T1').result === 'W' && e.teams.find(t => t.team === 'T1').oppPower === 7.25e9 && e.lockedBy === 'Joe', 'locked into the ledger');
ok(e.players.filter(x => x.team === 'T1' && x.role === 'Starter' && x.status === 'no-show').length === 1 && e.players.every(x => x.role === 'Starter' ? ['show','no-show'].includes(x.status) : ['played','not-needed'].includes(x.status)), 'chips saved');
const known = e.players.filter(x => uid(x.name)); ok(known.length > 0 && known.every(x => x.uid === uid(x.name)), 'players with a UID on file carry it (' + known.length + '/' + nPl + ')');
ok(e.players.every(x => x.pid && x.pid === PID[x.name]), 'every locked player carries their JTB ID');
ok(e.teams.every(t => ['23:00', '18:00'].includes(t.session)) && e.teams.find(t => t.team === 'T1').session === '23:00', 'sessions stored with each team');
ok(!(await p.isVisible('#lockbox')), 'panel closed after lock');
// Trends -> Canyon trends
await p.click('.tab[data-view=trends]'); await p.click('[data-tsub=canyon]'); await p.waitForTimeout(400);
const tiles = await p.$$eval('#ct-host .tile .big', a => a.map(x => x.textContent));
ok(tiles[0] === '3', 'canyons played = 3: ' + tiles.join(' | '));
const rows = await p.$$eval('#ct-host table[data-skey=ctp] tbody tr', a => a.length);
ok(rows > 40, 'player rows ' + rows);
const rr = await p.$$eval('#ct-host table[data-skey=ctp] tbody tr', (a, nm) => a.filter(tr => tr.cells[0].textContent.includes(nm)).map(tr => tr.cells[0].textContent + '|' + tr.cells[1].textContent), RENAMED);
ok(rr.length === 1 && rr[0].endsWith('|3') && rr[0].includes(PID[RENAMED]), 'renamed member (old name + merged ID + name-only row) is one row of 3 under the current name: ' + JSON.stringify(rr));
ok(!(await p.textContent('#ct-host table[data-skey=ctp]')).includes(OLDNAME + '\u00a0') && !(await p.$$eval('#ct-host table[data-skey=ctp] tbody tr', (a, o) => a.some(tr => tr.cells[0].textContent.trim().startsWith(o)), OLDNAME)), 'old name has no row of its own');
if (SH) await p.screenshot({ path: SH + '/trends.png', fullPage: true });
await p.selectOption('#ct-sess', '23:00'); await p.waitForTimeout(200);
ok((await p.textContent('#ct-host .tile:nth-of-type(2) .big')) !== '', 'session slice renders');
await p.selectOption('#ct-range', '4'); await p.selectOption('#ct-role', 'Starter'); await p.waitForTimeout(200);
// sort by no-show rate
await p.click('#ct-host table[data-skey=ctp] th:nth-child(7)'); await p.waitForTimeout(100);
// edit a Friday from the log
await p.selectOption('#ct-sess', 'all'); await p.waitForTimeout(150);
await p.click('[data-edit-ev="2026-10-09"]'); await p.waitForTimeout(400);
ok(current() && (await p.inputValue('#lk-date')) === '2026-10-09' && (await p.textContent('#lk-go')).includes('Save changes'), 'edit opens the locked roster');
function current(){ return true; }
// member drawer shows the canyon record
await p.click('#lk-cancel'); await p.waitForTimeout(150);
await p.click('.nudge [data-member], .slot [data-member]'); await p.waitForTimeout(300);
ok((await p.textContent('#drawer')).includes('Canyon record'), 'member drawer: canyon record');
ok(/JTB ID\s*J\d{4}/.test(await p.textContent('#drawer')), 'member drawer shows the JTB ID');
await p.keyboard.press('Escape'); await p.evaluate(n => document.querySelector('[data-member]') && 0, 0);
await p.evaluate(n => { const el = document.createElement('span'); el.dataset.member = n; el.id = 'probe'; el.textContent = 'x'; document.body.appendChild(el); el.click(); }, RENAMED); await p.waitForTimeout(300);
const dr = await p.textContent('#drawer'); ok(dr.includes('was ' + OLDNAME) && /Canyon record · 3 rostered/.test(dr), 'renamed member drawer: was-name + full record');
if (SH) await p.screenshot({ path: SH + '/drawer.png', clip: await p.$eval('#drawer-card', e => { const r = e.getBoundingClientRect(); return { x: r.x, y: r.y, width: r.width, height: Math.min(1000, r.height) }; }) });
// phone width
await p.setViewportSize({ width: 390, height: 900 }); await p.keyboard.press('Escape'); await p.click('.tab[data-view=trends]'); await p.waitForTimeout(300);
const over = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
ok(over <= 1, 'no sideways scroll on a phone (' + over + 'px)');
if (SH) await p.screenshot({ path: SH + '/phone.png', fullPage: false });
ok(!errs.length, 'no page errors ' + errs.join(' | '));
await b.close(); srv.close();
console.log(fails ? fails + ' FAILURES' : 'LEDGER E2E PASSED');
