from django.test import TestCase

from django.contrib.auth.models import User
from django.contrib import auth
from django.test import Client
from django.urls import reverse

def test_login_valid():
    username = {'username': 'bob','password': 'bobbobbob'}
    user = User.objects.create_user(**username)
    C = Client()
    r = C.post(reverse('login'), user)
    su = auth.get_user(r.wsgi_request)

    print(username)
    print(r)
    print(su)
    print(su.is_authenticated)
    print(r.wsgi_request.user)
    print(r.wsgi_request.user.is_authenticated)
