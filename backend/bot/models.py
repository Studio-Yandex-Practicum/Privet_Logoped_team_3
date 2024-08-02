from datetime import datetime

from django.db import models

from users.models import User


class UserProfile(models.Model):
    USER_ROLES = [
        ('parent', 'Родитель'),
        ('speech_therapist', 'Логопед'),
    ]

    PLATFORMS = [
        ('vk', 'Vk'),
        ('tg', 'Telegram'),
    ]

    user_id = models.CharField('user_id',max_length=50, unique=True)
    username  = models.CharField('username ',max_length=50)
    platform  = models.CharField('platform ',max_length=50, choices=PLATFORMS)
    role  = models.CharField('role ',max_length=50, choices=USER_ROLES)

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfile'
        ordering = ('user_id',)

    def __str__(self):
        return f'{self.user_id} {self.username} {self.platform} {self.role}'


class Notification(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField('Платформа',max_length=50)
    days_of_week = models.CharField('Дни недели',max_length=50)
    time = models.TimeField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = 'Напоминания'
        verbose_name_plural = 'Напоминание'
        ordering = ('user_id',)

    def __str__(self):
        return f'{self.user_id} {self.platform} {self.days_of_week} {self.time}'


class Content(models.Model):
    code_gift = models.CharField('Код gift',max_length=50)
    url_gift = models.URLField('Url gift', null=True, blank=True)
    usefull_url = models.CharField('usefull_url',max_length=50)
    track_file = models.BinaryField('Файл')
    payment_url  = models.URLField('payment_url', null=True, blank=True)
    ios_payment  = models.BinaryField('ios_payment ')
    help_install_file  = models.BinaryField('help_install_file ')
    present_on_PK  = models.BinaryField('present_on_PK ')
    date = models.DateField('Дата', default=datetime.now)

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Content'
        ordering = ('-date',)

    def __str__(self):
        return f'{self.code_gift}'
