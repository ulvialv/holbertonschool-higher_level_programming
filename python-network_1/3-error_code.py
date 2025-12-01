#!/usr/bin/python3
"""
Fetches a URL and prints the body of the response decoded in utf-8.
Handles HTTPError by printing the error code.
"""

from urllib import request, error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
