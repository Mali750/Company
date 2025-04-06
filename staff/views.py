from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.hashers import check_password, make_password
from .forms import StaffForm, LoginForm
from .models import Staff, LoginModel

# Create your views here.

# home page
def dashboard(request):
    return render(request, 'staff/dashboard.html')

# registration page
def staff_registration(request):
    if request.method == "POST":
        fm = StaffForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            mb = fm.cleaned_data['mobile']
            ui = fm.cleaned_data['userId']
            pw = make_password(fm.cleaned_data['password'])
            dp = fm.cleaned_data['department']
            stff = Staff(name=nm, email=em, mobile=mb, userId=ui, password=pw, department=dp)
            stff.save()
            # fm = StaffForm()  # Reset form after saving
            return redirect('submission')
        else:
            print("Form errors:", fm.errors)  # Debugging line
    else:
        fm = StaffForm()

    stff = Staff.objects.all()
    return render(request, 'staff/register.html', {'form': fm, 'staff': stff})

# for registration successful'
def Submission(request):
    return render(request, 'staff/submission.html')
    

# staff list page
def staff_details(request):
    stff = Staff.objects.all()
    return render(request, 'staff/staff_details.html', {'staff': stff})


###This function will update/edit###
def update_data(request, id):
    if request.method == 'POST':
        itm = Staff.objects.get(pk=id)
        fm = StaffForm(request.POST, instance=itm)
        if fm.is_valid():
            fm.save()
            fm = StaffForm()
    else:
        itm = Staff.objects.get(pk=id)
        fm = StaffForm(instance=itm)
    return render(request, 'staff/update.html', {'form':fm})


###This function will delete###
def delete_data(request, id):
    staff = get_object_or_404(Staff, pk=id)  # Get the staff object or show 404

    if request.method == "POST":
        staff.delete()
        return redirect(reverse('staff_details'))  # Use named URL pattern

    return render(request, 'staff/confirm_delete.html', {'staff': staff})  # Show confirmation page

# confirmation for deletion of record
def delete_confirm(request, id):
    staff = Staff.objects.get(pk=id)
    return render(request, 'staff/confirmation.html', {'stuff': staff})

#for login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userId = form.cleaned_data['userId']
            password = form.cleaned_data['password']
            print("Login attempt:", userId)

            try:
                staff_user = Staff.objects.get(userId=userId)
                print("User found:", staff_user)

                # Check password
                if check_password(password, staff_user.password):
                    print("Password matched")
                    request.session['staff_id'] = staff_user.id
                    request.session['staff_name'] = staff_user.name
                    return redirect('operations')
                else:
                    print("Password did NOT match")
                    form.add_error('password', 'Incorrect password')
            except Staff.DoesNotExist:
                print("UserId not found")
                form.add_error('userId', 'User ID not found')
    else:
        form = LoginForm()

    return render(request, 'staff/login.html', {'form': form})



def operations(request):
    stff = Staff.objects.all()
    return render(request, 'staff/special_operations.html', {'staff': stff})



