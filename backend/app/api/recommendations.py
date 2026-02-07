from fastapi import APIRouter
from pydantic import BaseModel

from app.services.course_recommendations import get_course_recommendations

router = APIRouter(prefix="/recommendations", tags=["recommendations"])


class CourseRecommendationResponse(BaseModel):
    title: str
    provider: str
    duration_weeks: int
    roi_score: float
    skill_outcome: str
    recommended: bool


@router.get("/courses", response_model=list[CourseRecommendationResponse])
def list_course_recommendations() -> list[CourseRecommendationResponse]:
    courses = get_course_recommendations()
    return [
        CourseRecommendationResponse(
            title=item.title,
            provider=item.provider,
            duration_weeks=item.duration_weeks,
            roi_score=item.roi_score,
            skill_outcome=item.skill_outcome,
            recommended=item.recommended,
        )
        for item in courses
    ]
