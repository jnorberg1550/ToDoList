from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='types'),
    path('newList/', views.newList name='newlist'),
]