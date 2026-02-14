from app.services.skill_frequency import build_skill_frequency


def test_build_skill_frequency_counts_and_sorts() -> None:
    skills = ["Python", "SQL", "python", "Docker", "sql", "and", "Python"]

    result = build_skill_frequency(skills)

    assert result == {"python": 3, "sql": 2, "docker": 1}
