from django.shortcuts import render,redirect
from models import *

# Create your views here.
def index(request):
    context={'courses':Course.objects.all()}
    return render(request,'index.html',context)

def add(request):
    Course.objects.create(name=request.POST['name'],desc=request.POST['desc'])
    return redirect('/')

def delete(request,id):
    context={'course':Course.objects.get(id=id)}
    return render(request,'delete.html',context)

def destroy(request,id):
    if request.POST['sub']!='NO':
        Course.objects.get(id=id).delete()
    return redirect('/')
