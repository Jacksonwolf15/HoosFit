from django.forms import ModelForm, ModelMultipleChoiceField, CharField, CheckboxSelectMultiple
import datetime
from .models import Exercise, Workout

class CreateNewExercise(ModelForm):
    class Meta:
        model = Exercise
        exclude = ['user', 'reps', 'date']

class CreateNewWorkout(ModelForm):
    class Meta:
        model = Workout
        exclude = ['user']

    workout_name = CharField()
    exercises = ModelMultipleChoiceField(
        queryset=Exercise.objects.filter(date=datetime.date(2000,1,1)),  # Need to filter out stuff that doesn't belong to user
        widget=CheckboxSelectMultiple
    )