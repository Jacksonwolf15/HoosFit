from django.forms import ModelForm, ModelMultipleChoiceField, CharField, CheckboxSelectMultiple
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
        queryset=Exercise.objects.all(),  # Need to filter out duplicate names and stuff that doesn't belong to user
        widget=CheckboxSelectMultiple
    )