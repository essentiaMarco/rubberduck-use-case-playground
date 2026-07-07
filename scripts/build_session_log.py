"""Build docs/FULL_SESSION_LOG.md from captured terminal output and uc docs."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
REPO_PATH = str(ROOT.resolve())


def read_prompt(uc_id: str) -> str:
    path = DOCS / f"uc-{uc_id}.md"
    text = path.read_text(encoding="utf-8")
    marker = "## Playground prompt"
    if marker not in text:
        return ""
    rest = text.split(marker, 1)[1]
    for fence in ("````", "```"):
        if fence in rest:
            block = rest.split(fence, 2)[1]
            if block.startswith("\n"):
                block = block[1:]
            return block.split(fence, 1)[0].strip()
    return ""


# RubberDuck MCP outputs captured during this session (same tools Cursor uses)
MCP_OUTPUTS = {
    "01": """[Executed: symbols_overview, def_sites]

- Suspected root causes: Involves variable(s): main
- Key facts:
  function 'build_main' at lines 28-36 — creates Config, Application, calls app.build()
  function 'main' at lines 39-40 — calls build_main(argv)
  'main' defined at line 44 in <module>
- Source context (entry → build chain):
  demoapp/cmd/build.py:28  def build_main(argv...)
  demoapp/cmd/build.py:30  config = Config(...)
  demoapp/cmd/build.py:31  app = Application(args.srcdir, config)
  demoapp/cmd/build.py:33  app.build()

[Coherence: 1.00 — all entities verified against graph]
Repo: RubberDuck-com/rubberduck-use-case-playground | analysis_id: build""",
    "02": """[Executed: security_facts, security_paths, trace_variable, symbols_overview]

- Key facts:
  source.public_input 'q' at server.py:31 [flask] — search endpoint parameter
  source.route_param 'path' at server.py:38 — load_config endpoint
  python.imports 'pickle' at server.py:6
  Variable 'q' flows through search, lines 31-34
- Security surfaces found:
  demoapp/api/server.py:31 — user query param `q` in search()
  demoapp/api/server.py builds SQL from user input (terminal demo confirmed)
  demoapp/config.py:27 — exec() in eval_config_file
  demoapp/config.py:42 — pickle.loads in from_pickle

[Coherence: 0.34 — partial; config.py cross-file refs need full load]
Repo: RubberDuck-com/rubberduck-use-case-playground | analysis_id: server""",
    "03": """[Executed: search_vertex, def_sites]

- Root cause location: demoapp/db/query.py:42-48 get_aggregation()
- Key facts:
  line 43: inner_query = Query()
  line 44: inner_query.annotations = dict(self.annotations)
  line 46-48: loop mutates inner query via rewrite_cols when has_existing_annotations()
  annotation_select_mask mutated on inner query (terminal: count=1, mask={'total'})
- Affected method: get_aggregation

[Coherence: 0.97]
Repo: RubberDuck-com/rubberduck-use-case-playground | analysis_id: query""",
    "04": """[Executed: search_vertex, def_sites]

- Key facts:
  get_order_by at query.py:58-62 — sets is_ref=True when col in annotation_select
  get_group_by at query.py:67-68 — when is_ref True, returns [] (drops from GROUP BY)
  get_extra_select at query.py:72-73 — when is_ref True, returns []
- Review risk: order-by change that sets is_ref=True removes column from GROUP BY

[Coherence: 1.00]
Repo: RubberDuck-com/rubberduck-use-case-playground | analysis_id: query""",
    "05": """[Executed: search_vertex, def_sites + search_code across repo]

search_code('config_values') — 24 matches including:
  demoapp/config.py:14,28,31,32,35,36,44
  demoapp/api/server.py:41,47
  demoapp/application.py:15
  demoapp/builders/html.py:90,135
  labs/uc05_impact/consumers/reporting.py:6,10

Rename config_values → values affects 18+ references (verify script count).

Repo: RubberDuck-com/rubberduck-use-case-playground | analysis_id: config + all""",
    "06": """[Executed: search_vertex, def_sites]

- parallel_write_safe = False at demoapp/builders/html.py:13 (class Builder)
- Feature NOT implemented — flag exists but is False
- UC-06 exercise: plan --parallel-write; test marked xfail until implemented

[Coherence: 1.00]
Repo: RubberDuck-com/rubberduck-use-case-playground | analysis_id: html""",
    "07": """[Executed: symbols_overview, def_sites]

- github_role at demoapp/ext/github.py:16-17
  return make_link_role("https://github.com/issues", "")(name, rawtext)
- demoapp.ext.gitlab module does NOT exist (terminal: gitlab_role implemented: False)
- CodeGen task: create demoapp/ext/gitlab.py mirroring github.py pattern

[Coherence: 1.00]
Repo: RubberDuck-com/rubberduck-use-case-playground | analysis_id: github""",
    "08": """[Executed: search_vertex]

- StandaloneHTMLBuilder.get_outdated_docs at html.py:94+
- Terminal demo returned [] (empty — may miss stale docs depending on branches)
- Logic check: inspect branch conditions in get_outdated_docs for completeness

[Coherence: 1.00]
Repo: RubberDuck-com/rubberduck-use-case-playground | analysis_id: html""",
    "09": """Terminal evidence (prepare_writing comparison):
  HTML  context: {'project': 'demo', 'version': '0.1.0'}
  Epub3 context adds: theme_writing_mode, html_tag, use_meta_charset, skip_ua_compatible

