from app.services.counsellor_chat import generate_counsellor_response


def test_generate_counsellor_response_increments_history() -> None:
    response = generate_counsellor_response("I want to become a backend engineer", history_length=2)
    assert response.history_length == 3
    assert "high-impact gap" in response.reply


def test_generate_counsellor_response_handles_blank_message() -> None:
    response = generate_counsellor_response("   ")
    assert response.history_length == 1
    assert "Detected focus area" in response.insight
