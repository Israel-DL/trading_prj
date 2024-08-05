from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput


# Register A User
class CreateUserForm(UserCreationForm):
    
    class Meta: 
         model = User
         fields = ['username', 'email', 'password1', 'password2']


# Authentication Form
class LoginForm(AuthenticationForm):
     
     email = forms.CharField(widget=TextInput())
     password = forms.CharField(widget=PasswordInput())