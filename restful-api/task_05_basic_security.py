from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, 
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key-2024'  # Fixed secret key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600

# Initialize auth extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User data stored in memory
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

# Basic Authentication verification
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

@auth.error_handler
def auth_error():
    return jsonify({"error": "Unauthorized"}), 401

# JWT Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

# Routes
@app.route('/')
def home():
    return "Welcome to the Secure Flask API!"

# Basic Authentication Protected Route
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# JWT Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password required"}), 400
    
    username = data['username']
    password = data['password']
    
    if username in users and check_password_hash(users[username]['password'], password):
        access_token = create_access_token(
            identity={'username': username, 'role': users[username]['role']}
        )
        return jsonify({"access_token": access_token})
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# JWT Protected Route
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Admin Only Route
@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)