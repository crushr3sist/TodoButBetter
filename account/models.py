from django.db import models
from django.db.models.base import Model
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User

# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#   # username, password, name etc. are already existing fields
#   # new fields here

class User(models.Model):
    Username       = models.CharField(null=False, max_length=30 )
    Password       = models.CharField(null=False, editable=True, max_length=30)
    Email          = models.EmailField(null=False)
    Firstname      = models.TextField(null=False, editable=True, max_length=20)
    Lastname       = models.TextField(null=False, editable=True, max_length=20)
    gender         = models.TextField()
    bio            = models.TextField(null=True, blank=True, editable=True, max_length=500)
    remember_me    = models.BooleanField(null=True,blank=True, default=True)
    
    profilePicture = models.ImageField(default='img/profile_img/default.jpg',upload_to='',null=True, blank=True, height_field='heightfield' , width_field='widthfield')
    heightfield    = models.IntegerField(default = 0)
    widthfield     = models.IntegerField(default = 0)

