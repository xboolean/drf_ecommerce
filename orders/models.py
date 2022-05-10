from django.db import models
from base.models import BaseModel
from users.models import User
from django.db.models import Sum

ORDER_STATUS = (
    ("new", "New order"),
    ("payment_confirmed", "Payment confirmed"),
    ("payment_declined", "Payment declined"),
)

class Order(BaseModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(choices=ORDER_STATUS, max_length=20)
    

    def __str__(self):
        return str(self.id)

    def total_order_price(self):
        return self.products.aggregate(total_price=Sum('product__store_price'))

class OrderPayment(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField()