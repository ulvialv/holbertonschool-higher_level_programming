#!/usr/bin/python3
"""
API Security and Authentication Implementation
Task 5: Basic and JWT Authentication with Role-Based Access Control
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, 
    get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

# Create Flask application
app = Flask(__name__)

# JWT secret key configuration (use stronger key in production)
app.config['JWT_SECRET_KEY'] = 'super-secret-key-change-this-in-production'

# Initialize HTTPBasicAuth
auth = HTTPBasicAuth()

# Initialize JWTManager
jwt = JWTManager(app)

# ============================================
# USER DATABASE (stored in memory)
# ============================================
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# ============================================
# BASIC AUTHENTICATION
# ============================================

@auth.verify_password
def verify_password(username, password):
    """
    Password verification function for Basic Authentication

    This function is automatically called when @auth.login_required is used

    Args:
        username: Username string
        password: Plain text password

    Returns:
        username if credentials are valid, None otherwise
    """
    if username in users:
        if check_password_hash(users[username]['password'], password):
            return username
    return None


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    Protected route using Basic Authentication

    User must provide valid username and password
    """
    return "Basic Auth: Access Granted"


# ============================================
# JWT AUTHENTICATION
# ============================================

@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint - creates JWT token

    Request body:
    {
        "username": "user1",
        "password": "password"
    }

    Response:
    {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhb..."
    }
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing JSON data"}), 401

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 401

    if username in users:
        if check_password_hash(users[username]['password'], password):
            access_token = create_access_token(
                identity=username,
                additional_claims={"role": users[username]['role']}
            )
            return jsonify({"access_token": access_token}), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    Protected route using JWT token

    Must include token in header:
    Authorization: Bearer <your_token_here>
    """
    current_user = get_jwt_identity()
    return f"JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    Admin-only protected route

    Returns 403 Forbidden if user role is not admin
    """
    claims = get_jwt()

    if claims.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# ============================================
# JWT ERROR HANDLERS (return 401)
# ============================================

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """No token provided or Authorization header missing"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Token format is invalid"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Token has expired"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Token has been revoked"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Fresh token required"""
    return jsonify({"error": "Fresh token required"}), 401


# ============================================
# HOME ROUTE (for testing)
# ============================================

@app.route('/', methods=['GET'])
def home():
    """Home page - API information"""
    return jsonify({
        "message": "API Security Task",
        "endpoints": {
            "basic_auth": "/basic-protected (GET)",
            "login": "/login (POST)",
            "jwt_protected": "/jwt-protected (GET)",
            "admin_only": "/admin-only (GET)"
        }
    })


# ============================================
# RUN APPLICATION
# ============================================

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
