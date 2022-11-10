from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from shop.models import Order
# Create your views here.


def index(request):
    redCard=False
    if request.user.is_authenticated:
        if  Order.objects.all().filter(user=request.user,is_purchased=False).exists(): #has order make red note
            redCard=True

    context={
        'redCard':redCard,
        'pro':Product.objects.all()
        }

    return render(request,'pages/index.html',context)

def about(request):
    redCard=False
    if request.user.is_authenticated:
        if  Order.objects.all().filter(user=request.user,is_purchased=False).exists(): #has order make red note
            redCard=True

    context={
        'redCard':redCard,
        'pro':Product.objects.all()
        }
    return render(request,'pages/about.html',context)

def contact(request):
       redCard=False
       if request.user.is_authenticated:
         if  Order.objects.all().filter(user=request.user,is_purchased=False).exists(): #has order make red note
            redCard=True

       context={
        'redCard':redCard,
        'pro':Product.objects.all()
        }
       return render(request,'pages/contact.html',context)    

