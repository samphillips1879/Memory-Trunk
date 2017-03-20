from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from memory_trunk_app import models

class PerspectiveListView(TemplateView):
    """
    Purpose: 
        List all of a user's perspectives as hyperlinked titles
    
    Author: Sam Phillips <samcphillips.com>
    """
    template_name = 'perspective_list.html'

    def get(self, request, id):
        perspectives = models.Perspective.objects.filter(user=id)
        return render(
            request, 
            self.template_name, 
            {
                'perspectives': perspectives,
                'page_title': 'Community Perspectives'
            }
        )


class PublicPerspectiveListView(TemplateView):
    """
    Purpose: 
        List all public perspectives as hyperlinked titles
    
    Author: Sam Phillips <samcphillips.com>
    """
    template_name = 'perspective_list.html'

    def get(self, request):
        perspectives = models.Perspective.objects.filter(is_public=True)
        return render(
            request, 
            self.template_name, 
            {
                'perspectives': perspectives,
                'page_title': 'Community Perspectives'
            }
        )
