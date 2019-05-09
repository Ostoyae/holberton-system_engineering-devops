#!/usr/bin/python3
"""This script will return the number of subscribers associated with 
a subreddit
"""
import json
import requests
from sys import argv

def number_of_subscribers(subreddit):
    """Method get the number of users subscribed to a subreddit
    
    subreddit (Str)- subreddit to check

    Returns - number of users (INT) else 0 (INT) if not subreddit is found 
    """
    try:
        h = {'user-agent' : 'Mozilla/5.0'}
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        req = requests.get(url, headers=h)
    except Exception as e:
        print(e)

    return req.json().get('data').get('subscribers', 0)

if __name__ == "__main__":
    pass
