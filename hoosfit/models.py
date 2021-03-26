from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Exercise (models.Model):
    user = models.CharField(max_length=200, null=True) #why would we give them any option for a user? shouldn't it just be them
    exercise_name = models.CharField(max_length=200)
    target_reps = models.IntegerField(default=0)

    def __str__(self):
        return self.exercise_name
