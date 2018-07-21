from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('foods/',views.index, name='foods'),
    path('grocerylist/', views.index, name="grocerylist"),
    path('pantrylist/', views.index, name="pantrylist")
    
]