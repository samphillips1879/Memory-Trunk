from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from memory_trunk_app import models

class PerspectiveDetailView(TemplateView):
    """
    Purpose: 
        Display the detaiils of a specific Perspective object
    
    Author: Sam Phillips <samcphillips.com>
    """
    template_name = 'perspective_detail.html'

    def get(self, request, id):
        perspective = models.Perspective.objects.get(id=id)
        if perspective.is_public == False:
            if perspective.user != request.user:
                return HttpResponseRedirect(redirect_to='/')
        return render(request, self.template_name, {'perspective': perspective})

def like_perspective(request, id):
    """
    Purpose:
        Provide a means for users to 'like' a Perspective, thus allowing 
        them to view it at a later date

    Arguments:
        id -- The primary key of the Perspective object to be liked by 
        the user

    Author: Sam Phillips <samcphillips.com>
    """
    perspective = models.Perspective.objects.get(id=id)
    perspective.likes.add(request.user)
    return HttpResponseRedirect(reverse('memory_trunk_app:perspective_detail', args=(perspective.id,)))


def dislike_perspective(request, id):
    """
    Purpose:
        Provide a means for users to 'dislike' a Perspective, thus removing it from their saved perspectives

    Arguments:
        id -- The primary key of the Perspective object to be disliked by 
        the user

    Author: Sam Phillips <samcphillips.com>
    """
    perspective = models.Perspective.objects.get(id=id)
    perspective.likes.remove(request.user)
    return HttpResponseRedirect(reverse('memory_trunk_app:perspective_detail', args=(perspective.id,)))