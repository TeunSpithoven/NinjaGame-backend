from django.test import TestCase


class LoginIntegrationTestCase(TestCase):
    def setUp(self):
        self.username = "testLoginUsername"
        self.password = "passwordhutser1!"
        self.url = "/auth/token/"

        register_data = {
            "username": self.username,
            "password": self.password,
            "password2": self.password
        }
        self.client.post('/auth/register/', register_data)

    def test_login_success(self):
        login_data = {
            "username": self.username,
            "password": self.password
        }
        response = self.client.post(self.url, login_data)
        jsonResponse = response.data
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(jsonResponse["access"])
        self.assertIsNotNone(jsonResponse["refresh"])

    def test_login_failure(self):
        login_data = {
            "username": self.username,
            "password": "passwo"
        }
        response = self.client.post(self.url, login_data)
        jsonResponse = response.data
        self.assertNotEqual(response.status_code, 200)
        self.assertIsNotNone(jsonResponse["detail"])
        self.assertEqual(jsonResponse["detail"], "No active account found with the given credentials")
