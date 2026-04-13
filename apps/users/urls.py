from django.urls import path
from apps.users.views import coach_dashboard

app_name = 'users'

urlpatterns = [
    path('coach/', coach_dashboard, name='coach_dashboard'),
]