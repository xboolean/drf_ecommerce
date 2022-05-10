from django.contrib import admin
from catalog.models import ProductOnOrder
from .models import Order

class ProductInline(admin.TabularInline):
    model = ProductOnOrder

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]

admin.site.register(Order, OrderAdmin)
