from rest_framework import viewsets, generics, status
from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAdminUser
from .serializers import ProductSerializer, ProductUnitSerializer, CategorySerializer, BrandSerializer, StockSerializer
from .models import Product, ProductUnit, Brand, Category, Stock
from .permissions import ProductPermission, AdminOrReadOnly
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from drf_yasg.inspectors import FieldInspector

class BrandCreateView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [AdminOrReadOnly]

class CategoryCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AdminOrReadOnly]

class StockViewSet(ListModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    """
    Viewset for managing leftovers in warehouse.
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdminUser]


class ProductViewSet(viewsets.ModelViewSet):
    """
    Viewset for creating products.
    """
    permission_classes = [ProductPermission]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Product.objects.filter(is_active=True)
        else:
            return super().get_queryset()
    
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
    
class ProductUnitViewSet(viewsets.ModelViewSet):
    """
    Viewset for creating product's units.
    """
    permission_classes = [ProductPermission]
    serializer_class = ProductUnitSerializer
    queryset = ProductUnit.objects.all()

    def get_queryset(self):
        if not self.request.user.is_staff:
            return ProductUnit.objects.filter(is_active=True)
        else:
            return super().get_queryset()
    
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

