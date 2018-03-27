from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('placeholder to later display all the list of users')

def new(request):
    return redirect(register)

def register(request):
    return HttpResponse('placeholder for users to create a new user record')

def login(request):
    return HttpResponse('placeholder for users to login')

def blogs(request):
    return redirect('/blogs')
