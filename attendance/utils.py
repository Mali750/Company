# attendance/utils.py

def simulate_biometric_check(employee_id):
    """
    Simulate biometric verification using fingerprint_hash.
    In a real system, integrate with hardware SDK/API.
    """
    from .models import Employee
    try:
        employee = Employee.objects.get(employee_id=employee_id)
        return employee.fingerprint_hash is not None  # Simplified check
    except Employee.DoesNotExist:
        return False

def simulate_rfid_check(rfid_tag):
    """
    Simulate RFID validation. Replace with actual hardware integration.
    """
    from .models import Employee
    try:
        employee = Employee.objects.get(rfid_tag=rfid_tag)
        return True
    except Employee.DoesNotExist:
        return False

def geofence_check(latitude, longitude):
    """
    Check if the user is within a predefined geofence (e.g., office coordinates).
    Example: Use Google Maps API for real implementation.
    """
    # Example: Check if within 1km radius of a location
    office_lat, office_lon = 37.7749, -122.4194  # Example coordinates (SF)
    radius_km = 1
    # Simplified distance calculation (use geopy in real projects)
    distance = ((latitude - office_lat)**2 + (longitude - office_lon)**2)**0.5
    return distance * 111 <= radius_km  # 1 degree ≈ 111 km