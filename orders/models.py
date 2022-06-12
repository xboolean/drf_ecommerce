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
    (1, 'pending'),
    (2, 'gathering'),
    (3, 'shipping'),
    (4, 'shipped'),
)

def generate_order_key():
    number_part = random.randint(100, 999)
    string_part = random.choices(string.ascii_uppercase, k=3)
    return str(number_part) + "".join(string_part)

class Order(BaseModel):
    key = models.CharField(max_length=6, unique=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    order_price = models.IntegerField(blank=True, null=True)
    order_status = models.CharField(max_length=30, choices=ORDER_STATUS, default=1)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS)

    def __str__(self):
        return self.key

    @property
    def calculate_total_order_price(self):
        return self.products.aggregate(Sum('order_price'))

    @property
    def get_item_quantity(self):
        return self.products.aggregate(Sum('qty'))


    def save(self, *args, **kwargs):
        if not self.key:
                self.key = generate_order_key()
        print(self.calculate_total_order_price['order_price__sum'])
        self.order_price = self.calculate_total_order_price['order_price__sum']

        super().save(*args, **kwargs)
    
