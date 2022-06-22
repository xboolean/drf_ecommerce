from rest_framework.viewsets import ModelViewSet
from .serializers import ProductOnPromo, CouponSerializer, PromotionSerializer
from .models import Promotion, Coupon
from .permissions import PromotionPermission
from drf_yasg.utils import swagger_auto_schema

class PromotionViewSet(ModelViewSet):
    serializer_class = PromotionSerializer
    permission_classes = [PromotionPermission]
    queryset = Promotion.objects.all()

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

class CouponViewset(ModelViewSet):
    serializer_class = CouponSerializer
    permission_classes = [PromotionPermission]
    queryset = Coupon.objects.all()

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)