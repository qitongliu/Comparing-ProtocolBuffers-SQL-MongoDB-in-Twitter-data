import twitter_pb2

tweets = twitter_pb2.Tweets()
f = open("twitter.pb", "rb")
tweets.ParseFromString(f.read())
f.close()

delnum = sum(tw.is_delete for tw in tweets.tweets)
repnum = sum(1 for tw in tweets.tweets if tw.insert.reply_to)
twnum = {}
for tw in tweets.tweets:
    if not tw.is_delete:
        uid = tw.insert.uid
        if uid in twnum:
            twnum[uid] += 1
        else:
            twnum[uid] = 1
ids = [k for k,v in sorted(twnum.items(), key=lambda(k, v): (-v, k))][0:5]
print 'The number of deleted messages: {0}'.format(delnum)
print 'The number of tweets that are replies to another tweet: {0}'.format(repnum)
print 'The five user IDs that have tweeted the most: ' + ', '.join(map(str,ids))