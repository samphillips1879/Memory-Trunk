from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from memory_trunk_app import models

class MemoryDetailView(TemplateView):
    """
    Purpose: 
        Display the detaiils of a specific Memory object
    
    Author: Sam Phillips <samcphillips.com>
    """
    template_name = 'memory_detail.html'

    def get(self, request, id):
        memory = models.Memory.objects.get(id=id)
        if memory.is_public == False:
            if memory.user != request.user:
                return HttpResponseRedirect(redirect_to='/')
        return render(request, self.template_name, {'memory': memory})

def like_memory(request, id):
    """
    Purpose:
        Provide a means for users to 'like' a memory, thus allowing 
        them to view it at a later date

    Arguments:
        id -- The primary key of the Memory object to be liked by 
        the user

    Author: Sam Phillips <samcphillips.com>
    """
    memory = models.Memory.objects.get(id=id)
    memory.likes.add(request.user)
    return HttpResponseRedirect(redirect_to='/')


def dislike_memory(request, id):
    """
    Purpose:
        Provide a means for users to 'unlike' a Memory, thus removing 
        it from their saved memories

    Arguments:
        id -- The primary key of the Memory object to be unliked by 
        the user

    Author: Sam Phillips <samcphillips.com>
    """
    memory = models.Memory.objects.get(id=id)
    memory.likes.remove(request.user)
    return HttpResponseRedirect(redirect_to='/')