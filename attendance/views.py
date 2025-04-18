from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.utils import timezone
from .models import AttendanceRecord, Employee, LeaveRequest
from .forms import EmployeeProfileForm
from .utils import simulate_biometric_check, simulate_rfid_check, geofence_check

@login_required
def check_in(request):
    employee = request.user.employee
    source = "biometric"  # Change based on input method
    
    # Check hardware input (example: RFID)
    if request.method == 'POST' and 'rfid_tag' in request.POST:
        if simulate_rfid_check(request.POST['rfid_tag']):
            source = 'rfid'
    
    # Create attendance record
    AttendanceRecord.objects.create(
        employee=employee,
        check_in=timezone.now(),
        source=source,
        location="Office"  # Replace with GPS data
    )
    return redirect('dashboard2')

@login_required
def check_out(request):
    employee = request.user.employee
    record = AttendanceRecord.objects.filter(employee=employee, check_out__isnull=True).latest('check_in')
    record.check_out = timezone.now()
    record.save()
    return redirect('dashboard2')

@login_required
def mobile_check_in(request):
    if request.method == 'POST':
        lat = request.POST.get('latitude')
        lon = request.POST.get('longitude')
        if geofence_check(float(lat), float(lon)):
            AttendanceRecord.objects.create(
                employee=request.user.employee,
                check_in=timezone.now(),
                source='mobile',
                location=f"{lat},{lon}"
            )
    return redirect('dashboard2')

@login_required
def dashboard(request):
    try:
        employee = request.user.employee  # Access the employee profile
    except Employee.DoesNotExist:
        # Redirect to a page to create an employee profile
        return redirect('create_employee_profile')

    attendance_records = AttendanceRecord.objects.filter(employee=employee).order_by('-check_in')[:10]
    leave_requests = LeaveRequest.objects.filter(employee=employee)
    return render(request, 'attendance/dashboard.html', {
        'records': attendance_records,
        'leave_requests': leave_requests
    })

# attendance/views.py
@login_required
def create_employee_profile(request):
    # Prevent duplicate profiles
    if hasattr(request.user, 'employee'):
        return redirect('dashboard2')  # Or redirect to profile update page

    try:
        if request.method == 'POST':
            form = EmployeeProfileForm(request.POST)
            if form.is_valid():
                employee = form.save(commit=False)
                employee.user = request.user
                employee.save()
                return redirect('dashboard2')
        
        else:
            form = EmployeeProfileForm()

    except IntegrityError:
        # Handle race condition if duplicate submitted simultaneously
        form = EmployeeProfileForm()
        form.add_error(None, "Profile already exists!")

    return render(request, 'attendance/create_profile.html', {
        'form': form,
        'existing_profile': hasattr(request.user, 'employee')
    })