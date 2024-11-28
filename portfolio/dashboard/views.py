from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.
def first_test(request):
    return render(request, 'base.html')


@login_required
def dashboard_view(request):
    user = User.objects.all()
    context = {
        'user': user,
    }
    return render(request, 'dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')  # Redirect to the login page
