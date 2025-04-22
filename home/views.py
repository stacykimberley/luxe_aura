from django.shortcuts import render
from products.models import Product


def index(request):
    featured_products = Product.objects.all()[:4]
    return render(request, 'home/index.html', {
        'featured_products': featured_products
    })