from rest_framework import viewsets
from .serializers import CustomerOrderSerializer
from .models import Order
from .service import PlaceOrderService, OrderDto

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerOrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        # instance = serializer.save(customer=self.request.user)
        # instance.order_price = instance.calculate_total_order_price['order_price__sum']
        # instance.save(update_fields=['order_price'])
        dto = self._get_dto_from_validated_data(serializer.validated_data)
        order_service = PlaceOrderService()
        order_service.allocate(dto)

    
    @staticmethod
    def _get_dto_from_validated_data(self, validated_data):
        data = validated_data
        return OrderDto(
            key=data['key'],
            customer=data['cutomer'],
            order_price=data['order_price'],
            order_status=data['order_status'],
            payment_status=data['payment_status']
        )