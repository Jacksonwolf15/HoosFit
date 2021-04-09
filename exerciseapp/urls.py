"""exerciseapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from hoosfit.views import home, profile, exercise_home, exercise_playlist_home, ExerciseAdd, ExerciseView, PlaylistAdd

app_name = 'exerciseapp'
urlpatterns = [
    path('', TemplateView.as_view(template_name='hoosfit/index.html'), name='start'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profiles/home/', home),
    path('profiles/<str:user_id>/', profile, name='homepage'),
    path('profiles/<str:user_id>/exercise/', ExerciseAdd.as_view(), name='exerciseadd'),
    path('profiles/<str:user_id>/exercise/submit', exercise_home, name='exercisesubmit'),
    path('profiles/<str:user_id>/playlist/', PlaylistAdd.as_view(), name='playlistadd'),
    path('profiles/<str:user_id>/playlist/submit', exercise_playlist_home, name='playlistsubmit'),
    path('profiles/<str:user_id>/exercise/view/', ExerciseView.as_view(), name='exerciseview'),
]
