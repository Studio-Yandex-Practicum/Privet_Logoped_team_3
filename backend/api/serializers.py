from rest_framework import serializers

from bot.models import Content, Notification, UserProfile, Mailing


class UserProfileSerializer(serializers.ModelSerializer):
    """Получение информации ID."""

    class Meta:
        model = UserProfile
        fields = '__all__'

    def validate_user_id(self, value):
        """Проверка уникальности user_id."""
        # if self.context['request'].stream.method != 'PUT':
        if UserProfile.objects.filter(user_id=value).exists():
            raise serializers.ValidationError("Этот user_id уже существует.")
        return value


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    """Обновление информации ID."""

    class Meta:
        model = UserProfile
        fields = ('username', 'platform', 'role')

    def to_representation(self, instance):
        return UserProfileSerializer(instance, context=self.context).data


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        exclude = ('id', )


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = '__all__'


class NotificationRetreiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ('user_id', 'platform', 'time')


class NotificationCreateByUIDSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='user_id',
        queryset=UserProfile.objects.all()
    )

    class Meta:
        model = Notification
        fields = ('user', 'platform', 'days_of_week', 'time')


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = '__all__'


class ContentFileLinksSerializer(serializers.ModelSerializer):
    url_gift = serializers.SerializerMethodField()
    track_file = serializers.SerializerMethodField()
    payment_url = serializers.SerializerMethodField()
    ios_payment = serializers.SerializerMethodField()
    help_install_file = serializers.SerializerMethodField()
    present_on_pk = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = (
            'code_gift', 'url_gift', 'usefull_url', 'track_file',
            'payment_url', 'ios_payment', 'help_install_file',
            'present_on_pk'
        )

    def get_url_gift(self, obj):
        return obj.url_gift if obj.url_gift else None

    def get_track_file(self, obj):
        return obj.track_file if obj.track_file else None

    def get_payment_url(self, obj):
        return obj.payment_url if obj.payment_url else None

    def get_ios_payment(self, obj):
        return obj.ios_payment if obj.ios_payment else None

    def get_help_install_file(self, obj):
        return obj.help_install_file if obj.help_install_file else None

    def get_present_on_pk(self, obj):
        return obj.present_on_pk if obj.present_on_pk else None
