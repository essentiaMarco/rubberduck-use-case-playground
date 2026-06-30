"""UC-05: count config_values references without external tools."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
count = 0
for base in [ROOT / "demoapp", ROOT / "labs" / "uc05_impact"]:
    for path in base.rglob("*.py"):
        count += path.read_text(encoding="utf-8").count("config_values")
print(f"UC-05 lab OK: {count} references to config_values (rename = high impact)")
