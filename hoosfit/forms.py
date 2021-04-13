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

    # def __init__(self, *args, **kwargs):
    #    user = kwargs.pop('user')
    #    super(CreateNewPlaylist, self).__init__(*args, **kwargs)
    #    self.fields['exercises'].queryset = Exercise.objects.filter(user=user)

    playlist_name = CharField()
    exercises = ModelMultipleChoiceField(
        queryset=Exercise.objects.all(),
        widget=CheckboxSelectMultiple
    )