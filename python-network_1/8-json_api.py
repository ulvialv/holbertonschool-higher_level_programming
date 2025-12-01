#!/usr/bin/python3
import sys
import requests

def main():
    # Command-line arg al
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    try:
        # POST isteği gönder
        response = requests.post(
            "http://0.0.0.0:5000/search_user",
            data={"q": q},
            timeout=5
        )

        # JSON parse etmeyi dene
        try:
            result = response.json()
        except ValueError:
            print("Not a valid JSON")
            return

        # Boş mu dolu mu?
        if result and isinstance(result,
