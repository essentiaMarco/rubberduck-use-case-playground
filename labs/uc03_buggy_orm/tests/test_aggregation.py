"""UC-03: aggregation bug — tests document expected vs actual behavior."""
from demoapp.db.query import Query


def test_aggregation_lab_reproduces_mask_gap():
    """Documented bug lab — RubberDuck should trace mask lifecycle in get_aggregation."""
    q = Query()
    q.annotations = {"hour": "expr", "total": "sum"}
    result = q.get_aggregation()
    inner = result["inner"]
    assert inner.annotations == {"hour": "expr", "total": "sum"}
    # Training note: inner_query.annotation_select_mask is never initialized via set_annotation_mask
    assert result["count"] >= 0
