from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic.base import View


def index(request):
    return render(request, 'index.html')
