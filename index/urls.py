from django.contrib import admin
from django.urls import path
from index import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('register', views.register, name='register'),
    path('signin', views.signIn, name='signIn'),


]
