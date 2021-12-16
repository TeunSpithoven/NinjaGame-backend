from rest_framework import serializers
from .models import Game
from django.contrib.auth.models import User


class GameSerializer(serializers.ModelSerializer):  # create class to serializer model
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Game
        fields = ('start_datetime', 'end_datetime', 'score', 'user')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    games = serializers.PrimaryKeyRelatedField(many=True, queryset=Game.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'games')
