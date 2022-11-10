from django.urls import path
from . import views
urlpatterns = [
   path('', views.news,name='news'),
   path('<int:news_id>', views.single_news,name='singl_news'),
   
]
