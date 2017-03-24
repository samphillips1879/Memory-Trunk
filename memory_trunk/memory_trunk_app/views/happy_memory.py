from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from memory_trunk_app import models
import random

def happy_memory(request):
    """
    Purpose:
        Grab a random happy Memory from the active user's Memory list 
        and render it in a Memory detail view. If user has no happy 
        Memories, we must give them a hug. After we give them a hug 
        (and perhaps some hot cocoa) we grab a random happy Memory 
        from the list of publicly available memories

    Author: Sam Phillips <samcphillips.com>
    """

    memories = None
    index = None
    mem_instance = request.GET.get('mem_instance', 0)

    try:
        memories = models.Memory.objects.filter(user=request.user, happy_factor__gte=6).exclude(id=mem_instance)
        index = random.randrange(0, len(memories))
    except (ValueError, TypeError) as e:
        memories = models.Memory.objects.filter(happy_factor__gte=6, is_public=True).exclude(id=mem_instance)
        index = random.randrange(0, len(memories))
    happy_memory = memories[index]
    print(happy_memory)
    return HttpResponseRedirect(reverse(
        'memory_trunk_app:memory_detail', 
        kwargs={'id':happy_memory.id}
    ))