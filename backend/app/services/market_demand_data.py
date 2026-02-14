from dataclasses import dataclass
from datetime import datetime, timedelta, timezone


@dataclass(frozen=True)
class SkillDemandRecord:
    skill: str
    job_frequency: float
    growth_index: float
    salary_impact: float


@dataclass(frozen=True)
class DemandUpdateSchedule:
    last_updated_at: datetime
    next_update_at: datetime
    refresh_interval_hours: int


REFRESH_INTERVAL_HOURS = 24 * 7


DATASET: list[SkillDemandRecord] = [
    SkillDemandRecord("python", 0.92, 0.9, 0.88),
    SkillDemandRecord("sql", 0.89, 0.83, 0.82),
    SkillDemandRecord("docker", 0.81, 0.86, 0.85),
    SkillDemandRecord("kubernetes", 0.75, 0.93, 0.9),
    SkillDemandRecord("aws", 0.84, 0.9, 0.89),
    SkillDemandRecord("machine learning", 0.7, 0.97, 0.94),
    SkillDemandRecord("deep learning", 0.62, 0.95, 0.92),
    SkillDemandRecord("fastapi", 0.58, 0.8, 0.77),
    SkillDemandRecord("react", 0.82, 0.79, 0.81),
    SkillDemandRecord("typescript", 0.8, 0.84, 0.83),
]


def get_market_demand_scores() -> dict[str, float]:
    """Return weighted market-demand scores indexed by normalized skill name."""
    scores: dict[str, float] = {}
    for item in DATASET:
        score = (item.job_frequency * 0.45) + (item.growth_index * 0.35) + (item.salary_impact * 0.2)
        scores[item.skill] = round(score, 2)
    return scores


def get_demand_update_schedule(reference_time: datetime | None = None) -> DemandUpdateSchedule:
    """Return periodic update timing metadata for demand dataset refreshes."""
    now = reference_time.astimezone(timezone.utc) if reference_time else datetime.now(timezone.utc)
    next_update = now + timedelta(hours=REFRESH_INTERVAL_HOURS)
    return DemandUpdateSchedule(
        last_updated_at=now,
        next_update_at=next_update,
        refresh_interval_hours=REFRESH_INTERVAL_HOURS,
    )
