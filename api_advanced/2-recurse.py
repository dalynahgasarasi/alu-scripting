#!/usr/bin/python3
"""Module that recursively retrieves all hot articles for a subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot articles for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python:alu.api.advanced:v1.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        return None
    data = response.json().get("data", {})
    children = data.get("children", [])
    if not children:
        return hot_list if hot_list else None
    for post in children:
        hot_list.append(post.get("data", {}).get("title"))
    after = data.get("after")
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
