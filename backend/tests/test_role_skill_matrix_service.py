from app.services.role_skill_matrix import build_role_skill_matrix


def test_build_role_skill_matrix_computes_weighted_rows() -> None:
    matrix = build_role_skill_matrix(
        role="Backend Engineer",
        extracted_skills=["Python", "SQL", "Python", "Docker", "SQL", "Python"],
    )

    assert matrix.role == "backend engineer"
    assert [row.skill for row in matrix.rows] == ["python", "sql", "docker"]
    assert matrix.rows[0].frequency == 3
    assert matrix.rows[0].weighted_score > matrix.rows[1].weighted_score
