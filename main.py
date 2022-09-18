import json
import re

def word_in_tweet(word, tweet):
    return re.search(f"\\b{word}\\b", tweet) is not None

def all_words_in_tweet(words, tweet):
    return all([word_in_tweet(word, tweet) for word in words])

tweets = []
with open('tweets.json', 'r') as f:
    tweets = json.load(f)

def any_keywords_match(tweets, words):
    if not words:
        return []
    tweet_ids = []
    for tweet in tweets['tweets']:
        id = tweet['id']
        tweet = tweet['tweet']
        if any([word_in_tweet(word, tweet) for word in words]):
            tweet_ids.append(id)
    
    return sorted(tweet_ids)

assert any_keywords_match(tweets, []) == []
assert any_keywords_match(tweets, ['Something']) == []
assert any_keywords_match(tweets, ['abouts']) == []
assert any_keywords_match(tweets, ['game', 'Nomatch']) == [14444]
assert any_keywords_match(tweets, ['game', 'games']) == [14444, 46664]
assert any_keywords_match(tweets, ['games', 'game']) == [14444, 46664]
assert any_keywords_match(tweets, ['I', 'Hello', 'jungle' ]) == [15677, 46664, 57775, 625700, 9999930]

def all_keywords_match(tweets, words):
    if not words:
        return []
    tweet_ids = []
    for tweet in tweets['tweets']:
        id = tweet['id']
        tweet = tweet['tweet']
        if all_words_in_tweet(words, tweet):
            tweet_ids.append(id)
    
    return sorted(tweet_ids)

assert all_keywords_match(tweets, ['Something']) == []
assert all_keywords_match(tweets, ['abouts']) == []
assert all_keywords_match(tweets, []) == []
assert all_keywords_match(tweets, ['game', 'Nomatch']) == []
assert all_keywords_match(tweets, ['This', 'occurred']) == [14444, 46664]
assert all_keywords_match(tweets, ['This', 'has', 'occurred']) == [14444]
assert all_keywords_match(tweets, ['I', 'a']) == [15677, 46664]