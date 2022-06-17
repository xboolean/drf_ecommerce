from dataclasses import dataclass
from catalog.models import ProductUnit, ProductOnOrder
from orders.models import Order
from rest_framework.generics import get_object_or_404

#dto for input data
@dataclass
class OrderDto:
    key: str
    customer: int
    order_price: int
    order_status: int
    payment_status: int

@dataclass
class Item:
    sku: str
    qty:int


class PlaceOrderService:
    def allocate(self, item, dto):
        if self.can_allocate(item):
            order = Order.objects.create(
                key=dto.key,
                customer=dto.cutomer,
                order_price=dto.order_price,
                order_status=dto.order_status,
                payment_status=dto.payment_status
            )
            product = ProductUnit.objects.get(sku=item['product'])
            ProductOnOrder.objects.create(order=order, product=product, qty=item.qty)

    def can_allocate(self, item):
        product = get_object_or_404(ProductUnit, sku=item.sku)
        return item.qty <= product.warehouse.units_remain
