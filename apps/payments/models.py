from django.db import models
from django.utils import timezone
from apps.students.models import StudentProfile


class PaymentStatus(models.Model):
    student = models.OneToOneField(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name='payment_status',
        verbose_name='Ученик'
    )
    paid_until = models.DateField(
        blank=True,
        null=True,
        verbose_name='Оплачено до'
    )
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
        return f'{self.student.user.username}'

    @property
    def is_paid(self):
        if self.paid_until:
            return self.paid_until >= timezone.localdate()
        return False