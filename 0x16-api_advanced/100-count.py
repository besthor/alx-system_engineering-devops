#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import re
import requests


def add_title(dictionary, hot_posts):
    """ Adds item into a list """
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile(r"^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, word_list, dictionary=None, after=None):
    """ Queries the Reddit API """
    if dictionary is None:
        dictionary = {}

    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        sorted_items = sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0].lower()))
        for item in sorted_items:
            if item[1] > 0:
                print("{}: {}".format(item[0].lower(), item[1]))
        return
    recurse(subreddit, word_list, dictionary, after=after)


def count_words(subreddit, word_list):
    """ Init function """
    recurse(subreddit, word_list)
