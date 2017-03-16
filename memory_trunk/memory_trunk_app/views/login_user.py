from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect


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

# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect(redirect_to='/')
