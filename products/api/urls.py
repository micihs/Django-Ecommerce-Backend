from django.urls import include, path
from rest_framework.routers import DefaultRouter

from products.api.views import ProductViewSet

router = DefaultRouter()
router.register("", ProductViewSet)

urlpatterns = [path("", include(router.urls))]