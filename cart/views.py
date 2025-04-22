from django.shortcuts import redirect
from products.models import Product
from django.contrib import messages

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart

    messages.success(request, "Product added to cart!")
    return redirect('all_products')