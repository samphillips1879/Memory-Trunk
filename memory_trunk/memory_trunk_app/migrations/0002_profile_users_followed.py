# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 14:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('memory_trunk_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='users_followed',
            field=models.ManyToManyField(related_name='profiles', to=settings.AUTH_USER_MODEL),
        ),
    ]
