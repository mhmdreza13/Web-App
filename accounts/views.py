from django.shortcuts import render ,redirect
from .forms import UserRegisterForm ,UserLoginForm ,UserUpdateForm ,ProfileUpdateForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].label = "کلمه عبور فعلی"
        self.fields['new_password1'].label = "کلمه عبور جدید"
        self.fields['new_password2'].label = "تکرار کلمه عبور جدید"

        # اضافه کردن placeholder فارسی
        self.fields['old_password'].widget.attrs.update({'placeholder': 'کلمه عبور فعلی را وارد کنید'})
        self.fields['new_password1'].widget.attrs.update({'placeholder': 'کلمه عبور جدید را وارد کنید'})
        self.fields['new_password2'].widget.attrs.update({'placeholder': 'کلمه عبور جدید را دوباره وارد کنید'})

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

        form = UserLoginForm(request.POST) # create An example where the user has entered information

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

@login_required(login_url="accounts:user_login")
def user_profile (request):

    profile = Profile.objects.get(user_id = request.user.id)
    return render (request ,'accounts/profile.html',{'profile':profile})

@login_required(login_url="accounts:user_login")
def user_update (request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
        if user_form and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'به روزرسانی با موفقت انجام شد','success')
            return redirect ('accounts:user_profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {'user_form':user_form , 'profile_form':profile_form}
    

    return render (request , "accounts/update.html",context)




def user_addresses(request):
    # گرفتن پروفایل کاربر لاگین شده
    profile = request.user.profile
    
    # گرفتن همه آدرس‌های مرتبط با پروفایل
    addresses = profile.addresses.all()
    
    context = {
        "addresses": addresses
    }
    return render(request, "accounts/addresses.html", context)

def user_changepassowrd (request):

    if request.method == "POST":
        form = CustomPasswordChangeForm (request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success (request ,"کلمه عبور ما موفقیت تغییر کرد",'success')
            return redirect ("accounts:user_profile")
        else:
            messages.error (request ,"کلمه عبور درست انتخاب نشده",'danger')
            return redirect ('accounts:user_changepassowrd')

    else:
        form = CustomPasswordChangeForm(request.user)
    
    return render (request ,"accounts/changepassword.html",{'form':form})