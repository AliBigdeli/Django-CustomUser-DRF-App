from django.urls import path,include
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from django_rest_passwordreset import urls

urlpatterns = [
    # Registration management
    path("register/", RegisterApiView.as_view(), name="register"),
    path('register/email-verify/', VerifyEmailApiView.as_view(), name="email_verify"),
    path('register/email-verify/resend/', ResendVerifyEmailApiView.as_view(), name="email_verify"),

    # Password management
    path("change-password/",ChangePasswordView.as_view(), name='change-password'),
    path('reset-password/', include('django_rest_passwordreset.urls', namespace='reset-password')),

    # Token authentication mechanism
    path("token/login/",ObtainTokenApiView.as_view(),name="token_obtain"),
    path("token/logout/",DiscardAuthTokenApiView.as_view(), name="token_discard"),

    # JWT authentication mechanism
    path("jwt/create/",JWTObtainPairTokenApiView.as_view()),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt_verify"),

    # User profile management
    path("user/profile/", ProfileApiView.as_view(), name="profile"),
]

