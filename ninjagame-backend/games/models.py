from django.db import models


class Game(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', related_name='movies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


