# api/views.py
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from shop.models import *
from home.models import *
from .serializers import *
from django.utils import timezone
from acount.models import UserProfile
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().prefetch_related("userDetail")
     

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


#7 Find catgory to show prodcut
@api_view(['POST'])
def find_showProCatg(request):
    product = Product.objects.all().filter(catgory=request.data['id'])
  
    serializer = ProductSerializer(product, many= True)
    return Response(serializer.data)


#8 Find user to login
@api_view(['POST'])
def find_user(request):
    user = auth.authenticate(username=request.data['username'],password= request.data['password'])
  
    serializer = UserSerializer(user)
    return Response(serializer.data)


#9 add cart order

def add_card(request,pro_id):

         
    if request.method=="GET":
        
          user = User.objects.get(username=request.GET["name"])
  
          product = Product.objects.get(id=pro_id)
          order = None

         
          if  Order.objects.all().filter(user= user, is_purchased=False).exists(): #old order
            order = Order.objects.get(user=user,is_purchased=False)
            
            if OrderDetails.objects.all().filter(order=order,product=product ).exists():
                        return HttpResponse("exist.. ")

                    # nothing
            else:

                details = OrderDetails.objects.create(product=product,order= order,price=product.price,quantity=1)
                return HttpResponse("added succefull ot old order.. ")


          else:#new order
            
            order = Order()
            order.user= user
            order.add_date = timezone.now()
            order.is_purchased = False
            order.save()
            order_details = OrderDetails.objects.create(product=product,quantity=1,order=order,price=product.price)
            return HttpResponse("added new order  succefull .. ")
            # here end 

#10  create user
@api_view(['POST'])
def createUser(request):
    user = User.objects.create_user(username =request.data['username'] ,password = request.data['password'],email = request.data['email'])
    user.save()
    userprofile = UserProfile(user=user)
    userprofile.save()
    serializer = UserSerializer(user)
    return Response(serializer.data)

#11 Update user
@api_view(['PUT'])
def updateUser(request):
    user = User.objects.get(pk =request.data['id'])
    user.username = request.data['username']
    user.email = request.data['email']
    user.last_name = request.data['last_name']
    user.first_name = request.data['first_name']
    user.set_password(request.data['password'])
    user.save()

    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def find_orders(request,user_id):
    user = User.objects.get(pk=user_id)
    order = Order.objects.get(user=user,is_purchased=False)
    orderDetail =  OrderDetails.objects.all().filter(order=order)
    serializer = OrderDetailSerializer(orderDetail,many= True)
    return Response(serializer.data)

class AllorderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetails.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class CatgoryViewSet(viewsets.ModelViewSet):
    serializer_class = CatgorySerializer
    queryset = Catgory.objects.all()