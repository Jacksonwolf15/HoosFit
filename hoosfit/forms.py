from django.forms import ModelForm
from .models import Exercise

class CreateNewExercise(ModelForm):
    class Meta:
        model = Exercise
        fields = "__all__"
