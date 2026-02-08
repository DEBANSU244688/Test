from app.services.market_demand_analytics import build_market_demand_summary


def test_build_market_demand_summary_shape_and_ranges() -> None:
    summary = build_market_demand_summary()

    assert 0 <= summary.average_job_frequency <= 1
    assert 0 <= summary.average_growth_index <= 1
    assert 0 <= summary.average_salary_impact <= 1
    assert len(summary.top_growth_skills) == 3


def test_build_market_demand_summary_top_growth_is_deterministic() -> None:
    summary = build_market_demand_summary()
    assert summary.top_growth_skills == ["machine learning", "deep learning", "kubernetes"]
