from flask import Flask, request, jsonify
from flask_cors import CORS

# Import your database functions here
from database import get_users, get_user_by_id, insert_user, update_user, delete_user

app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app, resources={r"/*": {"origins": "*"}})

# Define your API endpoints

# 1. Get all users
@app.route('/api/users', methods=['GET'])
def api_get_users():
    return jsonify(get_users())

# 2. Get a user by ID
@app.route('/api/users/<int:user_id>', methods=['GET'])
def api_get_user(user_id):
    return jsonify(get_user_by_id(user_id))

# 3. Add a new user
@app.route('/api/users/add', methods=['POST'])
def api_add_user():
    user = request.get_json() 
    return jsonify(insert_user(user))

# 4. Update an existing user
@app.route('/api/users/update', methods=['PUT'])
def api_update_user():
    user = request.get_json()  
    return jsonify(update_user(user))

# 5. Delete a user by ID
@app.route('/api/users/delete/<int:user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    return jsonify(delete_user(user_id))

if __name__ == '__main__':
    # Run the app
    app.run(debug=True)
