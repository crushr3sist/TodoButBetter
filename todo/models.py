from .db_models import AuthUser
from django.contrib.auth import get_user_model
from django.http import request
from django.db import models
from django.conf import settings
import uuid

class TodoApp_Fields(models.Model):
    author=models.ForeignKey('AuthUser', on_delete=models.CASCADE)
    activity = models.TextField(editable = True,null=False, blank=False,)
    createTime = models.TimeField(editable = True ,auto_now_add=True, null=False, blank=False)
    DueDate = models.DateField(null=True, auto_now_add=False, editable = True)
    urgency = models.IntegerField(null=True, editable=True)


