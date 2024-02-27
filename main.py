# main.py
from keygeneration import generate_rsa_key_pair
from jwthandling import create_jwt
from server import app
import requests

# Generate RSA key pair
private_key, _ = generate_rsa_key_pair()
key_id = "your_key_id"
expiry_timestamp = 3600  # Expiry in 1 hour

# Create JWT
jwt_token = create_jwt(private_key, key_id, expiry_timestamp)
print("Generated JWT:", jwt_token)

# Send a POST request to the /auth endpoint
auth_url = 'http://127.0.0.1:8080/auth'
response = requests.post(auth_url)
print("Response from /auth endpoint:", response.text)

# Start Flask server
if __name__ == '__main__':
    app.run(port=8080)
