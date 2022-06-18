from django.urls import path
from rest_framework.routers import DefaultRouter
from catalog.views import BrandCreateView, CategoryCreateView, StockViewSet

app_name = 'catalog'

router = DefaultRouter()
router.register("stock", StockViewSet, basename="stock")


urlpatterns = [
    path('brands/', BrandCreateView.as_view(), name='brands'),
    path('category/', CategoryCreateView.as_view(), name='category'),
    # path('stock/', StockView.as_view({'get': 'list', 'put': 'update'}), name='put_stock'),
]

urlpatterns += router.urls

