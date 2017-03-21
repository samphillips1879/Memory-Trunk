from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from memory_trunk_app import models

class LikedTipsView(TemplateView):
    """
    Purpose: 
        List all of the Tips a user has liked as hyperlinked titles
    
    Author: Sam Phillips <samcphillips.com>
    """
    template_name = 'tip_list.html'

    def get(self, request, id):
        tips = request.user.memory_likes_set.all()
        return render(
            request, 
            self.template_name, 
            {
                'tips': tips,
                'page_title': 'Liked Tips'
            }
        )