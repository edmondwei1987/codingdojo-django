from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count']=0

    return render(request,'random_word/index.html')

def generate(request):
    request.session['string']=get_random_string(length=14)
    request.session['count']+=1
    return redirect('/random_word')

def reset(request):
    del request.session['count']
    del request.session['string']
    return redirect('/random_word')
