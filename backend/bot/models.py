from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

MAX_LENGTH = 50

# Переименовал user в user_id
# Новое поле diff_to_msk
# present_on_pk теперь в нижнем регистре


class UserProfile(AbstractUser):
    PLATFORM_CHOICES = (
        ('telegram', 'Telegram'),  # Определяем выбор платформы: Telegram
        ('vk', 'VK'),  # Определяем выбор платформы: VK
    )
    ROLE_CHOICES = (
        ('parent', 'Родитель'),  # Определяем выбор роли: Родитель
        ('logoped', 'Логопед'),  # Определяем выбор роли: Логопед
    )
    user_id = models.CharField(
        # Поле для хранения уникального ID пользователя
        max_length=MAX_LENGTH,
        unique=True,
        verbose_name="ID пользователя")
    platform = models.CharField(
        # Поле для выбора платформы (Telegram или VK)
        max_length=MAX_LENGTH,
        choices=PLATFORM_CHOICES,
        verbose_name="Платформа")
    role = models.CharField(
        # Поле для выбора роли (Родитель или Логопед)
        max_length=MAX_LENGTH,
        choices=ROLE_CHOICES,
        default='parent',
        verbose_name="Роль")
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Специфические права доступа для этого пользователя.',
        verbose_name='Разрешения'
    )

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfile'
        ordering = ('user_id',)
        indexes = [
            models.Index(fields=['user_id']),
        ]

    def __str__(self):
        return f'{self.user_id} {self.username} {self.platform} {self.role}'


class Notification(models.Model):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    platform = models.CharField('platform ',max_length=50, choices=PLATFORMS)
    days_of_week = models.CharField('Дни недели',max_length=50)
    time = models.TimeField(auto_now=False, auto_now_add=False)


    class Meta:
        verbose_name = 'Напоминания'
        verbose_name_plural = 'Напоминание'
        ordering = ('time',)
        indexes = [
            models.Index(fields=['user_id']),
            models.Index(fields=['platform']),
            models.Index(fields=['time']),
        ]

    def __str__(self):
        return (
            f'{self.user_id} {self.platform}'
            f'{self.days_of_week} {self.time}'
        )


class Content(models.Model):
    code_gift = models.CharField('Код gift',max_length=50)
    url_gift = models.URLField('Url gift', null=True, blank=True)
    usefull_url = models.URLField('usefull_url',max_length=50)
    track_file = models.URLField('Файл', null=True, blank=True)
    payment_url  = models.URLField('payment_url', null=True, blank=True)
    ios_payment  = models.URLField('ios_payment ', null=True, blank=True)
    help_install_file  = models.URLField('help_install_file ', null=True, blank=True)
    present_on_pc  = models.URLField('present_on_pc ', null=True, blank=True)
    date = models.DateField('Дата', default=datetime.now)


    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Content'
        ordering = ('-date',)
        indexes = [
            models.Index(fields=['code_gift']),
        ]

    def __str__(self):
        return f'{self.code_gift}'
