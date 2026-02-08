from dataclasses import dataclass


@dataclass(frozen=True)
class JobRoleTemplate:
    role: str
    summary: str
    core_skills: list[str]
    optional_skills: list[str]


_TEMPLATES: dict[str, JobRoleTemplate] = {
    "backend engineer": JobRoleTemplate(
        role="backend engineer",
        summary="Design and maintain APIs, data layers, and scalable services.",
        core_skills=["python", "fastapi", "sql", "docker"],
        optional_skills=["aws", "kubernetes", "system design"],
    ),
    "data analyst": JobRoleTemplate(
        role="data analyst",
        summary="Analyze business data and build reporting/insight pipelines.",
        core_skills=["sql", "python", "pandas", "data visualization"],
        optional_skills=["statistics", "excel", "machine learning"],
    ),
    "frontend engineer": JobRoleTemplate(
        role="frontend engineer",
        summary="Build user-facing web interfaces with strong UX and performance.",
        core_skills=["javascript", "typescript", "react", "css"],
        optional_skills=["next.js", "testing", "accessibility"],
    ),
}


def list_job_role_templates() -> list[JobRoleTemplate]:
    return [_TEMPLATES[key] for key in sorted(_TEMPLATES)]


def get_job_role_template(role: str) -> JobRoleTemplate | None:
    return _TEMPLATES.get(role.strip().lower())
