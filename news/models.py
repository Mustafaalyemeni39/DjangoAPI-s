from django.db import models
from datetime import datetime
# Create your models here.
class News (models.Model):
    title = models.CharField(max_length=150)
    descr = models.TextField()
    photo = models.ImageField(upload_to = 'photos/newsImg/%Y/%m/%d')
    is_active = models.BooleanField(default=True)
    allow_comment = models.BooleanField(default=True)

    publish_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title




