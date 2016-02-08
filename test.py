import tw
import sys
from functools import wraps


def error_check(func):
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
            print("E\n")
            print(str(e) + "\n")
    return inner


class Test:

    passed_tests = 0
    failed_tests = 0
    tw = tw.Twitter()

    rate_limit = tw.get_twitter().rate_limit_status()
    if rate_limit['resources']['statuses']['/statuses/user_timeline']['remaining'] == 0:
        print("You have reached your rate limit")
        sys.exit(1)

    def __init__(self):
        print("Running tests")
        print("test_get_tweets:\t\t", end="")

        self.test_get_tweets()

        print("test_post_tweets:\t\t", end="")
        self.test_post_tweet()

        print("test_delete_tweets:\t\t", end="")
        self.test_delete_tweet()

        print("Tests are finished {} passed and {} failed".format(str(self.passed_tests), str(self.failed_tests)))

        # self.cleanup()

    @error_check
    def test_get_tweets(self):

        # Retrive the tweets
        tweets = self.tw.get_tweets()

        # Check the tweets are not empty

        if tweets is not None:
            print("P")
            self.passed_tests += 1
        else:
            print("F")
            self.failed_tests += 1

    @error_check
    def test_post_tweet(self):
        before = len(self.tw.get_tweets())
        self.tw.post_tweet("This tweet was generated in the test")
        after = len(self.tw.get_tweets())
        if before + 1 == after:
            print("P")
            self.passed_tests += 1
        else:
            print("F: Before:\t{}\tAfter:\t{}".format(str(before), str(after)))
            self.failed_tests += 1

    def test_delete_tweet(self):
        tweets = self.tw.get_twitter().user_timeline(count=1)[0]
        before = len(self.tw.get_tweets())
        self.tw.delete_tweet(tweets.id)
        after = len(self.tw.get_tweets())

        if before == after + 1:
            print("P")
            self.passed_tests += 1
        else:
            print("F: Before:\t{}\tAfter:\t{}".format(str(before), str(after)))
            self.failed_tests += 1


    def cleanup(self):
        t = tw.Twitter().get_twitter()
        last_tweet = t.user_timeline(count=1)[0]
        try:
            t.destroy_status(last_tweet.id)
        except Exception as e:
            print("Cleanup failed: " + str(e))
            pass


if __name__ == '__main__':
    print("Running...")
    Test()
