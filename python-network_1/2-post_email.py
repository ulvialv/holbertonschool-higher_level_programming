#!/usr/bin/python3
"""Sends a POST request with an email parameter and displays the response body"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare POST data (must be encoded)
    data = parse.urlencode({"email": email}).encode("utf-8")

    # Create POST request
    req = request.Request(url, data=data)

    # Send request using with
    with request.urlopen(req) as response:
        body = response.read().decode("utf-8")
        print(body)
