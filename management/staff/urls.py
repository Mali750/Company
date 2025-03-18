from django.urls import path
from staff import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('staff/', views.staff_registration, name='staff'),
    path('staff-details/', views.staff_details, name='staff_details'),
    path('edit-details/<int:id>/', views.update_data, name='update'),
    path('delete/<int:id>/', views.delete_data, name='delete'),
    path('confirm-delete/<int:id>/', views.delete_confirm, name='confirm'),

]
