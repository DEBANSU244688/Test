import pytest

pytest.importorskip("fastapi")
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_resume_parse() -> None:
    response = client.post("/api/resume/parse", json={"text": "Python SQL FastAPI"})
    assert response.status_code == 200
    assert response.json() == {"word_count": 3, "char_count": 18}
