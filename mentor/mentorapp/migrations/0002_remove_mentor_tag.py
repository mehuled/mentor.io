# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 04:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentorapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='tag',
        ),
    ]