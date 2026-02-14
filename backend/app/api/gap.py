from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.services.gap_analysis import analyze_skill_gaps

router = APIRouter(prefix="/gap", tags=["gap"])


class GapAnalyzeRequest(BaseModel):
    resume_skills: list[str] = Field(default_factory=list)
    job_skills: list[str] = Field(min_length=1)
    resume_skill_levels: dict[str, int] = Field(default_factory=dict)


class SkillGapResponse(BaseModel):
    skill: str
    severity: str
    recommendation: str


class FutureProofSkillResponse(BaseModel):
    skill: str
    trend_score: float
    rationale: str


class HeatmapDataPointResponse(BaseModel):
    skill: str
    current_level: int
    target_level: int
    demand_weight: float
    status: str


class GapAnalyzeResponse(BaseModel):
    match_percent: int
    missing_skills: list[str]
    weak_skills: list[str]
    future_proof_skills: list[FutureProofSkillResponse]
    heatmap_data: list[HeatmapDataPointResponse]
    gaps: list[SkillGapResponse]


@router.post("/analyze", response_model=GapAnalyzeResponse)
def analyze_gap(payload: GapAnalyzeRequest) -> GapAnalyzeResponse:
    result = analyze_skill_gaps(
        resume_skills=payload.resume_skills,
        job_skills=payload.job_skills,
        resume_skill_levels=payload.resume_skill_levels,
    )
    return GapAnalyzeResponse(
        match_percent=result.match_percent,
        missing_skills=result.missing_skills,
        weak_skills=result.weak_skills,
        future_proof_skills=[
            FutureProofSkillResponse(
                skill=item.skill,
                trend_score=item.trend_score,
                rationale=item.rationale,
            )
            for item in result.future_proof_skills
        ],
        heatmap_data=[
            HeatmapDataPointResponse(
                skill=item.skill,
                current_level=item.current_level,
                target_level=item.target_level,
                demand_weight=item.demand_weight,
                status=item.status,
            )
            for item in result.heatmap_data
        ],
        gaps=[
            SkillGapResponse(
                skill=item.skill,
                severity=item.severity,
                recommendation=item.recommendation,
            )
            for item in result.gaps
        ],
    )
