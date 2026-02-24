from django.contrib import admin
from django.urls import path
from products.views import *

urlpatterns = [
    path('', store, name="store"),
    path('<slug:category_slug>/', store, name="product_by_category"),
]
