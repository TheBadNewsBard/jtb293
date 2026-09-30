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
 */
const AVAIL = ['', '18:00 only', '23:00 only', 'Both', 'N/A'];
const MAX_PENDING = 300;   // queue cap (see /edit); the sheet drains the queue every minute
const SLOTS = ['auto', 'T1 Starter', 'T1 Sub', 'T2 Starter', 'T2 Sub', 'Bench', 'Not available'];
const CORS = { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET,POST,OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type,X-Code,X-Sync-Key', 'Access-Control-Max-Age': '86400' };
const json = (obj, status = 200, extra = {}) => new Response(JSON.stringify(obj), { status, headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', ...CORS, ...extra } });
const safeEq = (a, b) => { a = String(a || ''); b = String(b || ''); if (a.length !== b.length || !a.length) return false; let r = 0; for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i); return r === 0; };
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
      if (path === '/' ) return json({ service: 'JTB 293 board API', routes: ['GET /data', 'POST /edit', 'GET /log'] });
      return json({ error: 'not found' }, 404);
    } catch (err) {
      return json({ error: String(err && err.message || err) }, 500);
    }
  }
};
