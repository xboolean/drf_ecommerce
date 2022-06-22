from rest_framework import viewsets
from .serializers import CustomerOrderSerializer
from .permissions import OrderPermission
from .models import Order
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action 

class OrderViewSet(viewsets.ModelViewSet):
    """
    Viewset to make an order by customer.
    """
    permission_classes = [OrderPermission]
    serializer_class = CustomerOrderSerializer
    queryset = Order.objects.all()

    @transaction.atomic
    def perform_create(self, serializer):
        instance = serializer.save(customer=self.request.user)
        if hasattr(instance, 'coupon'):
            instance.order_price = instance.calculate_total_order_price['order_price__sum'] / 100 * (100 - instance.coupon.coupon.discount) 
        else:
            instance.order_price = instance.calculate_total_order_price['order_price__sum']
        instance.save(update_fields=['order_price'])
    
    @swagger_auto_schema(auto_schema=None)
    def list(self, request, *args, **kwargs):
        super().list(*args, **kwargs)
    
    @swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)