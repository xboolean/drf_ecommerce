from django.urls import path
from rest_framework.routers import DefaultRouter
from catalog.views import ProductViewSet
from catalog.views import ProductUnitViewSet

app_name = 'products'

router = DefaultRouter()
router.register("product", ProductViewSet, basename="product")
router.register("product_sku", ProductUnitViewSet, basename="product-unit")

urlpatterns = router.urls

