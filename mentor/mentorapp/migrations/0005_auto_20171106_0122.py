# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentorapp', '0004_auto_20171103_1036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentor',
            old_name='tag',
            new_name='tag1',
        ),
        migrations.AddField(
            model_name='mentor',
            name='tag2',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentor',
            name='tag3',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
    ]
