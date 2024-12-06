from django.urls import path
from . import views
from .forms import LoginForm
from django.contrib.auth import views as auth_views

app_name = 'dashboard'
urlpatterns = [
    path('base/', views.first_test, name='first_page'),
    path('dashboard_admin/', views.dashboard_view, name='dashboard_admin'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logout_view, name='logout'),
]