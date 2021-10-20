from django.http import HttpResponse
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.core import serializers

# Create your views here.

def create_user(request):
    response = "create user"
    return HttpResponse(response)

def get_user_all(request):
    User_json = serializers.serialize("json", User.objects.all())
    data = {"User_json": User_json}
    return JsonResponse(data)

def get_user_byusername(request, username):
    user = User.objects.get(username__iexact = username)
    return user
