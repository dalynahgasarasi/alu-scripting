#!/usr/bin/python3
"""Module that queries the Reddit API for subscriber count."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python:alu.api.advanced:v1.0 (by /u/dalynahgasarasi)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get("data", {}).get("subscribers", 0)
