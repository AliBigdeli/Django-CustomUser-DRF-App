from django.urls import path,include
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)



urlpatterns = [
    path("register/", RegisterApiView.as_view(), name="register"),
    path('register/email-verify/', VerifyEmailApiView.as_view(), name="email-verify"),
    path('register/email-verify/resend/', ResendVerifyEmailApiView.as_view(), name="email-verify"),
    path("change-password/",ChangePasswordView.as_view(), name='change-password'),
    path('reset-password/', include('django_rest_passwordreset.urls', namespace='reset-password')),
    path("token/login/",ObtainTokenApiView.as_view(),name="token_obtain"),
    path("token/logout/",DiscardAuthToken.as_view(), name="token_discard"),
    path("jwt/create/", TokenObtainPairPatchedView.as_view(), name="jwt_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt_verify"),
    path("user/profile/", ProfileApiView.as_view(), name="profile"),
]

