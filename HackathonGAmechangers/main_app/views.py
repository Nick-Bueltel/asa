from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>TEXAS STREET ART HOME</h1>')

def profile(request):
    return HttpResponse('<h1>PROFILE PAGE</h1>')

