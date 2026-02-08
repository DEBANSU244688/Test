from app.services.skill_extractor import extract_skills_from_text


def test_extract_skills_from_text_matches_known_and_alias_skills() -> None:
    text = "Python, FastAPI, SQL, JS, and postgres experience. Nice to have machine learning."

    result = extract_skills_from_text(text)

    assert result.skills == [
        "fastapi",
        "javascript",
        "machine learning",
        "postgresql",
        "python",
        "sql",
    ]
    assert result.normalized_skills == result.skills
