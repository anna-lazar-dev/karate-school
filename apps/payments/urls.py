from django.urls import path
from apps.payments.views import payment_list_view, payment_edit_view

app_name = 'payments'

urlpatterns = [
    path('payments/', payment_list_view, name='list'),
    path('payments/edit/<int:student_id>/', payment_edit_view, name='edit'),
]