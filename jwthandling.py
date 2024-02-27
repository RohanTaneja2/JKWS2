# jwt_handling.py
import jwt
from datetime import datetime, timedelta


def create_jwt(private_key, kid, expiry):
    """
    Create JWT.
    Args:
        private_key (bytes): Serialized private key.
        kid (str): Key ID associated with the key pair.
        expiry (int): Expiry timestamp for the JWT (in seconds).
    Returns:
        str: JWT string.
    """
    now = datetime.utcnow()
    payload = {
        "iss": "your_issuer",
        "sub": "your_subject",
        "aud": "your_audience",
        "exp": now + timedelta(seconds=expiry),
        "iat": now,
        "kid": kid
    }
    jwt_token = jwt.encode(
        payload,
        private_key,
        algorithm="RS256"
    )
    return jwt_token  # No need to decode here
