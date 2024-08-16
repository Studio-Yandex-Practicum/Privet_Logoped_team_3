from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import UserProfile, Notification, Content, Mailing

# admin.site.unregister(User)
admin.site.unregister(Group)


class UserProfileAdmin(UserAdmin):
    model = UserProfile
    list_display = (
        'username',
        'email',
        'role',
        'platform',
        'is_active',
    )
    search_fields = ('username', 'email', 'user_id')
    list_filter = ('role', 'platform')

    # Переопределяем поля формы, исключаем "is_staff" и "is_superuser"
    fieldsets = (
        (None, {'fields': ('username',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional info', {'fields': ('user_id', 'platform', 'role')}),
    )

    # Убираем поля `groups` и `user_permissions` из админки
    def get_form(self, request, obj=None, **kwargs):
        form = super(UserProfileAdmin, self).get_form(request, obj, **kwargs)
        if 'groups' in form.base_fields:
            del form.base_fields['groups']
        if 'user_permissions' in form.base_fields:
            del form.base_fields['user_permissions']
        return form

    def has_add_permission(self, request):
        # Отключаем возможность добавления новых пользователей
        return False


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',  # ЗДЕСЬ ИСПРАВИЛА
        'platform',
        'days_of_week',
        'time',
        'diff_to_msk'
    )
    search_fields = ('user_username', 'days_of_week')
    list_filter = ('platform', 'days_of_week')


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'code_gift',
        'usefull_url',
        'payment_url',
        'date_created'
    )
    search_fields = (
        'code_gift',
        'usefull_url',
        'payment_url'
    )


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'description')
    list_filter = ('date',)


admin.site.register(UserProfile, UserProfileAdmin)
