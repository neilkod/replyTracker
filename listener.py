#!/usr/bin/python
import ConfigParser


# get the configuration
def getConfiguration():

	config = ConfigParser.ConfigParser()
	config.readfp(open('configuration.cfg'))

	CONSUMER_KEY = config.get('TwitterOauth','CONSUMER_KEY')
	CONSUMER_SECRET = config.get('TwitterOauth','CONSUMER_SECRET')

	ACCESS_KEY = config.get('TheBotLebowski','ACCESS_KEY')
	ACCESS_SECRET = config.get('TheBotLebowski','ACCESS_SECRET')
	
	return {'CONSUMER_KEY':CONSUMER_KEY, 'CONSUMER_SECRET':CONSUMER_SECRET,'ACCESS_KEY':ACCESS_KEY, \
		'ACCESS_SECRET':ACCESS_SECRET}
		

def main():
	conf = getConfiguration()
	print conf
	
if __name__ == '__main__':
	main()