from django.test import TestCase
# from django.urls import reverse


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

        game_data = {
            "start_datetime": "2019-12-10 14:43:35.542195",
            "end_datetime": "2019-12-10 14:43:35.542195",
            "score": 69,
            "user": 1
        }
        response = self.client.post('/games/', game_data, **self.bearer)

    def test_getGames(self):
        response = self.client.get('/games/', **self.bearer)
        self.assertEqual(response.status_code, 200)
        results = response.data["results"]

        l1 = len(results[0]["start_datetime"])
        l2 = len(results[0]["end_datetime"])

        results[0]["start_datetime"] = results[0]["start_datetime"][:l1-1]
        results[0]["end_datetime"] = results[0]["end_datetime"][:l2-1]

        self.assertEqual(results[0]["start_datetime"], "2019-12-10T14:43:35.542195")
        self.assertEqual(results[0]["end_datetime"], "2019-12-10T14:43:35.542195")
        self.assertEqual(results[0]["score"], 69)
        self.assertEqual(results[0]["user"], "refreshTestUser")
