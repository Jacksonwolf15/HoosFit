from django import forms


class CreateNewExercise(forms.Form):
    name = forms.CharField(label="Exercise Name", max_length=200)
    target_reps = forms.IntegerField(label="Target Number of Reps")
