from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100)
    # Biometric data (simplified example - store hashes in real systems)
    fingerprint_hash = models.CharField(max_length=255, blank=True, null=True)
    rfid_tag = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.employee_id})"

class AttendanceRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)  # GPS coordinates or office location
    source = models.CharField(max_length=50, choices=[('biometric', 'Biometric'), ('rfid', 'RFID'), ('mobile', 'Mobile')])
    
    def duration(self):
        if self.check_out:
            return self.check_out - self.check_in
        return None

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    
    def __str__(self):
        return f"{self.employee} - {self.start_date} to {self.end_date}"