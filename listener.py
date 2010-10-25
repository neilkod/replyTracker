#!/usr/bin/python
import ConfigParser,tweepy,re



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

	terms = ['@thebotlebowski','@acenterforants','@abakingpowder','@which_is_nice','@iamjacksbot']
	(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) = getConfiguration()
	
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	rateStatus = api.rate_limit_status()
	results = api.search(q='@thebotlebowski',rpp=100)
	print len(results)
	for result in results:
		for term in terms:
			searchterm = '%s remove' % term
			regexp = re.compile(searchterm)
			if regexp.search(result.text.lower()):
				print "%s\t%s" % (result.from_user,result.text)


if __name__ == '__main__':
	main()