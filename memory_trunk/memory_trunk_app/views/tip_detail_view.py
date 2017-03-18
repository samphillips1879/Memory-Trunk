from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from memory_trunk_app import models

class TipDetailView(TemplateView):
    """
    Purpose: 
        Display the detaiils of a specific Tip object
    
    Author: Sam Phillips <samcphillips.com>
    """
    template_name = 'tip_detail.html'

    def get(self, request, id):
        tip = models.Tip.objects.get(id=id)
        if tip.is_public == False:
            if tip.user != request.user:
                return HttpResponseRedirect(redirect_to='/')
        return render(request, self.template_name, {'tip': tip})