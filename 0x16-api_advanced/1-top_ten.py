#!/usr/bin/python3
'''Queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
'''
import requests


def top_ten(subreddit):
    '''Prints the titles of the first 10 hot posts
    If not a valid subreddit, print None.
    '''

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {"limit": 10}
    response = requests.get(url, params=params, allow_redirects=False)

    if response.status_code == 200:
        results = response.json()['data']['children']
        for values in results:
            value = values['data']['title']
            print(value)
    else:
        print(None)
