"""UC-01 smoke check: demoapp imports and entry point exists."""
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[2]
build = ROOT / "demoapp" / "cmd" / "build.py"
assert build.exists(), "missing build.py"
spec = importlib.util.spec_from_file_location("build", build)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
assert hasattr(mod, "main")
print("UC-01 lab OK: entry point demoapp.cmd.build:main")
