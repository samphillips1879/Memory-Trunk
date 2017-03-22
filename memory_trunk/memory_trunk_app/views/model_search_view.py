from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from memory_trunk_app import models
from django.urls import reverse

class SearchModelView(TemplateView):
    """
    Purpose:
        Search the MemoryTrunk database for specific models relevant
        to a User-submitted query

    Author: Sam Phillips <samcphillips.com>
    """
    template_name = ''
    context = {}
    def get(self, request, model, query):
        """
        Purpose:
            Interpret the User's query, search through the appropriate 
            model, and return relevant results bound to the appropriate 
            list view

        Arguments:
            model -- The Django model collection to search through
            query -- The search parameters
        """

        if model == 'Memory':
            pass
        elif model == 'Tip':
            pass
        elif model == 'Perspective':
            pass

        return render(
            request,
            self.template_name,
            self.context
        )