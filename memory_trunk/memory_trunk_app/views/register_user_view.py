# from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# from django.contrib.auth import logout, login, authenticate
# from django.http import HttpResponse, HttpResponseRedirect
from memory_trunk_app import models
from .login_user import login_user


class UserRegistration(TemplateView):
    template_name = 'register.html'

def register_user(request):
        """
        Purpose: 
            Register a User, create their Profile, and log them in 
        
        Author: Sam Phillips <samcphillips.com>
        """
        # create_user is what holds the username/password. (Django magic)
        # then, we pass that into the 1:1 field on our model
        # send all of the information to login_customer on login_view.py

        data = request.POST

        new_user = User.objects.create_user(
            username = data['username'], 
            email = data['email'],
            password = data['password'],
            first_name = data['first_name'],
            last_name = data['last_name'],
        )

        models.Profile.objects.create(
            user = new_user,
        )

        return login_user(request)


