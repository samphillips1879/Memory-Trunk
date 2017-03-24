from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from memory_trunk_app import models
import random

@login_required
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

    try:
        memories = models.Memory.objects.filter(user=request.user, happy_factor__gte=6)
        index = random.randrange(0, len(memories)-1)
    except ValueError as e:
        memories = models.Memory.objects.filter(happy_factor__gte=6, is_public=True)
        index = random.randrange(0, len(memories)-1)
    happy_memory = memories[index]
    print(happy_memory)
    return HttpResponseRedirect(reverse(
        'memory_trunk_app:memory_detail', 
        kwargs={'id':happy_memory.id}
    ))