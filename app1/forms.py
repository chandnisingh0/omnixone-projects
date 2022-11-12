#### forms.py
from unicodedata import name
from django import forms
from django.contrib.auth.models import User

# class SubscribeForm(forms.Form):
#     email = forms.EmailField()

    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'password1', 'password2']


# dont know why not working 
# class resitrationform(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'name'}))
#     email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
#     password = forms.CharField(widget=forms.PasswordInput())
#     address_1 = forms.CharField(
#         label='Address',
#         widget=forms.TextInput(attrs={'placeholder': '12-address'})
#     )

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'address_1']


# class loginform(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'name'}))
#     password = forms.CharField(widget=forms.PasswordInput())
   

