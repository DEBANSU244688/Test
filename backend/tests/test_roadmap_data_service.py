from app.services.roadmap_data import generate_roadmap


def test_generate_roadmap_has_six_months() -> None:
    roadmap = generate_roadmap()
    assert len(roadmap) == 6
    assert roadmap[0].month == 1
    assert roadmap[-1].month == 6


def test_generate_roadmap_progress_range() -> None:
    roadmap = generate_roadmap()
    for item in roadmap:
        assert 0 <= item.progress <= 100
        assert item.focus_skill
        assert item.certification
