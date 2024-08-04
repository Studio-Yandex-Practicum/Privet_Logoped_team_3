from rest_framework import serializers

from bot.models import Content, Notification, UserProfile


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


class NotificationCreateByUIDSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='user_id',
        queryset=UserProfile.objects.all()
    )

    class Meta:
        model = Notification
        fields = ('user', 'platform', 'days_of_week', 'time')
