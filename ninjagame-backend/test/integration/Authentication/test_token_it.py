from django.test import TestCase


class LoginIntegrationTestCase(TestCase):
    def setUp(self):
        register_data = {
            "username": "testLoginUsername",
            "password": "passwordhutser1!",
            "password2": "passwordhutser1!"
        }
        self.client.post('/auth/register/', register_data)

    def test_login(self):
        login_data = {
            "username": "testLoginUsername",
            "password": "passwordhutser1!"
        }
        response = self.client.post('/auth/token/', login_data)
        jsonResponse = response.data
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(jsonResponse["access"])
        self.assertIsNotNone(jsonResponse["refresh"])
