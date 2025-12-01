#!/usr/bin/python3
"""
Sends a letter to an API endpoint using POST and displays the result.
"""

import sys
import requests

if __name__ == "__main__":
    # Take letter from argument
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    try:
        response = requests.post("http://0.0.0.0:5000/search_user",
                                 data={"q": q})
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        sys.exit(1)

    # Try parsing JSON
    try:
        result = response.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit(0)

    # If JSON exists
    if result and isinstance(result, dict):
        print(f"[{result.get('id')}] {result.get('name')}")
    else:
        print("No result")
