from flask import Flask, request, jsonify
from keygeneration import generate_rsa_key_pair
from jwthandling import create_jwt
import datetime
from cryptography.hazmat.primitives import serialization

app = Flask(__name__)

# Generate RSA key pair
private_key, public_key = generate_rsa_key_pair()
key_id = "your_key_id"
expiry_timestamp = datetime.datetime.now() + datetime.timedelta(hours=1)

# Create JWKS endpoint
@app.route('/jwks', methods=['GET'])
def jwks():
    jwks_data = {
        "keys": [{
            "alg": "RS256",
            "e": public_key.public_bytes(
                encoding=serialization.Encoding.DER,
                format=serialization.PublicFormat.PKCS1
            ).hex(),
            "kid": key_id,
            "kty": "RSA",
            "n": public_key.public_bytes(
                encoding=serialization.Encoding.DER,
                format=serialization.PublicFormat.PKCS1
            ).hex(),
            "use": "sig"
        }]
    }
    return jsonify(jwks_data)

# Create /auth endpoint
@app.route('/auth', methods=['POST'])
def auth():
    if request.method == 'POST':
        jwt_token = create_jwt(private_key, key_id, expiry_timestamp)
        return jwt_token
    else:
        return "Method Not Allowed", 405

if __name__ == '__main__':
    app.run(port=8080)
