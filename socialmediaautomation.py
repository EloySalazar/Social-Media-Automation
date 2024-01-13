import tweepy

# Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def post_on_twitter(content):
    try:
        # Post a tweet
        api.update_status(content)
        print("Tweet posted successfully!")
    except tweepy.TweepError as e:
        print(f"Error occurred while posting a tweet: {str(e)}")

# Content to be posted
tweet_content = "Hello, Twitter! This is an automated tweet using the Python Tweepy library. #Python #Tweepy"

# Post the content on Twitter
post_on_twitter(tweet_content)