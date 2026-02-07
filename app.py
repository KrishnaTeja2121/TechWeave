from flask import Flask, render_template
from hn_client import fetch_top_stories
from relevance import relevance_score
from summarizer import summarize

app = Flask(__name__)

@app.route("/")
def index():
    stories = fetch_top_stories(30)
    ranked = sorted(stories, key=relevance_score, reverse=True)[:8]

    curated = []
    for s in ranked:
        curated.append({
            "title": s["title"],
            "url": s.get("url", "#"),
            "summary": summarize(s["title"])
        })

    return render_template("index.html", stories=curated)

if __name__ == "__main__":
    app.run(debug=True)
