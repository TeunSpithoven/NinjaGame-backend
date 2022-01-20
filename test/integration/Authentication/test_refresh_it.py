from django.test import TestCase


class RefreshIntegrationTestCase(TestCase):
    def setUp(self):
        self.username = "refreshTestUser"
        self.password = "passwordhutser1!"

        register_data = {
            "username": self.username,
            "password": self.password,
            "password2": self.password
        }
        self.client.post('/auth/register/', register_data)
        login_data = {
            "username": self.username,
            "password": self.password
        }
        response = self.client.post('/auth/token/', login_data)
        self.accessToken = response.data["refresh"]

    def test_refresh(self):
        refresh_data = {
            "refresh": self.accessToken
        }
        response = self.client.post('/auth/token/refresh/', refresh_data)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data["access"])
