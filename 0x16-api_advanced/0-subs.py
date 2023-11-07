#!/usr/bin/python3
"""function for task0"""

import requests

def number_of_subscribers(subreddit):
    """Total number of subscribes on a given subreddit."""
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response_data = requests.get(api_url, headers=headers, allow_redirects=False)
    if response_data.status_code == 404:
        return 0
    red_results_data = response_data.json().get("data")
    return red_results_data.get("subscribers")
