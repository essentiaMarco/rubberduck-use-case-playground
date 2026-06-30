# RubberDuck Use Case Playground

**Runnable training labs** for all 10 RubberDuck workflows (+ codegen on UC-07).  
Not just docs — each use case has **code you can run**, **verify scripts**, and **copy-paste RubberDuck prompts**.

Official reference: [rubberduck.com/#docs](https://rubberduck.com/#docs)

## 3-click quick start

```bash
git clone https://github.com/oussama-rubberduck/rubberduck-use-case-playground.git
cd rubberduck-use-case-playground
python scripts/run-lab.py --uc 02 --verify
```

Windows:

```powershell
.\scripts\setup.ps1 -Uc 02 -Verify
```

This will:

1. Create `.venv` and install dependencies (first run only)
2. Run the lab smoke test for that UC
3. Print the RubberDuck **index** command + **prompt** to paste in your IDE

### Start the live API lab (UC-02)

```bash
python scripts/run-lab.py --uc 02 --start-server
```

Open http://127.0.0.1:8080/docs — then run RubberDuck security audit on the code.

## What is in this repo

| Layer | What you get |
|-------|----------------|
| **`labs/uc01` … `uc10`** | Per-UC project folder: README, verify script, tasks/tests |
| **`demoapp/`** | Shared Python codebase (~800 lines): CLI, builders, ORM bugs, HTTP API |
| **`demoapp/api/server.py`** | Runnable FastAPI for security/runtime exercises |
| **`scripts/run-lab.py`** | One command to setup + verify + print prompts |
| **`docs/uc-*.md`** | Official prompts (same as rubberduck.com) |
| **`git branches`** | `uc-01-understand-your-code` … `uc-10-quick-check` with `TUTORIAL.md` |

## Labs at a glance

| UC | Lab folder | Runnable? | What you do |
|----|------------|-----------|-------------|
| 01 | `labs/uc01_understand` | verify script | Trace entry points in `demoapp` |
| 02 | `labs/uc02_security_lab` | **API on :8080** | Audit live HTTP + `config.py` sinks |
| 03 | `labs/uc03_buggy_orm` | **pytest** | Find/fix aggregation bugs |
| 04 | `labs/uc04_pr_review` | verify + PR fixture | BLOCK/APPROVE fake PR |
| 05 | `labs/uc05_impact` | verify | Plan rename `config_values` |
| 06 | `labs/uc06_feature` | **failing tests** | Plan `--parallel-write` feature |
| 07 | `labs/uc07_codegen` | **failing tests** | Implement `gitlab.py` role |
| 08 | `labs/uc08_logic` | verify | Review `get_outdated_docs` logic |
| 09 | `labs/uc09_compare` | verify | Compare HTML vs Epub3 builders |
| 10 | `labs/uc10_quick` | verify | 30s assessment of `render_partial` |

## Full workflow (train yourself)

1. **Setup RubberDuck MCP** — see [SETUP.md](SETUP.md)
2. **Pick a UC:** `python scripts/run-lab.py --uc 03`
3. **Run the lab locally:** add `--verify` or follow `labs/uc03_buggy_orm/README.md`
4. **Index repo** in RubberDuck (command printed by run-lab)
5. **Paste prompt** from output into your IDE
6. **Compare** RubberDuck evidence vs what you saw running the lab

## Branches

Each `uc-*` branch adds a focused `TUTORIAL.md`. Code lives on `main` (all labs together).

```bash
git checkout uc-07-generate-code
```

## Tests

```bash
pip install -r requirements.txt
pytest tests labs -q
```

Some UC-06/07 tests **fail on purpose** until you implement the task (training).

## License

MIT
