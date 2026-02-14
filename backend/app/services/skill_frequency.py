from collections import Counter


STOPWORDS = {
    "and",
    "or",
    "with",
    "for",
    "the",
    "a",
    "an",
    "to",
    "in",
    "of",
    "is",
    "are",
    "required",
    "must",
    "have",
}


def build_skill_frequency(skills: list[str]) -> dict[str, int]:
    normalized = [skill.strip().lower() for skill in skills if skill.strip()]
    filtered = [skill for skill in normalized if skill not in STOPWORDS]
    return dict(sorted(Counter(filtered).items(), key=lambda item: (-item[1], item[0])))
