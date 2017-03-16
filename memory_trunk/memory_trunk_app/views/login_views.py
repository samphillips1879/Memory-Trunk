from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect

class LoginUserView(TemplateView):
    """
    Purpose:
        Provide users with a form for logging in

    Author: Sam Phillips <samcphillips.com>
    """
    template_name = "login_user.html"

def login_user(request):
    """
    Purpose: 
        Login a user using their username and password
    
    Author: Sam Phillips <samcphillips.com>
    """
    data = request.POST

    username = data['username']
    password = data['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request=request, user=user)
    else:
        # Not successful, redirect to index page
        return HttpResponseRedirect(redirect_to='/')
    # Successful, redirect to index page
    return HttpResponseRedirect(redirect_to='/')

def logout_user(request):
    """
    Purpose:
        Logout the user requesting this view

    Author: Sam Phillips <samcphillips.com>
    """
    logout(request)
    return HttpResponseRedirect(redirect_to='/')
