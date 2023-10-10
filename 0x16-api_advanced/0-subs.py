#!/usr/bin/python3
"""This module defines a function to query the Reddit API for subreddit information."""

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for information about a subreddit and returns the number of subscribers.
    
    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers to the subreddit or 0 if the subreddit is invalid or an error occurs.
    """
    import requests


    sub_info = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
