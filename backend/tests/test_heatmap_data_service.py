from app.services.heatmap_data import build_heatmap_data


def test_build_heatmap_data_shape() -> None:
    data = build_heatmap_data()
    assert len(data) >= 5
    for item in data:
        assert item.skill
        assert 0 <= item.current_level <= 100
        assert 0 <= item.target_level <= 100
        assert item.status in {"strong", "moderate", "weak"}
