# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-12 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencers', '0024_auto_20161211_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noisemakerprofile',
            name='instagram_ID',
            field=models.BigIntegerField(default=0),
        ),
    ]
