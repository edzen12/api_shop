from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.users.managers import CustomUserManager


class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Основной Email')
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        blank=True, null=True
    )
    city = models.CharField(
        max_length=255,
        verbose_name='Город',
        blank=True, null=True,
    )
    postcode = models.CharField(
        max_length=255,
        verbose_name='Почтовый индекс',
        blank=True, null=True
    )
    phone_number = models.CharField(
        max_length=13,
        blank=True, null=True,
        verbose_name='Номер телефона'
    )
    password_repeat = models.CharField(
        max_length=255, blank=True, null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ('-id',)

    def __str__(self):
        return self.email
