"""Focused regression + adversarial tests for F-01 (SQL injection in search).

Security invariant: request-derived ``q`` must reach SQL only as a bound
parameter, never interpolated into the statement. A legitimate substring
search still matches; an injection payload is treated as a literal LIKE
pattern and matches nothing.
"""
from rubber_duck_pizzeria import db as dbmod


def _seed():
    dbmod.init_db(force=True)


def test_legitimate_substring_search_still_matches():
    _seed()
    rows = dbmod.search_customers_raw("James")
    assert any(r["name"] == "James Witwicky" for r in rows)


def test_injection_payload_returns_no_rows():
    _seed()
    everything = dbmod.search_customers_raw("")  # "" -> LIKE %% matches all
    injected = dbmod.search_customers_raw("' OR 1=1--")
    assert injected == []            # classic payload no longer leaks rows
    assert len(everything) > len(injected)


def test_union_injection_returns_no_rows():
    _seed()
    rows = dbmod.search_customers_raw("x' UNION SELECT * FROM staff--")
    assert rows == []
