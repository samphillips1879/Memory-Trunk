from django.forms import ModelForm, Textarea
from memory_trunk_app import models
from django.utils.translation import ugettext_lazy as _
from datetimewidget.widgets import DateTimeWidget


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
            'is_public': _('Share this Memory with other users?'),
            'date': _('Date (yyyy-mm-dd)'),
            'happy_factor': _('How happy does this memory make you? (0-10)'),
            'sad_factor': _('How sad does this memory make you? (0-10)'),
        }
        widgets = {
            'content': Textarea(attrs={'id': 'object_content'}),
        }