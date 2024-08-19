from rest_framework import serializers

from bot.models import Content, Notification, UserProfile

RECORD_EXISTS = 'Запись с такими параметрами уже существует.'


class UserProfileSerializer(serializers.ModelSerializer):
    """Получение информации ID."""

    class Meta:
        model = UserProfile
        fields = '__all__'

    def validate_user_id(self, value):
        """Проверка уникальности user_id."""
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
    uid = serializers.CharField(
        source='user_id.user_id',
        read_only=True
    )

    class Meta:
        model = Notification
        fields = ('user_id', 'uid', 'platform', 'time')


class NotificationCreateByUIDSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='user_id',
        queryset=UserProfile.objects.all()
    )

    class Meta:
        model = Notification
        fields = ('user', 'platform', 'days_of_week', 'time')

    def create(self, validated_data):
        user_profile = validated_data.pop('user')
        notification = Notification.objects.create(
            user_id=user_profile,
            **validated_data
        )
        return notification

    def to_representation(self, value):
        return NotificationRetreiveSerializer(value).data

    def validate(self, attrs):
        if Notification.objects.filter(
            user_id=attrs['user'],
            platform=attrs['platform'],
            days_of_week=attrs['days_of_week'],
            time=attrs['time']
        ).exists():
            raise serializers.ValidationError(RECORD_EXISTS)
        return attrs
