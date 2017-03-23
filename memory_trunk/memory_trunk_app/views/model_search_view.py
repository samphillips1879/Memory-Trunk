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
        or in its tags (case sensitive) -- and returns all matching instances rendered to their relative model list html files.

    Author: Sam Phillips <samcphillips.com>
    """
    # model = request.GET.get('model', '')
    query = request.GET.get('query', '')

    mods = [models.Memory, models.Tip, models.Perspective,]

    context = {}
    template_name = 'search_results.html'
    ObjClass = None
    model_name = ''
    page_title = ''

    objects = set()
    # if model == 'Memory':
    #     template_name = 'memory_list.html'
    #     ObjClass = models.Memory
    #     model_name = 'memories'
    #     page_title = 'Memory Results'
    # elif model == 'Tip':
    #     template_name = 'tip_list.html'
    #     ObjClass = models.Tip
    #     model_name = 'tips'
    #     page_title = 'Tip Results'
    # elif model == 'Perspective':
    #     template_name = 'perspective_list.html'
    #     ObjClass = models.Perspective
    #     model_name = 'perspectives'
    #     page_title = 'Perspective Results'
    for model in mods:
        objects.update(model.objects.filter(content__icontains=query) | model.objects.filter(title__icontains=query) | model.objects.filter(tags__name__in=[query]))





    # objects = set(objects)

    context['objects'] = objects
    context['page_title'] = 'Search Results'

    return render(
        request,
        template_name,
        context
    )