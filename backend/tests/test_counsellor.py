import pytest

pytest.importorskip("fastapi")
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_counsellor_chat_endpoint() -> None:
    response = client.post(
        "/api/counsellor/chat",
        json={"message": "How do I prepare for backend interviews?", "history_length": 1},
    )
    assert response.status_code == 200
    payload = response.json()
    assert {"reply", "insight", "history_length"}.issubset(payload.keys())
    assert payload["history_length"] == 2
