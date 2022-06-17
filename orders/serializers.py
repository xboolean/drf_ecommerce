from django.shortcuts import get_object_or_404
from requests import request
from catalog.models import ProductOnOrder, ProductUnit
from .models import Order
from rest_framework.exceptions import NotFound, ValidationError
from catalog.models import ProductOnOrder, Stock
from rest_framework import serializers
from catalog.serializers import ProductOnOrderSerializer

def can_allocate(qty, product):
    unit = ProductUnit.objects.get(sku=product)
    stock_sku = get_object_or_404(Stock, product=unit)
    if qty <= stock_sku.units_remain:
        pass
    else:
        raise ValidationError(f"There are no so much {product} items in warehouse.")

class CustomerOrderSerializer(serializers.ModelSerializer):
    products = ProductOnOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('customer', 'qty', 'key', 'order_status', 'order_price', 'payment_status')

    # def create(self, validated_data):
    #     items = validated_data.pop('products')
    #     for item in items:
    #         qty = item['qty']
    #         can_allocate(qty, item['product'])
    #     order = Order.objects.create(**validated_data)
    #     for item in items:
    #         qty = item['qty']
    #         item = ProductUnit.objects.get(sku=item['product'])
    #         ProductOnOrder.objects.create(order=order, product=item, qty=qty)
    #         return order
                




