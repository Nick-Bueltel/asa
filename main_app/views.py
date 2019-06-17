from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
import uuid
import boto3
from .models import Photo
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'txstreetart'
# Create your views here.

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')

def add_photo(request):
    return render(request, 'home.html' )
def login(request):
    return render(request, 'login.html')

def myposts(request):
    return render(request, 'myposts.html')

def signup(request): 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


