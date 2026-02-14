from datetime import datetime, timedelta, timezone

from app.services.market_demand_data import (
    DATASET,
    REFRESH_INTERVAL_HOURS,
    get_demand_update_schedule,
    get_market_demand_scores,
)


def test_market_demand_dataset_structure() -> None:
    assert len(DATASET) >= 8
    assert all(record.skill for record in DATASET)


def test_market_demand_scores_are_normalized() -> None:
    scores = get_market_demand_scores()
    assert "python" in scores
    assert all(0 <= score <= 1 for score in scores.values())


def test_demand_update_schedule_uses_weekly_interval() -> None:
    reference = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)
    schedule = get_demand_update_schedule(reference)

    assert schedule.last_updated_at == reference
    assert schedule.refresh_interval_hours == REFRESH_INTERVAL_HOURS
    assert schedule.next_update_at == reference + timedelta(hours=REFRESH_INTERVAL_HOURS)
