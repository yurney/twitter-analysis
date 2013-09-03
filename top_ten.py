import sys
import json

def main():
	tweet_file = open(sys.argv[1])
	topics = {}
	for line in tweet_file:
		tweet = json.loads(line)
		entities = tweet["entities"]
		if entities is not None:
			hashtags = entities["hashtags"]
			if hashtags is not None:
				for hashtag in hashtags:
					key = hashtag["text"]
					if key in topics:
						topics[key] += 1
					else:
						topics[key] = 1
	trendTopic =[]
	for topic in topics:
		tuple = (topics[topic], topic)
		trendTopic.append(tuple)
	#print trendTopic

	sortedList = sorted(trendTopic)

	#print sortedList

	for i in range (10):
		if len(sortedList) > 0:
			element = sortedList.pop()
			value = float(element[0])
			print "{!s} {:f}".format(element[1].encode("utf-8"), value)

if __name__ == '__main__':
    main()
