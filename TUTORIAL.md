# Tutorial — UC-06: Plan a New Feature

> Branch `uc-06-plan-new-feature` — public playground for [RubberDuck](https://rubberduck.com) workflows.

## When to use

You want to add a new feature, preferably tests-first.

## Setup

1. Complete [SETUP.md](../SETUP.md) (MCP token + index this repo).
2. **Focus files:** `demoapp/builders/html.py` — `write_doc`, parallel patterns
3. Optional upstream repo: see [docs/recommended-repos.md](docs/recommended-repos.md)

## Prompt

```
I want to add a --parallel-write flag for parallel file writing in demoapp builders.

Using RubberDuck, help me plan tests-first:

Step 1 — Understand existing patterns:
1. Search for similar functionality (use search_code, analyze_code)
2. Find test directory and patterns
3. Identify where this feature belongs (use symbols_overview)

Step 2 — Design tests first:
Write test cases BEFORE implementation, following existing conventions.

Step 3 — Implementation plan:
- Which files to modify
- What new code to add
- What NOT to add (keep minimal)

Do NOT generate implementation code yet — only tests and plan.
```

## Expected RubberDuck tool flow

`search_code → symbols_overview → read_source → call_chain → analyze_code`

## Success criteria

- Every claim cites **file:line** from MCP tools
- Coherence / graph-backed evidence (not generic LLM guessing)
- Compare your run with the official doc narrative on rubberduck.com

## More detail

See [docs/uc-06.md](docs/uc-06.md)
