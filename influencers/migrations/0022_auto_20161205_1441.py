# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-05 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencers', '0021_auto_20161205_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaigns',
            name='follow_handle_id',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='tracking_ID',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
