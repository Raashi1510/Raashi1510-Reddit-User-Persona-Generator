import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="persona-script"
)

def scrape_user_data(username):
    redditor = reddit.redditor(username)
    posts = []
    comments = []

    try:
        for post in redditor.submissions.new(limit=20):
            posts.append(f"Post: {post.title} - {post.selftext}")
    except Exception as e:
        print(f"[ERROR] Fetching posts: {e}")

    try:
        for comment in redditor.comments.new(limit=20):
            comments.append(f"Comment: {comment.body}")
    except Exception as e:
        print(f"[ERROR] Fetching comments: {e}")

    return {"posts": posts, "comments": comments}
