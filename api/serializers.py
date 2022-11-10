# countries/serializers.py
from rest_framework import serializers
from home.models import *
from acount.models import *
from shop.models import *
from django.contrib.auth.models import User
from news.models import *
from acount.models import UserProfile

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "photo", "catgory","descr","price"]



class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ["photo","id"]

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        
        fields = ["id", "is_staff", "username","email","first_name","last_name","userDetail","password"]



class AddCardSerializer(serializers.ModelSerializer):
        model = Order
        fields = ["id", "user", "is_purchased", "order_details","add_date",]



class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = ["id","product","order","price","quantity"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["is_purchased"]


class CatgorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catgory
        fields = ["id","name","descr"]