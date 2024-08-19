from django.contrib import admin

from bot.models import Content, Notification, UserProfile


@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'username', 'platform', 'role')
    list_filter = ('user_id',)
    search_fields = ('user_id',)
    ordering = ('user_id',)


@admin.register(Notification)
class UserProfile(admin.ModelAdmin):
    list_display = ('id', 'user_id','platform', 'days_of_week', 'time')
    list_filter = ('user_id',)
    search_fields = ('user_id',)
    ordering = ('user_id',)


@admin.register(Content)
class Content(admin.ModelAdmin):
    list_display = ('code_gift','url_gift', 'usefull_url', 'track_file',
                    'payment_url', 'date')
    search_fields = ('code_gift',)
    ordering = ('-date',)
