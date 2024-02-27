# main.py
from keygeneration import generate_rsa_key_pair
from jwthandling import create_jwt
from server import app

# Generate RSA key pair
private_key, public_key = generate_rsa_key_pair()
key_id = "your_key_id"
expiry_timestamp = 3600  # Expiry in 1 hour

# Create JWT
jwt_token = create_jwt(private_key, key_id, expiry_timestamp)
print("Generated JWT:", jwt_token)

# Start Flask server
if __name__ == '__main__':
    app.run(port=8080)
