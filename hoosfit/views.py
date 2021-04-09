from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import CreateNewExercise, CreateNewPlaylist, CreateNewExerciseWithPlaylist
from .models import Exercise, ExercisePlaylist


# Create your views here.
@login_required
def home(request):
    return HttpResponseRedirect(
        reverse(profile,
                args=[request.user.username]))


def profile(request, user_id):
    return render(request, 'hoosfit/profile.html')


def exercise_home(request, user_id):
    context = {}
    if request.method == "POST":
        if len(ExercisePlaylist.objects.filter(user=request.user)) > 0:
            form = CreateNewExerciseWithPlaylist(request.POST)
            context['playlists'] = ExercisePlaylist.objects.filter(user=request.user)
        else:
            form = CreateNewExercise(request.POST)
            context['playlist'] = False
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.user = request.user
            exercise.save()
        context['form'] = form
    else:
        form = CreateNewExercise()
        context['form'] = form
    return HttpResponseRedirect(reverse('exerciseview', kwargs={'user_id' : user_id}), context)


class ExerciseAdd(generic.ListView):
    model = Exercise
    template_name = 'hoosfit/exercise.html'


def exercise_playlist_home(request, user_id):
    context = {}
    if request.method == "POST":
        form = CreateNewPlaylist(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
        context['form'] = form
    else:
        form = CreateNewPlaylist()
        context['form'] = form
    return HttpResponseRedirect(reverse('exerciseadd', kwargs={'user_id' : user_id}))


class PlaylistAdd(generic.ListView):
    model = ExercisePlaylist
    template_name = 'hoosfit/playlist.html'


class ExerciseView(generic.ListView):
    template_name = 'hoosfit/view_exercise.html'
    context_object_name = 'exercise_list'

    def get_queryset(self):
        return Exercise.objects.all()