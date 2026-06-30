# Tutorial — UC-09: Compare Versions

> Branch `uc-09-compare-versions` — public playground for [RubberDuck](https://rubberduck.com) workflows.

## When to use

Compare implementations across classes or versions for compatibility risks.

## Setup

1. Complete [SETUP.md](../SETUP.md) (MCP token + index this repo).
2. **Focus files:** `demoapp/builders/html.py` — HTML vs Epub3 `prepare_writing`
3. Optional upstream repo: see [docs/recommended-repos.md](docs/recommended-repos.md)

## Prompt

```
Compare prepare_writing between StandaloneHTMLBuilder and Epub3Builder in demoapp/builders/html.py.

Using RubberDuck:
1. read_source both methods
2. compare_snapshots or analyze_code for structural diff
3. search_code for all prepare_writing implementations
4. shared_variables and call_chain on both

Report what Epub3 adds, shared state, and compatibility risks.
```

## Expected RubberDuck tool flow

`load_repo → read_source → compare_snapshots → search_code → call_chain`

## Success criteria

- Every claim cites **file:line** from MCP tools
- Coherence / graph-backed evidence (not generic LLM guessing)
- Compare your run with the official doc narrative on rubberduck.com

## More detail

See [docs/uc-09.md](docs/uc-09.md)
