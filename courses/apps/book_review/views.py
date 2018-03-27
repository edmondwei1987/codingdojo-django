from django.shortcuts import render,redirect
from django.contrib import messages
from models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def regist(request):
    info=User.objects.validate_user(request.POST)
    if info['status']=='bad':
        for error in info['data']:
            messages.error(request,error)
        return redirect('/book_review')
    else:
        info['reviews']=Review.objects.order_by('-created_at').all()[0:3]
        reviews=Review.objects.order_by('-created_at').all()[0:3]
        info['books']=Book.objects.exclude(reviews__isnull=True)
        # -------------------------
        # bookids=[]
        # for review in reviews:
        #     bookids.append(review.book.id )
        #
        # newbooks=[]
        # books=Book.objects.exclude(reviews__isnull=True)
        # for book in books:
        #     if book.id not in newbooks:
        #         newbooks.append(book)
        # ------------------------------------
        request.session['user_id']=info['data'].id
        return render(request,'books.html',info)

def login(request):
    info=User.objects.validate_login(request.POST)
    if info['status']=='bad':
        messages.error(request,info['data'])
        return redirect('/book_review')
    else:
        info['reviews']=Review.objects.order_by('-created_at').all()[0:3]
        info['books']=Book.objects.exclude(reviews__isnull=True)
        request.session['user_id']=info['data'].id
        return render(request,'book.html',info)


def add(request):
    return render(request,'addbook.html')

def process_add(request):
    author=Author.objects.create(name=request.POST['author'])
    book=Book.objects.create(title=request.POST['title'],author=author)
    review=Review.objects.create(content=request.POST['review'],rating=request.POST['rating'],book=book,user=User.objects.get(id=request.session['user_id']))
    return redirect('/book_review/book/'+str(book.id))

def book(request,id):
    book=Book.objects.get(id=id)
    reviews=Review.objects.filter(book=book)
    context={
        'book':book,
        'reviews':reviews,
    }
    return render(request,'newbook.html',context)

def logout(request):
    request.session.flush();
    return redirect('/book_review')

def user(request,id):
    user=User.objects.get(id=id)
    reviews=user.reviews.all()
    books=[]
    for review in reviews:
        books.append(review.book)
    context={
        'user':user,
        'renum':reviews.count(),
        'books':books,
    }
    return render(request,'user.html',context)
