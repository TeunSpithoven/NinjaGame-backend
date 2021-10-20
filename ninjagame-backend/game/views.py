from django.http.response import HttpResponse
from django.shortcuts import render
from game.models import Game
from user import views as UserViews

# Create your views here.

def create_game(request):
    score = 500
    username = 'teun'
    user = UserViews.get_user_byusername(username)
    Game(score='{score}', user='{user}')
    return HttpResponse("game created")
