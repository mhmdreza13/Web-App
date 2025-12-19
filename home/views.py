from django.shortcuts import render
from .models import Category
# Create your views here.

def home (request):
    category = Category.objects.all()
    return render (request , 'home/home.html',{'category':category}) 