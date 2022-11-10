from django.db import models
from datetime import datetime
# Create your models here.
class Catgory (models.Model):
    name = models.CharField(max_length=150)
    descr = models.TextField()
    is_active = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name




# Create your models here.
class Product (models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places= 2)
    descr = models.TextField()
    catgory = models.ForeignKey(Catgory, on_delete = models.CASCADE)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d')
    is_active = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['-publish_date']