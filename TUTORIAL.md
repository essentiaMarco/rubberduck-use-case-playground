# Tutorial — UC-04: Code Review

> Branch `uc-04-code-review` — public playground for [RubberDuck](https://rubberduck.com) workflows.

## When to use

You need to review a code change — PR, colleague's code, or your own before merging.

## Setup

1. Complete [SETUP.md](../SETUP.md) (MCP token + index this repo).
2. **Focus files:** `fixtures/uc-04-pr-order-by-diff.md` + `demoapp/db/query.py`
3. Optional upstream repo: see [docs/recommended-repos.md](docs/recommended-repos.md)

## Prompt

```
Review the PR described in fixtures/uc-04-pr-order-by-diff.md against demoapp/db/query.py Compiler.get_order_by.

Using RubberDuck:
1. Prove whether annotation_select is always a subset of annotations
2. Trace is_ref to get_group_by and get_extra_select
3. search_code for annotation_select_mask and set_annotation_mask

Verdict: APPROVE or BLOCK with evidence (file:line).
```

## Expected RubberDuck tool flow

`load_repo → analyze_code → read_source → search_code → call_chain`

## Success criteria

- Every claim cites **file:line** from MCP tools
- Coherence / graph-backed evidence (not generic LLM guessing)
- Compare your run with the official doc narrative on rubberduck.com

## More detail

See [docs/uc-04.md](docs/uc-04.md)
