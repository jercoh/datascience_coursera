import sys, json, re

new_terms = {}

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

def compute_score_of_new_terms(tweet_file, score_dic):
	for tweet in tweet_file:
		tweet_score = 0
		json_tweet = json.loads(tweet)
		if "text" in json_tweet.keys():
			text = re.sub('[^a-zA-Z0-9\n\.]', ' ', json_tweet['text'])
			words = text.split()
			rated_words = score_dic.keys()
			for word in words:
				encoded_word = word.encode('utf-8')
				if encoded_word in rated_words:
					tweet_score += score_dic[word]

			for word in words:
				encoded_word = word.encode('utf-8')
				if encoded_word not in rated_words:
					if encoded_word not in new_terms.keys():
						new_terms[encoded_word] = [0,0,0] #[#of positive tweets, #of negative tweets, ratio pos/neg]
					
					if tweet_score > 0:
						new_terms[encoded_word][0] += 1
					elif tweet_score < 0:
						new_terms[encoded_word][1] += 1

	for word in new_terms.keys():
		new_terms[word][2] = new_terms[word][0]/new_terms[word][1] if new_terms[word][1] > 0 else new_terms[word][0]

def main():
    afinn_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    score_dic = get_scores(afinn_file)
    for line in tweet_file:
    	compute_score_of_new_terms(tweet_file, score_dic)
    for word in new_terms.keys():
    	print(word+" "+str(new_terms[word][2]))


if __name__ == '__main__':
    main()
