from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig
from users.views import PaymentsViewSet, UserViewSet


app_name = UsersConfig.name

router = SimpleRouter()
router.register(r"user", UserViewSet, basename="user")
router.register(r"payments", PaymentsViewSet, basename="payments")

urlpatterns = []

urlpatterns += router.urls
