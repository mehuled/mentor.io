# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentorapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=128)),
                ('lastname', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('aboutYourself', models.TextField(max_length=500)),
                ('github', models.URLField()),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=128)),
                ('lastname', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('isAStudent', models.BooleanField()),
                ('year_in_school', models.CharField(default=b'FR', max_length=2, choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior')])),
                ('aboutYourself', models.TextField(max_length=500)),
            ],
        ),
    ]
