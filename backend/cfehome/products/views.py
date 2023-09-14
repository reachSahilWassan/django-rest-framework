from django.shortcuts import render
from products.serializers import ProductSerializer
from rest_framework import generics
from products.models import Products

# Create your views here.
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


