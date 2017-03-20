from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
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