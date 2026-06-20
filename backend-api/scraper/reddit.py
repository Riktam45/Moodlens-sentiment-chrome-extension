import praw

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="sentiment-extension"
)


def get_reddit_comments(url):

    submission = reddit.submission(url=url)

    submission.comments.replace_more(limit=0)

    comments = []

    for comment in submission.comments.list()[:100]:
        comments.append(comment.body)

    return comments