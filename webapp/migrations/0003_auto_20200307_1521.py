# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-07 21:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_users_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='users',
            name='login_count',
        ),
        migrations.RemoveField(
            model_name='users',
            name='project_count',
        ),
    ]
