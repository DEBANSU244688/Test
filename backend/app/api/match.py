from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.match_score import calculate_match_score

router = APIRouter(prefix="/match", tags=["match"])


class MatchScoreRequest(BaseModel):
    skills: int = Field(ge=0, le=100)
    tools: int = Field(ge=0, le=100)
    experience: int = Field(ge=0, le=100)


class MatchScoreBreakdown(BaseModel):
    skills: int
    tools: int
    experience: int


class MatchScoreResponse(BaseModel):
    score: int
    breakdown: MatchScoreBreakdown
    explanation: str


@router.post("/score", response_model=MatchScoreResponse)
def match_score(payload: MatchScoreRequest) -> MatchScoreResponse:
    result = calculate_match_score(
        skills=payload.skills,
        tools=payload.tools,
        experience=payload.experience,
    )
    return MatchScoreResponse(
        score=result.score,
        breakdown=MatchScoreBreakdown(
            skills=result.breakdown.skills,
            tools=result.breakdown.tools,
            experience=result.breakdown.experience,
        ),
        explanation=result.explanation,
    )
