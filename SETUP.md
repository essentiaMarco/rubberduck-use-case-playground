# Rubber Duck Playground — MCP setup (5 minutes)

## 1. Get a token

Sign up at [rubberduck.com](https://rubberduck.com) and copy your API token from the dashboard.

For the full playground walkthrough, see **[GUIDE.md](GUIDE.md)**.

## 2. Connect Cursor (or Claude Code / Codex)

Add to `~/.cursor/mcp.json` (or project `.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "rubberduck-codebase-intelligence": {
      "url": "https://codebase.rubberduck.com/mcp",
      "headers": { "Authorization": "Bearer YOUR_TOKEN" }
    },
    "rubberduck-semantic-intelligence": {
      "url": "https://semantic.rubberduck.com/mcp",
      "headers": { "Authorization": "Bearer YOUR_TOKEN" }
    }
  }
}
```

Restart the IDE session.

## 3. Health check

Paste in chat:

```
Verify that both MCP servers are properly configured and reachable.
Respond only with "healthy" or "unhealthy."
```

## 4. Start the hub and index

```bash
cd demo-projects
# Windows: start-hub.bat
# Linux/macOS: ./start-hub.sh
```

Open http://127.0.0.1:5055/ → Launch the pizzeria demo → Generate prompts.

**Index (pick one):**

```
Index my GitHub repo: https://github.com/RubberDuck-com/rubberduck-use-case-playground
```

```
Index my local project at: /path/to/rubberduck-use-case-playground/demo-projects/rubberduck_pizzeria-demoapp
```

Then paste the UC prompt copied from the hub into Cursor / Claude.
