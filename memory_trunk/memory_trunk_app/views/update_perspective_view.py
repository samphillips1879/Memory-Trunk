from memory_trunk_app import models
from django.http import HttpResponseRedirect
from django.shortcuts import render
from memory_trunk_app.forms import PerspectiveForm

def update_perspective(request, id):
    """
    Purpose:
        Provide users with an interface for editing perspectives they have 
        saved to their MemoryTrunk

    Author: Sam Phillips <samcphillips.com>
    """
    perspective = models.Perspective.objects.get(id=id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PerspectiveForm(request.POST)
        if form.is_valid():
            perspective.title=form.cleaned_data['title']
            perspective.is_public=form.cleaned_data['is_public']
            perspective.content=form.cleaned_data['content']
            perspective.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PerspectiveForm(instance=perspective)

    return render(
        request, 
        'perspective_update_form.html', 
        {
            'form': form,
            'perspective': perspective
        }
    )