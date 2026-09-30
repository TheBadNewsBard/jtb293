# Board API (Cloudflare Worker)

Queues availability / slot changes from the public board and hands them to the JTB 293 Tracker Tools Apps Script,
which applies them to the Canyon Teams sheet (the source of truth) and pushes the fresh export back here.

## One-time setup (Cloudflare dashboard, free plan)
1. Workers & Pages -> Create -> Worker, name `jtb293-board`, deploy the hello-world, then Edit code and paste `worker.js` over it. Deploy.
2. Storage & Databases -> KV -> Create namespace `jtb293-board`.
3. Worker -> Settings -> Bindings -> Add -> KV namespace: variable name `BOARD`, namespace `jtb293-board`.
4. Worker -> Settings -> Variables and Secrets -> add three **secrets**: `SYNC_KEY`, `OFFICER_CODE`, `MEMBER_CODE`.
   - `SYNC_KEY`: a long random string; the same value goes into the Apps Script project's Script Properties as `BOARD_SYNC_KEY`.
   - `OFFICER_CODE`: what R4/R5s type into the board to change slots.
   - `MEMBER_CODE`: what members type to set their own availability. Rotate any of these here whenever you like.
5. Copy the worker URL (`https://jtb293-board.<your-subdomain>.workers.dev`) into `board_template.html` (`API_URL`) and into `tracker_tools.gs` (`BOARD_API_URL`).

## Smoke test
    curl https://jtb293-board.<sub>.workers.dev/            -> {"service":"JTB 293 board API",...}
    curl -H "X-Code: <member code>" .../whoami             -> {"role":"member"}
