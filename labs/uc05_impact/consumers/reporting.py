"""Consumers of Config.config_values — rename breaks these (UC-05)."""
from demoapp.config import Config


def load_project_name(cfg: Config) -> str:
    return str(cfg.config_values.get("project", "unknown"))


def export_config(cfg: Config) -> dict:
    return dict(cfg.config_values)
