from django.contrib import admin
from apps.payments.models import PaymentStatus


@admin.register(PaymentStatus)
class PaymentStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'paid_until', 'updated_at')
    search_fields = ('student__user__username',)