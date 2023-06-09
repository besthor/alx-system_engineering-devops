#!/usr/bin/python3
'''Get ALL hot posts'''
import pprint
import re
import requests

BASE_URL = 'http://reddit.com/r/{}/hot.json'


def count_words(subreddit, word_list, hot_list=[], after=None):
    '''Get ALL hot posts'''
    headers = {'User-agent': 'Unix:0-subs:v1'}
    params = {'limit': 100}
    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return print_results(word_list, hot_list)

    response = requests.get(BASE_URL.format(subreddit),
                            headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = response.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = "STOP"
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return count_words(subreddit, word_list, hot_list, after)


def print_results(word_list, hot_list):
    '''Prints request results'''
    count = {}
    for word in word_list:
        count[word] = 0
    for title in hot_list:
        for word in word_list:
            count[word] = count[word] +\
             len(re.findall(r'(?:^| ){}(?:$| )'.format(word), title, re.I))

    count = {k: v for k, v in count.items() if v > 0}
    words = sorted(list(count.keys()))
    for word in sorted(words,
                       reverse=True, key=lambda k: count[k]):
        print("{}: {}".format(word, count[word]))
