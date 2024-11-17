# coffee_app/urls.py
from django.urls import path
from .views import CoffeeListCreateAPIView, CoffeeDetailAPIView

urlpatterns = [
    path('coffees/', CoffeeListCreateAPIView.as_view(), name='coffee-list-create'),
    path('coffees/<int:pk>/', CoffeeDetailAPIView.as_view(), name='coffee-detail'),
]