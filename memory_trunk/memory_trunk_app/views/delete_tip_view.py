from memory_trunk_app import models
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse

def delete_tip(request, id):
    """
    Purpose:
        Processes the deletion of a Tip instance and redirects 
        the user to their Tip list

    Arguments:
        id -- The primary key of the Tip instance to be deleted

    Author: Sam Phillips <samcphillips.com>
    """

    tip = models.Tip.objects.get(id=id)
    if tip.user.id == request.user.id:
        tip.delete()    
    return HttpResponseRedirect(reverse('memory_trunk_app:tip_list', args=(request.user.id,)))
