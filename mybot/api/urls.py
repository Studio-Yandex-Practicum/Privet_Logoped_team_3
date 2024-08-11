from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserProfileViewSet, NotificationViewSet, ContentViewSet

router = DefaultRouter()
router.register(r'profile', UserProfileViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'content', ContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
