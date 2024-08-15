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
                             NotificationCreateByUIDSerializer,
                             MailingSerializer)
from bot.models import Content, Notification, UserProfile, Mailing


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
# class ProfileViewSet(viewsets.ModelViewSet):
    """(GET, LIST): Работа с профилем."""

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @action(
        methods=['get', 'put'],
        detail=False,
        url_path='uid/(?P<user_id>[^/.]+)'
        # url_path='uid/(?P<user_id>[''^/.]+)'
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
    """(GET, LIST): Работа с контентом."""
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    @action(detail=False, methods=['get'], url_path='by-code/(?P<code_gift>[^/.]+)')
    def get_content_by_code(self, request, code_gift=None):
        """Кастомный эндпоинт для получения контента по коду подарка."""
        content = get_object_or_404(Content, code_gift=code_gift)
        serializer = self.get_serializer(content)
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(detail=False, methods=['get'], url_path='by-url-gift/(?P<url_gift>[^/.]+)')
    def get_content_by_url_gift(self, request, url_gift=None):
        """Кастомный эндпоинт для получения контента по URL подарка."""
        content = get_object_or_404(Content, url_gift=url_gift)
        serializer = self.get_serializer(content)
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(detail=False, methods=['get'], url_path='by-usefull-url/(?P<usefull_url>[^/.]+)')
    def get_content_by_usefull_url(self, request, usefull_url=None):
        """Кастомный эндпоинт для получения контента по полезной ссылке."""
        content = get_object_or_404(Content, usefull_url=usefull_url)
        serializer = self.get_serializer(content)
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(detail=False, methods=['get'], url_path='by-track-file/(?P<track_file>[^/.]+)')
    def get_content_by_track_file(self, request, track_file=None):
        """Кастомный эндпоинт для получения контента по файлу для отслеживания."""
        content = get_object_or_404(Content, track_file=track_file)
        serializer = self.get_serializer(content)
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(detail=False, methods=['get'], url_path='by-payment-url/(?P<payment_url>[^/.]+)')
    def get_content_by_payment_url(self, request, payment_url=None):
        """Кастомный эндпоинт для получения контента по URL оплаты."""
        content = get_object_or_404(Content, payment_url=payment_url)
        serializer = self.get_serializer(content)
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(detail=False, methods=['get'], url_path='by-ios-payment/(?P<ios_payment>[^/.]+)')
    def get_content_by_ios_payment(self, request, ios_payment=None):
        """Кастомный эндпоинт для получения контента по файлу оплаты для iOS."""
        content = get_object_or_404(Content, ios_payment=ios_payment)
        serializer = self.get_serializer(content)
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(detail=False, methods=['get'], url_path='by-help-install-file/(?P<help_install_file>[^/.]+)')
    def get_content_by_help_install_file(self, request, help_install_file=None):
        """Кастомный эндпоинт для получения контента по файлу помощи по установке."""
        content = get_object_or_404(Content, help_install_file=help_install_file)
        serializer = self.get_serializer(content)
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(detail=False, methods=['get'], url_path='by-present-on-pk/(?P<present_on_pk>[^/.]+)')
    def get_content_by_present_on_pk(self, request, present_on_pk=None):
        """Кастомный эндпоинт для получения контента по файлу для ПК."""
        content = get_object_or_404(Content, present_on_pk=present_on_pk)
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
        """Создание напоминания по UID."""
        user_profile = get_object_or_404(UserProfile, user_id=user_id)
        queryset = Notification.objects.filter(user_id=user_profile)
        # serializer = self.get_serializer(data=request.data)
        serializer = self.get_serializer(queryset, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(
        methods=['get'],
        detail=False,
        url_path='(vk|tg)'
        # url_path='vk'
    )
    def notification_retreive_by_time(self, request, platform):
        """Создание напоминания по UID."""
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

        queryset = Notification.objects.filter(time=time, platform=platform)
        serializer = NotificationRetreiveSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTPStatus.OK)


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer
