from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
import uuid
import boto3
from .models import Photo
S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'txstreetart'
# Create your views here.

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

#todo

def add_photo(request):
    return render(request, 'home.html' )
def login(request):
    return render(request, 'login.html')

def myposts(request):
    return render(request, 'myposts.html')
