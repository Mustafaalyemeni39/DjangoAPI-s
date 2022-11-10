from django.urls import path
from . import views
urlpatterns = [
   path('', views.shop,name='shop'),
   path('test', views.testy,name='testy'),
   path('<int:pro_id>', views.single_pro,name='singl_pro'),
   path('cart/', views.cart,name='cart'),
   path('cart/<int:pro_id>', views.add_cart,name='add_cart'),
   path('check/', views.check,name='check'),  
   path('cart/delete/<int:pro_id>', views.delete,name='delete_card'),
   path('cart/update/<int:pro_id>', views.update,name='update'),
   path('cart/buy/<int:order_id>', views.buy,name='buy'),
   
]
