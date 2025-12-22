from django.shortcuts import render
from .models import Category ,Product
# Create your views here.

def home (request):
    category = Category.objects.all()
    return render (request , 'home/home.html',{'category':category}) 

def product (requrst,id = None):
    product = Product.objects.all()
    category = Category.objects.all()
    if id:
        data = category.get(id = id)
        product = product.filter(category = data)
    return render (requrst, 'home/product.html' ,{'product':product})

def productdetail (request , id):
    productdetail = Product.objects.get(id =id )
    return render (request , 'home/productdetails.html', {'productdetail':productdetail})
    