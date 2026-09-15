import os
import praw

reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent="personal-reddit-scheduler/1.0"
)

print("Connected to Reddit API")
print("Authenticated:", reddit.user.me())
