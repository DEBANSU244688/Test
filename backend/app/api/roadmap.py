from fastapi import APIRouter
from pydantic import BaseModel

from app.services.roadmap_data import generate_roadmap

router = APIRouter(prefix="/roadmap", tags=["roadmap"])


class RoadmapMilestoneResponse(BaseModel):
    month: int
    focus_skill: str
    target: str
    certification: str
    progress: int


@router.get("/generate", response_model=list[RoadmapMilestoneResponse])
def get_roadmap() -> list[RoadmapMilestoneResponse]:
    milestones = generate_roadmap()
    return [
        RoadmapMilestoneResponse(
            month=item.month,
            focus_skill=item.focus_skill,
            target=item.target,
            certification=item.certification,
            progress=item.progress,
        )
        for item in milestones
    ]
