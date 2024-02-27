# key_generation.py
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


def generate_rsa_key_pair():
    """
    Generate RSA key pair.
    Returns:
        Private key (bytes): Serialized private key.
        Public key (bytes): Serialized public key.
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key = private_key.public_key()
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return private_key_bytes, public_key_bytes
