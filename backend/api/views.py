from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.serializers import (ContentSerializer, UserProfileSerializer,
    UserProfileUpdateSerializer)
from bot.models import Content, UserProfile


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
# class ProfileViewSet(viewsets.ModelViewSet):
    """(GET, LIST): Работа с профилем."""

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @action(
        methods=['get', 'put'],
        detail=False,
        url_path='uid/(?P<user_id>[''^/.]+)'
    )
    def uid_retrieve_update(self, request, user_id=None):
        """Чтение и обновление профиля UID."""
        # user_profile = self.get_user_profile(user_id)
        user_profile = get_object_or_404(UserProfile, user_id=user_id)
        if self.request.method == "GET":
            serializer = self.get_serializer(user_profile)
            return Response(serializer.data, status=HTTPStatus.OK)
        if request.method == "PUT":
            # serializer = self.get_serializer(user_profile, data=request.data)
            serializer = UserProfileUpdateSerializer(user_profile, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.OK)

    @action(methods=['post'], detail=False, url_path='uid')
    def uid_create(self, request):
        """Создание профиля по UID."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTPStatus.CREATED)

    # def get_user_profile(self, user_id):
    #     """Получение профиля по user_id."""
    #     try:
    #         return UserProfile.objects.get(user_id=user_id)
    #     except UserProfile.DoesNotExist:
    #         raise NotFound(detail="UserProfile not found.")


# class ContentViewSet(viewsets.ReadOnlyModelViewSet):
class ContentViewSet(viewsets.ModelViewSet):
    """(GET, LIST): Работа с профилем."""

    queryset = Content.objects.all()
    serializer_class = ContentSerializer
