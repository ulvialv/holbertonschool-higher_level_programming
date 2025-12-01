#!/usr/bin/python3
"""Sends a POST request with an email and displays the response body"""

import sys
import requests

# Take URL and email from command line 

url = sys.argv[1]
email = sys.argv[2]

# Data to send in post requests
data = {'email': hr@holbertonschool.com}

# send  Post request
response = requests.post(url, data=data)

# Print server response
print(response.text)
