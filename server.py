# server.py
from flask import Flask, request, jsonify
from keygeneration import generate_rsa_key_pair
from jwthandling import create_jwt
from datetime import datetime

app = Flask(__name__)

# Generate RSA key pair
private_key, public_key = generate_rsa_key_pair()
key_id = "your_key_id"
expiry_timestamp = int(datetime.utcnow().timestamp()) + 3600  # Expiry in 1 hour


@app.route('/auth', methods=['POST'])
def auth():
    jwt_token = create_jwt(private_key, key_id, expiry_timestamp)
    return jsonify({"token": jwt_token})


@app.route('/jwks')
def jwks():
    return jsonify({
        "keys": [
            {
                "kid": key_id,
                "kty": "RSA",
                "alg": "RS256",
                "use": "sig",
                "n": public_key.decode('utf-8').split('\n')[1],
                "e": public_key.decode('utf-8').split('\n')[2]
            }
        ]
    })


if __name__ == '__main__':
    app.run(port=8080)
