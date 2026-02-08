import pytest

pytest.importorskip("fastapi")
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_heatmap_data() -> None:
    response = client.get("/api/heatmap/data")
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) >= 5
    assert {"skill", "current_level", "target_level", "demand_weight", "status"}.issubset(body[0].keys())
