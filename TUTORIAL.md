# Tutorial — UC-10: Quick Check

> Branch `uc-10-quick-check` — public playground for [RubberDuck](https://rubberduck.com) workflows.

## When to use

30-second assessment of an unfamiliar method — what it does, who depends on it, risk.

## Setup

1. Complete [SETUP.md](../SETUP.md) (MCP token + index this repo).
2. **Focus files:** `demoapp/builders/html.py` — `render_partial`
3. Optional upstream repo: see [docs/recommended-repos.md](docs/recommended-repos.md)

## Prompt

```
Never seen this code before. Give a 30-second assessment of render_partial in demoapp/builders/html.py:

1. read_source(function_name="render_partial")
2. call_chain(method="render_partial") — callers and callees
3. search_code(pattern="render_partial")

Report: what it does, who depends on it, risk level, with file:line evidence.
```

## Expected RubberDuck tool flow

`load_repo → read_source → call_chain → search_code`

## Success criteria

- Every claim cites **file:line** from MCP tools
- Coherence / graph-backed evidence (not generic LLM guessing)
- Compare your run with the official doc narrative on rubberduck.com

## More detail

See [docs/uc-10.md](docs/uc-10.md)
