from django.urls import path
from django.contrib.auth.views import LoginView
from staff import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('staff/', views.staff_registration, name='staff'),
    path('registration-successful/', views.Submission, name='submission'),
    path('staff-details/', views.staff_details, name='staff_details'),
    path('edit-details/<int:id>/', views.update_data, name='update'),
    path('delete/<int:id>/', views.delete_data, name='delete'),
    path('confirm-delete/<int:id>/', views.delete_confirm, name='confirm'),
    #path('login/', LoginView.as_view(template_name='staff/login.html'), name='login'),
    path('login/', views.login_view, name='login'),
    path('operations/', views.operations, name='operations')

]
