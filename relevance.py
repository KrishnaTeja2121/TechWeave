IMPORTANT_KEYWORDS = [
    "ai", "llm", "distributed", "database",
    "testing", "cloud", "open source"
]

IMPORTANT_DOMAINS = [
    "github.com",
    "arxiv.org"
]

def relevance_score(story):
    score = 0

    title = story.get("title", "").lower()
    url = story.get("url", "") or ""

    for kw in IMPORTANT_KEYWORDS:
        if kw in title:
            score += 2

    for domain in IMPORTANT_DOMAINS:
        if domain in url:
            score += 3

    score += min(story.get("score", 0) // 50, 5)
    score += min(story.get("descendants", 0) // 20, 5)

    return score


