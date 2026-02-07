from hn_client import fetch_top_stories
from relevance import relevance_score
from summarizer import summarize

stories = fetch_top_stories(30)
ranked = sorted(stories, key=relevance_score, reverse=True)

print("\n🧠 Hacker News – Daily Brief\n")

for story in ranked[:5]:
    title = story["title"]
    url = story.get("url", "HN Discussion")
    summary = summarize(title)

    print(f"• {title}")
    print(f"  {summary}")
    print(f"  🔗 {url}\n")

