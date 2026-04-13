from django.contrib import admin
from apps.attendance.models import TrainingSession, AttendanceRecord


@admin.register(TrainingSession)
class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'coach', 'created_at')
    list_filter = ('date', 'coach')
    search_fields = ('coach__username',)


@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'training', 'student', 'is_present')
    list_filter = ('is_present', 'training__date')
    search_fields = ('student__user__username',)