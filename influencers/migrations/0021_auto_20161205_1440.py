# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-05 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencers', '0020_campaigns_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaigns',
            name='follow_handle_id',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
