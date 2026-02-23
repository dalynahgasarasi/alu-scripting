#!/usr/bin/python3
"""
1. Queries the Reddit API and prints the first 10 hot post titles
for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit.

    Args:
        subreddit (str): Name of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'python:top_ten_script:v1.0 (by /u/yourusername)'
    }

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False, timeout=10)
        # Invalid subreddit redirects to search page or gives 302
        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get('data', {}).get('children')
        if not posts:  # empty or invalid subreddit
            print(None)
            return

        for post in posts:
            print(post['data']['title'])
    except requests.RequestException:
        print(None)
