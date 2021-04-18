from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .forms import CreateNewExercise, CreateNewPlaylist
from .models import Exercise, ExercisePlaylist, Award, Profile


# Create your views here.
@login_required
def home(request):
    return HttpResponseRedirect(
        reverse(profile,
                args=[request.user.username]))


def profile(request, user_id):
    request.user.profile.streak_number += 1
    request.user.profile.save()
    return render(request, 'hoosfit/profile.html')

def create_exercise(request, user_id):
    context = {}
    if request.method == "POST":
        form = CreateNewExercise(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.user = request.user
            exercise.save()
        context['form'] = form
    else:
        form = CreateNewExercise()
        context['form'] = form
    return HttpResponseRedirect(reverse('exerciseview', kwargs={'user_id' : user_id}))


class ExerciseCreate(generic.ListView):
    model = Exercise
    template_name = 'hoosfit/exercise.html'

class PlaylistCreate(CreateView):
    model = ExercisePlaylist
    form_class = CreateNewPlaylist
    template_name = 'hoosfit/playlist.html'

def create_playlist(request, user_id):
    context = {}
    if request.method == "POST":
        form = CreateNewPlaylist(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            form.save_m2m()
        context['form'] = form
    else:
        form = CreateNewPlaylist()
        context['form'] = form
    return HttpResponseRedirect(reverse('playlistview', kwargs={'user_id' : user_id}))

class ExerciseView(generic.ListView):
    template_name = 'hoosfit/view_exercise.html'
    context_object_name = 'exercise_list'

    def get_queryset(self):
        return Exercise.objects.all()

class PlaylistView(generic.ListView):
    template_name = 'hoosfit/view_playlists.html'
    context_object_name = 'playlist_list'

    def get_queryset(self):
        return ExercisePlaylist.objects.all()

class AwardView(generic.ListView):
    model = Award
    template_name = 'hoosfit/view_awards.html'