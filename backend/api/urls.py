from django.urls import path, include
from rest_framework import routers

from api.views import ContentViewSet, ProfileViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('profile', ProfileViewSet, basename='profile')
router_v1.register('content', ContentViewSet, basename='content')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
