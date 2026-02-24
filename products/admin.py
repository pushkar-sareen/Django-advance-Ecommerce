from django.contrib import admin
from products.models import Products

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('product_name',)
    }
    list_display = ('product_name', "slug", "price", 'category', 'is_available')


admin.site.register(Products, ProductAdmin)