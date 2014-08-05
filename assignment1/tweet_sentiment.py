import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def get_scores(afinnfile):
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer
	return scores

def get_tweet_score(tweet, score_dic):
	score = 0
	json_tweet = json.loads(tweet)
	if "text" in json_tweet.keys():
		words = json_tweet["text"].split(" ")
		rated_words = score_dic.keys()
		for word in words:
			if word.encode('utf-8') in rated_words:
				score += score_dic[word]
	return score

def main():
    afinn_file = open(sys.argv[1])
    tweets_file = open(sys.argv[2])
    score_dic = get_scores(afinn_file)
    for line in tweets_file:
    	print(get_tweet_score(line, score_dic))

if __name__ == '__main__':
    main()
