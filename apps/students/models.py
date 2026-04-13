from django.db import models
from django.conf import settings


class StudentProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student_profile',
        verbose_name='Пользователь'
    )

    birth_date = models.DateField(verbose_name='Дата рождения')

    belt = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Пояс'
    )

    weight_category = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Весовая категория'
    )

    sport_category = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Спортивная категория'
    )

    coach = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students',
        verbose_name='Тренер'
    )

    competitions_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество соревнований'
    )

    wins_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество побед'
    )

    def __str__(self):
        return str(self.user)