import os

import praw

def reddit_post(post_title, post_text, subreddit):
    reddit = praw.Reddit(
        client_id= os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        password=os.getenv("REDDIT_PASSWORD"),
        user_agent = os.getenv("REDDIT_USER_AGENT"),
        username=os.getenv("REDDIT_USERNAME"),
    )

    try:
        reddit.subreddit(subreddit).submit(post_title, selftext=post_text)
        print("Post sent successfully!")
    except Exception as e:
        print("Error sending post: {}".format(e))