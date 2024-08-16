import re
from http import HTTPStatus

from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.serializers import (NotificationRetreiveSerializer,
                             NotificationSerializer,
                             UserProfileSerializer,
                             UserProfileUpdateSerializer,
                             NotificationCreateByUIDSerializer,
                             MailingSerializer,
                             ContentFileLinksSerializer)
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
    serializer_class = ContentFileLinksSerializer

    @action(detail=False, methods=['get'], url_path='by-code')
    def get_content_by_code(self, request):
        """Кастомный эндпоинт для получения контента по коду подарка."""
        code_gift = request.query_params.get('code_gift')
        content = get_object_or_404(Content, code_gift=code_gift)
        serializer = self.get_serializer(content)
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(detail=False, methods=['get'], url_path='by-url-gift')
    def get_content_by_url_gift(self, request):
        """Кастомный эндпоинт для получения контента по URL подарка."""
        url_gift = request.query_params.get('url_gift')
        content = get_object_or_404(Content, url_gift=url_gift)
        serializer = self.get_serializer(content)
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(detail=False, methods=['get'], url_path='by-usefull-url')
    def get_content_by_usefull_url(self, request):
        """Кастомный эндпоинт для получения контента по полезной ссылке."""
        usefull_url = request.query_params.get('usefull_url')
        content = get_object_or_404(Content, usefull_url=usefull_url)
        serializer = self.get_serializer(content)
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(detail=False, methods=['get'], url_path='by-track-file')
    def get_content_by_track_file(self, request):
        """Кастомный эндпоинт для получения контента по файлу для отслеживания."""
        track_file = request.query_params.get('track_file')
        content = get_object_or_404(Content, track_file=track_file)
        serializer = self.get_serializer(content)
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(detail=False, methods=['get'], url_path='by-payment-url')
    def get_content_by_payment_url(self, request):
        """Кастомный эндпоинт для получения контента по URL оплаты."""
        payment_url = request.query_params.get('payment_url')
        content = get_object_or_404(Content, payment_url=payment_url)
        serializer = self.get_serializer(content)
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(detail=False, methods=['get'], url_path='by-ios-payment')
    def get_content_by_ios_payment(self, request):
        """Кастомный эндпоинт для получения контента по файлу оплаты для iOS."""
        ios_payment = request.query_params.get('ios_payment')
        content = get_object_or_404(Content, ios_payment=ios_payment)
        serializer = self.get_serializer(content)
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(detail=False, methods=['get'], url_path='by-help-install-file')
    def get_content_by_help_install_file(self, request):
        """Кастомный эндпоинт для получения контента по файлу помощи по установке."""
        help_install_file = request.query_params.get('help_install_file')
        content = get_object_or_404(Content, help_install_file=help_install_file)
        serializer = self.get_serializer(content)
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(detail=False, methods=['get'], url_path='by-present-on-pk')
    def get_content_by_present_on_pk(self, request):
        """Кастомный эндпоинт для получения контента по файлу для ПК."""
        present_on_pk = request.query_params.get('present_on_pk')
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
        """Получение уведомлений по UID."""
        user_profile = get_object_or_404(UserProfile, user_id=user_id)
        queryset = Notification.objects.filter(user_id=user_profile)
        serializer = NotificationRetreiveSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(
        methods=['get'],
        detail=False,
        url_path='(vk|tg)'
    )
    def notification_retreive_by_time(self, request, platform):
        """Получение уведомлений по текущему времени и платформе."""
        time = request.query_params.get('time', None)

        if not time:
            return Response(
                {"error": "Параметр 'time' обязателен"},
                status=HTTPStatus.BAD_REQUEST
            )

        # Проверка формата времени
        if not re.match(r'^(?:[01]\d|2[0-3]):[0-5]\d$', time):
            return Response(
                {"error": "Неверный формат времени"},
                status=HTTPStatus.BAD_REQUEST
            )

        # Рассчитываем фактическое время отправки с учетом разницы в часовых поясах
        queryset = Notification.objects.filter(
            platform=platform,
            time__lte=time
        )
        # Фильтруем только те уведомления, которые подходят под текущее время и платформу
        filtered_queryset = [
            notification for notification in queryset
            if (timezone.now().time() - notification.diff_to_msk).strftime('%H:%M') == time
        ]

        serializer = NotificationRetreiveSerializer(filtered_queryset, many=True)
        return Response(serializer.data, status=HTTPStatus.OK)


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer
