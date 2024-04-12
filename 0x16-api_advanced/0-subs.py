#!/usr/bin/python3
""" How many subs? """
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """return number of subs of a subreddit"""
    try:
        response = requests.get('https://www.reddit.com/r/{}/about.json'
                                .format(subreddit),
                                headers={'User-agent': 'Mozilla/5.0'},
                                allow_redirects=False)
    except requests.exceptions.RequestException:
        return 0
    try:
        data = response.json().get('data')
        n = data.get('subscribers')
    except (json.decoder.JSONDecodeError, AttributeError):
        return 0
    return n
