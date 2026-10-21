/**
 * JTB 293 board API - Cloudflare Worker.
 *
 * Bindings (set in the Cloudflare dashboard):
 *   KV namespace  BOARD          stores board data, pending edits and the change log
 *   Secret        SYNC_KEY       shared with the Apps Script project (pushes data, pulls + acks edits)
 *   Secret        OFFICER_CODE   passcode that may change any availability and any slot
 *   Secret        MEMBER_CODE    passcode that may change availability only
 *
 * Routes (all JSON, CORS open so the GitHub Pages site can call them):
 *   GET  /data                 current board_data.json (what the sheet last exported)
 *   POST /data                 X-Sync-Key   replace board data (Apps Script exportBoardData)
 *   POST /edit                 X-Code       {name, avail?, slot?, by?}  queue one change
 *   GET  /edits                X-Sync-Key   pending edits, oldest first
 *   POST /edits/ack            X-Sync-Key   {ids:[...]}  remove applied edits, move them to the log
 *   GET  /log                  last 200 applied changes (name, field, value, by, when)
 *   GET  /whoami               X-Code       {role: "officer" | "member"}  (lets the page check a code)
 *   POST /clear                X-Code (officer)  {slots?, by?}  start a new poll: queue "No vote" for every member
 *                              who has one (and "auto" for every manual slot when slots is true), and drop the vote
 *                              (and slot) part of any change still waiting, so last week's choices cannot land
 *                              after the reset. Votes sent after the reset queue behind it and win.
 */
