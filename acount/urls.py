from django.urls import path
from . import views
urlpatterns = [
  
   path('', views.acount,name='acount'),    
   path('logout/', views.loguot,name='logout'),  
   path('profile/', views.profile,name='profile'),     
   
]
