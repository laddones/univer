from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _


class Client(models.Model):
    class Meta:
        verbose_name = 'Користувача'
        verbose_name_plural = 'Користувачі'
        ordering = ['-time_update']

    user_id = models.BigIntegerField(unique=True,
                                     primary_key=True,
                                     db_index=True,
                                     verbose_name='User Id')
    status = models.BooleanField(default=False, max_length=10, verbose_name="Підтверджений")
    username = models.CharField(blank=True, null=True, max_length=64, verbose_name="Логин")
    first_name = models.CharField(blank=True, null=True, max_length=64, verbose_name="Ім'я")
    last_name = models.CharField(blank=True, null=True, max_length=64, verbose_name="Призвище")
    phone_number = models.CharField(blank=True, null=True, max_length=15, verbose_name="Номер телелефону")
    email = models.EmailField(blank=True, null=True, verbose_name="Електронна пошта")

    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Час створення")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Час оновлення")

    def __str__(self):
        return str(self.user_id)


class Links(models.Model):
    class Meta:
        verbose_name = 'Посилання'
        verbose_name_plural = 'Посилання'
        ordering = ['-time_update']

    class LinkStatusChoices(models.TextChoices):
        DELETED = 'DELETED', _('Видалений')
        PUBLISHED = 'PUBLISHED', _('Опублікований')
        PROCESSING = 'PROCESSING', _('В обробці')
        BLOCKED = 'BLOCKED', _('Заблокований')

    class LinkTypeChoices(models.TextChoices):
        YOUTUBE = 'YOUTUBE', _('Youtube')
        TWITTER = 'TWITTER', _('Twitter')
        TELEGRAM = 'TELEGRAM', _('Telegram')
        INSTAGRAM = 'INSTAGRAM', _('Instagram')
        FACEBOOK = 'FACEBOOK', _('Facebook')
        TIKTOK = 'TIKTOK', _('TikTok')
        OTHER = 'OTHER', _('Інший тип')

    link = models.CharField(unique=True, max_length=255, verbose_name="Посилання")
    description = models.TextField(verbose_name="Опис ресурсу", null=True, blank=True)

    link_status = models.CharField(choices=LinkStatusChoices.choices,
                                   default=LinkStatusChoices.PROCESSING,
                                   verbose_name="Статус посилання",
                                   max_length=10)

    link_type = models.CharField(choices=LinkTypeChoices.choices,
                                 default=LinkTypeChoices.OTHER,
                                 verbose_name="Статус посилання",
                                 max_length=10)

    client = models.ForeignKey(Client, on_delete=models.SET_NULL,
                               null=True,
                               blank=True,
                               verbose_name='Користувач',
                               related_name='client_creator')

    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                              verbose_name='Адмін',
                              related_name='admin_add',
                              blank=True)

    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Час створення")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Час оновлення")

    def __str__(self):
        return str(self.link)


class LinkClientStatus(models.Model):
    class LinkStatus(models.TextChoices):
        REPORTED = 'REPORTED', _('Reported')
        SKIPPED = 'SKIPPED', _('Skipped')
        DELETED = 'DELETED', _('Deleted')
        PROCESSING = 'PROCESSING', _('Processing')

    link_status = models.CharField(choices=LinkStatus.choices, default=LinkStatus.PROCESSING, verbose_name="Статус",
                                   max_length=20)

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="User Telegram",
                               related_name="client_telegram")
    link = models.ForeignKey(Links, on_delete=models.CASCADE, verbose_name="Link", related_name="client_link")

    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Час створення")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Час оновлення")

    def __str__(self):
        return str(self.link_status)


