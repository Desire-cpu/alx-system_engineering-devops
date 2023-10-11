#!/usr/bin/python3
"""Module for querying the Reddit API and retrieving."""

import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API for subreddit information.

    Args:
        subreddit (str): The name of the subreddit to retrieve information.

    Returns:
        int: The number of subscribers to the subreddit, or 0 if the subreddit.
    """
    # Construct the URL to request subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set custom headers with a User-Agent
    headers = {"User-Agent": "My-User-Agent"}

    # Send a GET request to the Reddit API's subreddit information endpoint
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the HTTP status code indicates an error (status code >= 300)
    if response.status_code >= 300:
        return 0

    # Extract the number of subscribers from the JSON response
    return response.json().get("data").get("subscribers")
