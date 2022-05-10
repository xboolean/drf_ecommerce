from argparse import Namespace
from django.urls import include, path

app_name = "api"

urlpatterns = [
    path("auth/", include("api.urls.users", namespace="users"))
]
