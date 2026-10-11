from config.roles import KEYWORD_THRESHOLD


def score_resume_for_role(text: str, keywords: list) -> tuple:
    text_lower = text.lower()
    matched = [kw for kw in keywords if kw in text_lower]
    return len(matched), matched


def assign_label(text: str, keywords: list, threshold: int = KEYWORD_THRESHOLD) -> int:
    count, _ = score_resume_for_role(text, keywords)
    return 1 if count >= threshold else 0


def get_missing_keywords(text: str, keywords: list, top_n: int = 10) -> list:
    text_lower = text.lower()
    missing = [kw for kw in keywords[:20] if kw not in text_lower]
    return missing[:top_n]
