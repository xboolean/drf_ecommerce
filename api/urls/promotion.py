from django.urls import path
from rest_framework.routers import DefaultRouter
from promotions.views import PromotionViewSet, CouponViewset


app_name = 'promotion'

router = DefaultRouter()
router.register("promotion", PromotionViewSet, basename="promotion")
router.register("coupon", CouponViewset, basename="coupon")

urlpatterns = router.urls

