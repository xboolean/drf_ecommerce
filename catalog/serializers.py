from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Product, ProductUnit

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductUnitSerializer(ModelSerializer):
    class Meta:
        model = ProductUnit
        fields = "__all__"