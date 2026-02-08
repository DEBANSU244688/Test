from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.skill_extractor import extract_skills_from_text

router = APIRouter(prefix="/skills", tags=["skills"])


class SkillExtractRequest(BaseModel):
    text: str = Field(min_length=1, description="Resume or job text to analyze for skills")


class SkillExtractResponse(BaseModel):
    skills: list[str]
    normalized_skills: list[str]


@router.post("/extract", response_model=SkillExtractResponse)
def extract_skills(payload: SkillExtractRequest) -> SkillExtractResponse:
    result = extract_skills_from_text(payload.text)
    return SkillExtractResponse(
        skills=result.skills,
        normalized_skills=result.normalized_skills,
    )
