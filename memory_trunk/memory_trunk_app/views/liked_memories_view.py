from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from memory_trunk_app import models

class LikedMemoriesView(TemplateView):
    """
    Purpose: 
        List all of the Memories a user has liked as hyperlinked titles
    
    Author: Sam Phillips <samcphillips.com>
    """
    template_name = 'memory_list.html'

    def get(self, request, id):
        perspectives = models.Perspective.objects.filter(user=id)
        return render(
            request, 
            self.template_name, 
            {
                'perspectives': perspectives,
                'page_title': 'My Perspectives'
            }
        )