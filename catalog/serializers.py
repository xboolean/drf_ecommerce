from django.forms import CharField
from rest_framework.generics import get_object_or_404
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from orders.models import Order
from .models import Product, ProductUnit, ProductOnOrder, Brand, Category, Stock

class CategorySerializer(ModelSerializer):
    products = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = Category
        fields = "__all__"

class BrandSerializer(ModelSerializer):
    products = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = Brand
        fields = "__all__"

class StockSerializer(ModelSerializer):
    product = serializers.SlugRelatedField(read_only=True, slug_field='sku')

    class Meta:
        model = Stock
        fields = "__all__"
        read_only_fields = ('product',)


class ProductSerializer(ModelSerializer):
    brand = serializers.SlugRelatedField(slug_field='name', queryset=Brand.objects.all())
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'brand', 'category', 'is_active', 'created_at', 'updated_at')

    def create(self, validated_data):
        brand = Brand.objects.get(name=validated_data.pop('brand'))
        category = Category.objects.get(name=validated_data.pop('category'))
        product = Product.objects.create(brand=brand, category=category, **validated_data)
        return product

class ProductUnitSerializer(ModelSerializer):
    product = serializers.CharField()

    class Meta:
        model = ProductUnit
        fields = '__all__'
        read_only_fields = ('sale_price',)
    
    def create(self, validated_data):
        product = get_object_or_404(Product, name=validated_data.pop('product'))
        product_unit = ProductUnit.objects.create(product=product, **validated_data)
        return product_unit      

class ProductOnOrderSerializer(ModelSerializer):
    product = serializers.SlugRelatedField(slug_field='sku', queryset=ProductUnit.objects.all())

    class Meta:
        model = ProductOnOrder
        fields = ('product', 'qty', 'order_price',)
        read_only_fields= ('order_price',)

    def validate(self, attrs):
        item, qty = attrs['product'], attrs['qty']
        if not item.warehouse.units_remain >= qty:
            raise serializers.ValidationError(f"There are no such many {item} in warehouse.")
        elif qty <= 0:
            raise serializers.ValidationError(f"The {item} must contain at least one item in order.")
        return attrs
        
    