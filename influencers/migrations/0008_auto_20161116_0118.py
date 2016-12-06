# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-16 00:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('influencers', '0007_auto_20161115_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaigns',
            name='url',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='action',
            field=models.CharField(choices=[('Retweet', 'Retweet'), ('Follow', 'Follow')], max_length=100),
        ),
        migrations.AlterField(
            model_name='noisemakerprofile',
            name='preferences',
            field=models.CharField(choices=[('Fashion and Lifestyle', 'Fashion and Lifestyle'), ('Sports, Politics and Education', 'Sports, Politics and Education'), ('Technology', 'Technology'), ('All', 'All')], max_length=250, null=True),
        ),
    ]
