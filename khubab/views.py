#-*- coding: utf-8 -*-

from django.shortcuts import render
from bab.models import Bab

def index(request):
   context = Bab.objects.all()
   return render(request, 'home.html', {'context' : context})