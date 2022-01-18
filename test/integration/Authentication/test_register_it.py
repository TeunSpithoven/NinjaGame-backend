from django.test import TestCase
# from django.urls import reverse
from django.contrib.auth.models import User


class RegisterIntegrationTestCase(TestCase):
    def test_register_success(self):
        register_data = {
            "username": "hutser",
            "password": "passwordhutser1!",
            "password2": "passwordhutser1!"
        }
        response = self.client.post('/auth/register/', register_data)
        self.assertEqual(response.status_code, 201)

        user = User.objects.get(username="hutser")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "hutser")

    def test_register_mustBeUnique(self):
        register_data = {
            "username": "hutser",
            "password": "passwordhutser1!",
            "password2": "passwordhutser1!"
        }
        response = self.client.post('/auth/register/', register_data)
        response = self.client.post('/auth/register/', register_data)
        code = response.data["username"][0]
        self.assertEqual(response.status_code, 400)
        self.assertEqual(code, "This field must be unique.")
