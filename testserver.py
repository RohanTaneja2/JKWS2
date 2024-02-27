import unittest
import requests

class TestServer(unittest.TestCase):

    def test_jwks_endpoint(self):
        response = requests.get('http://127.0.0.1:8080/jwks')
        self.assertEqual(response.status_code, 200)
        self.assertIn('keys', response.json())

    def test_auth_endpoint(self):
        response = requests.post('http://127.0.0.1:8080/auth')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
