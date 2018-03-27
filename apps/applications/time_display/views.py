from django.shortcuts import render
from time import gmtime,strftime
# Create your views here.
def index(request):
    context={
        'time':strftime('%Y-%m-%d %H:%M',gmtime())
    }
    return render(request,'time_display/index.html',context)
