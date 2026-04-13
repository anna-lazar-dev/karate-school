from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'role',
        'is_staff',
    )
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')

    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {
            'fields': ('role', 'phone', 'avatar'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Дополнительная информация', {
            'fields': ('role', 'phone', 'avatar'),
        }),
    )

    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('id',)