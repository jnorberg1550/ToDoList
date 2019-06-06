from .models import ListType
from django.shortcuts import render

def index (request):
    return render(request, 'ToDoApp/index.html')

def gettypes(request):
    type_list=ListType.objects.all()
    return render(request, 'ToDoApp/types.html' ,{'type_list' : type_list})