from reddit2telegram.reddit import Reddit
from reddit2telegram.telegram import Telegram


SUBREDDIT = "Arrasio"
CHANNEL = "@Arras_io"


def main():
    reddit = Reddit(SUBREDDIT)
    telegram = Telegram(CHANNEL)

    for submission in reddit.hot():
        telegram.send_submission(submission)


if __name__ == "__main__":
    main()