from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
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
    context = {}
    if request.method == "POST":
        form = CreateNewExercise(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.user = request.user
            exercise.save()
        context['form'] = form
        context['user_id'] = user_id
    else:
        form = CreateNewExercise()
        context['form'] = form
        context['user_id'] = user_id
    return render(request, "hoosfit/exercise.html", context)


class ExerciseView(generic.ListView):
    template_name = 'hoosfit/view_exercise.html'
    context_object_name = 'exercise_list'

    def get_queryset(self):
        return Exercise.objects.all()

#def view_exercises(request, user_id):  # this currently throws an error
    #form = CreateNewExercise(request.GET)
    #results = form.objects.all()  # specifically on this line
    #context = {'results' : results}
    #return render(request, 'hoosfit/view_exercise.html', context)
