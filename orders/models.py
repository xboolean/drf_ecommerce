import random, string
from django.db import models
from base.models import BaseModel
from django.db.models import Sum
from users.models import CustomerProfile

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

class OrderManager(models.Manager):

    def create(self, *args, **kwargs):
        kwargs["key"] = generate_order_key()
        return super().create(*args, **kwargs)

class Order(BaseModel):
    key = models.CharField(max_length=6, unique=True)
    customer = models.ForeignKey(CustomerProfile, to_field='uu_id', on_delete=models.CASCADE, related_name="orders")
    order_price = models.IntegerField(blank=True, null=True)
    order_status = models.CharField(max_length=30, choices=ORDER_STATUS, default=1)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default=1)

    def __str__(self):
        return self.key

    @property
    def calculate_total_order_price(self):
        return self.products.aggregate(Sum('order_price'))

    @property
    def get_item_quantity(self):
        return self.products.aggregate(Sum('qty'))

    objects = OrderManager()

    