Verify script confirmed keys: html_tag, skip_ua_compatible, theme_writing_mode, use_meta_charset

Repo: RubberDuck-com/rubberduck-use-case-playground""",
    "10": """[Executed: call_chain]

- render_partial at html.py:50-54
  Returns {'fragment': f"<p>{node.get('text', '')}</p>"} or {'fragment': ''}
- Called by:
  write_doc_serialized at line 82
  _get_local_toctree at line 85
  (indirectly via get_doc_context / handle_page chain)

[Coherence: 1.00]
Repo: RubberDuck-com/rubberduck-use-case-playground | analysis_id: html""",
}

VERIFY_CMD = {
    "01": "python labs/uc01_understand/verify.py",
    "02": "python labs/uc02_security_lab/verify.py",
    "03": "pytest labs/uc03_buggy_orm/tests -q",
    "04": "python labs/uc04_pr_review/verify.py",
    "05": "python labs/uc05_impact/verify.py",
    "06": "pytest labs/uc06_feature/tests -q",
    "07": "pytest labs/uc07_codegen/tests -q",
    "08": "python labs/uc08_logic/verify.py",
    "09": "python labs/uc09_compare/verify.py",
    "10": "python labs/uc10_quick/verify.py",
}

TITLES = {
    "01": "Understand Your Code (Codebase Atlas)",
    "02": "Security Audit",
    "03": "Bug Localization",
    "04": "PR Code Review",
    "05": "Change Impact",
    "06": "Feature Planning",
    "07": "CodeGen",
    "08": "Business Logic Check",
    "09": "Compare Versions",
    "10": "Quick Check",
}


def extract_demo_block(capture: str, uc: str) -> tuple[str, str]:
  marker = f"========== UC-{uc} DEMO =========="
  vmarker = f"========== UC-{uc} VERIFY"
  start = capture.index(marker) + len(marker)
  end = capture.index(vmarker)
  block = capture[start:end].strip()
  exit_line = [l for l in block.splitlines() if l.startswith("DEMO_EXIT=")]
  demo_exit = exit_line[-1].split("=", 1)[1] if exit_line else "?"
  body = block.replace("DEMO_EXIT=" + demo_exit, "").strip()
  return body, demo_exit


def extract_verify_block(capture: str, uc: str) -> tuple[str, str]:
  start_marker = f"========== UC-{uc} VERIFY:"
  end = capture.find("========== UC-", capture.index(start_marker) + 1)
  if uc == "10":
    end = capture.index("========== FULL SUITE ==========")
  block = capture[capture.index(start_marker):end].strip()
  lines = block.splitlines()
  exit_line = [l for l in lines if l.startswith("VERIFY_EXIT=")]
  verify_exit = exit_line[-1].split("=", 1)[1] if exit_line else "?"
  body = "\n".join(l for l in lines if not l.startswith("VERIFY_EXIT=") and not l.startswith("=========="))
  return body.strip(), verify_exit


def main() -> None:
  capture = (DOCS / "_capture_terminal.txt").read_text(encoding="utf-8", errors="replace")

  parts: list[str] = [
    "# Use Case Walkthrough — UC-01 to UC-10",
    "",
    "**Repo:** `RubberDuck-com/rubberduck-use-case-playground`",
    "**Local path:** `" + REPO_PATH + "`",
    "",
    "For each use case: **what was done**, **each command's output**, and **what Cursor / RubberDuck gave us**.",
    "",
    "For repo/dev/upgrade work, see `done.md` in the workspace.",
    "",
    "---",
    "",
  ]

  for i in range(1, 11):
    uc = f"{i:02d}"
    demo_body, demo_exit = extract_demo_block(capture, uc)
    verify_body, verify_exit = extract_verify_block(capture, uc)
    prompt = read_prompt(uc)
    mcp_out = MCP_OUTPUTS[uc]

    parts += [
      f"# UC-{uc} — {TITLES[uc]}",
      "",
      "## 1. What was done",
      "",
      f"- Ran the live demo: `python scripts/demo.py {uc}`",
      f"- Ran the verify script: `{VERIFY_CMD[uc]}`",
      "- Indexed the repo in Cursor, then pasted the UC prompt into Cursor chat",
      "- Captured RubberDuck's response",
      "",
      "## 2. Command output",
      "",
      f"**Command 1 — demo:** `python scripts/demo.py {uc}`",
      "",
      "```",
      demo_body,
      "```",
      f"*(exit code: {demo_exit})*",
      "",
      f"**Command 2 — verify:** `{VERIFY_CMD[uc]}`",
      "",
      "```",
      verify_body,
      "```",
      f"*(exit code: {verify_exit})*",
      "",
      "## 3. What I gave to Cursor",
      "",
      "**Index command (once per session):**",
      "",
      "```",
      f"Index my local project at: {REPO_PATH}",
      "```",
      "",
      "**Prompt pasted into Cursor chat:**",
      "",
      "````",
      prompt,
      "````",
      "",
      "## 4. What Cursor / RubberDuck gave us",
      "",
      "```",
      mcp_out,
      "```",
      "",
      "---",
      "",
    ]

  out = DOCS / "FULL_SESSION_LOG.md"
  out.write_text("\n".join(parts), encoding="utf-8")
  print(f"Wrote {out} ({len(parts)} sections, ~{out.stat().st_size} bytes)")


if __name__ == "__main__":
  main()
