from django.db import models
from products.models import Products

# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(max_length=50, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return self.product

