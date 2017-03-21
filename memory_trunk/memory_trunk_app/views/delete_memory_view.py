from memory_trunk_app import models
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse

def delete_memory(request, id):
    """
    Purpose:
        Processes the deletion of a Memory instance and redirects the user 
        to their Memory list

    Arguments:
        id -- The primary key of the Memory instance to be deleted

    Author: Sam Phillips <samcphillips.com>
    """

    memory = models.Memory.objects.get(id=id)
    if memory.user.id == request.user.id:
        memory.delete()    
    return HttpResponseRedirect(reverse('memory_trunk_app:memory_list', args=(request.user.id,)))