from django.db import models
from django.urls import reverse

# Create your models here.

class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=0) 

