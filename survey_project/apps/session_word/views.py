from django.shortcuts import render, redirect

def index(request):
    if 'words' not in request.session:
        request.session['words'] = []
    return render(request,'session_word/index.html')
# Create your views here.
def addsession(request):
    if 'word' not in request.POST:
        word=''
    else:
        word=request.POST['word']
    if 'color' not in request.POST:
        color='black'
    else:
        color=request.POST['color'];
    if 'font' not in request.POST:
        font='10px'
    else:
        font=request.POST['font']
    element = {
        'word':word,
        'color':color,
        'font':font
    }
    request.session['words'].append(element)
    request.session.modified = True
    return redirect('/session_word')


def clear(request):
    request.session.flush()
    print 'clearllkjkjkjlj'
    return redirect('/session_word')
