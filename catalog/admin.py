from django.contrib import admin

from catalog.models import ProductUnit
from catalog import models
class InventoryAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    model = models.Product
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'category', 'brand', 'is_active')

class ProductUnitAdmin(admin.ModelAdmin):
    model = models.ProductUnit
    list_display = ('sku', 'product', 'store_price', 'is_active')

class StockAdmin(admin.ModelAdmin):
    model = models.ProductUnit
    list_display = ('product', 'units_remain', 'units_sold')
    

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductUnit, ProductUnitAdmin)
admin.site.register(models.Stock, StockAdmin)
admin.site.register(models.Category)
admin.site.register(models.Brand)