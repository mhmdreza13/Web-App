from django.shortcuts import render ,get_object_or_404
from .models import Category ,Product
# Create your views here.

def home (request):
    category = Category.objects.filter(is_sub_category = 0)
    return render (request , 'home/home.html',{'category':category}) 

def product (requrst,slug = None,id = None):
    product = Product.objects.all()
    category = Category.objects.all()
    if slug and id:
        data = get_object_or_404(Category,slug = slug, id = id)
        product = product.filter(category = data)
    return render (requrst, 'home/product.html' ,{'product':product})

def productdetail (request , id):
    productdetail = get_object_or_404(Product,id = id)
    return render (request , 'home/productdetails.html', {'productdetail':productdetail})
    
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)