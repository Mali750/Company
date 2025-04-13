from django.urls import path 
from reports import views

urlpatterns = [
    path('reports/', views.Report, name='report'),
    path('salary-report/', views.salary_report, name='salary'),
    path('performance-report/', views.performance_report, name='performance'),
    path('leave-report/', views.leave_report, name='leave'),
    path('cuctom-report/', views.suctom_report, name='custom'),
]
