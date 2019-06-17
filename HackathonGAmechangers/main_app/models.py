from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Scene(models.Model):
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.location

class Photo(models.Model):
    url = models.CharField(max_length=200)
    