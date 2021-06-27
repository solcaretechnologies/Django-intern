from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL

# Create your models here.

class Task(models.Model):
    EmployeeName = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    Works = models.CharField(max_length=200)
    Description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    Create = models.DateTimeField(auto_now_add=True)

    def __str__(seLf):
       return seLf.Works

    class Meta:
        ordering = ['complete']