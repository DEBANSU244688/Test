from dataclasses import dataclass


@dataclass(frozen=True)
class RequirementGroups:
    must_have: list[str]
    preferred: list[str]
    responsibilities: list[str]


@dataclass(frozen=True)
class ParsedJobDescription:
    normalized_text: str
    extracted_skills: list[str]
    extracted_requirements: list[str]
    requirement_groups: RequirementGroups


KNOWN_SKILLS = {
    "python",
    "fastapi",
    "sql",
    "docker",
    "kubernetes",
    "aws",
    "machine learning",
    "deep learning",
    "pandas",
    "numpy",
    "react",
    "typescript",
}


def parse_job_description(text: str) -> ParsedJobDescription:
    normalized_text = " ".join(text.split()).strip()
    lowered = normalized_text.lower()

    skills = sorted(skill for skill in KNOWN_SKILLS if skill in lowered)
    requirement_groups = _extract_requirement_groups(normalized_text)
    requirements = requirement_groups.must_have + requirement_groups.preferred

    return ParsedJobDescription(
        normalized_text=normalized_text,
        extracted_skills=skills,
        extracted_requirements=requirements,
        requirement_groups=requirement_groups,
    )


def _extract_requirement_groups(text: str) -> RequirementGroups:
    sentences = _split_sentences(text)

    must_markers = ("must", "required", "proficient", "minimum")
    preferred_markers = ("nice to have", "preferred", "bonus", "plus")
    responsibility_markers = ("you will", "responsible", "build", "design", "maintain")

    must_have: list[str] = []
    preferred: list[str] = []
    responsibilities: list[str] = []

    for sentence in sentences:
        lowered = sentence.lower()
        if any(marker in lowered for marker in preferred_markers):
            preferred.append(sentence)
        elif any(marker in lowered for marker in must_markers):
            must_have.append(sentence)
        elif any(marker in lowered for marker in responsibility_markers):
            responsibilities.append(sentence)

    return RequirementGroups(
        must_have=must_have,
        preferred=preferred,
        responsibilities=responsibilities,
    )


def _split_sentences(text: str) -> list[str]:
    separators = [".", "\n", ";"]
    chunks = [text]

    for separator in separators:
        next_chunks: list[str] = []
        for chunk in chunks:
            next_chunks.extend(chunk.split(separator))
        chunks = next_chunks

    sentences: list[str] = []
    for chunk in chunks:
        cleaned = " ".join(chunk.split()).strip(" -")
        if cleaned:
            sentences.append(cleaned)

    return sentences
