import sys
import json

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

def main():
	sentiments = parse(open(sys.argv[1]))
	tweet_file = open(sys.argv[2])
	for line in tweet_file:
		tweet = json.loads(line)
		text = tweet["text"]
		if text is not None:
			words = text.split()
			score = 0
			for word in words:
				if word in sentiments:
					score+=sentiments[word]
			print score

if __name__ == '__main__':
    main()
