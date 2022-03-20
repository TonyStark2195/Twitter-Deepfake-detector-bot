# tweepy-bots/bots/config.py
import tweepy
import logging
import os

logger = logging.getLogger()


def create_api():
    # consumer_key = os.getenv("CONSUMER_KEY")
    # consumer_secret = os.getenv("CONSUMER_SECRET")
    # access_token = os.getenv("ACCESS_TOKEN")
    # access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    consumer_key = "k6jKdZo4K3sntrYKrNo7OXKRt"
    consumer_secret = "Ov00ZwC2o1tisCBMnkWc1VhE6549WdEKga5qfV9z8tLXDIJRNb"
    access_token = "1466577372371578884-9V3RNkYRkRhs7EEX7oZPA9qQchJj0v"
    access_token_secret = "qemvWMYEFQTS1EkDMaZ4YgKoRyUCHghjr2dU5Hqrh3rWf"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    # , wait_on_rate_limit_notify = True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
