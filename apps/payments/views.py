from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from apps.students.models import StudentProfile
from apps.payments.models import PaymentStatus


@login_required
def payment_list_view(request):
    if request.user.role != 'coach':
        return HttpResponseForbidden("Нет доступа")

    students = StudentProfile.objects.filter(coach=request.user).select_related('user')

    for student in students:
        PaymentStatus.objects.get_or_create(student=student)

    return render(request, 'payments/payment_list.html', {'students': students})


@login_required
def payment_toggle_view(request, student_id):
    if request.user.role != 'coach':
        return HttpResponseForbidden("Нет доступа")

    student = get_object_or_404(StudentProfile, id=student_id, coach=request.user)
    payment_status, created = PaymentStatus.objects.get_or_create(student=student)

    payment_status.is_paid = not payment_status.is_paid
    payment_status.save()

    return redirect('payments:list')