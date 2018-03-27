from django.shortcuts import render,redirect


products={
    '001':19.99,
    '002':4.99,
    '003':29.99,
}
# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count']=0
    if 'total' not in request.session:
        request.session['total']=0
    return render(request,'amadon/index.html')

def buy(request):
    product_id=request.POST['product_id']
    request.session['price']=int(request.POST['quantity'])*products[product_id]
    request.session['count']+=int(request.POST['quantity'])
    request.session['total']+=int(request.POST['quantity'])*products[product_id]
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request,'amadon/checkout.html')
