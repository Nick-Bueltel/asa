from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
import uuid
import boto3
from .models import Photo, Scene

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'txstreetart'
# Create your views here.

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def scenes_index(request):
    scenes = Scene.objects.all()
    return render(request,'scenes/index.html', { 'scenes': scenes })

def scenes_detail(request, scene_id):
    scene = Scene.objects.get(id=scene_id)
    return render(request,'scenes/detail.html', { 'scene': scene })

#todo

def add_photo(request):
    return render(request, 'home.html' )
def login(request):
    return render(request, 'login.html')

def myposts(request):
    return render(request, 'myposts.html')
