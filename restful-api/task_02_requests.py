#!/usr/bin/python3
import requests
import csv


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts and print status + titles"""
    response = requests.get(API_URL)
    
    # Print status code
    print(f"Status code: {response.status_code}")

    if response.status_code != 200:
        return

    #parse Json

    data = response.json()

    # Print all titles
    for post in data:
        print(post.get("title"))
def fetch_and_save_posts():
    """Fetch posts and save to posts.csv."""
    response = requests.get(API_URL)
    

    if response.status_code != 200:
        return

    data = response.json()

    
    # Prepare data: list of dicts with id, title, body
    clean_data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in data
    ]
    

    # Write CSV
    with open("posts.csv", "w", newline="", encoding="utf-8") as f:

        writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(clean_data)

                
    
    
