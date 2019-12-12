import mysql.connector
from mysql.connector import Error
import tweepy
import json
from dateutil import parser
import time
import os

consumer_key = 'RC2Kl8eVrzz1wEd7vIJLKbPWX'
consumer_secret = '9TC1hx6wdJLvfss5AW8NF8I6TmIuchHS9rXmt2752iaStKSHeH'
access_token = '956451552633397248-Xc3E5KMwUOBe7I2fHisHLYUnnDmiFuS'
access_token_secret = '7o7xZmNobDfeNWq0x8PSlIOwvyWpRQJSsZtAzZKAO99Hl'
password = 'february122000'


def connect(username, created_at, tweet, retweet_count, place , location):
	"""
	connect to MySQL database and insert twitter data
	"""
	try:
		con = mysql.connector.connect(host = 'localhost',
		database='twitterdb', user='root', password = password, charset = 'utf8')
		

		if con.is_connected():
			"""
			Insert twitter data
			"""
			cursor = con.cursor()
			# twitter, golf
			query = "INSERT INTO Golf (username, created_at, tweet, retweet_count,place, location) VALUES (%s, %s, %s, %s, %s, %s)"
			cursor.execute(query, (username, created_at, tweet, retweet_count, place, location))
			con.commit()
		cursor.close()
		con.close()
			
			
	except Error as e:
		print(e)

	return


# Tweepy class to access Twitter API
class Streamlistener(tweepy.StreamListener):
	

	def on_connect(self):
		print("You are connected to the Twitter API")


	def on_error(self):
		if status_code != 200:
			print("error found")
			# returning false disconnects the stream
			return False

	"""
	This method reads in tweet data as Json
	and extracts the data we want.
	"""
	def on_data(self,data):
		
		try:
			raw_data = json.loads(data)

			if 'text' in raw_data:
				 
				username = raw_data['user']['screen_name']
				created_at = parser.parse(raw_data['created_at'])
				tweet = raw_data['text']
				retweet_count = raw_data['retweet_count']

				if raw_data['place'] is not None:
					place = raw_data['place']['country']
					print(place)
				else:
					place = None
				

				location = raw_data['user']['location']

				#insert data just collected into MySQL database
				print("User Name is: ")
				print(username)
				print("Created At: ")
				print(created_at)
				print("tweet:")
				print(tweet)
				print("retweet count is:")
				print(retweet_count)
				print("place is:")
				print(place)
				print("location is:")
				print(location)
				connect(username, created_at, tweet, retweet_count, place, location)
				print("Tweet colleted at: {} ".format(str(created_at)))
		except Error as e:
			print(e)


if __name__== '__main__':

	# # #Allow user input
	# track = []
	# while True:

	# 	input1  = input("what do you want to collect tweets on?: ")
	# 	track.append(input1)

	# 	input2 = input("Do you wish to enter another word? y/n ")
	# 	if input2 == 'n' or input2 == 'N':
	# 		break
	
	# print("You want to search for {}".format(track))
	# print("Initialising Connection to Twitter API....")
	# time.sleep(2)

	# authentification so we can access twitter
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api =tweepy.API(auth, wait_on_rate_limit=True)

	# create instance of Streamlistener
	listener = Streamlistener(api = api)
	stream = tweepy.Stream(auth, listener = listener)

	track = ['golf', 'masters', 'reed', 'mcilroy', 'woods']
	#track = ['nba', 'cavs', 'celtics', 'basketball']
	# choose what we want to filter by
	stream.filter(track = track, languages = ['en'])
