from django.contrib import admin
from memory_trunk_app import models

admin.site.register(models.Profile)
admin.site.register(models.Memory)
admin.site.register(models.Tip)
admin.site.register(models.Perspective)