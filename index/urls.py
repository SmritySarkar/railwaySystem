from django.contrib import admin
from django.urls import path
from index import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('register', views.register, name='register'),
    path('signin', views.signIn, name='signIn'),
    path('about', views.aboutUs, name='aboutUs'),
    path('userHome', views.userHome, name='userHome'),
    path('userAbout', views.userAbout, name='userAbout'),


]
