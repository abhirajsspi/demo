import unittest
from app import app

class AppTestCase(unittest.TestCase):

    def test_home(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data.decode(), 'Hello, world!')

if __name__ == '__main__':
    unittest.main()
