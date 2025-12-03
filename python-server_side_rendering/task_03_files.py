#!/usr/bin/python3
from flask import Flask, request, render_template
import json
import csv
import os

app = Flask(__name__)


def load_json():
    path = os.path.join(os.path.dirname(__file__), "products.json")
    with open(path, "r") as f:
        return json.load(f)


def load_csv():
    path = os.path.join(os.path.dirname(__file__), "products.csv")
    products = []
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert id to int, price to float
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    # 1. WRONG SOURCE
    if source not in ["json", "csv"]:
        return render_template("product_display.html", error="Wrong source")

    # 2. Load the correct file
    products = load_json() if source == "json" else load_csv()

    # 3. Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template("product_display.html", error="Invalid ID")

        filtered = [p for p in products if p["id"] == product_id]

        if not filtered:
            return render_template("product_display.html", error="Product not found")

        products = filtered

    # 4. Render table
    return render_template("product_display.html", products=products)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
