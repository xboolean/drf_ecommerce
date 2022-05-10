from django.db import models
from base.models import BaseModel

class Product(BaseModel):
    slug = models.SlugField()
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

class ProductUnit(BaseModel):
    sku = models.CharField(max_length=8, unique=True, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

class Stock(models.Model):
    product = models.ForeignKey(ProductUnit, on_delete=models.CASCADE)
    units_remain = models.PositiveSmallIntegerField()
    units_sold = models.PositiveSmallIntegerField()

class Media(BaseModel):
    product = models.ForeignKey(ProductUnit, on_delete=models.CASCADE)
    img = models.FileField(upload_to='uploads')
    alt_text = models.CharField(max_length=60)

class Category(BaseModel):
    name = models.CharField(max_length=50)

class Brand(BaseModel):
    name = models.CharField(max_length=50)
