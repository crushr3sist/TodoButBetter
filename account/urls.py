from django import urls
from django.conf.urls import include, url
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.urls import path
from .views import *

urlpatterns = [
    path(r'user/<str:usr>/', accountView),
    path('register_/', register_),    

]
