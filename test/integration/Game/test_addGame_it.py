from django.test import TestCase
# from django.urls import reverse
from games.models import Game


class RegisterIntegrationTestCase(TestCase):
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
        self.accessToken = response.data["access"]
        self.bearer = {'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.accessToken)}

    def test_addGame(self):
        game_data = {
            "start_datetime": "2019-12-10 14:43:35.542195",
            "end_datetime": "2019-12-10 14:43:35.542195",
            "score": 69,
            "user": 1
        }
        response = self.client.post('/games/', game_data, **self.bearer)
        self.assertEqual(response.status_code, 201)

        game = Game.objects.get(user=1)
        self.assertIsNotNone(game)
        self.assertEqual(game.score, 69)
