#!/usr/bin/env bash
# Usage: ./scripts/setup.sh 02 [--verify] [--start-server]
set -euo pipefail
cd "$(dirname "$0")/.."
UC="${1:?pass UC number 01-10}"
shift || true
ARGS=(--uc "$UC")
for a in "$@"; do
  case "$a" in
    --verify) ARGS+=(--verify) ;;
    --start-server) ARGS+=(--start-server) ;;
  esac
done
python scripts/run-lab.py "${ARGS[@]}"
