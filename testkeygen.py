# test_key_generation.py
import unittest
from keygeneration import generate_rsa_key_pair


class TestKeyGeneration(unittest.TestCase):
    def test_generate_rsa_key_pair(self):
        private_key, public_key = generate_rsa_key_pair()
        self.assertIsNotNone(private_key)
        self.assertIsNotNone(public_key)


if __name__ == '__main__':
    unittest.main()
