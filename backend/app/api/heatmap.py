from fastapi import APIRouter
from pydantic import BaseModel

from app.services.heatmap_data import build_heatmap_data

router = APIRouter(prefix="/heatmap", tags=["heatmap"])


class HeatmapSkillResponse(BaseModel):
    skill: str
    current_level: int
    target_level: int
    demand_weight: float
    status: str


@router.get("/data", response_model=list[HeatmapSkillResponse])
def get_heatmap_data() -> list[HeatmapSkillResponse]:
    skills = build_heatmap_data()
    return [
        HeatmapSkillResponse(
            skill=item.skill,
            current_level=item.current_level,
            target_level=item.target_level,
            demand_weight=item.demand_weight,
            status=item.status,
        )
        for item in skills
    ]
