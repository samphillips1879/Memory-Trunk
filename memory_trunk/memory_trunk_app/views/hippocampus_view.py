from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from memory_trunk_app.forms import MemoryForm
from memory_trunk_app import models

@login_required
def hippocampus_view(request):
    """
    Purpose:
        Provide a user interface for creating Memory Objects

    Author: Sam Phillips <samcphillips.com>
    """

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MemoryForm(request.POST)
        if form.is_valid():
            print("request.user: {}".format(request.user))
            memory = models.Memory.objects.create(
                user=request.user,
                title=form.cleaned_data['title'],
                is_public=form.cleaned_data['is_public'],
                date=form.cleaned_data['date'],
                location=form.cleaned_data['location'],
                content=form.cleaned_data['content'],
                happy_factor=form.cleaned_data['happy_factor'],
                sad_factor=form.cleaned_data['sad_factor'],
            )
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MemoryForm()

    return render(request, 'hippocampus.html', {'form': form})