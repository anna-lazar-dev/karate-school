from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request, 'home.html')


@login_required
def dashboard_redirect(request):
    user = request.user

    if user.role == 'student':
        return redirect('students:dashboard')
    elif user.role == 'coach':
        return redirect('users:coach_dashboard')
    elif user.role == 'admin':
        return redirect('admin:index')

    return redirect('home')