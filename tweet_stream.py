import my_credential
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


class TweetStream():
    def __init__(self):
        pass

    def streaming_tweet(self, tweet_file, track_keyword):
        listener = FetchTweet(tweet_file)
        auth = OAuthHandler(my_credential.CONSUMER_KEY,
                            my_credential.CONSUMER_SECRET)
        auth.set_access_token(my_credential.ACCESS_TOKEN,
                              my_credential.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        stream.filter(track=track_keyword)


class FetchTweet(StreamListener):
    def __init__(self, tweet_file):
        self.tweet_file = tweet_file

    def on_data(self, data):
        try:
            # import ipdb; ipdb.set_trace()
            with open(self.tweet_file, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print('Error on_data %s' % str(e))
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    track_keyword = ['Amit Shah', 'Narendra Modi', 'India']
    tweet_file = '/tmp/tweets.json'

    streamer = TweetStream()
    streamer.streaming_tweet(tweet_file, track_keyword)
