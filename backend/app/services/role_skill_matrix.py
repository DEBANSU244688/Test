from dataclasses import dataclass

from app.services.market_demand_data import get_market_demand_scores
from app.services.skill_frequency import build_skill_frequency


@dataclass(frozen=True)
class RoleSkillDemand:
    skill: str
    frequency: int
    demand_score: float
    weighted_score: float


@dataclass(frozen=True)
class RoleSkillMatrix:
    role: str
    rows: list[RoleSkillDemand]


def build_role_skill_matrix(role: str, extracted_skills: list[str]) -> RoleSkillMatrix:
    normalized_role = role.strip().lower()
    frequency = build_skill_frequency(extracted_skills)
    demand_scores = get_market_demand_scores()

    rows = [
        RoleSkillDemand(
            skill=skill,
            frequency=count,
            demand_score=demand_scores.get(skill, 0.75),
            weighted_score=round(count * demand_scores.get(skill, 0.75), 2),
        )
        for skill, count in frequency.items()
    ]

    rows.sort(key=lambda row: (-row.weighted_score, -row.frequency, row.skill))

    return RoleSkillMatrix(role=normalized_role, rows=rows)
