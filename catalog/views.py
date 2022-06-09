from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer, ProductUnitSerializer
from .models import Product, ProductUnit
from .permissions import ProductPermission

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductUnitViewSet(viewsets.ModelViewSet):
    permission_classes = [ProductPermission]
    serializer_class = ProductUnitSerializer
    queryset = ProductUnit.objects.all()
