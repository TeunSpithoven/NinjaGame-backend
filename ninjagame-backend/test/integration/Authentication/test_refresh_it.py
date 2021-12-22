from django.test import TestCase


class RefreshIntegrationTestCase(TestCase):
    def setUp(self):
        register_data = {
            "username": "refreshTestUser",
            "password": "passwordhutser1!",
            "password2": "passwordhutser1!"
        }
        self.client.post('/auth/register/', register_data)
        login_data = {
            "username": "refreshTestUser",
            "password": "passwordhutser1!"
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
