from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE,related_name="userDetail")
    is_active = models.BooleanField(default= True)
    full_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to = 'photos/users/%Y/%m/%d')

    def __str__(self):
        return self.user.username
    
