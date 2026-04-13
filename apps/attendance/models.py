from django.db import models
from django.conf import settings
from apps.students.models import StudentProfile


class TrainingSession(models.Model):
    coach = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='training_sessions',
        verbose_name='Тренер'
    )
    date = models.DateField(verbose_name='Дата тренировки')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f'Тренировка {self.date} — {self.coach.username}'


class AttendanceRecord(models.Model):
    training = models.ForeignKey(
        TrainingSession,
        on_delete=models.CASCADE,
        related_name='attendance_records',
        verbose_name='Тренировка'
    )
    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name='attendance_records',
        verbose_name='Ученик'
    )
    is_present = models.BooleanField(default=False, verbose_name='Присутствовал')

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'
        unique_together = ('training', 'student')

    def __str__(self):
        status = 'был' if self.is_present else 'не был'
        return f'{self.student.user.username} — {self.training.date} — {status}'