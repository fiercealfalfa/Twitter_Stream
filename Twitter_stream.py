#Streaming Data from Twitter
import tweepy

#Read API and Consumer Keys

keys_file = open('keys.txt','r')
token_list = keys_file.readlines()

#API and Consumer Keys
access_token = token_list[0]
access_token_secret = token_list[1]
consumer_key = token_list[2]
consumer_secret = token_list[3]






