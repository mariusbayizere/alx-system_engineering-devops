#!/usr/bin/python3
"""
This module contains a function to query the Reddit API for
the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyRedditAPI/0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data', {}).get('children', [])
    if not data:
        print(None)
        return

    for post in data:
        print(post.get('data', {}).get('title'))


if __name__ == "__main__":
    top_ten('programming')
