import pytest

pytest.importorskip("fastapi")
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_job_parse_endpoint() -> None:
    payload = {
        "text": "Must have Python and SQL experience. FastAPI experience required. Nice to have React. You will build APIs.",
    }

    response = client.post("/api/job/parse", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body["normalized_text"] == payload["text"]
    assert body["extracted_skills"] == ["fastapi", "python", "react", "sql"]
    assert len(body["extracted_requirements"]) >= 2
    assert "requirement_groups" in body
    assert len(body["requirement_groups"]["must_have"]) >= 1
    assert len(body["requirement_groups"]["preferred"]) >= 1


def test_job_templates_endpoint_returns_templates() -> None:
    response = client.get("/api/job/templates")
    assert response.status_code == 200
    body = response.json()
    assert len(body) >= 3
    assert body[0]["role"] == "backend engineer"


def test_job_templates_endpoint_filters_by_role() -> None:
    response = client.get("/api/job/templates", params={"role": "frontend engineer"})
    assert response.status_code == 200
    assert response.json()[0]["role"] == "frontend engineer"
