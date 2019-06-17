from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.views.generic import ListView
import uuid
import boto3
from .models import Scene, Photo

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'txstreetart'
# Create your views here.

class SceneCreate(CreateView):
    model = Scene
    fields = '__all__'

class SceneUpdate(UpdateView):
    model = Scene
    fields = ['location', 'description']

class SceneDelete(DeleteView):
    model = Scene
    success_url = '/scenes/'


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

def add_photo(request, scene_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            
            photo = Photo(url=url, scene_id=scene_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', scene_id=scene_id)

def login(request):
    return render(request, 'login.html')

def myposts(request):
    return render(request, 'myposts.html')
