from django.shortcuts import render, HttpResponse
from django.core import serializers
from life.models import *
from django.core.serializers import serialize
import json


def index(request):
    #all_foods = Food.objects.all()
    #return render(request, 'life/index.html', {"foods": all_foods})
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        if(data['food'] and data['quantity']):
            new_food = Food(name = data['food'], price = 2.99)
            new_food.save()
            new_grocery = GroceryList(food = new_food, quantity=data['quantity'])
            new_grocery.save()
        return HttpResponse("")
    else:
        grocery_items = GroceryList.objects.all()
        pantry_items = PantryList.objects.all()
        return render(request, 'life/index.html', {"grocerylist": grocery_items, "pantrylist": pantry_items})
  
  
