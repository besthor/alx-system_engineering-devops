#!/usr/bin/python3
"""script for parsing web data from an api
    DISCLAIMER: THIS PROBABLY SHOULDN'T BE DONE RECURSIVELY
    but we had to for school :P
"""
import json
import requests
import sys


def get_hot_posts(subreddit, hot_list=[]):
    """api call to reddit to get the number of subscribers
    """
    base_url = 'https://www.reddit.com/r/{}/top.json'.format(
        subreddit
    )
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    if len(hot_list) == 0:
        # grab initial list
        url = base_url
    else:
        # grab next pagination after last obj in hot_list
        url = base_url + '?after={}_{}'.format(
            hot_list[-1].get('kind'),
            hot_list[-1].get('data').get('id')
        )
    response = requests.get(url, headers=headers)
    resp = json.loads(response.text)
    try:
        data = resp.get('data')
        children = data.get('children')
    except:
        return None
    if children is None or data is None or len(children) < 1:
        return hot_list
    hot_list.extend(children)
    return get_hot_posts(subreddit, hot_list)


def count_words(subreddit, wordlist):
    """count words in titles of hot posts for subreddit
    """
    posts = get_hot_posts(subreddit)
    if posts is None:
        print(end="")
        return
    words = gather_word_info(posts, wordlist)
    sorted_list = [(key, val) for key, val in words.items()]
    sorted_list = sorted(sorted_list, key=lambda tup: tup[1], reverse=True)
    [print("{}: {}".format(key, val)) for (key, val) in sorted_list if val > 0]


def gather_word_info(hot_posts, wordlist,
                     posts_len=None,
                     counter=0,
                     words_info=None):
    """does the recursion to grab word info from wordlist and posts
    """
    if hot_posts is None:
        return
    # generate defaults
    if posts_len is None:
        posts_len = len(hot_posts)
    if words_info is None:
        words_info = {key: 0 for key in wordlist}
    # base case
    if counter == posts_len - 1:
        return words_info

    # parse this title and move to next
    data = hot_posts[counter].get('data')
    if data is None:
        return words_info
    title = data.get('title')
    if title is None:
        return words_info
    # im sorry im not doing recursion for text parsing that's rediculous
    for word in title.split(' '):
        word = word.lower()
        if word in wordlist:
            words_info[word] += 1
    counter += 1
    return gather_word_info(
        hot_posts, wordlist, posts_len,
        counter, words_info
    )
