from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .forms import CreateNewExercise, CreateNewWorkout
from .models import Exercise, Workout, Award


# Create your views here.
@login_required
def home(request):
    return HttpResponseRedirect(
        reverse(profile,
                args=[request.user.username]))


def profile(request, user_id):
    return render(request, 'hoosfit/profile.html')

class ExerciseCreate(generic.ListView):
    model = Exercise
    template_name = 'hoosfit/exercise.html'

class WorkoutCreate(CreateView):
    model = Workout
    form_class = CreateNewWorkout
    template_name = 'hoosfit/workout.html'

class ExerciseView(generic.ListView):
    template_name = 'hoosfit/view_exercise.html'
    context_object_name = 'exercise_list'

    def get_queryset(self):
        return Exercise.objects.filter(user__exact = self.request.user, date=datetime.date(2000,1,1))

class WorkoutView(generic.DetailView):
    model = Workout
    template_name = 'hoosfit/workout_form.html'
    context_object_name = 'workout'
    
class WorkoutSummary(generic.DetailView):
    model = Workout
    template_name = 'hoosfit/workout_summary.html'
    context_object_name = 'workout'

class AwardView(generic.ListView):
    model = Award
    template_name = 'hoosfit/view_awards.html'


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


def create_workout(request, user_id):
    if request.method == "POST":
        form = CreateNewWorkout(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            form.save_m2m()
    else:
        form = CreateNewWorkout()
    return HttpResponseRedirect(reverse('workoutstart', kwargs={'user_id' : user_id, 'pk' : workout.id}))


def log_workout(request, user_id, pk):
    for data in request.POST:
        try:
            name = data
            reps = request.POST[data]
            exercise = Exercise()
            exercise.exercise_name = name
            exercise.reps = reps
            exercise.user = request.user
            exercise.date = datetime.date.today()
            exercise.save()
        except:
            continue  # need to have fallback incase of error (or maybe not)
    return HttpResponseRedirect(reverse('workoutsummary', kwargs={'user_id' : user_id, 'pk' : pk})) # also need to pass data to summary