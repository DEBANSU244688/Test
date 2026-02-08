from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field

from app.services.job_parser import parse_job_description
from app.services.job_templates import get_job_role_template, list_job_role_templates

router = APIRouter(prefix="/job", tags=["job"])


class JobParseRequest(BaseModel):
    text: str = Field(min_length=1, description="Raw job description text")


class RequirementGroupsResponse(BaseModel):
    must_have: list[str]
    preferred: list[str]
    responsibilities: list[str]


class JobParseResponse(BaseModel):
    normalized_text: str
    extracted_skills: list[str]
    extracted_requirements: list[str]
    requirement_groups: RequirementGroupsResponse


class JobRoleTemplateResponse(BaseModel):
    role: str
    summary: str
    core_skills: list[str]
    optional_skills: list[str]


@router.post("/parse", response_model=JobParseResponse)
def parse_job(payload: JobParseRequest) -> JobParseResponse:
    parsed = parse_job_description(payload.text)
    return JobParseResponse(
        normalized_text=parsed.normalized_text,
        extracted_skills=parsed.extracted_skills,
        extracted_requirements=parsed.extracted_requirements,
        requirement_groups=RequirementGroupsResponse(
            must_have=parsed.requirement_groups.must_have,
            preferred=parsed.requirement_groups.preferred,
            responsibilities=parsed.requirement_groups.responsibilities,
        ),
    )


@router.get("/templates", response_model=list[JobRoleTemplateResponse])
def get_job_templates(role: str | None = Query(default=None)) -> list[JobRoleTemplateResponse]:
    if role:
        template = get_job_role_template(role)
        if template is None:
            raise HTTPException(status_code=404, detail="Role template not found")
        return [
            JobRoleTemplateResponse(
                role=template.role,
                summary=template.summary,
                core_skills=template.core_skills,
                optional_skills=template.optional_skills,
            )
        ]

    templates = list_job_role_templates()
    return [
        JobRoleTemplateResponse(
            role=item.role,
            summary=item.summary,
            core_skills=item.core_skills,
            optional_skills=item.optional_skills,
        )
        for item in templates
    ]
