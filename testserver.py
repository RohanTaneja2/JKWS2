# test_server.py
import unittest
from server import app


class TestServer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_auth_endpoint(self):
        response = self.app.post('/auth')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json)

    def test_jwks_endpoint(self):
        response = self.app.get('/jwks')
        self.assertEqual(response.status_code, 200)
        self.assertIn('keys', response.json)


if __name__ == '__main__':
    unittest.main()
