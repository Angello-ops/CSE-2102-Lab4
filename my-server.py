from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)

# Secret key to encode and decode JWT tokens (in production, keep this secret)
SECRET_KEY = 'my_secret_key'

# Function to generate JWT token
def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)  # Token expires in 30 minutes
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

# Function to verify JWT token
def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return 'Token has expired'
    except jwt.InvalidTokenError:
        return 'Invalid token'

@app.route("/")
def hello():
    return "Server is running\n"

# Endpoint to handle POST requests with token authentication
@app.route("/login", methods=['POST'])
def login():
    auth_data = request.form
    user_id = auth_data.get("id")
    
    # For simplicity, assume the user_id is always valid (you could add real user validation here)
    if user_id:
        # Generate and return a JWT token
        token = generate_token(user_id)
        return jsonify({"status": "success", "token": token}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid login"}), 401

# Example echo endpoint that requires token authorization
@app.route("/echo", methods=['POST'])
def echo():
    auth_header = request.headers.get("Authorization")
    
    if auth_header:
        token = auth_header.split(" ")[1]  # Get the token part from 'Bearer <token>'
        user_id = verify_token(token)
        
        if user_id not in ['Invalid token', 'Token has expired']:
            text = request.form.get('text', '')
            return jsonify({"status": "success", "message": f"User {user_id} said: {text}"}), 200
        else:
            return jsonify({"status": "error", "message": user_id}), 401
    else:
        return jsonify({"status": "error", "message": "Authorization token missing"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
