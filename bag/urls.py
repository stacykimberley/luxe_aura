from django.urls import path
from . import views

app_name = 'bag'

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    # ... any other bag-related views
]
