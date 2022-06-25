from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.models import Sum
from catalog.models import Product, ProductUnit, Category, Brand, Stock, ProductOnOrder
from orders.models import Order

User = get_user_model()

class OrderUseTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@test.com",
            full_name="Евгений Марченко",
            password="test123",
        )
        self.category = Category.objects.create(name="T-Shirt", type="Clothing")
        self.brand = Brand.objects.create(name="ASOS")
        self.product = Product.objects.create(
            name="Mickey Mouse T-Shirt",
            brand=self.brand,
            category=self.category,
        )
        self.product_unit = ProductUnit.objects.create(
            sku="RU539R",
            product=self.product,
            description="boilerplate text",
            store_price=1490
        )
        self.product_unit_2 = ProductUnit.objects.create(
            sku="RU540R",
            product=self.product,
            store_price=1490
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
        assert self.category.name == "T-Shirt"
    
    def test_slug_correctness(self):
        assert self.product.slug == 'mickey-mouse-t-shirt'
    
    def test_brand(self):
        assert self.brand.name == "ASOS"

    def test_total_amount(self):
        assert self.order.order_status == 1
    
    def test_key_number(self):
        assert self.order.key is not None

    def order_customer(self):
        assert self.customer.email == 'test@test.com'
    
    def test_total_order_price(self):
        assert self.order.calculate_total_order_price['order_price__sum'] == 7450
    
    def test_product_unit_item_in_order(self):
        assert self.order.products.count() == 2

    def test_items_quantity_in_order(self):
        assert self.order.get_item_quantity == {'qty__sum': 5}
        

