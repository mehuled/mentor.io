# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mentorapp', '0002_mentor_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='year_in_school',
        ),
        migrations.AddField(
            model_name='mentor',
            name='confirmPassword',
            field=models.CharField(default=datetime.datetime(2017, 10, 30, 21, 35, 32, 870014, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentor',
            name='password',
            field=models.CharField(default=datetime.datetime(2017, 10, 30, 21, 35, 41, 270988, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mentor',
            name='username',
            field=models.CharField(default='overload', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='confirmPassword',
            field=models.CharField(default=datetime.datetime(2017, 10, 30, 21, 36, 15, 799892, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=datetime.datetime(2017, 10, 30, 21, 36, 26, 296073, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(default='override', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='usersince',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 30, 21, 36, 49, 320264, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mentor',
            name='github',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='website',
            field=models.CharField(max_length=128),
        ),
    ]
