from app import app
import unittest


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json, {"message": "OK", "data": "Hello World"})
        print("测试用例成功")
