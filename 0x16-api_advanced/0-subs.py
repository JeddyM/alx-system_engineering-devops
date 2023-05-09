#!/usr/bin/python3
'''A module that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.'''
import requests


def number_of_subscribers(subreddit):
    '''Returns the number of subscribers '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get("data").get("subscribers")
        return results

    return 0
