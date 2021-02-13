from django.db import models
import uuid
class TodoApp_Fields(models.Model):
    activity = models.TextField(editable = True,null=False, blank=False,)
    createTime = models.TimeField(editable = True ,auto_now_add=True, null=False, blank=False)
    DueDate = models.DateField(null=True, auto_now_add=False, editable = True)
    urgency = models.IntegerField(null=True, editable=True)