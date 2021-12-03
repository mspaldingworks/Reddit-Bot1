import praw
import random

reddit = praw.Reddit(
    client_id="QJSd_L86JTCDXhlWDYbPSA",
    client_secret="w8bwUejROGLB7k5R9Z2DwEzMnmmjsw",
    user_agent="<console:Floopitydoop:1.0>"
    
)

subreddit = reddit.subreddit("conspiracy")

sad_quotes = ["string can be anything"]

for submission in subreddit.hot(limit=10):
    #print("**********")
    #print(submission.title)
    
    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment_lower = comment.body.lower()
            if " sad " in comment_lower:
                print("-----------")
                print(comment.body)
                random_index = random.randint(0, len(sad_quotes) - 1)
                comment.reply(sad_quotes[random_index])
