from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    return HttpResponseRedirect(
        reverse(profile,
                args=[request.user.username]))


def profile(request, user_id):
    return render(request, 'hoosfit/profile.html')
