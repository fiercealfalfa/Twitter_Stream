#Streaming Data from Twitter
import tweepy
from tweepy.streaming import StreamListener
from keys import twitter_keys

#API and Consumer Keys
access_token = twitter_keys['a_token']
access_token_secret = twitter_keys['a_token_s']
consumer_key = twitter_keys['c_key']
consumer_secret = twitter_keys['c_secret']

#prints tweets to console
class StdOutListener(StreamListener):
	def on_data(self, data):
		print data
		return True
	def on_error(self, status):
		print status
		return True

#Program Starts here
if __name__ == '__main__':
	#Authentication
	needs_auth = StdOutListener()
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = tweepy.Stream(auth, needs_auth)
		
	#Here is the filter
	stream.filter(track = ["the"])




