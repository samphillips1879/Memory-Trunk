# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory_trunk_app', '0006_perspective'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='is_public',
            field=models.BooleanField(),
        ),
    ]