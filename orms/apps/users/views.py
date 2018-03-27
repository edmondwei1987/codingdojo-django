from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def index(request):
    context={
        'users':User.objects.all(),
    }
    return render(request,'index.html',context)

def new(request):
    return render(request,'new.html')

def create(request):
    User.objects.create(
    first_name=request.POST['first_name'],
    last_name=request.POST['last_name'],
    email=request.POST['email'])
    return redirect('/users')

def show(request,id):
    context={
        'user':User.objects.get(id=id),
    }
    return render(request,'show.html',context)

def destroy(request,id):
    User.objects.get(id=id).delete()
    return redirect('/users')

def edit(request,id):
    context={
        'user':User.objects.get(id=id),
    }
    return render(request,'edit.html',context)

def update(request,id):
    user=User.objects.get(id=id)
    user.first_name=request.POST['first_name']
    user.last_name=request.POST['last_name']
    user.email=request.POST['email']
    user.save()
    return redirect('/users/show/'+str(user.id))
