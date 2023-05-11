#!/usr/bin/python3
'''queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit. Use recursive
function instead of loops
'''
import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    '''Returns a list of titles of all hot articles for a given subreddit
    If not a valid subreddit, print None.
    '''

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {
            "limit": 50,
            "after": after,
            "count": count
            }
    response = requests.get(url, params=params, allow_redirects=False)

    if response.status_code == 404:
        return None

    if response.status_code == 200:
        results = response.json().get("data")
        after = results.get("after")
        count = len(results.get("children"))
        for i in results.get("children"):
            hot_list.append(i.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
