from django.contrib import admin
from django.urls import path
from carts.views import *

urlpatterns = [
    path('', cart, name="cart"),
    path('add_cart/<int:product_id>/', add_cart, name='add_cart'),
    path('delete_cart/<int:product_id>/', delete_cart_item, name="delete_cart"),
    path('decrease_item/<int:product_id>/', decrease_item, name="decrease_item"),
]
