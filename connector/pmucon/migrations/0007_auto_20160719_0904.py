# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmucon', '0006_eventquery_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='waiting',
            new_name='blocking',
        ),
        migrations.AddField(
            model_name='case',
            name='pro_uid',
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='tas_uid',
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
    ]
