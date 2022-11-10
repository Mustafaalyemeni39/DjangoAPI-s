from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News
from shop.models import Order
from home.models import Product

# Create your views here.


def news(request):
    redCard=False
    if request.user.is_authenticated:
        if  Order.objects.all().filter(user=request.user,is_purchased=False).exists(): #has order make red note
            redCard=True
    news=News.objects.all()
    context={
        "redCard":redCard,
        "news":news,
    }

    return render(request,'pages/news.html',context)

def single_news(request,news_id):
    redCard=False
  
    if request.user.is_authenticated:
        if  Order.objects.all().filter(user=request.user,is_purchased=False).exists(): #has order make red note
            redCard=True
    
   
    context = {
        'redCard':redCard,
        'products':Product.objects.all(),
        'allnews':News.objects.all(),
        'news': get_object_or_404(News,pk = news_id)
    }
    
    return render(request,'pages/singlnews.html',context)    

