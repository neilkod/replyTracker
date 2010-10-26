#!/usr/bin/python
import ConfigParser,tweepy,re


# get the configuration
def getConfiguration(configFile):
	""" Look up a few values out of a config file in order to authenticate
		as @thebotlebowski.  Eventually I'll support all of the bots"""

	config = ConfigParser.ConfigParser()
	config.readfp(open(configFile))

	consumerKey = config.get('TwitterOauth','CONSUMER_KEY')
	consumerSecret = config.get('TwitterOauth','CONSUMER_SECRET')

	accessKey = config.get('TheBotLebowski','ACCESS_KEY')
	accessSecret = config.get('TheBotLebowski','ACCESS_SECRET')
	
	lastTweet = config.get('search','last')

	return (consumerKey,consumerSecret,accessKey,accessSecret,lastTweet)

def getLast(configFile):
	""" retrieve the last tweet id used """	
	config = ConfigParser.ConfigParser()
	config.readfp(open(configFile))	
	last = config.getint('search','last')
	
	return last

def setLast(configFile,last):
	config = ConfigParser.ConfigParser()
	config.readfp(open(configFile))
	config.set('search','last',last)
	with open(configFile, 'wb') as theFile:
		config.write(theFile)
	
def testit():
	configFile = 'configuration.cfg'
	last = getLast(configFile)
	setLast(configFile,last + 1)

def loadExcludeList(excludeFile):
	users = []
	for line in open(excludeFile):
		users.append(line.strip())
	return set(users)

def writeExcludeList(excludeFile,theUser):
	
	theFile = open(excludeFile,'a')
	theText = "%s\n" % theUser
	theFile.write(theText)
	theFile.close()	
	
		
def main():
	configFile = 'configuration.cfg'
	excludeFile = 'exclude.txt'
	
	# 
	excludeUsers = loadExcludeList(excludeFile)
	
	terms = ['@thebotlebowski','@acenterforants','@abakingpowder','@which_is_nice','@iamjacksbot']
	(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET,last) = getConfiguration(configFile)
	
	# log in to twitter
	
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	rateStatus = api.rate_limit_status()
	results = api.search(q='@thebotlebowski',rpp=100,since_id=last)
	for result in reversed(results):
		for term in terms:
			searchterm = '%s remove' % term
			regexp = re.compile(searchterm)
			if regexp.search(result.text.lower()):
				print "%s\t%s\t%s" % (result.id,result.from_user,result.text)
				setLast(configFile,result.id)
				
				# if the user to exclude is not in the list
				# then add the user to the exclude list
				
				if result.from_user not in excludeUsers:
					excludeUsers.add(result.from_user)
					print "found a new user to ignore %s" % result.from_user
					writeExcludeList(excludeFile, result.from_user)

if __name__ == '__main__':
	main()