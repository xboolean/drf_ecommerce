from django.urls import path
from rest_framework.routers import DefaultRouter
from catalog.views import ProductViewSet
from catalog.views import ProductUnitViewSet

app_name = 'products'

router = DefaultRouter()
router.register("product", ProductViewSet, basename="users")
router.register("product_sku", ProductUnitViewSet, basename="users")

urlpatterns = []
urlpatterns += router.urls

