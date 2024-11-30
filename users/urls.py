from django.urls import path
from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import PaymentsViewSet, UserViewSet, UserCreateAPIView

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r"user", UserViewSet, basename="user")
router.register(r"payments", PaymentsViewSet, basename="payments")

urlpatterns = [
    path("users/create/", UserCreateAPIView.as_view(), name="users_create"),
]

urlpatterns += router.urls
