from django.urls import path
from .views import *

urlpatterns = [
    path(r'<str:usr>/', accountView)
]
