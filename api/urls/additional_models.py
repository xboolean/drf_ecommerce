from django.urls import path
from rest_framework.routers import DefaultRouter
from catalog.views import BrandCreateView, CategoryCreateView

app_name = 'catalog'

router = DefaultRouter()



urlpatterns = [
    path('brands/', BrandCreateView.as_view(), name='brands'),
    path('category/', CategoryCreateView.as_view(), name='category'),
    # path('stock/', StockView.as_view({'get': 'list', 'put': 'update'}), name='put_stock'),
]
