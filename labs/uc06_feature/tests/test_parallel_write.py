"""Tests-first: parallel write flag (UC-06) — fails until implemented."""
from demoapp.builders.html import StandaloneHTMLBuilder
from demoapp.application import Application


def test_parallel_write_flag_exists():
    app = Application(srcdir=".")
    builder = StandaloneHTMLBuilder(app)
    assert hasattr(builder, "parallel_write_safe") or getattr(builder, "parallel_write", False)
