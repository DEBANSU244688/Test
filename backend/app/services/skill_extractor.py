from dataclasses import dataclass


@dataclass(frozen=True)
class SkillExtractionResult:
    skills: list[str]
    normalized_skills: list[str]


SKILL_ALIASES: dict[str, str] = {
    "js": "javascript",
    "ts": "typescript",
    "py": "python",
    "postgres": "postgresql",
    "node": "node.js",
}

KNOWN_SKILLS = {
    "python",
    "fastapi",
    "sql",
    "postgresql",
    "docker",
    "kubernetes",
    "aws",
    "javascript",
    "typescript",
    "node.js",
    "react",
    "machine learning",
    "deep learning",
}


def extract_skills_from_text(text: str) -> SkillExtractionResult:
    lowered = text.lower()
    raw_tokens = lowered.replace("/", " ").split()
    tokenized = {token.strip(".,;:!?()[]{}\"'`") for token in raw_tokens}
    tokenized.discard("")

    matched: set[str] = set()
    for skill in KNOWN_SKILLS:
        if " " in skill:
            if skill in lowered:
                matched.add(skill)
        elif skill in tokenized:
            matched.add(skill)

    for alias, canonical in SKILL_ALIASES.items():
        if alias in tokenized:
            matched.add(canonical)

    normalized = sorted(matched)

    return SkillExtractionResult(skills=normalized, normalized_skills=normalized)
