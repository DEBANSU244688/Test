import pytest

pytest.importorskip("fastapi")
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_course_recommendations() -> None:
    response = client.get("/api/recommendations/courses")
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) >= 3
    assert {"title", "provider", "duration_weeks", "roi_score", "skill_outcome", "recommended"}.issubset(
        payload[0].keys()
    )
