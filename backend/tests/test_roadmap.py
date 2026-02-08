import pytest

pytest.importorskip("fastapi")
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_generate_roadmap_endpoint() -> None:
    response = client.get("/api/roadmap/generate")
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) == 6
    assert {"month", "focus_skill", "target", "certification", "progress"}.issubset(payload[0].keys())
