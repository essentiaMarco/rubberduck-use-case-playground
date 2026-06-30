#!/usr/bin/env python3
"""One-command lab launcher for RubberDuck use-case playground."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "labs" / "manifest.json"
VENV = ROOT / ".venv"


def load_manifest() -> dict:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def python_exe() -> str:
    if sys.platform == "win32":
        cand = VENV / "Scripts" / "python.exe"
    else:
        cand = VENV / "bin" / "python"
    return str(cand) if cand.exists() else sys.executable


def ensure_venv() -> None:
    if not VENV.exists():
        print("Creating .venv ...")
        subprocess.check_call([sys.executable, "-m", "venv", str(VENV)], cwd=ROOT)
    subprocess.check_call([python_exe(), "-m", "pip", "install", "-q", "-r", "requirements.txt"], cwd=ROOT)
    subprocess.check_call([python_exe(), "-m", "pip", "install", "-q", "-e", "."], cwd=ROOT)
    if not (VENV / ".rd-lab-ready").exists():
        (VENV / ".rd-lab-ready").write_text("ok", encoding="utf-8")
        print("Dependencies installed.\n")


def lab_env() -> dict:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT)
    return env


def run_verify(lab: dict) -> None:
    cmd = lab.get("verify")
    if not cmd:
        return
    print(f"Running verify: {cmd}\n")
    if cmd.startswith("pytest"):
        subprocess.check_call([python_exe(), "-m", *cmd.split()], cwd=ROOT, env=lab_env())
    elif cmd.startswith("python "):
        script = cmd.split("python ", 1)[1]
        subprocess.check_call([python_exe(), script], cwd=ROOT, env=lab_env())
    else:
        subprocess.check_call(cmd, shell=True, cwd=ROOT, env=lab_env())


def read_prompt(uc_id: str) -> str:
    path = ROOT / "docs" / f"uc-{uc_id}.md"
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    if "```" in text:
        block = text.split("```", 2)[1]
        if block.startswith("\n"):
            block = block[1:]
        return block.split("```", 1)[0].strip()
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a RubberDuck UC lab")
    parser.add_argument("--uc", required=True, help="Use case number 01-10")
    parser.add_argument("--setup-only", action="store_true", help="Install venv only")
    parser.add_argument("--verify", action="store_true", help="Run lab verify script")
    parser.add_argument("--start-server", action="store_true", help="Start lab server if defined")
    args = parser.parse_args()

    uc_key = args.uc.zfill(2)
    data = load_manifest()
    lab = data["labs"].get(uc_key)
    if not lab:
        print(f"Unknown UC: {args.uc}", file=sys.stderr)
        return 1

    ensure_venv()
    if args.setup_only:
        return 0

    repo_path = str(ROOT.resolve())
    print("=" * 60)
    print(f"UC-{uc_key}: {lab['title']}")
    print(f"Branch: {lab['slug']}")
    print(f"Lab folder: {lab['project_dir']}")
    print("=" * 60)

    lab_readme = ROOT / lab["project_dir"] / "README.md"
    if lab_readme.exists():
        print(f"\nSee: {lab_readme.relative_to(ROOT)}\n")

    if args.verify and lab.get("verify"):
        run_verify(lab)

    if args.start_server and lab.get("start"):
        cmd = lab["start"]
        print(f"Starting server (Ctrl+C to stop):\n  {cmd}\n")
        if lab.get("url"):
            print(f"Open: {lab['url']}\n")
        parts = cmd.split()
        subprocess.call([python_exe(), "-m", *parts], cwd=ROOT, env=lab_env())
        return 0

    prompt = read_prompt(uc_key)
    print("--- RubberDuck: index this repo ---\n")
    print(data["setup"]["index_prompt"].format(repo_path=repo_path))
    print("\n--- Copy this prompt into your IDE ---\n")
    print(prompt or f"(see docs/uc-{uc_key}.md)")
    print("\n--- Focus files ---\n")
    for p in lab.get("focus_paths", []):
        print(f"  - {p}")
    print("\nDone. Use --verify to smoke-test, --start-server for UC-02 API.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
