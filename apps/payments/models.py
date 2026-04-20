from django.db import models
from apps.students.models import StudentProfile


class PaymentStatus(models.Model):
    student = models.OneToOneField(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name='payment_status',
        verbose_name='Ученик'
    )
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')
    comment = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Комментарий'
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        verbose_name = 'Статус оплаты'
        verbose_name_plural = 'Статусы оплаты'

    def __str__(self):
        return f'{self.student.user.username} - {"Оплачено" if self.is_paid else "Не оплачено"}'