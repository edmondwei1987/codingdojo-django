from django.shortcuts import render,redirect
from django.contrib import messages
import re
import bcrypt
from models import *

EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
# Create your views here.
def index(request):
    return render(request,'index.html')

def regist(request):
    validForm=True
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    password=request.POST['password']
    cpassword=request.POST['cpassword']
    if len(first_name)<2 or not first_name.isalpha():
        messages.error(request,'First Name TOO SHORT or Contains non-letter!!')
        validForm=False
    if len(last_name)<2 or not last_name.isalpha():
        messages.error(request,'Last Name TOO SHORT or Contains non-letter!!')
        validForm=False
    if not EMAIL_REGEX.match(email):
        messages.error(request,'INVLID EMAIL!!')
        validForm=False
    if len(password)<8 or len(cpassword)<8 or password!=cpassword:
        messages.error(request,'WRONG PASSWORD!!')
        validForm=False
    if validForm:
        pw=bcrypt.hashpw(password.encode(),bcrypt.gensalt())
        User.objects.create(first_name=first_name,last_name=last_name,email=email,password=pw)
        return render(request,'success.html',{'name':first_name+' '+last_name})
    else:
        return redirect('/log_reg')

def login(request):
    email=request.POST['email']
    password=request.POST['password']
    users=User.objects.filter(email=email)
    if len(users)>0:
        user=users.first()
        if bcrypt.checkpw(password.encode(),user.password.encode()):
            return render(request,'success.html',{'name':user.first_name+' '+user.last_name})
        else:
            messages.error(request,'PASSWORD OR EMAIL NOT CORRECT!!')
    else:
        messages.error(request,'PASSWORD OR EMAIL NOT CORRECT!!')
    return redirect('/log_reg')
