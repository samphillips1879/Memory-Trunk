from django.views.generic.base import TemplateView
from django.shortcuts import render
from memory_trunk_app import models

class IndexView(TemplateView):
    """
    Purpose:
        This view serves as the landing page for MemoryTrunk

    Author: Sam Phillips <samcphillips.com>
    """

    template_name = "index.html"
    context = {}

    def get(self, request):
        """
        Retrieves the last ten instances created of each model for 
        displaying their links on the index view
        """
        self.context['memories'] = models.Memory.objects.filter(is_public=True).order_by('-id')[:10][::-1]
        self.context['tips'] = models.Tip.objects.filter(is_public=True).order_by('-id')[:10][::-1]
        self.context['perspectives'] = models.Perspective.objects.filter(is_public=True).order_by('-id')[:10][::-1]
        return render(request, self.template_name, self.context)