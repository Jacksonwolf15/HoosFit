from django.contrib import admin

# Register your models here.
from .models import Exercise, ExercisePlaylist, Award

admin.site.register(Exercise)
admin.site.register(ExercisePlaylist)
admin.site.register(Award)