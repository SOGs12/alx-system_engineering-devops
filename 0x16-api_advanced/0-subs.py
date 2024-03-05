#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "SOGs12"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    elif response.status_code == 302:
        # This indicates a redirect, which means the subreddit doesn't exist
        return 0
    else:
        # Handle other possible errors gracefully
        print(f"Error: {response.status_code}")
        return 0
