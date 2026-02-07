import requests

HN_TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"


def fetch_top_story_ids(limit=30):
    response=requests.get(HN_TOP_STORIES_URL)
    response.raise_for_status()
    return response.json()[:limit]


def fetch_story(story_id):
    response = requests.get(HN_ITEM_URL.format(story_id))
    response.raise_for_status()
    return response.json()


def fetch_top_stories(limit=30):
    stories = []
    for sid in fetch_top_story_ids(limit):
        story = fetch_story(sid)
        if story and story.get("type") == "story":
            stories.append(story)
    return stories


