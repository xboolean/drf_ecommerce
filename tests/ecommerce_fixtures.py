from unicodedata import category
import pytest
from catalog.models import Product, ProductUnit, Category, Brand, Stock, ProductOnOrder
from promotions.models import Coupon

@pytest.fixture
def single_brand(db):
    return Brand.objects.create(name="LuxuryBrand")

@pytest.fixture
def single_category(db):
    return Category.objects.create(name="Shoes", type="Clothing")

@pytest.fixture
def single_product(db, single_brand, single_category):
    return Product.objects.create(name='EA7 bleached T-Shirt', brand=single_brand, category=single_category)

@pytest.fixture
def single_product_item_1(db, single_product):
    return ProductUnit.objects.create(sku="555GHJ", product=single_product, description="Lorem Ipsum", store_price=1490)


@pytest.fixture
def single_product_item_2(db, single_product):
    return ProductUnit.objects.create(sku="555GHK", product=single_product, description="Lorem Ipsum", store_price=1490)

@pytest.fixture
def get_coupon(db):
    return Coupon.objects.create(discount=5.0, is_active=True)