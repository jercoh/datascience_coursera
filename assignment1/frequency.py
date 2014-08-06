import sys, json, re

word_count = {}

def count_terms(tweet_file):
	for tweet in tweet_file:
		json_tweet = json.loads(tweet)
		if "text" in json_tweet.keys():
			text = re.sub('[^a-zA-Z0-9\n\.]', ' ', json_tweet['text'])
			words = text.split()
			for word in words:
				if word not in word_count.keys():
					word_count[word] = 1
				else:
					word_count[word] += 1

def main():
    tweet_file = open(sys.argv[1])
    count_terms(tweet_file)
    total_count = 0
    for word in word_count.keys():
    	total_count += word_count[word]
    for word in word_count.keys():
    	print(word+" "+str(round(float(word_count[word])/float(total_count),4)))


if __name__ == '__main__':
    main()