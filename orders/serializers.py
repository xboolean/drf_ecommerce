from requests import request
from catalog.models import ProductOnOrder, ProductUnit
from .models import Order
from catalog.models import ProductOnOrder
from rest_framework import serializers
from catalog.serializers import ProductOnOrderSerializer

class CustomerOrderSerializer(serializers.ModelSerializer):
    products = ProductOnOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('customer', 'key', 'order_status', 'order_price', 'payment_status')

    def create(self, validated_data):
        request = self.context.get('request')
        products = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        for product in products:
            item = ProductUnit.objects.get(sku=product['product'])
            ProductOnOrder.objects.create(order=order, product=item, qty=product['qty'])
        return order


