from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Photo(models.Model):
    url = models.CharField(max_length=200)

class PicDetails(models.Model):
    location = models.CharField(max_length=200)
    