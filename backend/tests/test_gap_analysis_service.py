from app.services.gap_analysis import analyze_skill_gaps


def test_analyze_skill_gaps_returns_match_and_missing() -> None:
    result = analyze_skill_gaps(
        resume_skills=["Python", "FastAPI", "SQL"],
        job_skills=["Python", "SQL", "Docker", "AWS"],
    )

    assert result.match_percent == 50
    assert result.missing_skills == ["aws", "docker"]
    assert all(gap.severity in {"high", "medium", "low"} for gap in result.gaps)


def test_analyze_skill_gaps_uses_levels_for_weak_skills() -> None:
    result = analyze_skill_gaps(
        resume_skills=["Python", "FastAPI", "SQL"],
        job_skills=["Python", "FastAPI", "SQL", "Docker"],
        resume_skill_levels={"python": 85, "fastapi": 62, "sql": 66},
    )

    assert result.weak_skills == ["fastapi", "sql"]


def test_analyze_skill_gaps_detects_future_proof_skills() -> None:
    result = analyze_skill_gaps(
        resume_skills=["Python", "SQL"],
        job_skills=["Python", "SQL", "Docker", "Kubernetes", "Machine Learning"],
    )

    skills = [item.skill for item in result.future_proof_skills]
    assert len(skills) == 3
    assert set(skills) == {"kubernetes", "machine learning", "docker"}


def test_analyze_skill_gaps_generates_heatmap_data_structure() -> None:
    result = analyze_skill_gaps(
        resume_skills=["Python", "SQL"],
        job_skills=["Python", "SQL", "Docker"],
        resume_skill_levels={"python": 88, "sql": 64},
    )

    assert len(result.heatmap_data) == 3
    assert result.heatmap_data[0].skill == "docker"
    assert result.heatmap_data[0].status in {"strong", "moderate", "weak"}


def test_analyze_skill_gaps_handles_empty_job_skills() -> None:
    result = analyze_skill_gaps(resume_skills=["Python"], job_skills=[])
    assert result.match_percent == 100
    assert result.missing_skills == []
    assert result.gaps == []
