# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=128)),
                ('lastname', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=128)),
                ('confirmPassword', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('aboutYourself', models.TextField(max_length=500)),
                ('github', models.CharField(max_length=128)),
                ('website', models.CharField(max_length=128)),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=128)),
                ('lastname', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
                ('confirmPassword', models.CharField(max_length=128)),
                ('isAStudent', models.BooleanField()),
                ('aboutYourself', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('rank', models.IntegerField(default=0)),
            ],
        ),
    ]
