from django.forms import ModelForm
from memory_trunk_app import models
from django.utils.translation import ugettext_lazy as _

class PerspectiveForm(ModelForm):
    """
    Purpose:
        Instantiate forms to create Perspective objects

    Author: Sam Phillips <samcphillips.com>
    """

    class Meta:
        model = models.Perspective
        fields = ['title', 'is_public', 'content', 'tags',]
        labels = {
            'is_public': _('Share this Perspective with other users?'),
        }