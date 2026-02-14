from dataclasses import dataclass

from app.services.market_demand_data import get_market_demand_scores


@dataclass(frozen=True)
class SkillGap:
    skill: str
    severity: str
    recommendation: str


@dataclass(frozen=True)
class FutureProofSkill:
    skill: str
    trend_score: float
    rationale: str


@dataclass(frozen=True)
class HeatmapDataPoint:
    skill: str
    current_level: int
    target_level: int
    demand_weight: float
    status: str


@dataclass(frozen=True)
class GapAnalysisResult:
    match_percent: int
    missing_skills: list[str]
    weak_skills: list[str]
    future_proof_skills: list[FutureProofSkill]
    heatmap_data: list[HeatmapDataPoint]
    gaps: list[SkillGap]


def analyze_skill_gaps(
    resume_skills: list[str],
    job_skills: list[str],
    resume_skill_levels: dict[str, int] | None = None,
) -> GapAnalysisResult:
    demand_scores = get_market_demand_scores()
    normalized_resume = {skill.strip().lower() for skill in resume_skills if skill.strip()}
    normalized_job = [skill.strip().lower() for skill in job_skills if skill.strip()]
    normalized_levels = _normalize_skill_levels(resume_skill_levels)

    if not normalized_job:
        return GapAnalysisResult(
            match_percent=100,
            missing_skills=[],
            weak_skills=[],
            future_proof_skills=[],
            heatmap_data=[],
            gaps=[],
        )

    unique_job = sorted(set(normalized_job))
    missing = [skill for skill in unique_job if skill not in normalized_resume]

    overlap_count = len(unique_job) - len(missing)
    match_percent = round((overlap_count / len(unique_job)) * 100)

    weak = _identify_weak_skills(unique_job, normalized_resume, normalized_levels)
    future_proof = _detect_future_proof_skills(unique_job, normalized_resume, demand_scores)
    heatmap_data = _build_heatmap_data(unique_job, normalized_resume, normalized_levels, demand_scores)

    gaps = [
        SkillGap(
            skill=skill,
            severity=_compute_severity(skill, unique_job),
            recommendation=f"Focus on building practical experience in {skill.title()}.",
        )
        for skill in missing
    ]

    return GapAnalysisResult(
        match_percent=match_percent,
        missing_skills=missing,
        weak_skills=weak,
        future_proof_skills=future_proof,
        heatmap_data=heatmap_data,
        gaps=gaps,
    )


def _normalize_skill_levels(levels: dict[str, int] | None) -> dict[str, int]:
    if not levels:
        return {}

    normalized: dict[str, int] = {}
    for skill, level in levels.items():
        key = skill.strip().lower()
        normalized[key] = max(0, min(int(level), 100))
    return normalized


def _identify_weak_skills(
    job_skills: list[str],
    resume_skills: set[str],
    resume_skill_levels: dict[str, int],
) -> list[str]:
    overlap = sorted(skill for skill in job_skills if skill in resume_skills)

    if resume_skill_levels:
        return [skill for skill in overlap if resume_skill_levels.get(skill, 100) < 70]

    weak_count = max(0, len(job_skills) // 3)
    return overlap[:weak_count]


def _detect_future_proof_skills(
    job_skills: list[str],
    resume_skills: set[str],
    demand_scores: dict[str, float],
) -> list[FutureProofSkill]:
    candidates = sorted(
        {skill for skill in job_skills if skill in demand_scores and skill not in resume_skills},
        key=lambda skill: demand_scores[skill],
        reverse=True,
    )

    return [
        FutureProofSkill(
            skill=skill,
            trend_score=demand_scores[skill],
            rationale=f"{skill.title()} shows sustained market demand and long-term role relevance.",
        )
        for skill in candidates[:3]
    ]


def _build_heatmap_data(
    job_skills: list[str],
    resume_skills: set[str],
    resume_skill_levels: dict[str, int],
    demand_scores: dict[str, float],
) -> list[HeatmapDataPoint]:
    points: list[HeatmapDataPoint] = []
    for skill in job_skills:
        if skill in resume_skill_levels:
            current = resume_skill_levels[skill]
        elif skill in resume_skills:
            current = 65
        else:
            current = 40

        demand = demand_scores.get(skill, 0.75)
        target = 85 if demand >= 0.88 else 75
        gap = max(0, target - current)
        status = "strong" if gap <= 10 else "moderate" if gap <= 25 else "weak"

        points.append(
            HeatmapDataPoint(
                skill=skill,
                current_level=current,
                target_level=target,
                demand_weight=demand,
                status=status,
            )
        )

    return points


def _compute_severity(skill: str, job_skills: list[str]) -> str:
    priority_skills = {"python", "sql", "system design", "docker", "aws", "kubernetes"}
    if skill in priority_skills:
        return "high"

    scarcity_ratio = len(job_skills) / max(1, len(set(job_skills)))
    if scarcity_ratio > 1.2:
        return "medium"

    return "low"
