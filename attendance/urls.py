from django.urls import path
from . import views

urlpatterns = [
    path('dashboard-2/', views.dashboard, name='dashboard2'),
    path('check-in/', views.check_in, name='check_in'),
    path('check-out/', views.check_out, name='check_out'),
    path('mobile-check-in/', views.mobile_check_in, name='mobile_check_in'),
    path('create-profile/', views.create_employee_profile, name='create_employee_profile'),
]