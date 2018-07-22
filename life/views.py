from django.shortcuts import render, HttpResponse
from django.core import serializers
from life.models import *
from django.core.serializers import serialize
import json


def index(request):
    #all_foods = Food.objects.all()
    #return render(request, 'life/index.html', {"foods": all_foods})
    if request.method == "POST":
#         print(json.loads(request.body))
        print(json.loads(request.body.decode('utf-8')))

#         myResponse.json()
        return HttpResponse("")
    else:
        grocery_items = GroceryList.objects.all()
        pantry_items = PantryList.objects.all()
        return render(request, 'life/index.html', {"grocerylist": grocery_items, "pantrylist": pantry_items})
  
  
