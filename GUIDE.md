# Rubber Duck Playground — guide

## Goal

Use the **demo-projects hub** to launch Rubber Duck Pizzeria, connect RubberDuck MCP, then run UC-01…UC-10 from the built-in prompts.

## Steps

1. **Git clone** the repo:
   ```bash
   git clone https://github.com/RubberDuck-com/rubberduck-use-case-playground.git
   cd rubberduck-use-case-playground
   ```

2. **Open the hub**
   - `cd demo-projects`
   - Windows: double-click `start-hub.bat`
   - Linux/macOS: `chmod +x start-hub.sh && ./start-hub.sh`
   - Open http://127.0.0.1:5055/

3. **Welcome** — on the Welcome tab, select Rubber Duck Pizzeria (more demos will appear here later).

4. **Launch** — click **Select & launch** (or Launch tab → **Launch**). Wait until venv, deps, DB, API, and frontend are OK. Optional: http://127.0.0.1:5000/

5. **Connect RubberDuck MCP** — open the **Connect MCP** tab in the hub (token, `mcp.json`, health check, index). Full reference: [SETUP.md](SETUP.md).

6. **Generate prompts** — open the tab, pick a UC, read **What to expect**, **Copy prompt**, paste into Cursor or Claude, and compare to the bullets.

## Notes

- First Launch creates `package/.venv` and seeds SQLite on purpose (good for demos/recordings).
- Do not index `package/.venv` — hub prompts already exclude it.
- Instructor-only flag maps are kept out of this public repo.
