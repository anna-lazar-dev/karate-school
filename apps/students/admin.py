from django.contrib import admin
from apps.students.models import StudentProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'belt',
        'weight_category',
        'sport_category',
        'competitions_count',
        'wins_count',
    )

    search_fields = ('user__username',)