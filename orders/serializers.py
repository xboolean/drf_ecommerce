from wsgiref.validate import validator
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import NotFound, ValidationError
from django.db import transaction
from catalog.models import ProductOnOrder, ProductUnit
from .models import Order
from promotions.models import Coupon
from promotions.models import ClaimedCoupon
from catalog.models import ProductOnOrder, Stock

from catalog.serializers import ProductOnOrderSerializer

class CustomerOrderSerializer(serializers.ModelSerializer):
    products = ProductOnOrderSerializer(many=True)
    coupon = serializers.SlugRelatedField(slug_field='code', queryset=Coupon.objects.all(), source='coupon.coupon', required=False, allow_null=True)
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('customer', 'qty', 'key', 'order_status', 'order_price', 'payment_status', 'coupon')
        extra_kwargs = {'coupon': {}}

    @transaction.atomic
    def create(self, validated_data):
        request = self.context.get('request')
        products = validated_data.pop('products')
        if not validated_data['coupon'] is None:
            coupon = validated_data.pop('coupon')['coupon']
        order = self.Meta.model.objects.create(**validated_data)
        if coupon:
            if not ClaimedCoupon.objects.filter(coupon=coupon, customer=request.user):
                ClaimedCoupon.objects.create(customer=request.user, order=order, coupon=coupon,  redemeed=True)
            else:
                raise ValidationError("Your coupon is redemeed.")
        for product in products:
            line = ProductOnOrder.objects.create(order=order, **product)
        return order