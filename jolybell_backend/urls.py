"""jolybell_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from jolybell.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/<str:name>', category, name="category"),
    path('add_to_cart/<int:pk>', add_to_cart, name="add_to_cart"),
    path('cart/', cart, name="cart"),
    path('product/<int:pk>', product, name="product"),
    path('cabinet/', user_cabinet, name='cabinet'),
    path('order/<int:pk>', order, name="order"),

    path('api/categories/', category_collection),
    path('api/products/<str:name>/', products_collection),
    path('api/product/<int:pk>/', product_detail),
    path('api/carts/', cart_collection),
    path('api/cart/<int:pk>/', cart_detail),
    path('api/orders/', order_collection),
    path('api/order/<int:pk>/', order_detail),
    path('api/new_cart/', create_new_cart),
    path('', index, name="index"),
]
