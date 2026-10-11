import re

STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "is", "are", "was", "were", "be", "been", "have", "has",
    "had", "do", "does", "did", "will", "would", "could", "should", "may",
    "might", "shall", "can", "this", "that", "these", "those", "it", "its",
    "we", "our", "you", "your", "they", "their", "he", "she", "his", "her",
    "i", "my", "me", "us", "him", "them", "from", "by", "as", "into",
    "about", "not", "no", "so", "if", "than", "then", "when", "where",
    "which", "who", "how"
}


def clean_text(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    tokens = [w for w in text.split() if len(w) > 2 and w not in STOP_WORDS]
    return " ".join(tokens)
