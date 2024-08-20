from datetime import datetime

from django.db import models


PLATFORMS = [
    ('vk', 'Vk'),
    ('tg', 'Telegram'),
]


class UserProfile(models.Model):
    USER_ROLES = [
        ('parent', 'Родитель'),
        ('speech_therapist', 'Логопед'),
    ]

    user_id = models.CharField('ID пользователя', max_length=50, unique=True)
    username = models.CharField('username ', max_length=50)
    platform = models.CharField('Платформа', max_length=50, choices=PLATFORMS)
    role = models.CharField('Роль', max_length=50, choices=USER_ROLES)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('user_id',)
        indexes = [
            models.Index(fields=['user_id']),
        ]

    def __str__(self):
        return f'{self.user_id}'


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
        UserProfile,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    platform = models.CharField('Платформа', max_length=50, choices=PLATFORMS)
    days_of_week = models.CharField(
        'Дни недели',
        max_length=50,
        choices=DAYS_OF_WEEK_CHOICES,
        blank=True
    )
    time = models.TimeField('Время', auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = 'Напоминание'
        verbose_name_plural = 'Напоминания'
        ordering = ('time',)
        indexes = [
            models.Index(fields=['user_id']),
            models.Index(fields=['platform']),
            models.Index(fields=['time']),
        ]

    def __str__(self):
        return f'{self.user_id} {self.platform} {self.days_of_week} {self.time}'


class Content(models.Model):
    code_gift = models.CharField('Код подарка', max_length=50)
    url_gift = models.URLField('URL подарка', null=True, blank=True)
    usefull_url = models.URLField('Полезная ссылка', max_length=50)
    track_file = models.URLField('Файл для отслеживания', null=True, blank=True)
    payment_url = models.URLField('URL оплаты', null=True, blank=True)
    ios_payment = models.URLField('Файл оплаты для iOS', null=True, blank=True)
    help_install_file = models.URLField(
        'Файл помощи по установке',
        null=True,
        blank=True
    )
    present_on_pc = models.URLField('Файл для ПК', null=True, blank=True)
    date = models.DateField('Дата создания', default=datetime.now)

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'
        ordering = ('-date',)
        indexes = [
            models.Index(fields=['code_gift']),
        ]

    def __str__(self):
        return f'{self.code_gift}'
