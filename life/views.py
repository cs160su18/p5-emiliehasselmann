from django.shortcuts import render
from django.core import serializers
from life.models import *

def index(request):
    all_foods = Food.objects.all()
    return render(request, 'life/index.html', {"foods": all_foods})