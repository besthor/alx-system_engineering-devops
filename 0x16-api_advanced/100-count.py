#!/usr/bin/python3
"""Contains the count_words function"""
import requests

def count_words(subreddit, word_list, after="", count=None):
    if count is None:
        count = [0] * len(word_list)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after}

    response = requests.get(url, params=params, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        for topic in data['data']['children']:
            title_words = topic['data']['title'].lower().split()
            for i in range(len(word_list)):
                if word_list[i].lower() in title_words:
                    count[i] += title_words.count(word_list[i].lower())

        after = data['data']['after']
        if after is None:
            word_count = dict(zip(word_list, count))
            sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

            for word, count in sorted_words:
                print(f"{word.lower()}: {count}")
        else:
            count_words(subreddit, word_list, after, count)
