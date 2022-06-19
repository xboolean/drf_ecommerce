from rest_framework import viewsets
from .serializers import CustomerOrderSerializer
from .permissions import OrderPermission
from .models import Order
from django.db import transaction

class OrderViewSet(viewsets.ModelViewSet):
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


    
