#!/usr/bin/python
import ConfigParser


# get the configuration
def getConfiguration():

	config = ConfigParser.ConfigParser()
	config.readfp(open('configuration.cfg'))

	consumerKey = config.get('TwitterOauth','CONSUMER_KEY')
	consumerSecret = config.get('TwitterOauth','CONSUMER_SECRET')

	accessKey = config.get('TheBotLebowski','ACCESS_KEY')
	accessSecret = config.get('TheBotLebowski','ACCESS_SECRET')
	
	return {'consumerKey':consumerKey, 'consumerSecret':consumerSecret,'accessKey':accessKey, \
		'accessSecret':accessSecret}
		
def main():
	conf = getConfiguration()
	print conf

	
if __name__ == '__main__':
	main()