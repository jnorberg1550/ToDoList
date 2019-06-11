from .models import ListType
from django.shortcuts import render
from django.contrib.auth.decorators import login_required'

def index (request):
    return render(request, 'ToDoApp/index.html')

def gettypes(request):
    type_list=ListType.objects.all()
    return render(request, 'ToDoApp/types.html' ,{'type_list' : type_list})

def getduedate(request):
    listitemduedate_list=ListType.objects.all()
    return render(request, 'ToDoApp/duedatetemplate.html', {'listitemduedates_list': listitemduedates_list})

def listitempriority(request, id):
    prod=get_object_or_404(Product, pk=id)
    return render(request, 'ToDoApp/duedatetemplate.html', context=context)

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

    def loginmessage(request):
    return render(request, 'ToDoApp/loginmessage.html')

    def logoutmessage(request):
    return render(request, 'ToDoAppapp/logoutmessage.html')

@login_required
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
     return render(request, 'ToDoapp/newlist.html', {'form': form}
