from django.db import models

class Food(models.Model):
  name = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=6, decimal_places=2)

class GroceryList(models.Model):
# 	 = models.DateTimeField(auto_now_add=True)
  food = models.ForeignKey(Food, on_delete=models.CASCADE)
  quantity = models.CharField(max_length=50)
 # name = models.CharField(max_length=50)

class PantryList(models.Model):
# 	 = models.DateTimeField(auto_now_add=True)
  food = models.ForeignKey(Food, on_delete=models.CASCADE)
  quantity = models.CharField(max_length=50)
 # name = models.CharField(max_length=50)


class Ingredient(models.Model):
  name = models.CharField(max_length = 50)
  quantity = models.IntegerField()
  food = models.ForeignKey(Food, on_delete=models.CASCADE)
  
class Recipe(models.Model):
  name = models.CharField(max_length=50)
  ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
  steps = models.CharField(max_length=500)
  
class Test(models.Model):
  name = models.CharField(max_length=50)
  
