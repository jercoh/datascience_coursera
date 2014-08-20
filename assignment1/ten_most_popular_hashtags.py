import sys, json, re, operator

hashtag_count = {}

def count_hashtags(tweet_file):
	for line in tweet_file:
		tweet = json.loads(line)
		if "text" in tweet.keys() and 'entities' in tweet.keys() and tweet['entities']['hashtags'] != []:
			for hashtag in tweet['entities']['hashtags']:
				hashtag_text = hashtag['text']
				if hashtag_text not in hashtag_count.keys():
					hashtag_count[hashtag_text] = 1
				else:
					hashtag_count[hashtag_text] += 1

def main():
    tweet_file = open(sys.argv[1])
    count_hashtags(tweet_file)
    ten_most_popular_hashtags = dict(sorted(hashtag_count.iteritems(), key=operator.itemgetter(1), reverse=True)[:10])
    for hashtag in ten_most_popular_hashtags:
    	print(hashtag.encode('utf-8')+" "+str(float(ten_most_popular_hashtags[hashtag])))


if __name__ == '__main__':
    main()