from django.contrib import admin

# Register your models here.
from .models import Exercise, ExercisePlaylist

admin.site.register(Exercise)
admin.site.register(ExercisePlaylist)