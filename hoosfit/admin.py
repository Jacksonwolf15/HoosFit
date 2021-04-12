from django.contrib import admin

# Register your models here.
from .models import Exercise, ExercisePlaylist, Award, Profile

admin.site.register(Exercise)
admin.site.register(ExercisePlaylist)
admin.site.register(Award)
admin.site.register(Profile)