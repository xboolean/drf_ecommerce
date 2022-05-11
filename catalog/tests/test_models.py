from django.test import TestCase
from django.conf import settings
from users.models import User
from ..models import Product, ProductUnit, Category, Brand, Stock, ProductOnOrder
from orders.models import Order

class OrderTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@test.com",
            full_name="Евгений Марченко",
            password="barboris",
        )
        self.category = Category.objects.create(name="T-Shirt")
        self.brand = Brand.objects.create(name="ASOS")
        self.product = Product.objects.create(
            name="Mickey Mouse T-Shirt",
            description="Size M",
            brand="ASOS",
            category="T-Shirt",
        )
        self.product_unit = ProductUnit.objects.create(
            sku="RU539RUR",
            product=self.product,
            store_price="1490"
        )
        self.product_unit_2 = ProductUnit.objects.create(
            sku="RU540RUR",
            product=self.product,
            store_price="1490"
        )
        self.stock = Stock.objects.create(
            product=self.product_unit,
        )
        self.order = Order.objects.create( 
            customer=self.user,
            status="new"
        )
        self.products = ProductOnOrder.objects.create(
            product=self.product_unit,
            order=self.order,
        )
        

        

