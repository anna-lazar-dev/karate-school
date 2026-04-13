from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_STUDENT = 'student'
    ROLE_COACH = 'coach'
    ROLE_ADMIN = 'admin'

    ROLE_CHOICES = [
        (ROLE_STUDENT, 'Ученик'),
        (ROLE_COACH, 'Тренер'),
        (ROLE_ADMIN, 'Администратор'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ROLE_STUDENT,
        verbose_name='Роль',
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Телефон',
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name='Аватар',
    )

    def __str__(self):
        full_name = self.get_full_name()
        return full_name if full_name else self.username
