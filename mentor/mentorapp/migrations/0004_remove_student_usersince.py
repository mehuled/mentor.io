# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentorapp', '0003_auto_20171031_0306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='usersince',
        ),
    ]
