import tweepy
from functools import wraps


def post_method(func):
    """
    This is a decorator to try the function and return the error message if there is an
    error. This Allows the tests to complete if one has a problem, and also displays it
    nicely in the output terminal.
    """
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return False
    return inner


class Tweet(object):

    uname = None
    text = None
    image = None

    def __init__(self, tweet):
        self.uname = tweet.user.screen_name
        self.text = tweet.text
        self.image = tweet.user.profile_image_url
        print(self.image)


class Twitter:

    debug=False

    def __init__(self, debug=False):
        self.debug = debug

    def get_twitter(self):

        with open("/etc/pytwitter/config") as f:
            keys = []
            for lines in f:
                keys.append(lines)
            access_token = keys[0][:-1]
            access_token_secret = keys[1][:-1]
            consumer_key = keys[2][:-1]
            consumer_secret = keys[3][:-1]
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        t = tweepy.API(auth)
        return t


    def get_my_tweets(self, count=10):
        t = self.get_twitter()
        tweets = t.user_timeline(count=count)

        tweet_objects = []

        for tweet in tweets:

            tweet_obj = Tweet(tweet)
            tweet_objects.append(tweet_obj)

        if self.debug:
            for obj in tweet_objects:
                print(obj.text)
        return tweet_objects

    def get_all_tweets(self, count=10):
        t = self.get_twitter()
        tweets = t.home_timeline(count=count)

        tweet_objects = []

        for tweet in tweets:

            tweet_obj = Tweet(tweet)
            tweet_objects.append(tweet_obj)

        if self.debug:
            for obj in tweet_objects:
                print(obj.text)
        return tweet_objects

    @post_method
    def post_tweet(self, text):
        t = self.get_twitter()
        t.update_status(status=text)

    @post_method
    def delete_tweet(self, id):
        t = self.get_twitter()
        t.destroy_status(id)

