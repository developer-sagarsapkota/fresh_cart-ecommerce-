from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductListView(generics.ListAPIView):
    # for all active products
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

# retrieve will automatically detect pk and gives data
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
