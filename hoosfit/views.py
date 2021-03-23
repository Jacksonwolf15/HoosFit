from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CreateNewExercise
from .models import Exercise


# Create your views here.
@login_required
def home(request):
    return HttpResponseRedirect(
        reverse(profile,
                args=[request.user.username]))


def profile(request, user_id):
    return render(request, 'hoosfit/profile.html')


def exercise_home(request, user_id):
    if request.method == "POST":
        form = CreateNewExercise(request.POST)

        if form.is_valid():
            #n = form.cleaned_data["name"]
            #t = form.cleaned_data["target_reps"]
            #e = Exercise(user=request.user.username, exercise_name=n, target_reps=t)
            #e.save()
            #request.user.exercise.add(e)
            form.save()

            #return HttpResponseRedirect("/%i" % e.id)

    else:
        form = CreateNewExercise()

    return render(request, 'hoosfit/exercise.html', {"form": form})


def view_exercises(request, user_id):
    return render(request, 'hoosfit/view_exercise.html')
