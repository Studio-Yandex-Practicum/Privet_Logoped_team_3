from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Notification, Content

admin.site.unregister(User)


class UserProfileAdmin(UserAdmin):
    model = UserProfile
    list_display = ['username', 'email', 'role', 'platform', 'is_active', 'is_staff']
    search_fields = ['username', 'email', 'user_id']
    list_filter = ['role', 'platform']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'platform', 'days_of_week', 'time', 'diff_to_msk']
    search_fields = ['user_username', 'days_of_week']
    list_filter = ['platform', 'days_of_week']


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['code_gift', 'usefull_url', 'payment_url', 'date_created']
    search_fields = ['code_gift', 'usefull_url', 'payment_url']


admin.site.register(UserProfile, UserProfileAdmin)
