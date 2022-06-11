import random, string
from django.db import models
from base.models import BaseModel
from users.models import User
from django.db.models import Sum
from django.conf import settings

PAYMENT_STATUS = (
    (1, "New order"),
    (2, "Payment confirmed"),
    (3, "Payment declined"),
)

ORDER_STATUS = (
    (1, 'gathering'),
    (2, 'shipping'),
    (3, 'shipped'),
)

def generate_order_key():
    number_part = random.randint(100, 999)
    string_part = random.choices(string.ascii_uppercase, k=3)
    return str(number_part) + "".join(string_part)

class Order(BaseModel):
    key = models.CharField(max_length=6, unique=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    order_price = models.IntegerField(blank=True, null=True)
    order_status = models.CharField(max_length=30, choices=ORDER_STATUS)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS)

    def __str__(self):
        return self.key

    def total_order_price(self):
        print(self.products.aggregate(Sum('product__store_price')))
        return self.products.aggregate(Sum('product__store_price')) #total_price=Sum('product__store_price'))
    
    def save(self, *args, **kwargs):
        if not self.key:
                self.key = generate_order_key()
        super().save(*args, **kwargs)
    
    def get_item_quantity(self):
        order_id = Order.objects.filter(key=self.key)
        
        return len(self.products)