from rest_framework.viewsets import ModelViewSet
from .serializers import ProductOnPromo, CouponSerializer, PromotionSerializer
from .models import Promotion, Coupon
from .permissions import PromotionPermission

class PromotionViewSet(ModelViewSet):
    serializer_class = PromotionSerializer
    permission_classes = [PromotionPermission]
    queryset = Promotion.objects.all()

class CouponViewset(ModelViewSet):
    serializer_class = CouponSerializer
    permission_classes = [PromotionPermission]
    queryset = Coupon.objects.all()