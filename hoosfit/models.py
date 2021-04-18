from django.db import models
import datetime
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Exercise (models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE) 
    exercise_name = models.CharField(max_length=200)
    date = models.DateField(default=datetime.date(2000,1,1))
    reps = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.exercise_name

class Workout (models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='workouts')
    workout_name = models.CharField(max_length=200)
    exercises = models.ManyToManyField(Exercise)
    date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.workout_name

class Award (models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    exercise = models.OneToOneField(Exercise, on_delete=models.CASCADE)
    award_name = models.CharField(max_length=15)

    def __str__(self):
        return self.award_name

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    streak_number = models.PositiveIntegerField(default=0)
    previous_login = models.DateTimeField('streak', null=True) 
    

    def __str__(self):
        return self.user.username

    # def valid_streak(self):
    #     now = timezone.now()
    #     valid_streak.boolean = True

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()


