from app.services.job_parser import parse_job_description


def test_parse_job_description_extracts_skills_and_grouped_requirements() -> None:
    text = """
    We are hiring a backend engineer.
    Must have experience with Python, FastAPI, and SQL.
    Familiarity with Docker is required.
    You will design and maintain high-scale APIs.
    Nice to have: React.
    """

    parsed = parse_job_description(text)

    assert parsed.normalized_text.startswith("We are hiring a backend engineer")
    assert parsed.extracted_skills == ["docker", "fastapi", "python", "react", "sql"]
    assert len(parsed.extracted_requirements) == 3
    assert len(parsed.requirement_groups.must_have) == 2
    assert len(parsed.requirement_groups.preferred) == 1
    assert len(parsed.requirement_groups.responsibilities) == 1
