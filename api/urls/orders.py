from django.urls import path
from rest_framework.routers import DefaultRouter
from orders.views import OrderViewSet

app_name = 'orders'

router = DefaultRouter()
router.register("orders", OrderViewSet, basename="orders")

urlpatterns = router.urls
