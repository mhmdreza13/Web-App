from django.shortcuts import render ,redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
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