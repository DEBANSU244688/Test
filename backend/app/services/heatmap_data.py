from dataclasses import dataclass


@dataclass(frozen=True)
class HeatmapSkill:
    skill: str
    current_level: int
    target_level: int
    demand_weight: float
    status: str


def build_heatmap_data() -> list[HeatmapSkill]:
    """Generate a starter demand-weighted heatmap data set."""
    return [
        HeatmapSkill("Python", 85, 90, 1.0, "strong"),
        HeatmapSkill("SQL", 70, 85, 0.9, "moderate"),
        HeatmapSkill("FastAPI", 62, 80, 0.8, "moderate"),
        HeatmapSkill("System Design", 45, 75, 0.95, "weak"),
        HeatmapSkill("Docker", 55, 78, 0.85, "weak"),
        HeatmapSkill("Cloud (AWS)", 40, 72, 0.92, "weak"),
    ]
