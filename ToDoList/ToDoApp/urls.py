from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='types'),
    path('listitemduedate/<int:id>', views.listitemduedate, name='listitemduedate'),
    path('newList/', views.newList name='newlist'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
