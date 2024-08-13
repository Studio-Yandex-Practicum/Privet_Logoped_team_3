from django.urls import path, include
from rest_framework import routers

from api.views import ContentViewSet, NotificationViewSet, ProfileViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('profile', ProfileViewSet, basename='profile')
router_v1.register('content', ContentViewSet, basename='content')
router_v1.register('notification', NotificationViewSet, basename='notification')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
