from rest_framework import viewsets, generics
from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAdminUser
from .serializers import ProductOnOrderSerializer, ProductSerializer, ProductUnitSerializer, CategorySerializer, BrandSerializer, StockSerializer
from .models import Product, ProductOnOrder, ProductUnit, Brand, Category, Stock
from .permissions import ProductPermission, AdminOrReadOnly

class BrandCreateView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [AdminOrReadOnly]

class CategoryCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AdminOrReadOnly]

class StockViewSet(ListModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [ProductPermission]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Product.objects.filter(is_active=True)
        else:
            return super().get_queryset()
    

class ProductUnitViewSet(viewsets.ModelViewSet):
    permission_classes = [ProductPermission]
    serializer_class = ProductUnitSerializer
    queryset = ProductUnit.objects.all()

    def get_queryset(self):
        if not self.request.user.is_staff:
            return ProductUnit.objects.filter(is_active=True)
        else:
            return super().get_queryset()

