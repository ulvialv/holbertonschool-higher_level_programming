#!/usr/bin/python3
"""
A simple RESTful API using Flask.
This API manages users with CRUD operations.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users (dictionary with username as key)
users = {}


@app.route('/')
def home():
    """
    Root endpoint - returns a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """
    Returns a list of all usernames stored in the API.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """
    Status endpoint - returns OK.
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Returns the full user object for the provided username.
    If user doesn't exist, returns 404 error.

    Args:
        username (str): The username to look up
    """
    user = users.get(username)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Adds a new user to the users dictionary.
    Expects JSON data with username, name, age, and city.

    Returns:
        201: User added successfully
        400: Invalid JSON or missing username
        409: Username already exists
    """
    # Check if request contains valid JSON
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    # Check if data is None (invalid JSON)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Check if username is provided
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add the new user to the dictionary
    users[username] = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }

    # Return success message with user data
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
