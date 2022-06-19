from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from users.views import UserViewSet, VerifyEmail, TokenCreateView

app_name = "auth"

urlpatterns = [
    path('token/create', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('account-confirm/', VerifyEmail.as_view(), name='account_confirmation')
]