const AVAIL = ['', '18:00 only', '23:00 only', 'Both', 'N/A'];
const MAX_PENDING = 300;   // queue cap (see /edit); the sheet drains the queue every minute
const SLOTS = ['auto', 'T1 Starter', 'T1 Sub', 'T2 Starter', 'T2 Sub', 'Bench', 'Not available'];
const CORS = { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET,POST,OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type,X-Code,X-Sync-Key', 'Access-Control-Max-Age': '86400' };
const json = (obj, status = 200, extra = {}) => new Response(JSON.stringify(obj), { status, headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', ...CORS, ...extra } });
const safeEq = (a, b) => { a = String(a || ''); b = String(b || ''); if (a.length !== b.length || !a.length) return false; let r = 0; for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i); return r === 0; };
const LEDGER_TEAMS = ['T1', 'T2'], ROLE_STATUS = { Starter: ['show', 'no-show'], Sub: ['played', 'not-needed'] };
const str = (v, n = 40) => v == null ? '' : String(v).trim().slice(0, n);
const numOrNull = v => { if (v === '' || v == null) return null; const n = Number(String(v).replace(/,/g, '')); return Number.isFinite(n) ? n : null; };
// Validate one Canyon event; returns [event, error]. Unknown fields are dropped so the KV value stays small and predictable.
function cleanEvent(e) {
  if (!e || typeof e !== 'object') return [null, 'event required'];
  const date = str(e.date, 10); if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) return [null, 'date must be YYYY-MM-DD'];
  const teams = [];
  for (const t of Array.isArray(e.teams) ? e.teams : []) {
    if (!LEDGER_TEAMS.includes(t.team)) return [null, 'bad team ' + t.team];
    const result = str(t.result, 1).toUpperCase();
    if (result && !['W', 'L', 'D'].includes(result)) return [null, 'result must be W, L or D'];
    teams.push({ team: t.team, session: str(t.session, 20), oppServer: str(t.oppServer, 10), oppAlliance: str(t.oppAlliance, 40),
      oppPower: numOrNull(t.oppPower), score: numOrNull(t.score), oppScore: numOrNull(t.oppScore), result, ourPower: numOrNull(t.ourPower), starters: numOrNull(t.starters) });
  }
  if (new Set(teams.map(t => t.team)).size !== teams.length) return [null, 'team listed twice'];
  const players = [], seen = new Set();
  for (const p of Array.isArray(e.players) ? e.players : []) {
    const name = str(p.name), uid = str(p.uid, 24), team = p.team, prole = p.role, status = p.status;
    if (!name) return [null, 'player name required'];
    if (!LEDGER_TEAMS.includes(team)) return [null, 'bad team for ' + name];
    if (!ROLE_STATUS[prole]) return [null, 'role must be Starter or Sub (' + name + ')'];
    if (!ROLE_STATUS[prole].includes(status)) return [null, 'bad status ' + status + ' for ' + prole + ' ' + name];
    const k = uid || 'name:' + name; if (seen.has(k)) return [null, name + ' listed twice']; seen.add(k);
    players.push({ uid, name, team, role: prole, status, points: numOrNull(p.points) });
  }
  if (players.length > 120) return [null, 'too many players'];
  return [{ date, measure: str(e.measure, 20), teams, players }, null];
}
function mergeEvent(old, inc) {
  const out = JSON.parse(JSON.stringify(old));
  for (const t of inc.teams || []) {
    let o = out.teams.find(x => x.team === t.team); if (!o) { o = { team: t.team }; out.teams.push(o); }
    for (const [k, v] of Object.entries(t)) if (v !== undefined && v !== null && v !== '') o[k] = v;
  }
  for (const p of inc.players || []) {
    const o = out.players.find(x => (p.uid && x.uid === p.uid) || (!p.uid && x.name === p.name));
    if (!o) continue;                              // merge never adds players: the locked roster stays as locked
    if (p.points !== undefined) o.points = numOrNull(p.points);
    if (p.status !== undefined && ROLE_STATUS[o.role].includes(p.status)) o.status = p.status;
  }
  return out;
}
const role = (env, code) => safeEq(code, env.OFFICER_CODE) ? 'officer' : safeEq(code, env.MEMBER_CODE) ? 'member' : null;

export default {
  async fetch(req, env) {
    const url = new URL(req.url), path = url.pathname.replace(/\/+$/, '') || '/';
    if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: CORS });
    try {
      if (path === '/data' && req.method === 'GET') {
        const body = await env.BOARD.get('data');
        return body ? new Response(body, { headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', ...CORS } }) : json({ error: 'no data yet' }, 404);
      }
      if (path === '/data' && req.method === 'POST') {
        if (!safeEq(req.headers.get('X-Sync-Key'), env.SYNC_KEY)) return json({ error: 'forbidden' }, 403);
        const text = await req.text(); let parsed;
        try { parsed = JSON.parse(text); } catch (e) { return json({ error: 'body is not JSON' }, 400); }
        if (!parsed || !Array.isArray(parsed.canyon) || !Array.isArray(parsed.history)) return json({ error: 'not board data' }, 400);
        await env.BOARD.put('data', text);
        return json({ ok: true, bytes: text.length, canyon: parsed.canyon.length });
      }
      if (path === '/whoami' && req.method === 'GET') {
        const r = role(env, req.headers.get('X-Code'));
        return r ? json({ role: r }) : json({ error: 'bad code' }, 401);
      }
      if (path === '/edit' && req.method === 'POST') {
        const r = role(env, req.headers.get('X-Code'));
        if (!r) return json({ error: 'bad code' }, 401);
        let e; try { e = await req.json(); } catch (x) { return json({ error: 'body is not JSON' }, 400); }
        const name = String(e.name || '').trim(); if (!name || name.length > 40) return json({ error: 'name required' }, 400);
        const out = { id: Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 8), name, by: String(e.by || r).slice(0, 40), role: r, at: new Date().toISOString() };
        if (e.avail !== undefined) { if (!AVAIL.includes(String(e.avail))) return json({ error: 'bad avail' }, 400); out.avail = String(e.avail); }
        if (e.slot !== undefined) { if (r !== 'officer') return json({ error: 'slots need the officer code' }, 403); if (!SLOTS.includes(String(e.slot))) return json({ error: 'bad slot' }, 400); out.slot = String(e.slot); }
        if (out.avail === undefined && out.slot === undefined) return json({ error: 'nothing to change' }, 400);
        // the sheet is the source of truth; the worker only queues. Keep names in the data file honest: reject unknown members.
        const data = await env.BOARD.get('data', 'json');
        if (data && !data.canyon.some(c => c.name === name)) return json({ error: 'unknown member' }, 404);
        // A shared passcode can leak. Cap the queue so a script cannot burn the KV write quota before anyone notices;
        // the sheet drains it every minute, so a real backlog never approaches this.
        const pending = await env.BOARD.list({ prefix: 'edit:', limit: MAX_PENDING + 1 });
        if (pending.keys.length > MAX_PENDING) return json({ error: 'too many pending changes, try again in a minute' }, 429, { 'Retry-After': '60' });
        await env.BOARD.put('edit:' + out.id, JSON.stringify(out), { expirationTtl: 60 * 60 * 24 * 7 });
        return json({ ok: true, edit: out });
      }
      if (path === '/clear' && req.method === 'POST') {
        const r = role(env, req.headers.get('X-Code'));
        if (!r) return json({ error: 'bad code' }, 401);
        if (r !== 'officer') return json({ error: 'clearing votes needs the officer code' }, 403);
        let b = {}; try { b = await req.json(); } catch (x) { /* empty body = votes only */ }
        const slots = b.slots === true, by = String(b.by || 'officer').slice(0, 40);
        const data = await env.BOARD.get('data', 'json');
        if (!data) return json({ error: 'no data yet' }, 409);
        // 1. Changes still waiting for the sheet: strip the parts the reset replaces, so they cannot land after it.
        const list = await env.BOARD.list({ prefix: 'edit:', limit: 1000 });
        const waiting = (await Promise.all(list.keys.map(async k => [k.name, await env.BOARD.get(k.name, 'json')]))).filter(x => x[1]);
        let dropped = 0;
        for (const [k, e] of waiting) {
          const had = e.avail !== undefined || (slots && e.slot !== undefined);
          if (!had) continue;
          delete e.avail; if (slots) delete e.slot;
          if (e.slot === undefined) await env.BOARD.delete(k); else await env.BOARD.put(k, JSON.stringify(e), { expirationTtl: 60 * 60 * 24 * 7 });
          dropped++;
        }
        // 2. One change per member who has something to clear (members with nothing to clear cost no KV writes).
        const t = Date.now(), at = new Date(t).toISOString(); let votes = 0, overrides = 0, n = 0;
        for (const c of data.canyon) {
          const out = {};
          if (c.avail) { out.avail = ''; votes++; }
          if (slots && c.manual) { out.slot = 'auto'; overrides++; }
          if (!Object.keys(out).length) continue;
          const id = t.toString(36) + '-' + String(n++).padStart(3, '0') + Math.random().toString(36).slice(2, 5);
          await env.BOARD.put('edit:' + id, JSON.stringify({ id, name: c.name, ...out, by: 'Clear votes · ' + by, role: r, at, bulk: true }), { expirationTtl: 60 * 60 * 24 * 7 });
        }
        return json({ ok: true, votes, overrides, dropped, at });
      }
      if (path === '/ledger' && req.method === 'GET') {
        const L = (await env.BOARD.get('ledger', 'json')) || { rev: 0, events: [] };
        if (url.searchParams.get('rev') === String(L.rev)) return json({ rev: L.rev, unchanged: true });
        return json(L);
      }
      if ((path === '/ledger' || path === '/ledger/delete' || path === '/ledger/rename') && req.method === 'POST') {
        const sync = safeEq(req.headers.get('X-Sync-Key'), env.SYNC_KEY), r = sync ? 'sync' : role(env, req.headers.get('X-Code'));
        if (!r) return json({ error: 'bad code' }, 401);
        if (r === 'member') return json({ error: 'the ledger needs the officer code' }, 403);
        let b; try { b = await req.json(); } catch (x) { return json({ error: 'body is not JSON' }, 400); }
        const L = (await env.BOARD.get('ledger', 'json')) || { rev: 0, events: [] }, by = str(b.by) || r, now = new Date().toISOString();
        if (path === '/ledger/rename') {
          const from = str(b.from), to = str(b.to), uid = str(b.uid, 24);
          if (!from || !to || from === to) return json({ error: 'from and to required' }, 400);
          let n = 0;
          for (const e of L.events) for (const p of e.players) if (p.name === from || (uid && p.uid === uid)) { p.name = to; if (uid) p.uid = uid; n++; }
          if (!n) return json({ ok: true, renamed: 0, rev: L.rev });
          L.renames = (L.renames || []).concat({ from, to, uid: uid || undefined, at: now, by }).slice(-200);
        } else if (path === '/ledger/delete') {
          const n = L.events.length; L.events = L.events.filter(e => e.date !== String(b.date));
          if (L.events.length === n) return json({ error: 'no event on that date' }, 404);
        } else {
          const old = L.events.find(e => e.date === str(b.event && b.event.date, 10));
          let ev;
          if (b.merge) {
            if (!old) return json({ error: 'no event on that date to merge into' }, 404);
            ev = mergeEvent(old, b.event || {});
            const [chk, err] = cleanEvent(ev); if (err) return json({ error: err }, 400);
            ev = { ...old, ...chk };
          } else {
            const [chk, err] = cleanEvent(b.event); if (err) return json({ error: err }, 400);
            if (!chk.players.length) return json({ error: 'no rostered players to lock in' }, 400);
            ev = { ...chk, lockedAt: old ? old.lockedAt : now, lockedBy: old ? old.lockedBy : by };
          }
          if (old) { ev.editedAt = now; ev.editedBy = by; }
          L.events = L.events.filter(e => e.date !== ev.date).concat(ev).sort((x, y) => x.date < y.date ? -1 : 1);
        }
        L.rev = (L.rev || 0) + 1; L.updated = now; L.updatedBy = by;
        const prev = await env.BOARD.get('ledger'); if (prev) await env.BOARD.put('ledger:prev', prev);   // one-step undo copy
        await env.BOARD.put('ledger', JSON.stringify(L));
        return json({ ok: true, rev: L.rev, events: L.events.length });
      }
      if (path === '/edits' && req.method === 'GET') {
        if (!safeEq(req.headers.get('X-Sync-Key'), env.SYNC_KEY)) return json({ error: 'forbidden' }, 403);
        const list = await env.BOARD.list({ prefix: 'edit:', limit: 500 });
        const edits = (await Promise.all(list.keys.map(k => env.BOARD.get(k.name, 'json')))).filter(Boolean).sort((a, b) => a.at < b.at ? -1 : 1);
        return json({ edits });
      }
      if (path === '/edits/ack' && req.method === 'POST') {
        if (!safeEq(req.headers.get('X-Sync-Key'), env.SYNC_KEY)) return json({ error: 'forbidden' }, 403);
        const { ids = [], failed = {} } = await req.json();
        const log = (await env.BOARD.get('log', 'json')) || [];
        for (const id of ids) {
          const e = await env.BOARD.get('edit:' + id, 'json');
          if (e) { log.push({ ...e, applied: new Date().toISOString(), error: failed[id] || undefined }); await env.BOARD.delete('edit:' + id); }
        }
        while (log.length > 200) log.shift();
        await env.BOARD.put('log', JSON.stringify(log));
        return json({ ok: true, acked: ids.length });
      }
      if (path === '/log' && req.method === 'GET') {
        const log = (await env.BOARD.get('log', 'json')) || [];
        return json({ log: log.map(e => ({ name: e.name, avail: e.avail, slot: e.slot, by: e.by, role: e.role, at: e.at, applied: e.applied, error: e.error })) });
      }
      if (path === '/' ) return json({ service: 'JTB 293 board API', routes: ['GET /data', 'POST /edit', 'GET /log', 'GET /ledger'] });
      return json({ error: 'not found' }, 404);
    } catch (err) {
      return json({ error: String(err && err.message || err) }, 500);
    }
  }
};

