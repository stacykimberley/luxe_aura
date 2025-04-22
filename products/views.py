from django.shortcuts import render
from .models import Product


def all_products(request):
    products = Product.objects.all()
    
    for product in products:
        rating = product.rating or 0
        full_stars = int(rating)
        half_star = (rating - full_stars) >= 0.5
        empty_stars = 5 - full_stars - int(half_star)

        product.star_display = {
            'full': range(full_stars),
            'half': half_star,
            'empty': range(empty_stars)
        }

    return render(request, 'products/all_products.html', {'products': products})