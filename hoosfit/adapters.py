from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.adapter import DefaultAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from django.http import HttpResponse

class MySocialAccount(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        u = sociallogin.user
        if not u.email.split('@')[1] == "virginia.edu":
            return render(request, 'hoosfit/index2.html')
    def populate_user(self, request, sociallogin, data):
        email = data.get("email")
        username = email.split('@')[0]
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        user = sociallogin.user
        user.email = email
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        return user
