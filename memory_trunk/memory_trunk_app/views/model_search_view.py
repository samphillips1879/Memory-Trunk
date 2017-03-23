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
    model = request.GET.get('model', '')
    query = request.GET.get('query', '')

    context = {}
    template_name = ''
    ObjClass = None
    model_name = ''
    page_title = ''
    if model == 'Memory':
        template_name = 'memory_list.html'
        ObjClass = models.Memory
        model_name = 'memories'
        page_title = 'Memory Results'
    elif model == 'Tip':
        template_name = 'tip_list.html'
        ObjClass = models.Tip
        model_name = 'tips'
        page_title = 'Tip Results'
    elif model == 'Perspective':
        template_name = 'perspective_list.html'
        ObjClass = models.Perspective
        model_name = 'perspectives'
        page_title = 'Perspective Results'

    objects = ObjClass.objects.filter(content__icontains=query) | ObjClass.objects.filter(title__icontains=query) | ObjClass.objects.filter(tags__name__in=[query])
    objects = set(objects)

    context[model_name] = objects
    context['page_title'] = page_title

    return render(
        request,
        template_name,
        context
    )