from django.forms import ModelForm
from .models import Exercise, ExercisePlaylist

class CreateNewExercise(ModelForm):
    class Meta:
        model = Exercise
        exclude = ['user']


class CreateNewExerciseWithPlaylist(ModelForm):
    class Meta:
        model = Exercise
        exclude = ['user', 'playlist']


class CreateNewPlaylist(ModelForm):
    class Meta:
        model = ExercisePlaylist
        exclude = ['user']
