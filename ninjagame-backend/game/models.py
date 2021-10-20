from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Game(models.Model):
    created = models.DateTimeField(default=timezone.now())
    score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=CASCADE)
