# UC-03: Bug localization lab

## Run failing / exploratory tests

```bash
pytest labs/uc03_buggy_orm/tests -v
```

## RubberDuck exercise

Use UC-03 prompt on `demoapp/db/query.py` — find all 3 interacting bugs in `get_aggregation` / `rewrite_cols`.

## Goal

Propose a fix, then re-run tests until green.
