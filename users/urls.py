from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from users.views import PaymentsViewSet, UserViewSet, UserCreateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"user", UserViewSet, basename="user")
router.register(r"payments", PaymentsViewSet, basename="payments")

urlpatterns = [
    path('', include(router.urls)),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login",),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh",),
]

urlpatterns += router.urls
