# test_jwt_handling.py
import unittest
from jwthandling import create_jwt
from keygeneration import generate_rsa_key_pair


class TestJWTHandling(unittest.TestCase):
    def test_create_jwt(self):
        private_key, _ = generate_rsa_key_pair()
        jwt_token = create_jwt(private_key, "test_key_id", 3600)
        self.assertIsNotNone(jwt_token)


if __name__ == '__main__':
    unittest.main(exit=False)
