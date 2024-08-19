from django.contrib import admin
from django.contrib.auth.models import Group

from bot.models import Content, Notification, UserProfile

admin.site.unregister(Group)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_id',
        'username',
        'platform',
        'role'
    )
    list_filter = ('role', 'platform')
    search_fields = ('username',)
    ordering = ('user_id',)

    def has_add_permission(self, request):
        # Отключаем возможность добавления новых пользователей
        return False


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_id',
        'platform',
        'days_of_week',
        'time'
    )
    list_filter = ('user_id', 'platform')
    search_fields = ('user_id', 'platform')
    ordering = ('id',)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'code_gift',
        'url_gift',
        'usefull_url',
        'track_file',
        'payment_url',
        'date'
    )
    search_fields = ('code_gift',)
    ordering = ('-date',)

    def has_add_permission(self, request):
        # Отключаем возможность добавления новых пользователей
        return False
