from app.services.job_templates import get_job_role_template, list_job_role_templates


def test_list_job_role_templates_returns_seeded_roles() -> None:
    templates = list_job_role_templates()
    assert len(templates) >= 3
    assert templates[0].role == "backend engineer"


def test_get_job_role_template_case_insensitive_lookup() -> None:
    template = get_job_role_template("Backend Engineer")
    assert template is not None
    assert "python" in template.core_skills
