"""prodj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register(r"product",views.ProductViewSet)
router.register(r"user",views.UserViewSet)
router.register(r"userProfile",views.UserProfileViewSet)
router.register(r"all",views.AllorderViewSet)
router.register(r"order",views.OrderViewSet)
router.register(r"catgory",views.CatgoryViewSet)
urlpatterns = [
    path('', include('home.urls')),
    path('acount/', include('acount.urls')),
    path('shop/', include('shop.urls')),
    path('news/', include('news.urls')),
    path('admin/', admin.site.urls),
    # url for API's
    path("api/", include(router.urls)),
    path('find_user/', include('api.urls')),
    path('add_card/<int:pro_id>', views.add_card),
    path('all_order/<int:user_id>', views.find_orders),
    path('show_pro_catg', views.find_showProCatg),
    path('create_user', views.createUser),
    path('update_user', views.updateUser),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
