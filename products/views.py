from django.shortcuts import render, get_object_or_404
from products.models import Products
from category.models import Category

# Create your views here.


def store(request, category_slug=None):
    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Products.objects.filter(category=category)
    else:
        products = Products.objects.all()
    context = {
        'products' : products
    }

    return render(request, "shop.html", context=context)