from flask import Flask, jsonify, request


app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane",
             "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John",
             "age": 30, "city": "New York"}
}


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
    user_data = request.get_json()

    if not user_data or 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400

    username = user_data['username']

    new_user = {
        "username": username,
        "name": user_data.get('name', ''),
        "age": user_data.get('age', ''),
        "city": user_data.get('city', '')
    }

    users[username] = new_user

    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201


if __name__ == '__main__':
    app.run(debug=True)
