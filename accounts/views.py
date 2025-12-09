from django.shortcuts import render ,redirect
from .forms import UserRegisterForm ,UserLoginForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
# Create your views here.

def user_register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user =User.objects.create_user(username = data['Username'] ,
                                     email= data['Email'] ,
                                     first_name = data['Firstname'] ,
                                     last_name = data ['Lastname'], 
                                     password=data ['Password_1'])
            user.save()
            return redirect ('home:home') # redirect ('appname : utl name from utls.py = 'home'')
    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render (request , 'accounts/register.html',context)

def user_login (request):

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = authenticate(request ,username = User.objects.get(email= data ['user']),password = data ['password'])
            except:
                user = authenticate(request ,username = data ['user'],password = data ['password'])
            if user is not None :
                login(request,user)
                messages.success(request,'با موفقیت وارد شدید.','success')
                return redirect ('home:home')
            else:
                messages.success(request,'نام کاربر یا رمز عبور اشتباه است','danger')
                redirect ('accounts:user_login')

    else:
        form = UserLoginForm()
    context = {'form':form}
    return render(request , 'accounts/login.html',context)    
    

def user_logout (request):
    logout(request)
    messages.success(request,'با موفقیت خارج شدید.','info')
    return redirect ('home:home')   


def user_profile (request):
    profile = Profile.objects.get(user_id = request.user.id)
    print (profile.address)
    return render (request ,'accounts/profile.html',{'profile':profile})