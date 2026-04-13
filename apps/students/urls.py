from django.urls import path
from apps.students.views import student_dashboard

app_name = 'students'

urlpatterns = [
    path('student/dashboard/', student_dashboard, name='dashboard'),
]