from django.shortcuts import render
from django.core import serializers
from life.models import *

def index(request):
    #all_foods = Food.objects.all()
    #return render(request, 'life/index.html', {"foods": all_foods})
    grocery_items = GroceryList.objects.all()
    pantry_items = PantryList.objects.all()
    return render(request, 'life/index.html', {"grocerylist": grocery_items, "pantrylist": pantry_items})
  
  
