# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-07 21:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20200307_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='last_login',
        ),
    ]