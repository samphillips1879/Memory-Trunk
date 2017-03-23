from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from memory_trunk_app import models
from django.urls import reverse

def search(request, user=None):
    """
    Purpose:
        Act as the switchboard operator for directing search requests
        from a User-submitted query

    Author: Sam Phillips <samcphillips.com>
    """
    model = request.GET.get('model', '')
    query = request.GET.get('query', '')

    context = {}
    template_name = ''
    ObjClass = None
    model_name = ''
    if model == 'Memory':
        template_name = 'memory_list.html'
        ObjClass = models.Memory
        model_name = 'memories'
    elif model == 'Tip':
        template_name = 'tip_list.html'
        ObjClass = models.Tip
        model_name = 'tips'
    elif model == 'Perspective':
        template_name = 'perspective_list.html'
        ObjClass = models.Perspective
        model_name = 'perspectives'

    objects = ObjClass.objects.filter(content__icontains=query) | ObjClass.objects.filter(title__icontains=query) 
    # | ObjClass.objects.filter(tags__icontains=query)

    context[model_name] = objects

    return render(
        request,
        template_name,
        context
    )