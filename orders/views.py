from base. views import UUIDModelViewSet
from .serializers import CustomerOrderSerializer
from .permissions import OrderPermission
from .models import Order
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

class OrderViewSet(UUIDModelViewSet):
    """
    Viewset to make an order by customer.
    """
    permission_classes = [OrderPermission]
    serializer_class = CustomerOrderSerializer
    queryset = Order.objects.all()

    @transaction.atomic
    def perform_create(self, serializer):
        if hasattr(self.request.user, 'profile'):
            instance = serializer.save(customer=self.request.user.profile)
        else:
            return Response({'error': 'Superuser is unable to place an order!'}, status=status.HTTP_400_BAD_REQUEST)
        if hasattr(instance, 'coupon'):
            instance.order_price = instance.calculate_total_order_price['order_price__sum'] / 100 * (100 - instance.coupon.coupon.discount) 
        else:
            instance.order_price = instance.calculate_total_order_price['order_price__sum']
        instance.save(update_fields=['order_price'])
    
    def get_queryset(self):
        if hasattr(self.request.user, 'profile'):
            return super().get_queryset().filter(customer=self.request.user.profile)
        elif getattr(self.request.user, 'is_staff') == True:
            return super().get_queryset()
    
    
    @swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)