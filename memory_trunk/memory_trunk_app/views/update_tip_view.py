from memory_trunk_app import models
from django.http import HttpResponseRedirect
from django.shortcuts import render
from memory_trunk_app.forms import TipForm

def update_tip(request, id):
    """
    Purpose:
        Provide users with an interface for editing tips they have 
        saved to their MemoryTrunk

    Author: Sam Phillips <samcphillips.com>
    """
    tip = models.Tip.objects.get(id=id)
    if request.method == 'POST':
        if tip.user == request.user:
            # create a form instance and populate it with data from the request:
            form = TipForm(request.POST)
            if form.is_valid():
                tip.title=form.cleaned_data['title']
                tip.do=form.cleaned_data['do']
                tip.is_public=form.cleaned_data['is_public']
                tip.content=form.cleaned_data['content']
                tip.save()
                return HttpResponseRedirect('/')
        return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TipForm(instance=tip)

    return render(
        request, 
        'tip_update_form.html', 
        {
            'form': form,
            'tip': tip
        }
    )