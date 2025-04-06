from django.urls import path 
from .views import Report

urlpatterns = [
    path('reports/', Report, name='report'),
]
