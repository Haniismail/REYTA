# importing necessairy laibrairies
import tweepy
import time

# Authentication from my twitter account
auth = tweepy.OAuthHandler('tg7nTWJTCxpyjqY8EgecL3le2',
                           'IpZr9XUxr6EL59TRH77tWgiC2bkfBkNSZXS3ZT2cpnTJiq0Ym9')
auth.set_access_token('1351899886724280320-k8XUtJdal2p6lW0B46bSJ9JKBH6bzw',
                      'e7hmXdtby5oNfYBtgCDS5N4zOVUO1B0n2HZ0a7Fzv8Fkm')

# Last seen ID is 1350591332528611328

# initiating the twitterbot APi
# wait limit so we dont get banned from twitter
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()


# Like and Retweet depending on a keyword
def KeywordLikeRetweet():
    search = ['']  # we choose the keyword here
    tweetsnumber = 4
    tweets = tweepy.Cursor(api.search, search).items(tweetsnumber)
    for tweet in tweets:
        try:
            print('Tweet about favorited')
            tweet.favorite()  # like the tweet
            tweet.retweet()  # retweet the tweet
            time.sleep(10)
        except tweepy.TweepError as e:
            # if there's an error we will know through the print(e.reason)
            print(e.reason)
        except StopIteration:
            break


# follow all my followers
def Followback():
    followers = tweepy.Cursor(api.followers).items()
    for follower in followers:
        if follower.followers_count > 1:
            follower.follow()
            if follower.follow() == True:
                print('I just followed someone back !')


# Retweet everything in feed
def LikeRetweetEverything():
    tweetNumber = 7
    tweets = tweepy.Cursor(api.home_timeline).items(tweetNumber)
    for tweet in tweets:
        try:
            tweet.retweet()
            print('Tweet retweeted')  # like the tweet
            tweet.favorite()
            print('Tweet favorited')  # retweet the tweet
        except tweepy.TweepError as e:
            # if there's an error we will know through the print(e.reason)
            print(e.reason)
            time.sleep(2)


# tells the name of the status writers which will be the ones who's tweets gonna be retweeted once the LikeRetweetEverything() function is called
def NameofstatusWriter():
    statuses = api.home_timeline(count=7)
    for status in statuses:
        print(status.user.screen_name)


# Calling the functions
NameofstatusWriter()
Followback()
LikeRetweetEverything()
input('Press ENTER to exit')
