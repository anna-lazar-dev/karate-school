from django.urls import path
from apps.attendance.views import attendance_create_view, attendance_success_view

app_name = 'attendance'

urlpatterns = [
    path('attendance/create/', attendance_create_view, name='attendance_create'),
    path('attendance/success/', attendance_success_view, name='attendance_success'),
]