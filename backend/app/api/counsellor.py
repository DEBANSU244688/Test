from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.counsellor_chat import generate_counsellor_response

router = APIRouter(prefix="/counsellor", tags=["counsellor"])


class CounsellorChatRequest(BaseModel):
    message: str = Field(min_length=1)
    history_length: int = Field(default=0, ge=0)


class CounsellorChatResponse(BaseModel):
    reply: str
    insight: str
    history_length: int


@router.post("/chat", response_model=CounsellorChatResponse)
def counsellor_chat(payload: CounsellorChatRequest) -> CounsellorChatResponse:
    response = generate_counsellor_response(
        message=payload.message,
        history_length=payload.history_length,
    )
    return CounsellorChatResponse(
        reply=response.reply,
        insight=response.insight,
        history_length=response.history_length,
    )
