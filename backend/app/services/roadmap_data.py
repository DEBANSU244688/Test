from dataclasses import dataclass


@dataclass(frozen=True)
class RoadmapMilestone:
    month: int
    focus_skill: str
    target: str
    certification: str
    progress: int


def generate_roadmap() -> list[RoadmapMilestone]:
    """Return an initial six-month roadmap scaffold."""
    return [
        RoadmapMilestone(1, "Python & DSA", "Solve 40 interview problems", "NPTEL Problem Solving", 15),
        RoadmapMilestone(2, "SQL & Data Modeling", "Build analytics mini-project", "Coursera SQL for Data Science", 10),
        RoadmapMilestone(3, "Backend APIs", "Ship 3 FastAPI endpoints", "FastAPI Advanced Concepts", 8),
        RoadmapMilestone(4, "System Design", "Design 2 scalable systems", "Grokking System Design", 5),
        RoadmapMilestone(5, "Cloud Deployment", "Deploy full-stack app on cloud", "AWS Cloud Practitioner", 0),
        RoadmapMilestone(6, "Interview Readiness", "Mock interviews + portfolio polish", "Interview Masterclass", 0),
    ]
