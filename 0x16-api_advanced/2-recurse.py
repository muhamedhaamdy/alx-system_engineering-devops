#!/usr/bin/python3
""" How many subs? """
import json
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """return number of subs of a subreddit"""
    try:
        response = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'
                                .format(subreddit, after),
                                headers={'User-agent': 'Mozilla/5.0'},
                                allow_redirects=False)
    except requests.exceptions.RequestException as e:
        return None
    try:
        data = response.json().get('data').get('children')
        after = response.json().get('data').get('after')
        for i in data:
            title = i.get('data').get('title')
            hot_list.append(title)
    except (json.decoder.JSONDecodeError, AttributeError) as e:
        return None
    if after is not None:
        recurse(subreddit, hot_list, after)
    return hot_list
