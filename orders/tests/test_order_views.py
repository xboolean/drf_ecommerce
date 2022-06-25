import json
import pytest
from utils import conver_to_dot_notation
from rest_framework.test import APIClient
from typing import Any
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User

def get_tokens_for_user():
    refresh = RefreshToken.for_user(User.objects.get(email='super@ex.com'))
    return refresh.access_token


@pytest.mark.django_db
def test_create_order_use_case(api_client, single_product_item_1, single_product_item_2, get_coupon):
    product = single_product_item_1
    product_2 = single_product_item_2
    _coupon = get_coupon
    endpoint = f"/api/v1/orders/orders"
    response = api_client().credentials(HTTP_AUTHORIZATION='Token' + get_tokens_for_user()).post(endpoint, {"products": [{"product": product.sku, "qty": 3}, {"product": product_2.sku, "qty": 3}],"coupon": _coupon.code }, format='json')

    expected_json = {"products": [
                            {
                            "product": "555GHJ",
                            "qty": 3,
                            "order_price": 4470
                            },
                            {
                            "product": "555GHK",
                            "qty": 3,
                            "order_price": 4470
                            }
                    ],
                    "key": Any,
                    "order_price": 8940,
                    "coupon": ""
                    }
    assert response.status_code == 201
    assert response.data == expected_json