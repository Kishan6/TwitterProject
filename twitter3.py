import tweepy

# Replace the API_KEY and API_SECRET with your application's key and secret.
consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

import sys
import jsonpickle
import os

searchQuery = ''  # this is what we're searching for
maxTweets = 300000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = 'xxxxxxxxx.txt' # We'll store the tweets in a text file.


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None


places = []
time = []
tweets = []

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))

with open(fName, 'w') as f:
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, lang="en", tweet_mode = 'extended')
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId, lang="en", tweet_mode = 'extended')
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1), lang="en", tweet_mode = 'extended')
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId, lang="en", tweet_mode = 'extended')
            if not new_tweets:
                
                print("No more tweets found")
                break
            for tweet in new_tweets:
                
                #add data to lists
                if tweet.full_text[:3] == "RT " or (tweet.full_text in tweets):
                    continue
                tweetCount += 1
                
                #1. creted at
                time.append((tweet.created_at.month,tweet.created_at.year))
                
                #location of user
                places.append(tweet.user.location)
                
                #text of tweet
                tweets.append(tweet.full_text)
                
                f.write(jsonpickle.encode(tweet.user.id, unpicklable=False)
                    #+'\n' + jsonpickle.encode(tweet.full_text, unpicklable=False)
                    #+'\n' + jsonpickle.encode(tweet.entities['hashtags'], unpicklable=False)
                    +'\n' + jsonpickle.encode(tweet.user.verified, unpicklable=False)
                    +'\n' + jsonpickle.encode(tweet.user.description, unpicklable=False)
                    +'\n' + jsonpickle.encode(tweet.user.statuses_count, unpicklable=False)
                    +'\n' + jsonpickle.encode(tweet.user.followers_count, unpicklable=False)
                    +'\n' + jsonpickle.encode(tweet.user.friends_count, unpicklable=False)
                    +'\n' + jsonpickle.encode(tweet.user.favourites_count, unpicklable=False)
                    +'\n' + jsonpickle.encode(tweet.created_at, unpicklable=False)
                    # +'\n' + jsonpickle.encode(tweet.text, unpicklable=False)
                    # +'\n' + jsonpickle.encode(tweet.text, unpicklable=False) 
                    # +'\n' + jsonpickle.encode(tweet.text, unpicklable=False)
                    # +'\n' + jsonpickle.encode(tweet.text, unpicklable=False)
                    # +'\n' + jsonpickle.encode(tweet.text, unpicklable=False)
                    # +'\n' + jsonpickle.encode(tweet.text, unpicklable=False)
                    + '\n\n')
                
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))
