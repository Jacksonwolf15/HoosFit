from django.db import models
from django.contrib.auth.models import User

class ExercisePlaylist (models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='playlists')
    playlist_name = models.CharField(max_length=200)

    def __str__(self):
        return self.playlist_name


class Exercise (models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE) 
    playlist = models.ForeignKey(ExercisePlaylist, null=True, default=1, on_delete=models.SET_DEFAULT, related_name='exercises')
    exercise_name = models.CharField(max_length=200)
    target_reps = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.exercise_name

