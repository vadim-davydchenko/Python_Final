from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServerViewSet, ServerStatusViewSet

router = DefaultRouter()
router.register(r'', ServerViewSet)
router.register(r'servers/status', ServerStatusViewSet, basename='serverstatus')

urlpatterns = [
    path('', include(router.urls)),
]