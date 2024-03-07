#!/usr/bin/python3
""" 
A function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    :param subreddit: The name of the subreddit.
    :return: The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
    """
    # Construct the URL for the subreddit's about page in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers={'User-Agent': 'app/1.0'})
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0


# Test the function
if __name__ == "__main__":
    # Test for existing subreddit
    existing_subreddit = "python"
    print(f"Subscribers for {existing_subreddit}: {number_of_subscribers(existing_subreddit)}")

    # Test for non-existing subreddit
    non_existing_subreddit = "nonexistingsubreddit"
    print(f"Subscribers for {non_existing_subreddit}: {number_of_subscribers(non_existing_subreddit)}")
