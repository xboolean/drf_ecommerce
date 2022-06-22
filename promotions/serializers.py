from rest_framework.serializers import ModelSerializer
from .models import Coupon, Promotion

class CouponSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"
        read_only_fields = ('code',)

class PromotionSerializer(ModelSerializer):
    class Meta:
        model = Promotion
        fields = "__all__"
        