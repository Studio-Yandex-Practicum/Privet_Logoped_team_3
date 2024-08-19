import re
from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.serializers import (ContentSerializer, NotificationRetreiveSerializer,
                             NotificationSerializer,
                             UserProfileSerializer,
                             UserProfileUpdateSerializer,
                             NotificationCreateByUIDSerializer)
from bot.models import Content, Notification, UserProfile


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """(GET, LIST): Работа с профилем."""

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @action(
        methods=['get', 'put'],
        detail=False,
        url_path='uid/(?P<user_id>[^/.]+)'
    )
    def uid_retrieve_update(self, request, user_id=None):
        """Чтение и обновление профиля UID."""
        user_profile = get_object_or_404(UserProfile, user_id=user_id)
        if self.request.method == "GET":
            serializer = self.get_serializer(user_profile)
            return Response(serializer.data, status=HTTPStatus.OK)
        if request.method == "PUT":
            serializer = UserProfileUpdateSerializer(
                user_profile,
                data=request.data
            )
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


class ContentViewSet(viewsets.ModelViewSet):
    """(GET, LIST): Работа с профилем."""

    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    @action(
        methods=['get'],
        detail=False,
        url_path='one'
    )
    def get_one(self, request):
        """Чтение и обновление профиля UID."""
        content = Content.objects.last()
        if self.request.method == "GET":
            serializer = self.get_serializer(content)
            return Response(serializer.data, status=HTTPStatus.OK)


class NotificationViewSet(viewsets.ModelViewSet):
    """(GET, LIST): Работа с профилем."""

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    @action(methods=['post'], detail=False, url_path='uid')
    def notification_create(self, request):
        """Создание напоминания по UID."""
        serializer = NotificationCreateByUIDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTPStatus.CREATED)

    @action(
        methods=['get'],
        detail=False,
        url_path='uid/(?P<user_id>[^/.]+)'
    )
    def notification_retreive(self, request, user_id):
        """Получение напоминания по UID."""
        user_profile = get_object_or_404(UserProfile, user_id=user_id)
        queryset = Notification.objects.filter(user_id=user_profile)
        serializer = self.get_serializer(queryset, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(
        methods=['get'],
        detail=False,
        url_path='(vk|tg)'
    )
    def notification_retreive_by_time(self, request, platform):
        """Получение напоминания по времени."""
        print(platform)
        if 'time' not in request.query_params:
            return Response(
                {"error": "Параметр 'time' обязателен"},
                status=HTTPStatus.BAD_REQUEST
            )
        time = request.query_params.get('time', None)

        # Проверка формата времени
        if not re.match(r'^(?:[01]\d|2[0-3]):[0-5]\d$', time):
            return Response(
                {"error": "Неверный формат времени"},
                status=HTTPStatus.BAD_REQUEST
            )

        queryset = Notification.objects.filter(
            time=time,
            platform=platform
        ).select_related('user_id')
        for i in queryset:
            print(i)
        serializer = NotificationRetreiveSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTPStatus.OK)
