# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-31 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photographers', '0003_auto_20180830_0507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photographer',
            name='followees',
        ),
        migrations.AddField(
            model_name='photographer',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='_photographer_following_+', to='photographers.Photographer'),
        ),
    ]