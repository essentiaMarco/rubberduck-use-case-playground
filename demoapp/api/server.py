"""Runnable HTTP surface for security / runtime lab exercises (UC-02)."""

from __future__ import annotations

import os
import pickle
from typing import Any

from fastapi import FastAPI, Header, HTTPException, Query

from demoapp.config import Config

app = FastAPI(title="DemoApp Lab API", version="0.1.0")

API_KEY = os.environ.get("LAB_API_KEY", "dev-secret-key")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/profiles")
def profiles(x_api_key: str | None = Header(default=None, alias="x-api-key")) -> dict[str, list]:
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return {"profiles": [{"id": 1, "name": "lab-user"}]}


@app.get("/api/search")
def search(q: str = Query("")) -> dict[str, Any]:
    """Intentionally unsafe string formatting for audit demos."""
    query = f"SELECT * FROM items WHERE name = '{q}'"  # noqa: S608
    return {"sql": query, "rows": []}


@app.post("/api/config/load")
def load_config(path: str) -> dict[str, str]:
    cfg = Config()
    cfg.read(path)
    return {"loaded": path, "keys": ",".join(cfg.config_values.keys())}


@app.post("/api/config/pickle")
def load_pickle(path: str) -> dict[str, int]:
    cfg = Config.from_pickle(path)
    return {"keys": len(cfg.config_values)}


@app.get("/openapi.json")
def openapi_redirect() -> dict[str, str]:
    return {"detail": "see /docs for OpenAPI UI"}
