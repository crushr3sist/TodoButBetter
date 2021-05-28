from django.db import models
from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
    input_type = 'date'

class reg_user_Ext(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "Firstname",
            "Lastname",
            "bio",
            "gender",
        ]
        OPTIONS = (
            ('Male','Male'),
            ('Female','Female'),
            ('Other','Other')
        )
        

        widgets = {
            'Username': forms.TextInput(attrs={'class': 'form-control', 'name':'username'}),
            'Password': forms.TextInput(attrs={'class': 'form-control', 'name':'password'}),
            'Email' : forms.EmailInput(attrs={'class': 'form-control', 'name':'email'}),
            "Firstname" : forms.TextInput(attrs={'class': 'form-control', 'name':'fname'}),
            "Lastname" : forms.TextInput(attrs={'class': 'form-control', 'name':'lname'}),
            "bio" : forms.Textarea(attrs={'class': 'form-control', 'name':'bio'}),
            "gender" : forms.Select(attrs={'class': 'form-control', 'name':'gender'}, choices=OPTIONS),
            
        } 

class reg_user(UserCreationForm):
    
    class meta:
        model = User
        Fields = ['username', 'email', 'password','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Email'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
            'password2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }
    def __init__(self, *args, **kwargs):
        super(reg_user, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

        self.fields['username'].widget.attrs['placeholder'] =  'Enter Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'