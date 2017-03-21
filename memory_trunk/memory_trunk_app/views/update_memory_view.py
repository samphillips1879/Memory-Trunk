from memory_trunk_app import models
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
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
        print("trying to post")
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




            # memory = models.Memory.objects.create(
            #     user=request.user,
            #     title=form.cleaned_data['title'],
            #     is_public=form.cleaned_data['is_public'],
            #     date=form.cleaned_data['date'],
            #     location=form.cleaned_data['location'],
            #     content=form.cleaned_data['content'],
            #     happy_factor=form.cleaned_data['happy_factor'],
            #     sad_factor=form.cleaned_data['sad_factor'],
            # )
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


    

# def update_tip(self, request, id):
#     """
#     Purpose:
#         Processes the deletion of a Tip instance and redirects 
#         the user to home

#     Arguments:
#         id -- The primary key of the Tip instance to be deleted

#     Author: Sam Phillips <samcphillips.com>
#     """

#     tip = models.Tip.objects.get(id=id)
#     if tip.user.id == request.user.id:
#         tip.delete()    
#     return HttpResponseRedirect(redirect_to='/')