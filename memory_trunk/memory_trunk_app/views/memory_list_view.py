from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from memory_trunk_app import models

class MemoryListView(TemplateView):
    """
    Purpose: 
        List all of a user's memories as hyperlinked titles
    
    Author: Sam Phillips <samcphillips.com>
    """
    template_name = 'memory_list.html'

    def get(self, request, id):
        memories = models.Memory.objects.filter(user=id)


        return render(request, self.template_name, {'memories': memories})