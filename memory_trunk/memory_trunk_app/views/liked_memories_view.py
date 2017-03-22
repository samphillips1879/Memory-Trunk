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
        memories = request.user.memory_likes.all()
        return render(
            request, 
            self.template_name, 
            {
                'memories': memories,
                'page_title': 'Liked Memories'
            }
        )