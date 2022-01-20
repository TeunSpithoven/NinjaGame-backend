from django.test import TestCase
# from django.urls import reverse
from django.contrib.auth.models import User


class RegisterIntegrationTestCase(TestCase):
    def test_register_success(self):
        username = "hutser"
        password = "passwordhutser1!"
        url = "/auth/register/"

        register_data = {
            "username": username,
            "password": password,
            "password2": password
        }
        response = self.client.post(url, register_data)
        self.assertEqual(response.status_code, 201)

        user = User.objects.get(username=username)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, username)

    def test_register_mustBeUnique(self):
        username = "hutser"
        password = "passwordhutser1!"
        url = "/auth/register/"

        register_data = {
            "username": username,
            "password": password,
            "password2": password
        }
        response = self.client.post(url, register_data)
        response = self.client.post(url, register_data)
        code = response.data["username"][0]
        self.assertEqual(response.status_code, 400)
        self.assertEqual(code, "This field must be unique.")
