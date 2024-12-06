from django.shortcuts import render
from dashboard.models import AboutUser, UserProject
from django.contrib.auth.models import User
# from portfolio.dashboard.models import AboutUser, UserProject

# Create your views here.
def home(request):
    about_user = AboutUser.objects.first()
    user = User.objects.all()
    context = {
        'aboutuser': about_user,
        'user': user,
    }
    return render(request, 'home.html', context)


def project(request):
    userproject = UserProject.objects.all()
    context = {
        'userproject': userproject,
    }
    return render(request, 'projects.html', context)

