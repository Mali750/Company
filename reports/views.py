from django.shortcuts import render
# Create your views here.

#Report Section
def Report(request):
    return render(request, 'reports/reports.html')
def salary_report(request):
    return render(request, 'reports/salary_report.html')
def performance_report(request):
    return render(request, 'reports/performance_report.html')
def leave_report(request):
    return render(request, 'reports/leave_report.html')
def suctom_report(request):
    return render(request, 'reports/custom_report.html')


