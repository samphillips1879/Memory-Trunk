from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from memory_trunk_app import models

class LikedPerspectivesView(TemplateView):
    """
    Purpose: 
        List all of the Perspectives a user has liked as hyperlinked titles
    
    Author: Sam Phillips <samcphillips.com>
    """
    template_name = 'perspective_list.html'

    def get(self, request, id):
        perspectives = request.user.perspective_likes.all()
        return render(
            request, 
            self.template_name, 
            {
                'perspectives': perspectives,
                'page_title': 'Liked Perspectives'
            }
        )