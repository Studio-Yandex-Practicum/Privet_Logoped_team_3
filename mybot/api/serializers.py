from rest_framework import serializers
from .models import UserProfile, Notification, Content


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'role', 'platform']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['user', 'platform', 'days_of_week', 'time', 'diff_to_msk']


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['code_gift', 'url_gift', 'usefull_url', 'track_file', 'payment_url', 'ios_payment', 'help_install_file', 'present_on_pk']
