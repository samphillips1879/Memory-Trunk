from django.forms import ModelForm
from memory_trunk_app import models
from django.utils.translation import ugettext_lazy as _


class MemoryForm(ModelForm):
    """
    Purpose:
        Instantiate forms to create Memory objects

    Author: Sam Phillips <samcphillips.com>
    """

    class Meta:
        model = models.Memory
        fields = ['title', 'is_public', 'date', 'location', 'content', 'happy_factor', 'sad_factor', 'tags',]
        labels = {
            'is_public': _('Share this memory with other users?')
        }