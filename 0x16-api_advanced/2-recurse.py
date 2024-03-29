#!/usr/bin/python3
"""Returns titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Return titles of all hot articles recursive function way a subreddit"""
    url = 'https://api.reddit.com'
    headers = {
        "User-Agent": "ChangeMeClient/0.1"
    }
    params = {
        "after": after,
        "count": count
    }
    res = requests.get("{}/r/{}/hot".format(url, subreddit),
                       headers=headers, params=params)
    if res.status_code == 404:
        return None
    data = res.json().get('data')
    after = data.get('after')
    count += data.get('dist')
    children = data.get('children')
    for child in children:
        hot_list.append(child.get('data').get('title'))

    if after is not None:
        recurse(subreddit, hot_list, after, count)

    return hot_list
