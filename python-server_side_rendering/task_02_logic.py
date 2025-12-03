from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/items')
def items_page():
    # items.json dosyasını oku
    json_path = os.path.join(os.path.dirname(__file__), 'items.json')
    with open(json_path, 'r') as f:
        data = json.load(f)

    # JSON içindeki listeyi çek
    items = data.get("items", [])

    # Template’e gönder
    return render_template('items.html', items=items)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
