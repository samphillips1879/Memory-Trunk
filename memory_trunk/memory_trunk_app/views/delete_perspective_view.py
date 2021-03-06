from memory_trunk_app import models
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse

def delete_perspective(request, id):
    """
    Purpose:
        Processes the deletion of a Perspective instance and redirects 
        the user to their Perspective list

    Arguments:
        id -- The primary key of the Perspective instance to be deleted

    Author: Sam Phillips <samcphillips.com>
    """

    perspective = models.Perspective.objects.get(id=id)
    if perspective.user.id == request.user.id:
        perspective.delete()
    return HttpResponseRedirect(reverse('memory_trunk_app:perspective_list', args=(request.user.id,)))