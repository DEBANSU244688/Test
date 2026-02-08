from app.services.course_recommendations import get_course_recommendations


def test_recommendations_are_ranked() -> None:
    courses = get_course_recommendations()
    assert len(courses) >= 3
    assert courses[0].roi_score >= courses[1].roi_score


def test_recommendations_have_valid_fields() -> None:
    courses = get_course_recommendations()
    for course in courses:
        assert course.title
        assert course.provider
        assert course.duration_weeks > 0
        assert 0 <= course.roi_score <= 10
