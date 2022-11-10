from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from home.models import Product,Catgory
from .models import Order
from .models import OrderDetails
from django.contrib.auth.models import User
from django.utils import timezone
# Create your views here.


def shop(request):
    allpro = Product.objects.all()
    if 'searchname' in request.GET :
        if request.GET['searchname']:

          name = request.GET['searchname']
          allpro = allpro.filter(name__icontains = name)
        #   you can use tow filters :
        #   allpro = allpro.filter(name__icontains = name,descr__icontains = name)
                #   allpro = allpro.filter(name__icontains = name,descr__gte  (it >=  ok) = name)



    # allcat = [x for el in allpro.catgory x ]
    catgory =Catgory.objects.all()
    redCard=False
    if request.user.is_authenticated:
        if  Order.objects.all().filter(user=request.user,is_purchased=False).exists(): #has order make red note
            redCard=True
    context = {
        'redCard':redCard,
        'pro':allpro,
        'catgory':catgory
    
    }
    return render(request,'pages/shop.html',context)

def single_pro(request,pro_id):
    redCard=False
    if request.user.is_authenticated:
        if  Order.objects.all().filter(user=request.user,is_purchased=False).exists(): #has order make red note
            redCard=True
    context = {
        'redCard':redCard,
        'pro': get_object_or_404(Product,pk=pro_id)
    }

    return render(request,'pages/singlpro.html', context)

def check(request):
      redCard=False
      if request.user.is_authenticated:
        if  Order.objects.all().filter(user=request.user,is_purchased=False).exists(): #has order make red note
            redCard=True
      if request.user.is_authenticated:
        total = 0.0
        subtotl = 0.0
        tax = 0.0
        order = None
        order_details = None
        if Order.objects.all().filter(user=request.user,is_purchased=False).exists():
            order = Order.objects.get(user=request.user,is_purchased=False)
            order_details = OrderDetails.objects.all().filter(order=order)
            total = 0.0
            subtotl = 0.0
            tax = 0.0
            for pro in order_details :
                subtotl = subtotl + float(pro.price) * float(pro.quantity)
            tax = subtotl * (5/100)
            total = subtotl + tax
        context = {

                'redCard':redCard,
                'order':order,
                'total':total,
                'subtotl':subtotl,
                'order_details':order_details,
                'tax':tax
              }
        return render(request,'pages/checkout.html',context)
      else:
        return redirect('acount')


def cart(request):
    redCard=False
    if request.user.is_authenticated:
      if  Order.objects.all().filter(user=request.user,is_purchased=False).exists(): #has order make red note
        redCard=True
  
    if request.user.is_authenticated:
      order = None
      order_details = None
      total = 0.0
      subtotl = 0.0
      tax = 0.0
      if  Order.objects.all().filter(user=request.user,is_purchased=False).exists():

        order = Order.objects.get(user=request.user,is_purchased=False)
        order_details = OrderDetails.objects.all().filter(order=order)
     
        for pro in order_details :
          subtotl = subtotl + float(pro.price) * float(pro.quantity)
        tax = subtotl * (5/100)
        total = subtotl + tax
      
      context = {
        'redCard':redCard,
        'order':order,
        'total':total,
        'subtotl':subtotl,

        'order_details':order_details,
        'tax':tax
            }
      return render(request,'pages/cart.html',context)
      
    else:
        return redirect('acount')

def add_cart(request,pro_id):
    if request.user.is_authenticated:

        if Product.objects.all().filter(id=pro_id).exists():
          # from here
          product = Product.objects.get(id=pro_id)
          order = None


          if  Order.objects.all().filter(user=request.user,is_purchased=False).exists(): #old order
            order = Order.objects.get(user=request.user,is_purchased=False)
            print("old order")
            if OrderDetails.objects.all().filter(order=order,product=product ).exists():
                print("id is exists in cart dnt repeat it ")
            else:

              details = OrderDetails.objects.create(product=product,order= order,price=product.price,quantity=1)


            return redirect('shop')
          else:#new order
            print("new order")
            new_order = Order()
            new_order.user= request.user
            new_order.add_date = timezone.now()
            new_order.is_purchased = False
            new_order.save()
            new_order_details = OrderDetails.objects.create(product=product,quantity=1,order=new_order,price=product.price)

            # here end 

            return redirect('shop')

        else:   #not exist pro_id
            print(" order not exists ID")
            return redirect('shop')



    else:
       return redirect('acount')

def delete(request,pro_id):

    if request.user.is_authenticated:
        if OrderDetails.objects.all().filter(id=pro_id).exists():
             product = OrderDetails.objects.get(id=pro_id)  
             product.delete()
            
        return redirect('cart')
    else:
        return redirect('acount')

def update(request,pro_id):
    if request.user.is_authenticated:

        if OrderDetails.objects.all().filter(id=pro_id).exists()and 'qty' in request.GET and request.GET['qty']:
             
            if  int(request.GET['qty']) >= 1 :
                pro=OrderDetails.objects.get(id=pro_id)
                pro.quantity = int(request.GET['qty'])
                pro.save()

        return redirect('cart')
    else:
        return redirect('acount')
  



def buy(request,order_id):
     if request.user.is_authenticated:

        if Order.objects.all().filter(id=order_id,user=request.user,is_purchased=False).exists():
             
            
            pro=Order.objects.get(id=order_id)
            pro.is_purchased = True
            pro.save()

        return redirect('cart')
     else:
        return redirect('acount')

def testy(request):

  return HttpResponse("goood")