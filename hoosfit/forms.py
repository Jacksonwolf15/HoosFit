from django.forms import ModelForm
from .models import Exercise, ExercisePlaylist

class CreateNewExercise(ModelForm):
    class Meta:
        model = Exercise
        exclude = ['user']

class CreateNewPlaylist(ModelForm):
    class Meta:
        model = ExercisePlaylist
        exclude = ['user', 'exercises']