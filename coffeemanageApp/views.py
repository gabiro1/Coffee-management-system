# coffee_app/views.py
from rest_framework import generics
from .models import Coffee
from .serializers import CoffeeSerializer

class CoffeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer

class CoffeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer