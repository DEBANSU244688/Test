from dataclasses import dataclass
import re


@dataclass(frozen=True)
class JobPostRecord:
    role: str
    description: str


COMMON_SKILLS = {
    "python",
    "sql",
    "docker",
    "kubernetes",
    "aws",
    "fastapi",
    "machine learning",
    "deep learning",
    "react",
    "typescript",
}


def ingest_job_posts(posts: list[JobPostRecord]) -> dict[str, int]:
    aggregated: dict[str, int] = {}

    for post in posts:
        skills = _extract_skills(post.description)
        for skill in skills:
            aggregated[skill] = aggregated.get(skill, 0) + 1

    return dict(sorted(aggregated.items(), key=lambda item: (-item[1], item[0])))


def _extract_skills(description: str) -> set[str]:
    lowered = description.lower()
    raw_tokens = re.findall(r"[a-zA-Z0-9.+#-]+", lowered)
    tokenized = {token.strip(".,;:!?()[]{}\"'`") for token in raw_tokens}
    tokenized.discard("")

    extracted: set[str] = set()
    for skill in COMMON_SKILLS:
        if " " in skill and skill in lowered:
            extracted.add(skill)
        elif skill in tokenized:
            extracted.add(skill)

    return extracted
