# Tutorial — UC-01: Understand Your Code

> Branch `uc-01-understand-your-code` — public playground for [RubberDuck](https://rubberduck.com) workflows.

## When to use

You're new to a codebase, or need to understand how a specific feature works.

## Setup

1. Complete [SETUP.md](../SETUP.md) (MCP token + index this repo).
2. **Focus files:** `demoapp/cmd/build.py` (main), `demoapp/application.py` (Application)
3. Optional upstream repo: see [docs/recommended-repos.md](docs/recommended-repos.md)

## Prompt

```
Using the RubberDuck semantic intelligence tools, give me a complete overview of this codebase.
Show me:
1. All major classes and functions (use symbols_overview)
2. The main entry points
3. How the request/data flows through the system (use call_chain on the main entry points)

Base your answer ONLY on the analysis tools, not on general knowledge.
```

## Expected RubberDuck tool flow

`list_repos → load_repo → search_code → load_code → symbols_overview → call_chain → trace_variable`

## Success criteria

- Every claim cites **file:line** from MCP tools
- Coherence / graph-backed evidence (not generic LLM guessing)
- Compare your run with the official doc narrative on rubberduck.com

## More detail

See [docs/uc-01.md](docs/uc-01.md)
