def test_gitlab_role_module_exists():
    import importlib
    mod = importlib.import_module("demoapp.ext.gitlab")
    assert hasattr(mod, "gitlab_role")
