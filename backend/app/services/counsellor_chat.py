from dataclasses import dataclass


@dataclass(frozen=True)
class CounsellorResponse:
    reply: str
    insight: str
    history_length: int


def generate_counsellor_response(message: str, history_length: int = 0) -> CounsellorResponse:
    cleaned = message.strip()
    if not cleaned:
        cleaned = "I want career guidance"

    reply = (
        "Great question. Focus on one high-impact gap this week, "
        "ship a small proof-of-work project, and track progress daily."
    )
    insight = (
        f"Detected focus area from your message: '{cleaned[:60]}'. "
        "Prioritize skills that align with your target role and market demand."
    )
    return CounsellorResponse(reply=reply, insight=insight, history_length=history_length + 1)
