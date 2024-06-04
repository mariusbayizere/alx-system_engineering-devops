#!/usr/bin/python3
"""
This module contains a recursive function to query the Reddit API,
parse the titles of all hot articles, and print a sorted count of
given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords.
    """
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditAPI/0.1'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    children = data.get('children', [])
    for child in children:
        title = child.get('data', {}).get('title', '').lower()
        for word in word_list:
            if word.lower() in title:
                counts[word.lower()] = counts.get(word.lower(), 0) + 1

    after = data.get('after', None)
    if after:
        return count_words(subreddit, word_list, after, counts)

    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'"
              .format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        count_words(subreddit, word_list)
