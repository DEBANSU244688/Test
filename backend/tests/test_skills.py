import pytest

pytest.importorskip("fastapi")
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_skills_extract_endpoint() -> None:
    response = client.post(
        "/api/skills/extract",
        json={"text": "Required: Python, Docker, TS, React."},
    )

    assert response.status_code == 200
    assert response.json() == {
        "skills": ["docker", "python", "react", "typescript"],
        "normalized_skills": ["docker", "python", "react", "typescript"],
    }
