import random, string
from base.models import M2MBaseModel, BaseModel
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from catalog.models import Product
from orders.models import Order

User = get_user_model()

class Promotion(BaseModel):
    name = models.CharField(max_length=50)
    products = models.ManyToManyField(Product, through='ProductOnPromo')
    promo_discount = models.FloatField(validators=(MaxValueValidator(100.0), MinValueValidator(0.0)))
    promo_start = models.DateField()
    promo_end = models.DateField()
    is_active = models.BooleanField(default=False)
    is_scheduled = models.BooleanField(default=False)

class ProductOnPromo(M2MBaseModel):
    product_id = models.ForeignKey(Product, to_field='uu_id', related_name='productOnPromotion', on_delete=models.PROTECT)
    promotion_id = models.ForeignKey(Promotion, to_field='uu_id', related_name="promotion", on_delete=models.CASCADE)


def generate_coupon_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))


class CouponManager(models.Manager):
    def create(self, *args, **kwargs):
        kwargs["code"] = generate_coupon_code()
        return super().create(*args, **kwargs)


class Coupon(BaseModel):
    code = models.CharField(max_length=12)
    discount = models.FloatField(validators=(MaxValueValidator(100.0), MinValueValidator(0.0)))
    customer = models.ManyToManyField(User, through='ClaimedCoupon', blank=True)
    is_active = models.BooleanField()
    objects = CouponManager()

class ClaimedCoupon(M2MBaseModel):
    customer = models.ForeignKey(User, to_field='uu_id', on_delete=models.CASCADE, related_name='coupons')
    coupon = models.ForeignKey(Coupon, to_field='uu_id', on_delete=models.CASCADE, related_name='claimed_by')
    order = models.OneToOneField(Order, to_field='uu_id', on_delete=models.PROTECT, related_name='coupon')
    redemeed = models.BooleanField()

    @property
    def coupon_code(self):
        self.coupon.code

    class Meta:
        unique_together = ["order", "coupon"]