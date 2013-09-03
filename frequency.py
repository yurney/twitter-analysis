import sys
import json
import string

def isprintable(text):
	letterSet = set(string.letters)
	letterSet = letterSet.union('@')
	letterSet = letterSet.union('#')
	isPrintable = set(text).issubset(letterSet)
	return isPrintable
	
def main():
	timeTerms = {}
	tweetFile = open(sys.argv[1])
	ocurrences = 0
	for line in tweetFile:
		tweet = json.loads(line)
		text = tweet["text"]
		if text is not None:
			words = text.split()
			for word in words:
				if isprintable(word):
					ocurrences += 1
					if word in timeTerms:
						timeTerms[word] = timeTerms[word] + 1
					else:
						timeTerms[word] = 1
	for term in timeTerms:
		frequency = timeTerms[term] / float(ocurrences)
		print "{!s} {:f}".format(term, frequency)
		
if __name__ == '__main__':
	main()
