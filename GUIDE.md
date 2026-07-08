# Rubber Duck Playground — guide

## Goal

Use the **demo-projects hub** to launch Rubber Duck Pizzeria, then run RubberDuck MCP use cases from the built-in prompts.

## Steps

1. Connect MCP — [SETUP.md](SETUP.md).
2. Start the hub:
   - Windows: `demo-projects/start-hub.bat`
   - Linux/macOS: `demo-projects/start-hub.sh`
3. Open http://127.0.0.1:5055/
4. **Launch** Rubber Duck Pizzeria; wait until venv, deps, DB, API, and frontend are OK.
5. Open the app at http://127.0.0.1:5000/ (optional sanity check).
6. **Generate prompts** → pick a UC → **What to expect** (read the bullets) → **Copy prompt**.
7. Paste into a separate Cursor / Claude chat with RubberDuck MCP connected.
8. Compare the assistant’s result to the hub’s expected bullets.

## Notes

- First Launch creates `package/.venv` and seeds SQLite on purpose (good for demos/recordings).
- Do not index `package/.venv` in UC prompts — hub prompts already exclude it.
- Instructor-only flag maps are kept out of this public repo.
