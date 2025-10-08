from flask import Flask, jsonify, request

app = Flask(__name__)

# Start with empty users dictionary as required
users = {}

@app.route('/')
def home():
    """Root endpoint - welcome message"""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Return list of all usernames"""
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route('/status')
def get_status():
    """Return API status"""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Return user data for specific username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user via POST request"""
    # Get JSON data from request
    user_data = request.get_json()
    
    # Check if username is provided
    if not user_data or 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400
    
    username = user_data['username']
    
    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    
    # Create user object with all provided fields
    new_user = {
        "username": username,
        "name": user_data.get('name', ''),
        "age": user_data.get('age', ''),
        "city": user_data.get('city', '')
    }
    
    # Add user to dictionary
    users[username] = new_user
    
    # Return success response
    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201

if __name__ == '__main__':
    app.run(debug=True)