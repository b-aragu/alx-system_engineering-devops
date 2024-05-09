#!/user/bin/env python3
"""
queries the Reddit API and returns the number of subscribers 
(not active users, total subscribers) for a given subreddit.
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function to do so
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'user-agent': 'Google Chrome Version 124.0.6367.118'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
