from dataclasses import dataclass


@dataclass(frozen=True)
class CourseRecommendation:
    title: str
    provider: str
    duration_weeks: int
    roi_score: float
    skill_outcome: str
    recommended: bool


def get_course_recommendations() -> list[CourseRecommendation]:
    """Return starter certification/course recommendations sorted by ROI."""
    return [
        CourseRecommendation(
            title="AWS Cloud Practitioner",
            provider="Coursera",
            duration_weeks=6,
            roi_score=9.1,
            skill_outcome="Cloud deployment fundamentals",
            recommended=True,
        ),
        CourseRecommendation(
            title="System Design Essentials",
            provider="Educative",
            duration_weeks=8,
            roi_score=8.7,
            skill_outcome="Design scalable backend systems",
            recommended=True,
        ),
        CourseRecommendation(
            title="Advanced SQL for Analytics",
            provider="NPTEL",
            duration_weeks=4,
            roi_score=8.2,
            skill_outcome="Query optimization and modeling",
            recommended=False,
        ),
    ]
