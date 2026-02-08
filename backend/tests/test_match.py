import pytest

pytest.importorskip("fastapi")
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_match_score_endpoint() -> None:
    payload = {"skills": 80, "tools": 70, "experience": 60}
    response = client.post("/api/match/score", json=payload)

    assert response.status_code == 200
    assert response.json()["score"] == 72
    assert response.json()["breakdown"] == payload
