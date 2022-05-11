from argparse import Namespace
from unicodedata import name
from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("auth/", include("api.urls.users", namespace="users")),
    path("products/", include("api.urls.products", namespace="products")),
]
