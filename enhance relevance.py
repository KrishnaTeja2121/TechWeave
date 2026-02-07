from memory import load_memory

memory = load_memory()

def relevance_score(story):
    score = 0
    title = story.get("title", "").lower()
    url = story.get("url", "") or ""

    for kw in memory.get("ignored_keywords", []):
        if kw in title:
            return -10  # suppress hard

    for domain in memory.get("liked_domains", []):
        if domain in url:
            score += 5

    # existing logic continues...
