# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=10)
    last_login = models.DateTimeField()
    login_count = models.IntegerField()
    project_count = models.IntegerField()

    def __str__(self):
        return self.username
