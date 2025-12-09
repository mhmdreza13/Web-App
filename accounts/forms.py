from django import forms
from django.contrib.auth.models import User
from .models import Profile
class UserRegisterForm (forms.Form):
    Username = forms.CharField( max_length = 50 )
    Email = forms.EmailField()
    Firstname = forms.CharField(max_length=50)
    Lastname = forms.CharField (max_length=50)
    Password_1 = forms.CharField(max_length=50)
    Password_2 = forms.CharField(max_length=50)

    # def name is clean_field need to validate
    def clean_Username (self):
        user = self.cleaned_data ['Username']
        if User.objects.filter ( username = user).exists():
            raise forms.ValidationError ('این نام کاربری استفاده شده')
        return user
    
    def clean_Email (self):
        email = self.cleaned_data ['Email']
        if User.objects.filter (email = email).exists():
            raise forms.ValidationError ("این ایمیل تکراری است ")
        return email
    
    def clean_Password_2 (self): # must same feild like clean_field = clena_Lastname
        pass_1 = self.cleaned_data ['Password_1']
        pass_2 = self.cleaned_data ['Password_2']
        if pass_1 != pass_2:
            raise forms.ValidationError ('پسورد ها یکسان نیست')
        
        return pass_2

class UserLoginForm (forms.Form):
    user = forms.CharField()
    password = forms.CharField()


class UserUpdateForm (forms.ModelForm):

    class Meta:
        model = User
        fields = ['email','first_name','last_name']


class ProfileUpdateForm (forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['phone','address','postalcode']