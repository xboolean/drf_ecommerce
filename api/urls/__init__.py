from argparse import Namespace
from unicodedata import name
from django.urls import include, path
from users.views import RegisterAPIView

app_name = "api"

urlpatterns = [
    path("", include("api.urls.additional_models", namespace="brands_categories")),
    path("auth/", include("api.urls.auth", namespace="auth")),
    path("products/", include("api.urls.products", namespace="products")),
    path("oders/", include("api.urls.orders", namespace="orders")),
    path("users/", include("api.urls.users", namespace="users")),
    path("register/", RegisterAPIView.as_view(), name="user-register"),

]
