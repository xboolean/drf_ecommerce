from django.dispatch import receiver
from django.db.models import signals, Model
from .models import Stock, ProductUnit

@receiver(signal=signals.post_save, sender=ProductUnit)
def create_stock_model(sender: Model, instance: ProductUnit, created: bool, raw: bool, update_fields:dict, using: str, **kwargs):
    if created:
        stock = Stock.objects.create(product=instance)
        stock.save()



