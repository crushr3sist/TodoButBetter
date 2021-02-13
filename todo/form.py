from django.db import models
from django.forms import ModelForm
from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class ListCreation(forms.ModelForm):
    class Meta:
        model = TodoApp_Fields
        fields = [
            "activity",
            "urgency",
            "DueDate",

            
        ]

        widgets = {
            'activity': forms.TextInput(attrs={'class': 'form-control'}),
            'urgency': forms.Select(choices=[(x, x) for x in range(0, 10)],attrs={'class': 'form-control'}),
            "DueDate" : DateInput(attrs={'class': 'form-control'}),

        }
