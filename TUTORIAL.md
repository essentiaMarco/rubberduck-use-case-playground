# Tutorial — UC-02: Codebase Audit

> Branch `uc-02-codebase-audit` — public playground for [RubberDuck](https://rubberduck.com) workflows.

## When to use

You want to check for security vulnerabilities or quality issues in your code.

## Setup

1. Complete [SETUP.md](../SETUP.md) (MCP token + index this repo).
2. **Focus files:** `demoapp/config.py` — `eval_config_file`, `from_pickle`
3. Optional upstream repo: see [docs/recommended-repos.md](docs/recommended-repos.md)

## Prompt

```
Using RubberDuck semantic intelligence tools, perform a security-sensitive path audit on my loaded code:

1. First, find all entry points that accept external input (use search_code to find HTTP handlers, API endpoints, form handlers, user input processing)
2. For each entry point, trace the data flow of the input variable (use trace_variable)
3. Search for dangerous sinks: exec, eval, subprocess, SQL queries, file operations, shell commands (use search_code with regex patterns)
4. For any dangerous sink found, check if user input can reach it (use call_chain to trace the path from entry to sink)

Focus ONLY on the loaded code scope. If no dangerous path is found in the loaded files, say so honestly — do not speculate about code outside the loaded scope.

Report findings as:
- Entry point (file, line)
- Data flow path
- Sink (file, line, type of danger)
- Risk level (high/medium/low)
```

## Expected RubberDuck tool flow

`codebase_audit → load_repo → search_code → read_source → trace_variable → call_chain`

## Success criteria

- Every claim cites **file:line** from MCP tools
- Coherence / graph-backed evidence (not generic LLM guessing)
- Compare your run with the official doc narrative on rubberduck.com

## More detail

See [docs/uc-02.md](docs/uc-02.md)
