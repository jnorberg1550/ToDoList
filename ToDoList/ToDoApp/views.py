from .models import ListType
from django.shortcuts import render

def index (request):
    return render(request, 'ToDoApp/index.html')

def gettypes(request):
    type_list=ListType.objects.all()
    return render(request, 'ToDoApp/types.html' ,{'type_list' : type_list})

def getduedate(request):
    listitemduedate_list=ListType.objects.all()
    return render(request, 'ToDoApp/listitemduedate.html', {'listitemduedates_list': listitemduedates_list})

def newList(request):
     form=ListForm
     if request.method=='POST':
          form=ListForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ListForm()
     else:
          form=ListForm()
     return render(request, 'ToDoApp/newlistform,.html', {'form': form})