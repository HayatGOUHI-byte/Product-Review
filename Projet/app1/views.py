from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant


def home(request):
    return render(request,'index.html')




def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request,'restaurants/index.html')

