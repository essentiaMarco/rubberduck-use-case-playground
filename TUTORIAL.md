# Tutorial — UC-05: Change Impact Analysis

> Branch `uc-05-change-impact-analysis` — public playground for [RubberDuck](https://rubberduck.com) workflows.

## When to use

Before making a change, you need to know what will break and what tests to run.

## Setup

1. Complete [SETUP.md](../SETUP.md) (MCP token + index this repo).
2. **Focus files:** `demoapp/config.py` — rename `config_values`
3. Optional upstream repo: see [docs/recommended-repos.md](docs/recommended-repos.md)

## Prompt

```
I want to rename Config.config_values to Config.values in demoapp/config.py.

Using RubberDuck, analyze the impact:
1. Use plan_change with description of what I want to change
2. Find all callers (use call_chain direction="callers")
3. Find downstream functions (use call_chain direction="callees")
4. Check shared variables (use shared_variables)
5. Trace key variables (use trace_variable)

Report:
- Risk level with reasoning
- Affected functions (file, line, dependency type)
- Recommended change order
- What tests to run
```

## Expected RubberDuck tool flow

`plan_change → search_code → call_chain → shared_variables → trace_variable`

## Success criteria

- Every claim cites **file:line** from MCP tools
- Coherence / graph-backed evidence (not generic LLM guessing)
- Compare your run with the official doc narrative on rubberduck.com

## More detail

See [docs/uc-05.md](docs/uc-05.md)
