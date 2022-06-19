from argparse import Namespace
from unicodedata import name
from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("auth/", include("api.urls.auth", namespace="auth")),
    path("products/", include("api.urls.products", namespace="products")),
    path("", include("api.urls.misc", namespace="misc")),
    path("oders/", include("api.urls.orders", namespace="orders")),
    path("promotion/", include("api.urls.promotion", namespace="promotion")),
    path("users/", include("api.urls.users", namespace="users")),
]
