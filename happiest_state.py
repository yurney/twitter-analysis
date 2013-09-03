import sys
import json
import string

def isState(code):
	states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
	if states.count(code) > 0:
		return True 
	else:
		return False

def parse(fp):
	sentiments = {}
	for line in fp:
		word, value = line.split('\t')
		sentiments[word] = int(value)
	fp.close
	return sentiments

def getState(tweet):
	isUS = False
	place = tweet["place"]
	if place is not None:
		countryCode = place["country_code"]
		if countryCode is not None:
			if countryCode is "US":
				isUS = True
		if isUS:
			fullName = place["full_name"]
			if fullName is not None:
				state = getStateCode(fullName)
				return state
	else:
		user = tweet["user"]
		if user is not None:
			location = user["location"]
			if location is not None:
				words = location.split(',')
				for word in words:
					word = string.strip(word)
					if isState(word):
						return word
					else:
						return None
	return None

		#user = tweet["user"]
		#if user is not None:
		#	location = user["location"]
		#	if location is not None:
		#		lines = location.split()
		#		checkNext = False
		#		for line in lines:
		#			print line
		#			if checkNext:
		#				line = string.strip(line)
		#				if len(line) == 2 and isUppercase(line):
		#					return line
		#			if line.endswith(','):
		#				checkNext = True
		#			else:
		#				checkNext = False
		#		return None
		#else:
		#	return None
	
	
def main():
	states = {}
	sentiments = parse(open(sys.argv[1]))
	tweet_file = open(sys.argv[2])
	for line in tweet_file:
		tweet = json.loads(line)
		try:
			text = tweet["text"]
			score = 0
			if text is not None:
				words = text.split()
				for word in words:
					if word in sentiments:
						score+=sentiments[word]
			state = getState(tweet)
			if state is not None:
				if state in states:
					states[state] = states[state] + score
				else:
					states[state] = score
		except KeyError:
			KeyError
	highestScore = 0
	happiestState = None
	for state in states:
		if states[state] > highestScore:
			highestScore = states[state]
			happiestState = state
	print happiestState
			

if __name__ == '__main__':
    main()
