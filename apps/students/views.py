from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from apps.attendance.models import AttendanceRecord


@login_required
def student_dashboard(request):
    user = request.user

    if user.role != 'student':
        return HttpResponseForbidden("Нет доступа")

    student_profile = getattr(user, 'student_profile', None)

    attendance = AttendanceRecord.objects.none()
    total = 0
    present = 0
    absent = 0
    percent = 0

    if student_profile:
        attendance = AttendanceRecord.objects.filter(
            student=student_profile
        ).select_related('training').order_by('-training__date', '-id')

        total = attendance.count()
        present = attendance.filter(is_present=True).count()
        absent = attendance.filter(is_present=False).count()

        if total > 0:
            percent = round((present / total) * 100)

    context = {
        'user': user,
        'student': student_profile,
        'attendance': attendance,
        'total': total,
        'present': present,
        'absent': absent,
        'percent': percent,
    }

    return render(request, 'students/dashboard.html', context)