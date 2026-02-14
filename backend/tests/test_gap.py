import pytest

pytest.importorskip("fastapi")
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_gap_analyze_endpoint() -> None:
    response = client.post(
        "/api/gap/analyze",
        json={
            "resume_skills": ["Python", "FastAPI", "SQL"],
            "job_skills": ["Python", "SQL", "Docker", "AWS", "Machine Learning"],
            "resume_skill_levels": {"python": 88, "sql": 65, "fastapi": 60},
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["match_percent"] == 40
    assert body["missing_skills"] == ["aws", "docker", "machine learning"]
    assert body["weak_skills"] == ["sql"]
    assert body["future_proof_skills"][0]["skill"] == "aws"
    assert len(body["heatmap_data"]) == 5
    assert {"skill", "current_level", "target_level", "demand_weight", "status"}.issubset(
        body["heatmap_data"][0].keys()
    )
    assert len(body["gaps"]) == 3
