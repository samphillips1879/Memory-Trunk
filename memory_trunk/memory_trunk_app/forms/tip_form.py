from django.forms import ModelForm
from memory_trunk_app import models
from django.utils.translation import ugettext_lazy as _

class TipForm(ModelForm):
    """
    Purpose:
        Instantiate forms to create Tip objects

    Author: Sam Phillips <samcphillips.com>
    """

    class Meta:
        model = models.Tip
        fields = ['title', 'is_public', 'do', 'content',]
        labels = {
            'is_public': _('Share this Tip with other users?'),
        }