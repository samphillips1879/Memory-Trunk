from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
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
            perspective = models.Perspective.objects.create(
                user=request.user,
                title=form.cleaned_data['title'],
                is_public=form.cleaned_data['is_public'],
                content=form.cleaned_data['content'],
            )
            for tag in form.cleaned_data['tags']:
                perspective.tags.add(tag)
            perspective.save()
            return HttpResponseRedirect(reverse('memory_trunk_app:perspective_detail', args=(perspective.id,)))

    # if a GET (or any other method) create a blank form
    else:
        form = PerspectiveForm()

    return render(
        request, 
        'perspective_creation.html', 
        {'form': form, 'page_title': 'Share a Perspective'}
    )