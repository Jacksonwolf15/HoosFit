from django.forms import ModelForm, ModelMultipleChoiceField, CharField, CheckboxSelectMultiple
from .models import Exercise, ExercisePlaylist

class CreateNewExercise(ModelForm):
    class Meta:
        model = Exercise
        exclude = ['user']

class CreateNewPlaylist(ModelForm):
    class Meta:
        model = ExercisePlaylist
        exclude = ['user']
    playlist_name = CharField()
    exercises = ModelMultipleChoiceField(
        queryset=Exercise.objects.all(),
        widget=CheckboxSelectMultiple
    )