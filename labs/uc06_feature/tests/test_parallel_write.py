"""Tests-first: parallel write flag (UC-06).

This is the UC-06 exercise: the feature is intentionally not implemented yet.
The test is marked xfail so the suite stays green on a fresh clone; when a
trainee implements --parallel-write, it flips to XPASS.
"""
import pytest

from demoapp.builders.html import StandaloneHTMLBuilder
from demoapp.application import Application


@pytest.mark.xfail(reason="UC-06 exercise: implement --parallel-write", strict=False)
def test_parallel_write_flag_exists():
    app = Application(srcdir=".")
    builder = StandaloneHTMLBuilder(app)
    assert getattr(builder, "parallel_write_safe", False) is True
