from django.urls import path
from .views import *

urlpatterns = [
    path(r'accounts/<str:usr>/', accountView),
    path('register_/', register_),
    path('login_/', login_),
]
