# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Users
from . serializers import UserSerializer


class UserList(APIView):

    def get(self, request):
        query = self.request.GET.get('q')
        query_set = Users.objects.all()
        if query:
            if query == "true":
                query_set = query_set.filter(
                    Q(login_count__gt=0)
                )
            else:
                query_set = query_set.filter(
                    Q(login_count=0)
                )
        serializer = UserSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self):
        pass
