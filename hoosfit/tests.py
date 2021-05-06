from django.test import TestCase
from django.contrib.auth.models import User
from .models import Exercise, Award, Workout
import datetime

class ExerciseModelTest(TestCase):
    def test_duplicate_exercise(self):
        user = User.objects.create_user(username='test', email='test@virginia.edu', password='password')
        exercise = Exercise.objects.create(user=user, exercise_name='test')
        duplicate_exercise = Exercise.objects.create(user=user, exercise_name='test')
        qs = Exercise.objects.filter(user__exact=user, date=datetime.date(2000,1,1))
        self.assertEqual(qs.count(), 1)
