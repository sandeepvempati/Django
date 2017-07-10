# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index1(request):
    return HttpResponse("<h1>This is videos app</h1>")
