from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from apps.students.models import StudentProfile
from apps.payments.models import PaymentStatus
from apps.payments.forms import PaymentStatusForm


@login_required
def payment_list_view(request):
    if request.user.role != 'coach':
        return HttpResponseForbidden("Нет доступа")

    students = StudentProfile.objects.filter(coach=request.user).select_related('user')

    for student in students:
        PaymentStatus.objects.get_or_create(student=student)

    return render(request, 'payments/payment_list.html', {'students': students})


@login_required
def payment_edit_view(request, student_id):
    if request.user.role != 'coach':
        return HttpResponseForbidden("Нет доступа")

    student = get_object_or_404(StudentProfile, id=student_id, coach=request.user)
    payment_status, created = PaymentStatus.objects.get_or_create(student=student)

    if request.method == 'POST':
        form = PaymentStatusForm(request.POST, instance=payment_status)
        if form.is_valid():
            form.save()
            return redirect('payments:list')
    else:
        form = PaymentStatusForm(instance=payment_status)

    context = {
        'student': student,
        'form': form,
        'payment_status': payment_status,
    }
    return render(request, 'payments/payment_edit.html', context)