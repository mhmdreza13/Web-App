from django.shortcuts import render ,redirect
from .forms import UserRegisterForm ,UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
# Create your views here.

def user_register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(username = data['Username'] ,
                                     email= data['Email'] ,
                                     first_name = data['Firstname'] ,
                                     last_name = data ['Lastname'], 
                                     password=data ['Password_1'])
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
                messages.success(request,'با موفقیت وارد شدید.')
                return redirect ('home:home')
            else:
                messages.success(request,'نام کاربر یا رمز عبور اشتباه است')
                redirect ('accounts:user_login')

    else:
        form = UserLoginForm()
    context = {'form':form}
    return render(request , 'accounts/login.html',context)    
    

def user_logout (request):
    logout(request)
    messages.success(request,'با موفقیت خارج شدید.')
    return redirect ('home:home')   