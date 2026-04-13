from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from apps.students.models import StudentProfile
from apps.attendance.models import TrainingSession, AttendanceRecord
from apps.attendance.forms import TrainingAttendanceForm


@login_required
def attendance_create_view(request):
    if request.user.role != 'coach':
        return HttpResponseForbidden('Нет доступа')

    students = StudentProfile.objects.filter(coach=request.user).select_related('user')

    if request.method == 'POST':
        form = TrainingAttendanceForm(request.POST)

        if form.is_valid():
            training = TrainingSession.objects.create(
                coach=request.user,
                date=form.cleaned_data['date']
            )

            for student in students:
                is_present = request.POST.get(f'student_{student.id}') == 'on'

                AttendanceRecord.objects.create(
                    training=training,
                    student=student,
                    is_present=is_present
                )

            return redirect('attendance:attendance_success')
    else:
        form = TrainingAttendanceForm()

    context = {
        'form': form,
        'students': students,
    }
    return render(request, 'attendance/attendance_form.html', context)


@login_required
def attendance_success_view(request):
    if request.user.role != 'coach':
        return HttpResponseForbidden('Нет доступа')

    return render(request, 'attendance/attendance_success.html')