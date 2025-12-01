#!/usr/bin/python3
"""
Uses GitHub API to display the user id based on credentials.
"""

import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    # Basic Authentication
    response = requests.get("https://api.github.com/user",
                            auth=(username, token))

    try:
        data = response.json()
    except ValueError:
        print("None")
        sys.exit(0)

    # If authentication fails → no id
    print(data.get("id"))
