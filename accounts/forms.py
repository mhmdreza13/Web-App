from django import forms

class UserRegisterForm (forms.Form):
    Username = forms.CharField( max_length = 50 )
    Email = forms.EmailField()
    Firstname = forms.CharField(max_length=50)
    Lastname = forms.CharField (max_length=50)
    Password_1 = forms.CharField(max_length=50)
    Password_2 = forms.CharField(max_length=50)