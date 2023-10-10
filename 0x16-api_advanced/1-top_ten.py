#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import request
import sys


def top_ten(subreddit):
    """queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit"""
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': 'u_agent'
    }

    params = {
        'limit' = 10
    }

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit"
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False)
    if (response.status_code != 200):
        print(None)
        return
    posts = request.json()['data']['children']
    if len(posts) is 0:
        print(None)
    else:
        print(post['data']['title'])
