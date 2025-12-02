#!/usr/bin/python3
import requests
import csv


API_URL = "https://jsonplaceholder.typicode.com/posts"


response = requests.get(API_URL)

print(f"Status code: {response.status_code}")

if response.status_code != 200:
    return

data = response.json()

for post in data:
    print(post.get("title"))

    response = requests.get(API_URL)
    if response.status_code != 200:
        return

    data = response.json()

    clean_data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in data
    ]
    with open("posts.csv", "w", newline="", encoding="utf-8") as f:

        writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(clean_data)

                
    
    
