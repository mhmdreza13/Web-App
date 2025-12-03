from django.shortcuts import render

# Create your views here.


def user_register (requests):
    
    return render (requests , 'accounts/register.html')