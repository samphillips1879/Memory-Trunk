from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from memory_trunk_app.forms import TipForm
from memory_trunk_app import models

@login_required
def tip_creation_view(request):
    """
    Purpose:
        Provide a user interface for creating Tip objects

    Author: Sam Phillips <samcphillips.com>
    """

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TipForm(request.POST)
        if form.is_valid():
            tip = models.Tip.objects.create(
                user=request.user,
                title=form.cleaned_data['title'],
                do=form.cleaned_data['do'],
                is_public=form.cleaned_data['is_public'],
                content=form.cleaned_data['content'],
            )
            for tag in form.cleaned_data['tags']:
                tip.tags.add(tag)
            tip.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TipForm()

    return render(request, 'tip_creation.html', {'form': form})