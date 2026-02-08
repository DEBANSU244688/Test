from app.services.match_score import calculate_match_score


def test_calculate_match_score_weighting() -> None:
    result = calculate_match_score(skills=80, tools=70, experience=60)
    assert result.score == 72
    assert result.breakdown.skills == 80
    assert result.breakdown.tools == 70
    assert result.breakdown.experience == 60


def test_calculate_match_score_clamps_values() -> None:
    result = calculate_match_score(skills=200, tools=-20, experience=40)
    assert result.score == 62
    assert result.breakdown.skills == 100
    assert result.breakdown.tools == 0
    assert result.breakdown.experience == 40
