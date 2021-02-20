from django.db import models
from django.db.models.base import Model
from django.db.models.fields.files import ImageField

class AccountsDB(models.Model):

    Username       = models.CharField(null=False, editable=True, max_length=30, help_text="Enter Your Username" )
    Password       = models.CharField(null=False, editable=True, max_length=30, help_text="Enter Your Password" )
    Email          = models.EmailField(null=False)
    Firstname      = models.TextField(null=False, editable=True, max_length=20)
    Lastname       = models.TextField(null=False, editable=True, max_length=20)
    gender         = models.TextField()
    bio            = models.TextField(null=True, editable=True, max_length=500, help_text="enter a bio for others to know more about you and your interests")
    
    profilePicture = models.ImageField(default='img/profile_img/default.jpg',upload_to='',null=True, blank=True, height_field='heightfield' , width_field='widthfield')
    heightfield    = models.IntegerField(default=0)
    widthfield     = models.IntegerField(default=0)
    def __str__(self):
        return "AccountsDB"


