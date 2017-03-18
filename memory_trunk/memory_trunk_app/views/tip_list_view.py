from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from memory_trunk_app import models

class TipListView(TemplateView):
    """
    Purpose: 
        List all of a user's tips as hyperlinked titles
    
    Author: Sam Phillips <samcphillips.com>
    """
    template_name = 'tip_list.html'

    def get(self, request, id):
        tips = models.Tip.objects.filter(user=id)
        return render(
            request, 
            self.template_name, 
            {
                'tips': tips,
                'page_title': 'My Tips'
            }
        )


class PublicTipListView(TemplateView):
    """
    Purpose: 
        List all public tips as hyperlinked titles
    
    Author: Sam Phillips <samcphillips.com>
    """
    template_name = 'tip_list.html'

    def get(self, request):
        tips = models.Tip.objects.filter(is_public=True)
        return render(
            request, 
            self.template_name, 
            {
                'tips': tips,
                'page_title': 'Community Tips'
            }
        )
