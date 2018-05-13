import json

fname = '/tmp/tweets.json'
with open(fname, 'r') as f:
    tweet_info = []
    for line in f:
        try:
            tweet = json.loads(line)
            tweet_info.append(tweet)
        except:
            continue

user_name_list = list(map(lambda tweet: tweet['user']['screen_name'],
                          tweet_info))
tweet_list = list(map(lambda tweet: tweet['text'], tweet_info))
print(list(zip(user_name_list, tweet_list)))
