from django.db import models
from base.models import BaseModel
from orders.models import Order
from django.conf import settings

class Product(BaseModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField()
    brand = models.ForeignKey("Brand", related_name="products", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", related_name="products", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class ProductUnit(BaseModel):
    sku = models.CharField(max_length=8, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    order = models.ManyToManyField(Order, through="ProductOnOrder")
    sale_price = models.PositiveSmallIntegerField(null=True, blank=True)
    store_price = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.sku} {self.product.name}"

class ProductOnOrder(models.Model):
    product = models.ForeignKey(ProductUnit, on_delete=models.CASCADE, related_name="products")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="products")
    qty = models.PositiveSmallIntegerField()
    order_price = models.IntegerField()

    @property
    def order_row_price(self):
        return self.product__store_price * self.qty
    
    def save(self, *args, **kwargs):
        if not self.product:
            self.order_price = self.order_row_price
        super.save(*args, **kwargs)

class Stock(models.Model):
    product = models.OneToOneField(ProductUnit, on_delete=models.CASCADE, unique=True)
    units_remain = models.PositiveSmallIntegerField(default=0)
    units_sold = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return str(self.product)
    
class Media(BaseModel):
    product = models.ForeignKey(ProductUnit, on_delete=models.CASCADE)
    img_url = models.URLField(unique=False, null=False, blank=False)
    alt_text = models.CharField(max_length=140)

class Category(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Brand(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
