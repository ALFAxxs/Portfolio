from django.urls import path
from . import views

app_name = 'general'

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project, name='projects')
]