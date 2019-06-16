from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name="login"),
    path('myposts/', views.myposts, name="myposts"),
    path('add_photo/', views.add_photo, name='add_photo'),
]