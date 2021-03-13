from django.db import models
from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
    input_type = 'date'


class Register(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "Username",
            "Password",
            "Email",
            "Firstname",
            "Lastname",
            "bio",
            "gender",
            "profilePicture"
        ]
        OPTIONS = (
            ('Male','Male'),
            ('Female','Female'),
            ('Other','Other')
        )
        

        widgets = {
            'Username': forms.TextInput(attrs={'class': 'form-control'}),
            'Password': forms.TextInput(attrs={'class': 'form-control'}),
            'Email' : forms.EmailInput(attrs={'class': 'form-control'}),
            "Firstname" : forms.TextInput(attrs={'class': 'form-control'}),
            "Lastname" : forms.TextInput(attrs={'class': 'form-control'}),
            "bio" : forms.Textarea(attrs={'class': 'form-control'}),
            "gender" : forms.Select(attrs={'class': 'form-control'}, choices=OPTIONS),
            "profilePicture": forms.FileInput(attrs={'class': 'form-control'})
        } 

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    help_texts = {
            'username': None,
            'email': None,
            'password': None,
            'password2': None
        }
    class meta:
        model = User
        Fields = ['username', 'email', 'password','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),
        }
