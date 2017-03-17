from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from memory_trunk_app.forms import MemoryForm

def hippocampus_view(request):
    """
    Purpose:
        Provide a user interface for creating Memory Objects

    Author: Sam Phillips <samcphillips.com>
    """

    if request.method == 'POST':
        """Form view"""
        # create a form instance and populate it with data from the request:
        form = MemoryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MemoryForm()

    return render(request, 'hippocampus.html', {'form': form})