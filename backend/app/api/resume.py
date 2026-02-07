from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/resume", tags=["resume"])


class ResumeParseRequest(BaseModel):
    text: str = Field(min_length=1, description="Extracted resume text")


class ResumeParseResponse(BaseModel):
    word_count: int
    char_count: int


@router.post("/parse", response_model=ResumeParseResponse)
def parse_resume(payload: ResumeParseRequest) -> ResumeParseResponse:
    words = [w for w in payload.text.split() if w.strip()]
    return ResumeParseResponse(word_count=len(words), char_count=len(payload.text))
