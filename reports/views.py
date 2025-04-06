from django.shortcuts import render

# Create your views here.

#Report Section
def Report(request):
    return render(request, 'reports/reports.html')