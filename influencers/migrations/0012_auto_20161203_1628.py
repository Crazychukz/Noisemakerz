# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-03 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencers', '0011_auto_20161203_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaigns',
            name='follow_handle',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campaigns',
            name='follow_handle_id',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
