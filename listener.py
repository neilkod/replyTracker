#!/usr/bin/python
import ConfigParser,tweepy



# get the configuration
def getConfiguration():
	""" Look up a few values out of a config file in order to authenticate
		as @thebotlebowski.  Eventually I'll support all of the bots"""

	config = ConfigParser.ConfigParser()
	config.readfp(open('configuration.cfg'))

	consumerKey = config.get('TwitterOauth','CONSUMER_KEY')
	consumerSecret = config.get('TwitterOauth','CONSUMER_SECRET')

	accessKey = config.get('TheBotLebowski','ACCESS_KEY')
	accessSecret = config.get('TheBotLebowski','ACCESS_SECRET')

	return (consumerKey,consumerSecret,accessKey,accessSecret)
	
		
def main():

	(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) = getConfiguration()
	
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)

	
if __name__ == '__main__':
	main()