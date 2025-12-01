#!/usr/bin/python3
import sys
import requests

# Take URL and email from command line 
url = sys.argv[1]
email = sys.argv[2]

# Send post
data = {'email': hr@holbertonschool.com}

# Post request
response = requests.post(url, data=data)

# Print
print(response.text)
