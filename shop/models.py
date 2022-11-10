from django.db import models
from acount.models import UserProfile
from datetime import datetime
from django.contrib.auth.models import User
from home.models import Product
# Create your models here.
class Catgory (models.Model):
    name = models.CharField(max_length=150)
    descr = models.TextField()
    is_active = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name


# Create order models here.
class Order  (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_purchased = models.BooleanField(default=False)
    add_date = models.DateTimeField(default=datetime.now)
    order_details = models.ManyToManyField(Product,through='OrderDetails')

    def __str__(self):
        return 'User: '+ self.user.username+'| order id: '+str(self.id)

class OrderDetails (models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    order = models.ForeignKey(Order,on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places= 2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return 'User : '+self.order.user.username+'|  product name : '+self.product.name+' |order id :' +str(self.order.id)
    