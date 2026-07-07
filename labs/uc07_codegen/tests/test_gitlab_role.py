"""Tests-first: GitLab role module (UC-07).

This is the UC-07 exercise: demoapp.ext.gitlab does not exist yet. The test is
marked xfail so the suite stays green on a fresh clone; when a trainee adds the
module (mirroring demoapp.ext.github), it flips to XPASS.
"""
import importlib

import pytest


@pytest.mark.xfail(raises=ModuleNotFoundError, reason="UC-07 exercise: add demoapp.ext.gitlab", strict=False)
def test_gitlab_role_module_exists():
    mod = importlib.import_module("demoapp.ext.gitlab")
    assert hasattr(mod, "gitlab_role")
