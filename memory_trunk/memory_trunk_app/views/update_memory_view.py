from memory_trunk_app import models
from django.http import HttpResponseRedirect
from django.shortcuts import render
from memory_trunk_app.forms import MemoryForm

def update_memory(request, id):
    """
    Purpose:
        Provide users with an interface for editing memories they have 
        saved to their MemoryTrunk

    Author: Sam Phillips <samcphillips.com>
    """
    memory = models.Memory.objects.get(id=id)
    if request.method == 'POST':
        if memory.user == request.user:
            # create a form instance and populate it with data from the request:
            form = MemoryForm(request.POST)
            if form.is_valid():
                memory.title=form.cleaned_data['title']
                memory.is_public=form.cleaned_data['is_public']
                memory.date=form.cleaned_data['date']
                memory.location=form.cleaned_data['location']
                memory.content=form.cleaned_data['content']
                memory.happy_factor=form.cleaned_data['happy_factor']
                memory.sad_factor=form.cleaned_data['sad_factor']
                memory.save()
                return HttpResponseRedirect('/')
        return HttpResponseRedirect('/')
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MemoryForm(instance=memory)

    return render(
        request, 
        'memory_update_form.html', 
        {
            'form': form,
            'memory': memory
        }
    )