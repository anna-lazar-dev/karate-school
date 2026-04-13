from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from apps.students.models import StudentProfile


@login_required
def coach_dashboard(request):
    user = request.user

    if user.role != 'coach':
        return HttpResponseForbidden("Нет доступа")

    students = StudentProfile.objects.filter(coach=user).select_related('user').order_by('user__username')

    context = {
        'students': students,
    }

    return render(request, 'users/coach_dashboard.html', context)