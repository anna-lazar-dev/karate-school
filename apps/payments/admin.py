from django.contrib import admin
from apps.payments.models import PaymentStatus


@admin.register(PaymentStatus)
class PaymentStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'is_paid', 'updated_at')
    list_filter = ('is_paid',)
    search_fields = ('student__user__username',)