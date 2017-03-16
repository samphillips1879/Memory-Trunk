from django.views.generic.base import TemplateView
# from django.shortcuts import render

class IndexView(TemplateView):
    """
    Purpose:
        This view serves as the landing page for MemoryTrunk

    Author: Sam Phillips <samcphillips.com>
    """

    template_name = "index.html"