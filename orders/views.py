from rest_framework import viewsets
from .serializers import CustomerOrderSerializer
from .models import Order

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerOrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)