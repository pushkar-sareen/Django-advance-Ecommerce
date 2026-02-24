from django.shortcuts import render, redirect
from carts.models import Cart, CartItem
from products.models import Products



def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Products.objects.get(id=product_id)

    try :
        cart = Cart.objects.get(cart_id= _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id = _cart_id(request))
        cart.save()

    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(cart=cart, product=product, quantity=1)
        cart_item.save()
    return redirect('cart')

def cart(request, total= 0, tax=0):
    try :
        cart = Cart.objects.get(cart_id= _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id = _cart_id(request))
        cart.save()
    
    cart_items= CartItem.objects.all()
    for item in cart_items:
        total += item.product.price * item.quantity
    tax =  (total * 2)/100
    grand_total = total + tax
    context = {
        'cart_items':cart_items,
        'total' : total,
        'tax': tax,
        'grand_total': grand_total
    }
    return render(request, 'cart.html', context=context)


def delete_cart_item(request, product_id):
    product = Products.objects.get(id = product_id)
    product.delete()
    return redirect('cart')

def decrease_item(request, product_id):
    products =Products.objects.get(id= product_id)
    cart = Cart.objects.get(cart_id = _cart_id(request))
    cart_items = CartItem.objects.get(cart=cart, product=products)
    if cart_items.quantity > 1:
        cart_items.quantity -= 1
        cart_items.save()
    else:
        cart_items.delete()
    return redirect('cart')