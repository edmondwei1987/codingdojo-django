from django.shortcuts import render,redirect

def index(request):
    return render(request,'index.html')

def process(request):
    for key,value in request.POST.items():
        request.session[key]=value
    return redirect('/result')

def result(request):
    return render(request,'result.html')
# Create your views here.
