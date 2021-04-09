from django.db import models
from django.contrib.auth.models import User

class Exercise (models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE) 
    exercise_name = models.CharField(max_length=200)
    target_reps = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.exercise_name

class ExercisePlaylist (models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='playlists')
    playlist_name = models.CharField(max_length=200)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.playlist_name

class Award (models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    exercise = models.OneToOneField(Exercise, on_delete=models.CASCADE)
    award_name = models.CharField(max_length=15)

    def __str__(self):
        return self.award_name