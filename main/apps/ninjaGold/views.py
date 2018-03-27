from django.shortcuts import render,redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if 'golds' not in request.session:
        request.session['golds']=0
    if 'logs' not in request.session:
        request.session['logs']=[]
    return render(request,'ninjaGold/index.html')

def process_money(request,location):
    time=datetime.now().strftime('%Y-%m-%d %H:%M')
    if location=='farm':
        gold=random.randint(10,20)
    elif location=='cave':
        gold=random.randint(5,10)
    elif location=='house':
        gold=random.randint(2,5)
    elif location=='casino':
        gold=random.randint(-50,50)
    if gold<0:
        activity='Entered a casino and lost {} gold...OUch..({})'.format(gold,time)
        flag='lose'
    else:
        activity='Earned {} golds form the {}! ({})'.format(gold,location,time)
        flag='win'
    request.session['golds']+=gold
    log=(flag,activity)
    request.session['logs'].insert(0,log)
    return redirect('/')


def reset(request):
    request.session.flush()
    return redirect('/')
