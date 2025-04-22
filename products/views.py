from django.shortcuts import render
from django.db.models import Q
from .models import Product
from django.contrib import messages
from django.urls import reverse

def all_products(request):

    products = Product.objects.all()
    query = None
    sort = None

    # Handle search query
    if 'q' in request.GET:
        query = request.GET['q']
        if query:
            products = products.filter(name__icontains=query)
        else:
            messages.error(request, "You didn't enter any search criteria!")

    # Handle sorting
    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey

        if sortkey == 'price':
            products = products.order_by('price')  # Sort by price (ascending)
        elif sortkey == 'rating':
            products = products.order_by('-rating')  # Sort by rating (descending)
        elif sortkey == 'volume':
            products = products.order_by('-volume')  # Sort by volume (descending)

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': sort,
    }

    return render(request, 'products/all_products.html', context)