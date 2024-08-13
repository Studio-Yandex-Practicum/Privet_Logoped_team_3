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
    DAYS_OF_WEEK_CHOICES = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]

    user_id = models.ForeignKey(
        # Поле для связи с пользователем
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    platform = models.CharField(
        # Поле для выбора платформы
        max_length=MAX_LENGTH,
        choices=UserProfile.PLATFORM_CHOICES,
        verbose_name="Платформа"
    )
    days_of_week = models.CharField(
        # Поле для указания дней недели
        max_length=MAX_LENGTH,
        choices=DAYS_OF_WEEK_CHOICES,
        verbose_name="Дни недели"
    )
    time = models.TimeField(
        # Поле для указания времени
        verbose_name="Время"
    )
    diff_to_msk = models.IntegerField(
        # Поле для указания разницы во времени относительно МСК
        verbose_name="Разница с МСК"
    )

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
    code_gift = models.CharField(
        # Поле для хранения кода подарка
        max_length=255,
        verbose_name="Код подарка"
    )
    url_gift = models.URLField(
        # Поле для хранения URL подарка
        blank=True,
        null=True,
        verbose_name="URL подарка"
    )
    usefull_url = models.URLField(
        # Поле для хранения полезной ссылки
        verbose_name="Полезная ссылка"
    )
    track_file = models.FileField(
        # Поле для загрузки файла для отслеживания
        upload_to='content/',
        verbose_name="Файл для отслеживания"
    )
    payment_url = models.URLField(
        # Поле для хранения URL для оплаты
        verbose_name="URL оплаты"
    )
    ios_payment = models.FileField(
        # Поле для загрузки файла оплаты для iOS
        upload_to='content/',
        verbose_name="Файл оплаты для iOS"
    )
    help_install_file = models.FileField(
        # Поле для загрузки файла помощи по установке
        upload_to='content/',
        verbose_name="Файл помощи по установке"
    )
    present_on_pk = models.FileField(
        # Поле для загрузки файла для ПК
        upload_to='content/',
        verbose_name="Файл для ПК"
    )
    date_created = models.DateTimeField(
        # Поле для хранения даты и времени создания контента
        default=timezone.now,
        verbose_name="Дата создания"
    )

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Content'
        ordering = ('-date',)
        indexes = [
            models.Index(fields=['code_gift']),
        ]

    def __str__(self):
        return f'{self.code_gift}'
