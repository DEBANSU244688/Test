from dataclasses import dataclass


@dataclass(frozen=True)
class MatchBreakdown:
    skills: int
    tools: int
    experience: int


@dataclass(frozen=True)
class MatchScoreResult:
    score: int
    breakdown: MatchBreakdown
    explanation: str


def calculate_match_score(skills: int, tools: int, experience: int) -> MatchScoreResult:
    """Calculate weighted match score from 0 to 100."""
    skills = max(0, min(skills, 100))
    tools = max(0, min(tools, 100))
    experience = max(0, min(experience, 100))

    weighted_score = round((skills * 0.5) + (tools * 0.2) + (experience * 0.3))
    explanation = (
        f"Score is weighted toward skills (50%), tools (20%), and experience (30%). "
        f"Your strongest area is {max((skills, 'skills'), (tools, 'tools'), (experience, 'experience'))[1]}."
    )
    return MatchScoreResult(
        score=weighted_score,
        breakdown=MatchBreakdown(skills=skills, tools=tools, experience=experience),
        explanation=explanation,
    )
