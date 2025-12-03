from flask import Flask, request, render_template
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# -------- JSON ----------
def load_json():
    path = os.path.join(os.path.dirname(__file__), "products.json")
    with open(path, "r") as f:
        return json.load(f)

# -------- CSV -----------
def load_csv():
    path = os.path.join(os.path.dirname(__file__), "products.csv")
    products = []
    with open(path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

# -------- SQL (SQLite) ----------
def load_sql():
    path = os.path.join(os.path.dirname(__file__), "products.db")
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    products = []
    for row in cursor.execute("SELECT id, name, category, price FROM Products"):
        products.append({
            "id": row[0],
            "name": row[1],
            "category": row[2],
            "price": row[3]
        })

    conn.close()
    return products


@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    # ---- Validate source ----
    if source not in ["json", "csv", "sql"]:
        return render_template("product_display.html", error="Wrong source")

    # ---- Load data ----
    try:
        if source == "json":
            products = load_json()
        elif source == "csv":
            products = load_csv()
        elif source == "sql":
            products = load_sql()
    except Exception as e:
        return render_template("product_display.html", error="Database error")

    # ---- Filter by ID ----
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template("product_display.html", error="Invalid ID")

        filtered = [p for p in products if p["id"] == product_id]

        if not filtered:
            return render_template("product_display.html", error="Product not found")

        products = filtered

    return render_template("product_display.html", products=products)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
