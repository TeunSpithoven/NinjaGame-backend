from django.test import TestCase
from django.contrib.auth.models import User


class RegisterTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="testRegisterUsername", password="hats123!")

    def test_user_created(self):
        user = User.objects.get(username="testRegisterUsername")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "testRegisterUsername")
