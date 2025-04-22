from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('', include('home.urls')),
    path('', views.all_products, name='all_products'),
    path('', views.all_products, name='products'),
]