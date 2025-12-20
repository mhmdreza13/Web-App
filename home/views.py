from django.shortcuts import render
from .models import Category ,Product
# Create your views here.

def home (request):
    category = Category.objects.all()
    return render (request , 'home/home.html',{'category':category}) 

def product (requrst):
    product = Product.objects.all()
    return render (requrst, 'home/product.html' ,{'product':product})