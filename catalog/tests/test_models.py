from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model
from ..models import Product, ProductUnit, Category, Brand, Stock, ProductOnOrder
from orders.models import Order

User = get_user_model()

class OrderUseTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@test.com",
            full_name="Евгений Марченко",
            password="test123",
        )
        self.category = Category.objects.create(name="T-Shirt")
        self.brand = Brand.objects.create(name="ASOS")
        self.product = Product.objects.create(
            name="Mickey Mouse T-Shirt",
            description="Just regulat T-Shirt",
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
        self.stock_p1 = Stock.objects.create(
            product=self.product_unit,
            units_remain = 5
        )
        self.stock_p2 = Stock.objects.create(
            product=self.product_unit_2,
            units_remain = 5
        )
        self.order = Order.objects.create( 
            customer=self.user,
        )
        self.products = ProductOnOrder.objects.create(
            product=self.product_unit,
            order=self.order,
            qty=3
        )
        self.products = ProductOnOrder.objects.create(
            product=self.product_unit_2,
            order=self.order,
            qty=2
        )
        
        
    
    def test_category(self):
        assert self.category == "T-Shirt"
    
    def test_brand(self):
        assert self.brand == "ASOS"

    def test_total_amount(self):
        assert self.order.order_payment == 1490
    
    def test_key_number(self):
        assert self.key is not None

    def test_ordet_items(self):
        assert len(self.products)==2
    
    def ordet_user(self):
        assert self.customer.email == 'test@test.com'
    
    def test_total_order_price(self):
        assert self.order_pice == 7450
    
    def test_items_quantity(self):
        assert self.get_item_quantity == 5
        

