from django.urls import path
from apps.payments.views import payment_list_view, payment_toggle_view

app_name = 'payments'

urlpatterns = [
    path('payments/', payment_list_view, name='list'),
    path('payments/toggle/<int:student_id>/', payment_toggle_view, name='toggle'),
]