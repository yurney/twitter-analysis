import sys
import json
import string

def lines(fp):
    print str(len(fp.readlines()))

def parse(fp):
	sentiments = {}
	for line in fp:
		#print line
		word, value = line.split('\t')
		sentiments[word] = int(value)
	fp.close
	return sentiments

def isprintable(text):
	letterSet = set(string.letters)
	letterSet = letterSet.union('@')
	letterSet = letterSet.union('#')
	isPrintable = set(text).issubset(letterSet)
	return isPrintable
	
def main():
	terms = {}
	timeTerms = {}
	sentiments = parse(open(sys.argv[1]))
	tweetFile = open(sys.argv[2])
	for line in tweetFile:
		tweet = json.loads(line)
		text = tweet["text"]
		if text is not None:
			words = text.split()
			score = 0
			unknownWords = []
			for word in words:
				if word in sentiments:
					score+=sentiments[word]
				else:
					unknownWords.append(word)
			for unknownWord in unknownWords:
				if isprintable(unknownWord):
					if unknownWord in terms:
						terms[unknownWord] = terms[unknownWord] + score
						timeTerms[unknownWord] = timeTerms[unknownWord] + 1
					else:
						terms[unknownWord] = score
						timeTerms[unknownWord] = 1
	for newTerm in terms:
		value = terms[newTerm] / float(timeTerms[newTerm])
		print "{!s} {:f}".format(newTerm, value)

if __name__ == '__main__':
    main()
