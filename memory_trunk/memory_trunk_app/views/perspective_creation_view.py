from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from memory_trunk_app.forms import PerspectiveForm
from memory_trunk_app import models

@login_required
def perspective_creation_view(request):
    """
    Purpose:
        Provide a user interface for creating Perspective objects

    Author: Sam Phillips <samcphillips.com>
    """

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PerspectiveForm(request.POST)
        if form.is_valid():
            tip = models.Perspective.objects.create(
                user=request.user,
                title=form.cleaned_data['title'],
                is_public=form.cleaned_data['is_public'],
                content=form.cleaned_data['content'],
            )
            return HttpResponseRedirect('/')

    # if a GET (or any other method) create a blank form
    else:
        form = PerspectiveForm()

    return render(request, 'perspective_creation.html', {'form': form})