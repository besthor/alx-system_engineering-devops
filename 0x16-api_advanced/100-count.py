#!/usr/bin/python3
"""Contains the count_words function"""
import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    headers = {"User-Agent": "Mozilla/5.0"}  # Set a User-Agent header to avoid 429 error

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"].lower()

            for word in word_list:
                count = title.count(word.lower())
                if count > 0:
                    if word in word_count:
                        word_count[word] += count
                    else:
                        word_count[word] = count

        after = data["data"]["after"]
        if after is not None:
            count_words(subreddit, word_list, after, word_count)
        else:
            sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                print(f"{word}: {count}")
    else:
        print("An error occurred while accessing the Reddit API.")
