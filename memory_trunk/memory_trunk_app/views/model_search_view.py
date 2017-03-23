from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from memory_trunk_app import models
from django.urls import reverse

def search(request, user=None):
    """
    Purpose:
        Searches the MemoryTrunk database for model instances containing
        a User's query -- either in the object's title, its content, 
        or in its tags (case sensitive) -- and returns all matching instances rendered to search_results.html

    Author: Sam Phillips <samcphillips.com>
    """
    # model = request.GET.get('model', '')
    query = request.GET.get('query', '')
    mods = [models.Memory, models.Tip, models.Perspective,]
    context = {}
    template_name = 'search_results.html'

    objects = set()
    for model in mods:
        query_set = model.objects.filter(content__icontains=query, is_public=True) | model.objects.filter(title__icontains=query, is_public=True) | model.objects.filter(tags__name__in=[query], is_public=True)
        objects.update(query_set)

    context['objects'] = objects
    context['page_title'] = 'Search Results'

    return render(
        request,
        template_name,
        context
    )